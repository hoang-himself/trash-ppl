"""
 * @author nhphung
"""
from os import name
from AST import *
from Visitor import *
from Utils import *
from StaticError import *

# !!! COMMENT THIS OUT
from main.d96.utils.AST import *
from main.d96.utils.Utils import *
from main.d96.utils.Visitor import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype  # This should not exist
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class MetaAttribute:
    def __init__(self, name, type, static=False, constant=False):
        self.name = name
        self.type = type
        self.static = static
        self.constant = constant


class MetaVariable:
    def __init__(self, name, type, scope, constant=False):
        self.name = name
        self.type = type
        self.scope = scope
        self.constant = constant


class MetaMethod:
    def __init__(
        self, name, partype: List[VarDecl], rettype=None, static=False
    ):
        if name == "main":
            static = True
        self.name = name
        self.partype = partype
        self.rettype = rettype
        self.static = static

        # { str: List[MetaVariable] }
        # because we must keep track of variables in outer scope
        self.variable = dict()

        # Not in loop
        self.loop_nest = 0

        # Already in scope of class
        self.scope_nest = 1

    def enter_loop(self):
        self.loop_nest += 1

    def exit_loop(self):
        # TODO maybe add a context param so we can raise MustInLoop here
        self.loop_nest -= 1

    def enter_scope(self):
        self.scope_nest += 1

    def exit_scope(self):
        self.scope_nest -= 1
        # Remove inner scope variables
        for name, val in self.variable.items():
            # TODO this feels wrong
            if val[-1].scope_nest > self.scope_nest:
                self.variable[name].pop()

    def add_var(self, name, type):
        self.check_redeclared_variable(name)
        self.variable[name] = MetaVariable(name, type, self.scope_nest)

    def add_const(self, name, type):
        self.check_redeclared_variable(name)
        self.variable[name] = MetaVariable(name, type, self.scope_nest, True)

    def check_entrypoint(self):
        return self.name == "main" and self.static

    def check_redeclared_variable(self, name):
        if name in self.variable.keys():
            raise Redeclared(Variable(), name)


class MetaClass:
    def __init__(self, name, super_cls=None):
        self.name = name
        self.attr = dict()
        self.method = dict()
        if super_cls:
            self.attr = super_cls.attrs.copy()
            self.method = super_cls.methods.copy()

    def add_attr(self, name, type, static=False, constant=False):
        self.check_redeclared_attr(name)
        self.attr[name] = MetaAttribute(name, type, static, constant)

    def add_method(self, name, partype, rettype=None, static=False):
        self.check_redeclared_method(name, partype)
        self.method[name] = MetaMethod(name, partype, rettype)

    def get_or_raise_undeclared_attr(self, name):
        if name not in self.attr.keys():
            raise Undeclared(Attribute(), name)
        return self.attr[name]

    def get_or_raise_undeclared_method(self, name):
        if name not in self.method.keys():
            raise Undeclared(Method(), name)
        return self.method[name]

    def check_entrypoint(self):
        return any(
            [method.check_entrypoint()
             for method in self.method.values()] if self.method else [False]
        )

    def check_redeclared_attr(self, name):
        if name in self.attr.keys():
            raise Redeclared(Attribute(), name)

    def check_redeclared_method(self, name, partype: List[VarDecl]):
        # TODO Test this partype comparison
        if name in self.method.keys() and self.method[name].partype == partype:
            raise Redeclared(Method(), name)


class MetaProgram:
    def __init__(self):
        self.cls = dict()

    def add_class(self, name, super_cls=None):
        self.check_redeclared_class(name)
        if super_cls:
            self.check_undeclared_class(super_cls)
        self.cls[name] = MetaClass(
            name, self.cls[super_cls] if super_cls else None
        )

    def add_method(self, cls, name, partype, rettype=None, static=False):
        self.check_undeclared_class(cls)
        self.cls[cls].add_method(name, partype, rettype, static)

    def add_attr(self, cls, name, type, static=False, constant=False):
        self.check_undeclared_class(cls)
        self.cls[cls].add_attr(name, type, static, constant)

    def get_class(self, name):
        self.check_undeclared_class(name)
        return self.cls[name]

    def check_entrypoint(self):
        return any(
            [cls.check_entrypoint()
             for cls in self.cls.values()] if self.cls else [False]
        )

    def check_redeclared_class(self, name):
        if name in self.cls.keys():
            raise Redeclared(Class(), name)

    def check_undeclared_class(self, name):
        if name not in self.cls.keys():
            raise Undeclared(Class(), name)


class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, None)

    def visitProgram(self, ast, global_env=None):
        self.meta_program = MetaProgram()

        # Traverse all classes
        [self.visit(x, global_env) for x in ast.decl]

        if not self.meta_program.check_entrypoint():
            raise NoEntryPoint()

    def visitClassDecl(self, ast, c=None):
        # Load classes into meta_program
        self.meta_program.add_class(
            ast.classname.name, ast.parentname.name if ast.parentname else None
        )

        # Make classes load attributes and methods
        [
            self.visit(x, self.meta_program.get_class(ast.classname.name))
            for x in ast.memlist
        ]

    def visitMethodDecl(self, ast, meta_cls: MetaClass):
        static = type(ast.kind) is Static
        meta_cls.add_method(ast.name.name, ast.param, None, static)
        [
            self.visit(
                ast.body, (
                    meta_cls,
                    meta_cls.get_or_raise_undeclared_method(ast.name.name)
                )
            )
        ]

    def visitBlock(self, ast, c: tuple):
        meta_class, meta_method = c
        meta_method.enter_scope()
        # TODO ast.inst is [None, None] for some reason
        [self.visit(x, c) for x in ast.inst]
        meta_method.exit_scope()

    def visitAttributeDecl(self, ast, c):
        pass

    def visitAssign(self, ast, c):
        pass

    def visitIf(self, ast, c):
        pass

    def visitFor(self, ast, c):
        pass

    def visitBreakStmt(self, ast, c):
        pass
        is_in_loop = c[1]
        if not is_in_loop:
            raise MustInLoop('Break')
        return (ast, Break())

    def visitContinueStmt(self, ast, c):
        pass
        is_in_loop = c[1]
        if not is_in_loop:
            raise MustInLoop('Continue')
        return (ast, Continue())

    def visitReturn(self, ast, c):
        pass
