import unittest
from TestUtils import TestChecker
from AST import *

# !!! COMMENT THIS OUT
from main.d96.utils.AST import *


class CheckerSuite(unittest.TestCase):
    def test_bkel_1(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"), [
                        MethodDecl(Static(), Id("main"), [], Block([])),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("myVar"), StringType(),
                                StringLiteral("Hello World")
                            )
                        ),
                        AttributeDecl(
                            Instance(), VarDecl(Id("myVar"), IntType())
                        )
                    ]
                )
            ]
        )
        expect = """Redeclared Attribute: myVar"""
        self.assertTrue(TestChecker.test(input, expect, 1))

    def test_bkel_2(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"), [
                        MethodDecl(
                            Static(), Id("main"), [],
                            Block([Assign(Id("myVar"), IntLiteral(10))])
                        )
                    ]
                )
            ]
        )
        expect = """Undeclared Identifier: myVar"""
        self.assertTrue(TestChecker.test(input, expect, 2))

    def test_bkel_3(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"), [
                        MethodDecl(
                            Static(), Id("main"), [],
                            Block(
                                [
                                    ConstDecl(
                                        Id("myVar"), IntType(), IntLiteral(5)
                                    ),
                                    Assign(Id("myVar"), IntLiteral(10))
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        expect = """Cannot Assign To Constant: AssignStmt(Id(myVar),IntLit(10))"""
        self.assertTrue(TestChecker.test(input, expect, 3))

    def test_bkel_4(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"),
                    [MethodDecl(Static(), Id("main"), [], Block([Break()]))]
                )
            ]
        )
        expect = """Break Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 4))

    def test_bkel_5(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"), [
                        MethodDecl(
                            Static(), Id("main"), [],
                            Block(
                                [
                                    ConstDecl(
                                        Id("myVar"), IntType(),
                                        FloatLiteral(1.2)
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        expect = """Type Mismatch In Constant Declaration: ConstDecl(Id(myVar),IntType,FloatLit(1.2))"""
        self.assertTrue(TestChecker.test(input, expect, 5))

    # def test_spec(self):
    #     input = """
    #         Class Shape {
    #             Val $numOfShape: Int = 0;
    #             Val immutableAttribute: Int = 0;
    #             $getNumOfShape() {
    #                 Return Shape::$numOfShape;
    #             }
    #         }
    #         Class Rectangle: Shape {
    #             Var length, width: Int;
    #             getArea() {
    #                 Return Self.length * Self.width;
    #             }
    #         }
    #         Class Program {
    #             main() {
    #                 Out.printInt(Shape::$numOfShape);
    #             }
    #         }
    #     """
    #     expect = """Undeclared Class: Out"""
    #     self.assertTrue(TestChecker.test(input, expect, 69))

    def test_1(self):
        input = """
        Class Program {}
        Class Program {}
        """
        expect = """Redeclared Class: Program"""
        self.assertTrue(TestChecker.test(input, expect, 101))

    def test_2(self):
        input = """
        Class woa: error {}
        Class Program {
            main() {}
        }
        """
        expect = """Undeclared Class: error"""
        self.assertTrue(TestChecker.test(input, expect, 102))

    def test_3(self):
        input = """
            Class Shape {
                sample(num: Int) {}
                sample(num: Int) {}
            }
        """
        expect = """Redeclared Method: sample"""
        self.assertTrue(TestChecker.test(input, expect, 103))

    def test_4(self):
        input = """
            Class Program {
                main() {
                    Var arr: Array[Array[String, 3], 2] = Array(Array(1,1,1),Array(1,1,"a"));
                }
            }
        """
        expect = """Illegal Array Literal: [IntLit(1),IntLit(1),StringLit(a)]"""
        self.assertTrue(TestChecker.test(input, expect, 104))

    def test_5(self):
        input = """
            Class Program {
                Var a: Array[Array[Int, 3], 2] = Array(Array(2, 3, 4), Array());
                main() {}
            }
        """
        expect = """Illegal Array Literal: [[IntLit(2),IntLit(3),IntLit(4)],[]]"""
        self.assertTrue(TestChecker.test(input, expect, 105))

    def test_6(self):
        input = """
            Class Program {
                main() {
                    Val x: Int = 0;
                    Foreach (x In 1 .. 10 By 2) {}
                }
            }
        """
        expect = """Cannot Assign To Constant: AssignStmt(Id(x),IntLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 106))
