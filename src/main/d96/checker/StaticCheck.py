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


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


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
        return [self.visit(x, c) for x in ast.decl]

    def visitClass_decl(self, ast, c):
        # TODO
        pass

    def visitClass_mem_decl(self, ast, c):
        # TODO
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

    def visitAttr_name_list(self, ast, c):
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

    def visitCons_method(self, ast, c):
        # TODO
        pass

    def visitDes_method(self, ast, c):
        # TODO
        pass

    def visitParam_list(self, ast, c):
        # TODO
        pass

    def visitParam(self, ast, c):
        # TODO
        pass

    def visitLiteral_list(self, ast, c):
        # TODO
        pass

    def visitLiteral(self, ast, c):
        # TODO
        pass

    def visitInt_literal(self, ast, c):
        # TODO
        pass

    def visitBoolean_literal(self, ast, c):
        # TODO
        pass

    def visitStatic_idname_list(self, ast, c):
        # TODO
        pass

    def visitIdname_list(self, ast, c):
        # TODO
        pass

    def visitArray_literal(self, ast, c):
        # TODO
        pass

    def visitAny_type(self, ast, c):
        # TODO
        pass

    def visitExpr_list(self, ast, c):
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

    def visitNew_object_expr(self, ast, c):
        # TODO
        pass

    def visitAssign_stmt(self, ast, c):
        # TODO
        pass

    def visitAssign_lhs(self, ast, c):
        # TODO
        pass

    def visitAssign_rhs(self, ast, c):
        # TODO
        pass

    def visitFlow_stmt(self, ast, c):
        # TODO
        pass

    def visitIf_stmt(self, ast, c):
        # TODO
        pass

    def visitElseif_stmt(self, ast, c):
        # TODO
        pass

    def visitElse_stmt(self, ast, c):
        # TODO
        pass

    def visitFor_stmt(self, ast, c):
        # TODO
        pass

    def visitFor_range(self, ast, c):
        # TODO
        pass

    def visitBreak_stmt(self, ast, c):
        # TODO
        pass

    def visitContinue_stmt(self, ast, c):
        # TODO
        pass

    def visitReturn_stmt(self, ast, c):
        # TODO
        pass

    def visitAny_stmt(self, ast, c):
        # TODO
        pass

    def visitCall_stmt(self, ast, c):
        # TODO
        pass

    def visitBlock_stmt(self, ast, c):
        # TODO
        pass

    # def visitFuncDecl(self, ast, c):
    #     return list(map(lambda x: self.visit(x, (c, True)), ast.body.stmt))

    # def visitCallExpr(self, ast, c):
    #     at = [self.visit(x, (c[0], False)) for x in ast.param]

    #     res = self.lookup(ast.method.name, c[0], lambda x: x.name)
    #     if res is None or not type(res.mtype) is MType:
    #         raise Undeclared(Function(), ast.method.name)
    #     elif len(res.mtype.partype) != len(at):
    #         if c[1]:
    #             raise TypeMismatchInStatement(ast)
    #         else:
    #             raise TypeMismatchInExpression(ast)
    #     else:
    #         return res.mtype.rettype

    # def visitIntLiteral(self, ast, c):
    #     return IntType()
