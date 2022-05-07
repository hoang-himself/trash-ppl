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
    def __init__(self, name, type, static=False):
        self.name = name
        self.type = type
        self.static = static


class MetaMethod:
    pass


class MetaClass:
    def __init__(self, name, super_cls):
        self.name = name
        self.attr = list()
        self.method = list()
        if super_cls:
            self.attr = super_cls.attrs.copy()
            self.method = super_cls.methods.copy()

    def add_attr(self, name, type):
        self.check_redeclared_attr(name)
        self.attr.append(MetaAttribute(name, type))

    def add_method(self, name, partype, rettype=None):
        self.check_redeclared_method(name, partype)
        self.method.append(MetaMethod(name, partype, rettype))

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


class MetaClassManager:
    def __init__(self):
        self.cls_set = list()

    def add_class(self, name, super_cls=None):
        self.check_redeclared_class(name)
        self.check_undeclared_class(super_cls)
        self.cls_set.append(MetaClass(name, self.cls_set[super_cls]))

    def add_method(self, cls, name, partype, rettype):
        self.check_undeclared_class(cls)
        self.cls_set[cls].add_method(name, partype, rettype)

    def add_attr(self, cls, name, type):
        self.check_undeclared_class(cls)
        self.cls_set[cls].add_attr(name, type)

    def check_entrypoint(self):
        if not any([cls.check_entrypoint() for cls in self.cls_set.values()]):
            raise NoEntryPoint()

    def check_redeclared_class(self, name):
        if name in self.cls_set:
            raise Redeclared(Class(), name)

    def check_undeclared_class(self, name):
        if name not in self.cls_set:
            raise Undeclared(Class(), name)


class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        # TODO
        glob_env = c[:]

        # Find Program::main()
        exists_entrypoint = False
        for cls in ast.decl:
            if isinstance(cls, ClassDecl) and cls.classname.name == 'Program':
                for mem in cls.memlist:
                    if isinstance(mem, MethodDecl) and mem.name.name == 'main':
                        exists_entrypoint = True
                        break
        if not exists_entrypoint:
            raise NoEntryPoint()

        # Find redeclare
        for cls in ast.decl:
            if isinstance(cls, ClassDecl):
                glob_env.append(self.visit(cls, glob_env))
            for mem in cls.memlist:
                if isinstance(mem, VarDecl) or isinstance(mem, ConstDecl):
                    glob_env.append(self.visit(mem, glob_env))
                elif isinstance(mem, MethodDecl):
                    pass

        return [self.visit(x, c) for x in ast.decl]

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
