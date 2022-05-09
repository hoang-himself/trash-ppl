"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from StaticError import *

# !!! COMMENT THIS OUT
from main.d96.utils.AST import *
from main.d96.utils.Visitor import *


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
        self.name = name
        self.partype = partype
        self.rettype = rettype
        self.static = static

        # { str: List[MetaVariable] }
        # because we must keep track of variables in outer scope
        self.variable = dict()

        # Not in loop
        self.loop = 0

        # Already in scope of class
        self.scope = 1

    def enter_loop(self):
        self.loop += 1

    def exit_loop(self):
        self.loop -= 1

    def enter_scope(self):
        self.scope += 1

    def exit_scope(self):
        self.scope -= 1
        # Remove inner scope variables
        for name, val in self.variable.items():
            if val[-1].scope > self.scope:
                self.variable[name].pop()

    def add_var(self, name, type):
        self.check_redeclared_variable(name)
        if name in self.variable.keys():
            self.variable[name] += [MetaVariable(name, type, self.scope)]
        else:
            self.variable[name] = [MetaVariable(name, type, self.scope)]

    def add_const(self, name, type):
        self.check_redeclared_variable(name)
        if name in self.variable.keys():
            self.variable[name] += [MetaVariable(name, type, self.scope, True)]
        else:
            self.variable[name] = [MetaVariable(name, type, self.scope, True)]

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
            self.attr = super_cls.attr.copy()
            self.method = super_cls.method.copy()

    def add_attr(self, name, type, static=False, constant=False):
        self.check_redeclared_attr(name)
        self.attr[name] = MetaAttribute(name, type, static, constant)

    def add_method(self, name, partype, rettype=None, static=False):
        self.check_redeclared_method(name, partype)
        if self.name == "Program" and name == "main":
            static = True
        self.method[name] = MetaMethod(name, partype, rettype, static)

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
        if name in self.method.keys():
            # Test with type of parameters, not names
            partype_old = list(map(lambda x: type(x.varType), self.method[name].partype))
            partype_new = list(map(lambda x: type(x.varType), partype))
            if partype_old == partype_new:
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


class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast

    def lookup(self, name, lst, func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def check(self):
        return self.visit(self.ast, None)

    def visitProgram(self, ast, c=None):
        self.meta_program = MetaProgram()

        # Traverse all classes
        [self.visit(x, c) for x in ast.decl]

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

    def visitAttributeDecl(self, ast, c: MetaClass):
        static = type(ast.kind) is Static
        const = type(ast.decl) is ConstDecl
        if const:
            partype = ast.decl.constType
            name = ast.decl.constant.name
        else:
            partype = ast.decl.varType
            name = ast.decl.variable.name
        c.add_attr(name, partype, static, const)

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
        [self.visit(x, c) for x in ast.inst]
        meta_method.exit_scope()

    def visitVarDecl(self, ast, c: tuple):
        meta_class, meta_method = c
        meta_method.add_var(ast.variable.name, ast.varType)
        # Var can exist without being initialized
        if ast.varInit:
            rettype = self.visit(ast.varInit, c)
            if type(rettype) != type(ast.varType):
                raise TypeMismatchInStatement(ast)

    def visitConstDecl(self, ast, c: tuple):
        meta_class, meta_method = c
        meta_method.add_const(ast.constant.name, ast.constType)
        if not ast.value:
            raise IllegalConstantExpression(ast.value)
        rettype = self.visit(ast.value, c)
        if type(rettype) != type(ast.constType):
            raise TypeMismatchInConstant(ast)

    def visitAssign(self, ast, c):
        lhs = self.visit(ast.lhs, c)
        rhs = self.visit(ast.exp, c)

        if not lhs:
            raise Undeclared(Identifier(), ast.lhs.name)

        lhs = lhs[-1]
        if lhs.constant:
            raise CannotAssignToConstant(ast)

        # TODO Cannot mismatch type

    # LHS of Assign
    def visitId(self, ast, c: tuple):
        meta_class, meta_method = c
        if ast.name not in meta_method.variable.keys():
            raise Undeclared(Identifier(), ast.name)
        return meta_method.variable[ast.name]

    def visitCallStmt(self, ast, c: tuple):
        # TODO why obj?
        rettype = self.visit(ast.obj, c)

    def visitBreak(self, ast, c):
        meta_class, meta_method = c
        if meta_method.loop < 1:
            raise MustInLoop(Break())

    def visitContinue(self, ast, c):
        meta_class, meta_method = c
        if meta_method.loop < 1:
            raise MustInLoop(Continue())

    def visitReturn(self, ast, c):
        meta_class, meta_method = c
        meta_method.rettype = self.visit(ast.expr, c)

    def visitIf(self, ast, c):
        pass

    def visitFor(self, ast, c):
        pass

    def visitBinaryOp(self, ast, c: BinaryOp):
        left = ast.left
        right = ast.right
        op = ast.op

        # Arithmetic
        if op == '%':
            if type(left) is not IntLiteral or type(right) is not IntLiteral:
                raise TypeMismatchInExpression(ast)
        if op in ['+', '-', '*', '/']:
            if type(left) not in [
                IntLiteral, FloatLiteral
            ] or type(right) not in [IntLiteral, FloatLiteral]:
                raise TypeMismatchInExpression(ast)
            if type(left) is IntLiteral and type(right) is IntLiteral:
                return IntType()
            return FloatType()

        # TODO bool
        if op == '==.':
            pass
        if op in ['&&', '||']:
            pass

        # TODO string
        if op == '+.':
            pass

        # TODO relational
        if op in ['==', '!=']:
            pass
        if op in ['<', '>', '<=', '>=']:
            pass

    def visitUnaryOp(self, ast, c: UnaryOp):
        body = ast.body
        op = ast.op

        # Arithmetic
        if op == '-':
            if type(body) not in [IntLiteral, FloatLiteral]:
                raise TypeMismatchInExpression(ast)
            return IntType() if type(body) is IntLiteral else FloatType()

        # Boolean
        if op == '!':
            if type(body) is not BooleanLiteral:
                raise TypeMismatchInExpression(ast)
            return BoolType()

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()
