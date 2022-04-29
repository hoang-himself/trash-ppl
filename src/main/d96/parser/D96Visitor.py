# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_decl.
    def visitClass_decl(self, ctx:D96Parser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#entry_class.
    def visitEntry_class(self, ctx:D96Parser.Entry_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_mem_decl.
    def visitClass_mem_decl(self, ctx:D96Parser.Class_mem_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_decl.
    def visitAttr_decl(self, ctx:D96Parser.Attr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_decl_wo_asg.
    def visitAttr_decl_wo_asg(self, ctx:D96Parser.Attr_decl_wo_asgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_decl_w_asg.
    def visitAttr_decl_w_asg(self, ctx:D96Parser.Attr_decl_w_asgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_decl_rep.
    def visitAttr_decl_rep(self, ctx:D96Parser.Attr_decl_repContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_name_list.
    def visitAttr_name_list(self, ctx:D96Parser.Attr_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_decl.
    def visitMethod_decl(self, ctx:D96Parser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_local_decl.
    def visitMethod_local_decl(self, ctx:D96Parser.Method_local_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_local_decl_wo_asg.
    def visitMethod_local_decl_wo_asg(self, ctx:D96Parser.Method_local_decl_wo_asgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_local_decl_w_asg.
    def visitMethod_local_decl_w_asg(self, ctx:D96Parser.Method_local_decl_w_asgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_local_decl_rep.
    def visitMethod_local_decl_rep(self, ctx:D96Parser.Method_local_decl_repContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#entry_method.
    def visitEntry_method(self, ctx:D96Parser.Entry_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_wo_return.
    def visitStmt_wo_return(self, ctx:D96Parser.Stmt_wo_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#cons_method.
    def visitCons_method(self, ctx:D96Parser.Cons_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#des_method.
    def visitDes_method(self, ctx:D96Parser.Des_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param_list.
    def visitParam_list(self, ctx:D96Parser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal_list.
    def visitLiteral_list(self, ctx:D96Parser.Literal_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_literal.
    def visitInt_literal(self, ctx:D96Parser.Int_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#boolean_literal.
    def visitBoolean_literal(self, ctx:D96Parser.Boolean_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_idname_list.
    def visitStatic_idname_list(self, ctx:D96Parser.Static_idname_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idname_list.
    def visitIdname_list(self, ctx:D96Parser.Idname_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_literal.
    def visitArray_literal(self, ctx:D96Parser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#any_type.
    def visitAny_type(self, ctx:D96Parser.Any_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_list.
    def visitExpr_list(self, ctx:D96Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx:D96Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx:D96Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx:D96Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx:D96Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx:D96Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx:D96Parser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx:D96Parser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operand.
    def visitOperand(self, ctx:D96Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#new_object_expr.
    def visitNew_object_expr(self, ctx:D96Parser.New_object_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:D96Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_lhs.
    def visitAssign_lhs(self, ctx:D96Parser.Assign_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_rhs.
    def visitAssign_rhs(self, ctx:D96Parser.Assign_rhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_lhs_sub_expr_list.
    def visitAssign_lhs_sub_expr_list(self, ctx:D96Parser.Assign_lhs_sub_expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_lhs_sub_expr.
    def visitAssign_lhs_sub_expr(self, ctx:D96Parser.Assign_lhs_sub_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_lhs_sub_expr1.
    def visitAssign_lhs_sub_expr1(self, ctx:D96Parser.Assign_lhs_sub_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_lhs_sub_expr2.
    def visitAssign_lhs_sub_expr2(self, ctx:D96Parser.Assign_lhs_sub_expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_lhs_sub_expr3.
    def visitAssign_lhs_sub_expr3(self, ctx:D96Parser.Assign_lhs_sub_expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#flow_stmt.
    def visitFlow_stmt(self, ctx:D96Parser.Flow_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_stmt.
    def visitElseif_stmt(self, ctx:D96Parser.Elseif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_stmt.
    def visitElse_stmt(self, ctx:D96Parser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_stmt.
    def visitFor_stmt(self, ctx:D96Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_range.
    def visitFor_range(self, ctx:D96Parser.For_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)



del D96Parser