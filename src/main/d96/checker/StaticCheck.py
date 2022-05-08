"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import *
from StaticError import *

# !!! COMMENT THIS OUT
from main.d96.utils.AST import *
from main.d96.utils.Utils import *
from main.d96.utils.Visitor import *


# Method type
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


class MetaMethod:
    def __init__(
        self, name, partype: List[VarDecl], rettype=None, static=False
    ):
        self.name = name
        self.partype = partype
        self.rettype = rettype
        self.static = static
        self.variable = dict()


class MetaClass:
    def __init__(self, name, super_cls):
        self.name = name
        self.attr = dict()
        self.method = dict()
        if super_cls:
            self.attr = super_cls.attrs.copy()
            self.method = super_cls.methods.copy()

    def add_attr(self, name, type):
        self.check_redeclared_attr(name)
        self.attr[name] = MetaAttribute(name, type)

    def get_attr(self, name):
        if name not in self.attr.keys():
            raise Undeclared(Attribute(), name)
        return self.attr[name]

    def add_method(self, name, partype, rettype=None):
        self.check_redeclared_method(name, partype)
        self.method[name] = MetaMethod(name, partype, rettype)

    def get_method(self, name):
        if name not in self.method.keys():
            raise Undeclared(Method(), name)
        return self.method[name]

    def check_entrypoint(self):
        return any(map(lambda method: method.name == "main", self.method))

    def check_redeclared_method(self, name, partype):
        # TODO partype: List[VarDecl]
        if any(
            map(
                lambda method: method.name == name and method.partype ==
                partype, self.method
            )
        ):
            raise Redeclared(Method(), self.name)

    def check_redeclared_attr(self, name):
        if any(map(lambda attr: attr.name == name, self.attr)):
            raise Redeclared(Attribute(), self.name)


class MetaProgram:
    def __init__(self):
        self.cls = dict()

    def add_class(self, name, super_cls=None):
        self.check_redeclared_class(name)
        self.check_undeclared_class(super_cls)
        self.cls[name] = MetaClass(name, self.cls[super_cls])

    # Might not need this
    def add_method(self, cls, name, partype, rettype, static=False):
        self.check_undeclared_class(cls)
        self.cls[cls].add_method(name, partype, rettype, static)

    # Might not need this
    def add_attr(self, cls, name, type):
        self.check_undeclared_class(cls)
        self.cls[cls].add_attr(name, type)

    def get_class(self, name):
        self.check_undeclared_class(name)
        return self.cls[name]

    def check_entrypoint(self):
        if not any([cls.check_entrypoint() for cls in self.cls.values()]):
            raise NoEntryPoint()

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
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        # Dependency rejection
        self.meta_program = MetaProgram()
        # Traverse all classes
        [self.visit(x, c) for x in ast.decl]
        # idk you tell me
        if not self.meta_program.check_entrypoint():
            raise NoEntryPoint()

    def visitClassDecl(self, ast, c):
        # TODO
        pass

    def visitClass_mem_decl(self, ast, c):
        # TODO Remove
        pass

    def visitAttr_decl(self, ast, c):
        # TODO
        pass

    def visitAttr_decl_wo_asg(self, ast, c):
        # TODO
        pass

    def visitAttr_decl_w_asg(self, ast, c):
        # TODO
        pass

    def visitAttr_decl_rep(self, ast, c):
        # TODO
        pass

    def visitAttr_nameList(self, ast, c):
        # TODO
        pass

    def visitMethod_decl(self, ast, c):
        # TODO
        pass

    def visitGeneric_name(self, ast, c):
        # TODO
        pass

    def visitMethod_local_decl(self, ast, c):
        # TODO
        pass

    def visitMethod_local_decl_wo_asg(self, ast, c):
        # TODO
        pass

    def visitMethod_local_decl_w_asg(self, ast, c):
        # TODO
        pass

    def visitMethod_local_decl_rep(self, ast, c):
        # TODO
        pass

    def visitConsMethod(self, ast, c):
        # TODO
        pass

    def visitDesMethod(self, ast, c):
        # TODO
        pass

    def visitParamList(self, ast, c):
        # TODO
        pass

    def visitParam(self, ast, c):
        # TODO
        pass

    def visitLiteralList(self, ast, c):
        # TODO
        pass

    def visitLiteral(self, ast, c):
        # TODO
        pass

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStaticIdnameList(self, ast, c):
        # TODO
        pass

    def visitIdnameList(self, ast, c):
        # TODO
        pass

    def visitArrayLiteral(self, ast, c):
        # TODO
        pass

    def visitAnyType(self, ast, c):
        # TODO
        pass

    def visitExprList(self, ast, c):
        # TODO
        pass

    def visitExpr(self, ast, c):
        # TODO
        pass

    def visitExpr1(self, ast, c):
        # TODO
        pass

    def visitExpr2(self, ast, c):
        # TODO
        pass

    def visitExpr3(self, ast, c):
        # TODO
        pass

    def visitExpr4(self, ast, c):
        # TODO
        pass

    def visitExpr5(self, ast, c):
        # TODO
        pass

    def visitExpr6(self, ast, c):
        # TODO
        pass

    def visitExpr7(self, ast, c):
        # TODO
        pass

    def visitExpr8(self, ast, c):
        # TODO
        pass

    def visitExpr9(self, ast, c):
        # TODO
        pass

    def visitExpr10(self, ast, c):
        # TODO
        pass

    def visitOperand(self, ast, c):
        # TODO
        pass

    def visitNewObjectExpr(self, ast, c):
        # TODO
        pass

    def visitAssignStmt(self, ast, c):
        # TODO
        pass

    def visitAssignLhs(self, ast, c):
        # TODO
        pass

    def visitAssignRhs(self, ast, c):
        # TODO Remove
        pass

    def visitFlowStmt(self, ast, c):
        # TODO
        pass

    def visitIfStmt(self, ast, c):
        # TODO
        pass

    def visitElseifStmt(self, ast, c):
        # TODO
        pass

    def visitElseStmt(self, ast, c):
        # TODO
        pass

    def visitForStmt(self, ast, c):
        # TODO
        pass

    def visitForRange(self, ast, c):
        # TODO
        pass

    def visitBreakStmt(self, ast, c):
        is_in_loop = c[1]
        if not is_in_loop:
            raise MustInLoop('Break')
        return (ast, Break())

    def visitContinueStmt(self, ast, c):
        is_in_loop = c[1]
        if not is_in_loop:
            raise MustInLoop('Continue')
        return (ast, Continue())

    def visitReturnStmt(self, ast, c):
        # TODO
        pass

    def visitAnyStmt(self, ast, c):
        # TODO Remove
        pass

    def visitCallStmt(self, ast, c):
        # TODO
        pass

    def visitBlockStmt(self, ast, c):
        # TODO
        pass
