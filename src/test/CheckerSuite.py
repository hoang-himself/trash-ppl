import unittest
from TestUtils import TestChecker
from AST import *

# !!! COMMENT THIS OUT
from main.d96.utils.AST import *


class CheckerSuite(unittest.TestCase):
    def test_bkel(self):
        # input = Program(
        #     [
        #         ClassDecl(
        #             Id(Program), [
        #                 MethodDecl(Static(), Id("main"), [], Block([])),
        #                 AttributeDecl(
        #                     Instance(),
        #                     VarDecl(
        #                         Id("myVar"), StringType(),
        #                         StringLiteral("Hello World")
        #                     )
        #                 ),
        #                 AttributeDecl(
        #                     Instance(), VarDecl(Id("myVar"), IntType())
        #                 )
        #             ]
        #         )
        #     ]
        # )
        input = """
        Class Program {
            main() {
                Var myVar: Int;
                Val myConst: Int = 69;
            }
            ## myVar: String = "Hello World"; ##
        }"""
        expect = """Redeclared Attribute: myVar"""
        self.assertTrue(TestChecker.test(input, expect, 1))

    # def test_undeclared_function(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {foo();}"""
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input, expect, 400))

    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn();
    #     }"""
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(getInt(4));
    #     }"""
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program(
    #         [
    #             FuncDecl(
    #                 Id("main"), [], IntType(),
    #                 Block([], [CallExpr(Id("foo"), [])])
    #             )
    #         ]
    #     )
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(
    #                 Id("main"), [], IntType(),
    #                 Block(
    #                     [], [
    #                         CallExpr(
    #                             Id("putIntLn"),
    #                             [CallExpr(Id("getInt"), [IntLiteral(4)])]
    #                         )
    #                     ]
    #                 )
    #             )
    #         ]
    #     )
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input, expect, 404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(
    #                 Id("main"), [], IntType(),
    #                 Block([], [CallExpr(Id("putIntLn"), [])])
    #             )
    #         ]
    #     )
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input, expect, 405))
