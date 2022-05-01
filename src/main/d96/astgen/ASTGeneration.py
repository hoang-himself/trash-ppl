from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from functools import reduce
from itertools import zip_longest

# !!! COMMENT THIS OUT
from main.d96.utils.AST import *


class ASTGeneration(D96Visitor):
    def binary_op(self, ctx):
        child_count = ctx.getChildCount()
        if child_count == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(
                ctx.getChild(1).getText(), self.visit(ctx.getChild(0)),
                self.visit(ctx.getChild(2))
            )

    def unary_op(self, ctx):
        child_count = ctx.getChildCount()
        if child_count == 1:
            return self.visit(ctx.getChild(0))
        else:
            return UnaryOp(
                ctx.getChild(0).getText(), self.visit(ctx.getChild(1))
            )

    def field_access(self, ctx):
        child_count = ctx.getChildCount()
        if child_count == 1:
            return self.visit(ctx.getChild(0))
        elif child_count == 3:
            return FieldAccess(
                self.visit(ctx.getChild(0)), Id(ctx.getChild(2).getText())
            )
        elif child_count == 5:
            return CallExpr(
                self.visit(ctx.getChild(0)), Id(ctx.getChild(2).getText()), []
            )
        elif child_count == 6:
            expr_list = self.visit(ctx.getChild(4))
            return CallExpr(
                self.visit(ctx.getChild(0)), Id(ctx.getChild(2).getText()),
                expr_list
            )

    def visitProgram(self, ctx: D96Parser.ProgramContext):
        class_list = []
        for cls in ctx.class_decl():
            class_decl = self.visit(cls)
            if isinstance(class_decl, list):
                class_list.extend(class_decl if class_decl else [])
            else:
                class_list.append(class_decl)
        return Program(class_list)

    def visitClass_decl(self, ctx: D96Parser.Class_declContext):
        name = Id(ctx.ID_NAME(0).getText())
        super_name = Id(ctx.ID_NAME(1).getText()) if ctx.COLON() else None

        class_mem_list = []
        for mem_decl in ctx.class_mem_decl():
            _mem_decl = self.visit(mem_decl)
            if isinstance(_mem_decl, list):
                class_mem_list.extend(_mem_decl if _mem_decl else [])
            else:
                class_mem_list.append(_mem_decl)
        return ClassDecl(name, class_mem_list, super_name)

    def visitClass_mem_decl(self, ctx: D96Parser.Class_mem_declContext):
        return self.visitChildren(ctx)

    def visitAttr_decl(self, ctx: D96Parser.Attr_declContext):
        store_decl = ConstDecl if bool(ctx.VAL()) else VarDecl
        attr_decl_list = self.visit(ctx.getChild(1))
        return_list = []
        for attr_tuple in attr_decl_list:
            if attr_tuple[0].name[0] == '$':
                kind = Static
            else:
                kind = Instance
            if ctx.VAR() and isinstance(attr_tuple[1],
                                        ClassType) and attr_tuple[2] is None:
                attr_data = (attr_tuple[0], attr_tuple[1], NullLiteral())
            else:
                attr_data = attr_tuple
            attr_decl = [AttributeDecl(kind(), store_decl(*attr_data))]
            return_list.extend(attr_decl if attr_decl else [])
        return return_list

    def visitAttr_decl_wo_asg(self, ctx: D96Parser.Attr_decl_wo_asgContext):
        attr_type = self.visit(ctx.any_type())
        attr_name_list = self.visit(ctx.attr_name_list())
        return [(attr_name, attr_type, None) for attr_name in attr_name_list]

    def visitAttr_decl_w_asg(self, ctx: D96Parser.Attr_decl_w_asgContext):
        attr_type, attr_data = self.visit(ctx.attr_decl_rep())
        attr_data = [
            (self.visit(ctx.generic_name()), self.visit(ctx.expr()))
        ] + attr_data
        attr_name, attr_expr = list(zip(*attr_data))
        return list(
            zip_longest(
                attr_name, [attr_type], attr_expr[::-1], fillvalue=attr_type
            )
        )

    def visitAttr_decl_rep(self, ctx: D96Parser.Attr_decl_repContext):
        if ctx.attr_decl_rep():
            attr_type, attr_data = self.visit(ctx.attr_decl_rep())
            return (
                attr_type,
                [(self.visit(ctx.generic_name()), self.visit(ctx.expr()))] +
                attr_data
            )
        elif ctx.any_type():
            return (self.visit(ctx.any_type()), [])

    def visitAttr_name_list(self, ctx: D96Parser.Attr_name_listContext):
        name_list = [self.visit(ctx.generic_name(0))]
        for name in ctx.generic_name()[1:] or []:
            name_list.append(self.visit(name))
        return name_list

    def visitMethod_decl(self, ctx: D96Parser.Method_declContext):
        if ctx.generic_name().ID_NAME():
            return MethodDecl(
                Instance(), Id(ctx.generic_name().ID_NAME().getText()),
                self.visit(ctx.param_list()) if ctx.param_list() else [],
                self.visit(ctx.block_stmt())
            )
        elif ctx.generic_name().STATIC_ID_NAME():
            return MethodDecl(
                Static(), Id(ctx.generic_name().STATIC_ID_NAME().getText()),
                self.visit(ctx.param_list()) if ctx.param_list() else [],
                self.visit(ctx.block_stmt())
            )

    def visitGeneric_name(self, ctx: D96Parser.Generic_nameContext):
        if ctx.ID_NAME():
            return Id(ctx.ID_NAME().getText())
        elif ctx.STATIC_ID_NAME():
            return Id(ctx.STATIC_ID_NAME().getText())

    def visitMethod_local_decl(self, ctx: D96Parser.Method_local_declContext):
        store_decl = ConstDecl if ctx.VAL() else VarDecl
        method_local_decl_list = self.visit(ctx.getChild(1))
        return_list = []
        for method_tuple in method_local_decl_list:
            if ctx.VAR() and isinstance(method_tuple[1],
                                        ClassType) and method_tuple[2] is None:
                method_data = (method_tuple[0], method_tuple[1], NullLiteral())
            else:
                method_data = method_tuple
            method_decl = [store_decl(*method_data)]
            return_list.extend(method_decl if method_decl else [])
        return return_list

    def visitMethod_local_decl_wo_asg(
        self, ctx: D96Parser.Method_local_decl_wo_asgContext
    ):
        method_type = self.visit(ctx.any_type())
        idname_list = self.visit(ctx.idname_list())
        return [(idname, method_type, None) for idname in idname_list]

    def visitMethod_local_decl_w_asg(
        self, ctx: D96Parser.Method_local_decl_w_asgContext
    ):
        method_type, method_data = self.visit(ctx.method_local_decl_rep())
        method_data = [
            (Id(ctx.ID_NAME().getText()), self.visit(ctx.expr()))
        ] + method_data
        method_name, method_expr = list(zip(*method_data))
        return list(
            zip_longest(
                method_name, [method_type],
                method_expr[::-1],
                fillvalue=method_type
            )
        )

    def visitMethod_local_decl_rep(
        self, ctx: D96Parser.Method_local_decl_repContext
    ):
        if ctx.method_local_decl_rep():
            method_type, method_data = self.visit(ctx.method_local_decl_rep())
            return (
                method_type,
                [(Id(ctx.ID_NAME().getText()), self.visit(ctx.expr()))] +
                method_data
            )
        elif ctx.any_type():
            return (self.visit(ctx.any_type()), [])

    def visitCons_method(self, ctx: D96Parser.Cons_methodContext):
        return MethodDecl(
            Instance(), Id("Constructor"),
            self.visit(ctx.param_list()) if ctx.param_list() else [],
            self.visit(ctx.block_stmt())
        )

    def visitDes_method(self, ctx: D96Parser.Des_methodContext):
        return MethodDecl(
            Instance(), Id("Destructor"), [], self.visit(ctx.block_stmt())
        )

    def visitParam_list(self, ctx: D96Parser.Param_listContext):
        param_list = []
        for param in ctx.param() or []:
            _param = self.visit(param)
            if isinstance(_param, list):
                param_list.extend(_param if _param else [])
            else:
                param_list.append(_param)
        return param_list

    def visitParam(self, ctx: D96Parser.ParamContext):
        param_type = self.visit(ctx.any_type())
        idname_list = self.visit(ctx.idname_list())
        return_list = []
        for idname in idname_list:
            return_list.append(VarDecl(idname, param_type, None))
        return return_list

    def visitLiteral_list(self, ctx: D96Parser.Literal_listContext):
        literal_list = [self.visit(ctx.literal(0))]
        for literal in ctx.literal()[1:] or []:
            _literal = self.visit(literal)
            if isinstance(_literal, list):
                literal_list.extend(_literal if _literal else [])
            else:
                literal_list.append(_literal)
        return literal_list

    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        if ctx.FLOAT_LITERAL():
            num = ctx.FLOAT_LITERAL().getText()
            if len(num) > 2 and (num[:2] == '.e' or num[:2] == 'E'):
                return FloatLiteral(float(0))
            else:
                return FloatLiteral(float(num))
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        else:
            return self.visitChildren(ctx)

    def visitInt_literal(self, ctx: D96Parser.Int_literalContext):
        if ctx.DEC_LITERAL():
            return IntLiteral(int(ctx.DEC_LITERAL().getText()))
        elif ctx.HEX_LITERAL():
            return IntLiteral(int(ctx.HEX_LITERAL().getText(), 16))
        elif ctx.OCT_LITERAL():
            return IntLiteral(int(ctx.OCT_LITERAL().getText(), 8))
        elif ctx.BIN_LITERAL():
            return IntLiteral(int(ctx.BIN_LITERAL().getText(), 2))

    def visitBoolean_literal(self, ctx: D96Parser.Boolean_literalContext):
        return BooleanLiteral(bool(ctx.TRUE()))

    def visitStatic_idname_list(self, ctx: D96Parser.Static_idname_listContext):
        name_list = [ctx.STATIC_ID_NAME(0).getText()]
        for name in ctx.STATIC_ID_NAME()[1:] or []:
            _name = self.visit(name)
            if isinstance(_name, list):
                name_list.extend(_name if _name else [])
            else:
                name_list.append(_name)
        return name_list

    def visitIdname_list(self, ctx: D96Parser.Idname_listContext):
        name_list = [Id(ctx.ID_NAME(0).getText())]
        for name in ctx.ID_NAME()[1:] or []:
            name_list.append(Id(name.getText()))
        return name_list

    def visitArray_literal(self, ctx: D96Parser.Array_literalContext):
        return ArrayLiteral(
            self.visit(ctx.literal_list()) if ctx.literal_list() else []
        )

    def visitAny_type(self, ctx: D96Parser.Any_typeContext):
        if ctx.INTEGER():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.ARRAY():
            return ArrayType(
                self.visit(ctx.int_literal()).value, self.visit(ctx.any_type())
            )
        elif ctx.ID_NAME():
            return ClassType(Id(ctx.ID_NAME().getText()))

    def visitExpr_list(self, ctx: D96Parser.Expr_listContext):
        expr_list = [self.visit(ctx.expr(0))]
        for expr in ctx.expr()[1:] or []:
            _expr = self.visit(expr)
            if isinstance(_expr, list):
                expr_list.extend(_expr if _expr else [])
            else:
                expr_list.append(_expr)
        return expr_list

    def visitExpr(self, ctx: D96Parser.ExprContext):
        return self.binary_op(ctx)

    def visitExpr1(self, ctx: D96Parser.Expr1Context):
        return self.binary_op(ctx)

    def visitExpr2(self, ctx: D96Parser.Expr2Context):
        return self.binary_op(ctx)

    def visitExpr3(self, ctx: D96Parser.Expr3Context):
        return self.binary_op(ctx)

    def visitExpr4(self, ctx: D96Parser.Expr4Context):
        return self.binary_op(ctx)

    def visitExpr5(self, ctx: D96Parser.Expr5Context):
        return self.unary_op(ctx)

    def visitExpr6(self, ctx: D96Parser.Expr6Context):
        return self.unary_op(ctx)

    def visitExpr7(self, ctx: D96Parser.Expr7Context):
        if ctx.LSB() and ctx.RSB():
            return ArrayCell(
                self.visit(ctx.expr8()), [self.visit(e) for e in ctx.expr()]
            )
        else:
            return self.visit(ctx.expr8())

    def visitExpr8(self, ctx: D96Parser.Expr8Context):
        return self.field_access(ctx)

    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        return self.field_access(ctx)

    def visitExpr10(self, ctx: D96Parser.Expr10Context):
        if ctx.NEW():
            expr_list = self.visit(ctx.expr_list()) if ctx.expr_list() else []
            return NewExpr(Id(ctx.ID_NAME().getText()), expr_list)
        else:
            return self.visit(ctx.operand())

    def visitOperand(self, ctx: D96Parser.OperandContext):
        if ctx.LP() and ctx.RP():
            return self.visit(ctx.expr())
        elif ctx.ID_NAME():
            return Id(ctx.ID_NAME().getText())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.literal():
            return self.visit(ctx.literal())

    def visitNew_object_expr(self, ctx: D96Parser.New_object_exprContext):
        return NewExpr(
            Id(ctx.ID_NAME().getText()),
            self.visit(ctx.expr_list() if ctx.expr_list() else [])
        )

    def visitAssign_stmt(self, ctx: D96Parser.Assign_stmtContext):
        return Assign(
            self.visit(ctx.assign_lhs()), self.visit(ctx.assign_rhs())
        )

    def visitAssign_lhs(self, ctx: D96Parser.Assign_lhsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        return FieldAccess(
            self.visit(ctx.expr7()), Id(ctx.getChild(2).getText())
        )

    def visitAssign_rhs(self, ctx: D96Parser.Assign_rhsContext):
        return self.visitChildren(ctx)

    def visitFlow_stmt(self, ctx: D96Parser.Flow_stmtContext):
        condition_list = [self.visit(ctx.if_stmt())]
        for cond in ctx.elseif_stmt() or []:
            condition_list.append(self.visit(cond))
        if ctx.else_stmt():
            condition_list.append(self.visit(ctx.else_stmt()))
        return reduce(
            lambda x, y: If(y[0], y[1], x), condition_list[:-1][::-1],
            condition_list[-1] if ctx.else_stmt() else If(*condition_list[-1])
        )

    def visitIf_stmt(self, ctx: D96Parser.If_stmtContext):
        return (self.visit(ctx.expr()), self.visit(ctx.block_stmt()))

    def visitElseif_stmt(self, ctx: D96Parser.Elseif_stmtContext):
        return (self.visit(ctx.expr()), self.visit(ctx.block_stmt()))

    def visitElse_stmt(self, ctx: D96Parser.Else_stmtContext):
        return self.visit(ctx.block_stmt())

    def visitFor_stmt(self, ctx: D96Parser.For_stmtContext):
        expr1, expr2, expr3 = self.visit(ctx.for_range())
        loop = self.visit(ctx.block_stmt()) if ctx.block_stmt() else []
        return For(Id(ctx.ID_NAME().getText()), expr1, expr2, loop, expr3)

    def visitFor_range(self, ctx: D96Parser.For_rangeContext):
        return (self.visit(ctx.expr(e)) for e in ctx.expr())

    def visitBreak_stmt(self, ctx: D96Parser.Break_stmtContext):
        return Break()

    def visitContinue_stmt(self, ctx: D96Parser.Continue_stmtContext):
        return Continue()

    def visitReturn_stmt(self, ctx: D96Parser.Return_stmtContext):
        return Return(self.visit(ctx.expr()) if ctx.expr() else None)

    # TODO
    def visitAny_stmt(self, ctx: D96Parser.Any_stmtContext):
        return self.visitChildren(ctx)

    # TODO
    def visitCall_stmt(self, ctx: D96Parser.Call_stmtContext):
        expr_list = self.visit(ctx.expr_list()) if ctx.expr_list() else []
        return CallStmt(
            self.visit(ctx.getChild(0)), Id(ctx.getChild(2).getText()),
            expr_list
        )

    def visitBlock_stmt(self, ctx: D96Parser.Block_stmtContext):
        stmt_list = []
        for stmt in ctx.any_stmt() or []:
            _stmt = self.visit(stmt)
            if isinstance(_stmt, list):
                stmt_list.extend(_stmt if _stmt else [])
            else:
                stmt_list.append(_stmt)
        return Block(stmt_list)
