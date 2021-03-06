import unittest
from TestUtils import TestChecker
from AST import *

# !!! COMMENT THIS OUT
from main.d96.utils.AST import *


class CheckerSuite(unittest.TestCase):
    def test_spec(self):
        input = """
            Class Program {
                main() {
                    Var num: Int = 3.4;
                }
            }
        """
        expect = """Type Mismatch In Statement: VarDecl(Id(num),IntType,FloatLit(3.4))"""
        self.assertTrue(TestChecker.test(input, expect, 69))

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

    def test_400(self):
        input = """
            Class Program { main() {} }
            Class a {
                a(a: Int; a:String) {}
            }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_401(self):
        input = """
            Class a {
                Var a: Int;
                a() {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_402(self):
        input = """
            Class Program { main() {} }
            Class a {
                b() {
                    Var a: Int;
                    Var a: Int;
                }
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_403(self):
        input = """
            Class Program { main() {} }
            Class a {
                b() {
                    Val a: Int = 1;
                    Val a: Int = 1;
                }
            }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_404(self):
        input = """
            Class Program { main() {} }
            Class a {
                b(a: Int) {
                    Val a: Int = 1;
                }
            }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_405(self):
        input = """
            Class Program { main() {} }
            Class a {
                b() {
                    Var a: Int = 1;
                    {
                        Var a: Int = 1;
                        Var b: Int = 1;
                        Var b: Int = 1;
                    }
                }
            }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_406(self):
        input = """
            Class Program { main() {} }
            Class Shape {
                sample(num: Int) {}
                sample(num: Int) {}
            }
        """
        expect = """Redeclared Method: sample"""
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_407(self):
        input = """
            Class Program {
                main() {
                    Val x: Int = 0;
                    Foreach (x In 1 .. 10 By 2) {}
                }
            }
        """
        expect = """Cannot Assign To Constant: AssignStmt(Id(x),IntLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_408(self):
        input = """
            Class Program {
                main() {
                    Var arr: Array[Array[String, 3], 2] = Array(Array(1,1,1),Array(1,1,"a"));
                }
            }
        """
        expect = """Illegal Array Literal: [IntLit(1),IntLit(1),StringLit(a)]"""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_409(self):
        input = """
            Class Program {
                Var a: Array[Array[Int, 3], 2] = Array(Array(2, 3, 4), Array());
                main() {}
            }
        """
        expect = """Illegal Array Literal: [[IntLit(2),IntLit(3),IntLit(4)],[]]"""
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_410(self):
        input = """
            Class Program { main() {} }
            Class a {
                b() {
                    Var b: Int = 1;
                    Var c: Int = 1;
                    a = 1;
                }
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_411(self):
        input = """
            Class Program { main() {} }
            Class B {}
            Class A {
                b() {
                    Var b: Int = 1;
                    Var c: A;
                    Var a: C;
                }
            }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_412(self):
        input = """
            Class Program { main() {} }
            Class B {
                Val b: Int = 1;
            }
            Class A {
                b() {
                    Var b: Int = 1;
                    Var c: B;
                    c.b = 1;
                    c.c = 1;
                }
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_413(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var b: Int = 1;
                c() {}
            }
            Class A{
                b() {
                    Var b: Int = 1;
                    c.b = 1;
                    c.c = 1;
                }
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_414(self):
        input = """
            Class Program { main() {} }
            Class B {
                Var b: Int = 1;
                c() {}
            }
            Class A {
                b() {
                    Var b: Int = 1;
                    Var c: B = New B();
                    c.b = 1;
                    c.c();
                    c.d();
                }
            }
        """
        expect = "Undeclared Method: d"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_415(self):
        input = """
            Class Program { main() {} }
            Class B {
                Var b: Int = 1;
                c() {}
            }
            Class A: B {}
            Class C: D {}"""
        expect = "Undeclared Class: D"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_416(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var b: Int = 1;
                c(){}
            }
            Class A:B{}
            Class C{
                e(){
                    Var a:A;
                    a.b = 2;
                    a.c();
                    a.e = 2;
                }
            }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_417(self):
        input = """
            Class Program { main() {} }
            Class B{}
            Class A:B{
                Var b: Int = 1;
                c(){}
            }
            Class C{
                e(){
                    Var a:A = New A();
                    a.b= 2;
                    a.c();
                    a.e();
                }
            }"""
        expect = "Undeclared Method: e"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_418(self):
        input = """
            Class Program { main() {} }
            Class C {
                e() {
                    Val a: Int = 2;
                    a = 3;
                }
            }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_419(self):
        input = """
            Class Program { main() {} }
            Class C{
                e(){
                    Var a: Int = 2;
                    Var b:Array[Int,5];
                    a = 3;
                    b[1]=1;
                    a[1]=1;
                }
            }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_420(self):
        input = """
            Class Program { main() {} }
            Class C{
                e(){
                    Var a: Int = 2;
                    Var b:Array[Int,5];
                    b[1.2]=1;
                }
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),[FloatLit(1.2)])"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_421(self):
        input = """
            Class Program { main() {} }
            Class C{
                e(){
                    Var a: Int = 1+2;
                    Var b:Float = 1+2.2;
                    Var c:Float = 1+True;
                }
            }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_422(self):
        input = """
            Class Program { main() {} }
            Class C{
                e(){
                    Var c:String = "abc" +. "def";
                    Var d:Boolean = ("abc" +. "def") ==. "ghi";
                    Var e:String = ("abc" ==. "def") +. "ghi";
                }
            }"""
        expect = "Type Mismatch In Expression: BinaryOp(+.,BinaryOp(==.,StringLit(abc),StringLit(def)),StringLit(ghi))"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_423(self):
        input = """
            Class Program { main() {} }
                Class C{
                e(){
                    Var c:Float = 1.22;
                    Var d:Boolean = (("abc" +. "def") ==. "ghi") || False;
                    Var e:Boolean = 0==False;
                    Var f:Boolean = "abc"||1;
                }
            }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,IntLit(0),BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):
        input = """
            Class Program { main() {} }
            Class C{
                e(){
                    Var c:Float = --------1.22;
                    Var d:Boolean = !((("abc" +. "def") ==. "ghi") || False);
                    Var e:Float = !!!!--1.22;
                }
            }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,UnaryOp(-,UnaryOp(-,FloatLit(1.22))))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var b: Int = 1;
                c(g: Int; h:Float){
                    Return 1;
                }
                d(){}
            }
            Class C{
                e(){
                    Var a: B = New B();
                    Var d: Int = a.c(1,2);
                    Var e: Int = a.c(1,"abc");
                }
            }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(c),[IntLit(1),StringLit(abc)])"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_426(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var b: Int = 1;
                c(g: Int; h:Float){
                    Return 1;
                }
                d(){}
            }
            Class C{
                e(){
                    Var a:B = New B();
                    Var d:Float = a.c(1,2);
                    Var e:String = a.c(1.1,2);
                }
            }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(c),[FloatLit(1.1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_427(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var b: Int = 1;
                c(g: Int; h:Float){
                    Return 1;
                }
                d(){}
            }
            Class C{
                e(){
                    Var a:B = New B();
                    Var d:Float = a.c(1,2);
                    Var e:String = a.c(1.1,2);
                }
            }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(c),[FloatLit(1.1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_428(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var b: Int = 1;
                c(g: Int; h:Float){
                    Return 1;
                }
                d(){}
            }
            Class C{
                e(){
                    Var a:B;
                    Var d:Float = a.c(1,2);
                    Var e:String = a.c(1,2);
                }
            }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(e),StringType,CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_429(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var b: Int = 1;
                c(g: Int; h:Float){
                    Return 1;
                }
                d(){}
            }
            Class C{
                e(){
                    Var a:B;
                    Var d:Float = a.c(1,2);
                    a.d();
                    Var e:String = a.d();
                }
            }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(d),[])"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_430(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var b: Int = 1;
                c(g: Int; h:Float){
                    Return 1;
                }
                d(){}
            }
            Class C{
                e(){
                    Var a:B = New B();
                    Var d:Float = a.c(1,2);
                    a.d();
                    Var e:Float = a.b;
                    Var f:Float = a.d;
                }
            }"""
        expect = "Undeclared Attribute: d"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_431(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var b: Int = 1;
                c(g: Int; h:Float){
                    Return 1;
                }
                d(){}
            }
            Class C{
                e(){
                    Var a:B = New B();
                    Var d:Float = a.c(1,2);
                    a.d();
                    Var e:Float = a.b;
                    Var f:String = a.b;
                }
            }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(f),StringType,FieldAccess(Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_432(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var b: Int = 1;
                c(g: Int; h:Float){
                    Return 1;
                }
                d(){}
            }
            Class C{
                e(){
                    Val a:B = New B();
                    Val d:Float = a.c(1,2);
                    Val e:String = a.c(1,2);
                }
            }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(e),StringType,CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_433(self):
        input = """
            Class Program { main() {} }
            Class C{
                e(){
                    Val a : Int = 1.2;
                }
            }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_434(self):
        input = """
            Class Program { main() {} }
            Class C{
                e(){
                    Val a : Float = -(1.2 +1);
                    Val b : Float = -(1 + 1);
                    Val c : Boolean = !!((1>2)&&(True || ("abc"==."cef")));
                    Val d :String = ("abc" +. "def")+."ghi";
                    Val e :String = True==1;
                }
            }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,BooleanLit(True),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_435(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var b: Int = 1;
                c(g: Int; h:Float){
                    Return 1;
                }
                d(){}
            }
            Class C{
                e(){
                    Val a:B = New B();
                    Val d:Float = a.c(1,2);
                    Val e:String = a.d(1,2);
                }
            }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(d),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_436(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var b: Int = 1;
                c(g: Int; h:Float){
                    Return 1;
                }
                d(x: Int; y:Float; z:String){}
            }
            Class C{
                e(){
                    Val a:B = New B();
                    Val d:Float = a.c(1,2);
                    a.d(1,2,"a");
                    a.d(1,2,3);
                }
            }"""
        expect = "Type Mismatch In Statement: Call(Id(a),Id(d),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_437(self):
        input = """
        Class Program {
            mainN() {
                Var a: Boolean = !True;
            }
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_438(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var b: Int = 1;
                c(g: Int; h:Float){
                    Return 1;
                }
                d(x: Int; y:Float; z:String){}
            }
            Class C{
                e(){
                    Val a:B = New B();
                    Val d:Float = a.c(1,2);
                    a.d(1+2,2--2.0,"a"==."bcd");
                }
            }"""
        expect = "Type Mismatch In Statement: Call(Id(a),Id(d),[BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(-,IntLit(2),UnaryOp(-,FloatLit(2.0))),BinaryOp(==.,StringLit(a),StringLit(bcd))])"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_439(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var b: Int = 1;
                c(g: Int; h:Float){
                    Return 1;
                }
                d(x: Int; y:Float; z:String){}
            }
            Class C{
                e(){
                    Val a:B = New B();
                    Val d:Float = a.c(1,2);
                    a.d(1+2,2--2.0,("a"==."bcd")+1);
                }
            }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,BinaryOp(==.,StringLit(a),StringLit(bcd)),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_440(self):
        input = """
            Class B{
                Var b: Int = 1;
                c(g: Int; h:Float){
                    Return 1;
                }
                d(x: Int; y:Float; z:String){}
            }
            Class A{}
            Class C{
                e(){}
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_441(self):
        input = """
            Class B{
                Var b: Int = 1;
                c(g: Int; h:Float){
                    Return 1;
                }
                d(x: Int; y:Float; z:String){}
            }
            Class A:B{}
            Class C{}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_442(self):
        input = """
            Class Program { main() {} }
            Class C{
                e(){
                    Val a: Int = 1;
                    Val b:Float = 1;
                    Val c:Float = a+b;
                    Val d: Int = a+b;
                }
            }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(d),IntType,BinaryOp(+,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_443(self):
        input = """
            Class Program { main() {} }
            Class C{
                e(){
                    Var a: Int = 1;
                    Var b:Float = 1;
                    Var c:Float = a+b;
                    Var d: Int = a+b;
                }
            }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(d),IntType,BinaryOp(+,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_444(self):
        input = """
            Class Program { main() {} }
            Class C{
                e(){
                    Var a: Int = 1;
                    Var b: Int = 1;
                    If (True){
                        Var a: Int = 2;
                    }
                    Elseif(True){
                        Var a: Int = 2;
                    }
                    Else{
                        Var a: Int = 2;
                    }
                    Var b: Int = 2 ;
                }
            }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_445(self):
        input = """
            Class Program { main() {} }
            Class C {
                e() {
                    Var a: Int = 1;
                    Var b: Int = 1;
                    Var i: Int = 0;
                    Foreach(i In 1 .. 10 By 1) {
                        Var a: Int = 1;
                        Break;
                        If (True) {
                            Var a: Int = 1;
                            Continue;
                        }
                    }
                    Var b: Int = 2;
                }
            }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_446(self):
        input = """
            Class Program { main() {} }
            Class C{
                e(){
                    Var i: Int = 0;
                    Foreach(i In 1 .. 10 By 1){
                        Var a: Int = 1;
                        Break;
                        If (True){
                            Var a: Int = 1;
                            Continue;
                        }
                    }
                    Break;
                }
            }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_447(self):
        input = """
            Class Program { main() {} }
            Class C{
                e(){
                    Var i: Int = 0;
                    Foreach(i In 1 .. 10 By 1){
                        Var a: Int = 1;
                        Break;
                        If (True){
                            Var a: Int = 1;
                            Continue;
                        }
                    }
                    Continue;
                }
            }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_448(self):
        input = """
            Class C{
                e(){
                    Var a: Int = 0;
                    Val b: Int = 1;
                    Val c:Float = b+1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_449(self):
        input = """
            Class Program { main() {} }
            Class C{
                e(){
                    Var a: Int = 0;
                    Val b: Int = 1;
                    Val c:Float = b+1;
                    Val d:Float = a + "abc";
                }
            }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_450(self):
        input = """
            Class Program { main() {} }
            Class C{
                e(){
                    Var a: Int = 0;
                    Val b: Int = 1;
                    Val c:Float = b+1;
                    Val d:Float = a + "abc";
                }
            }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_451(self):
        input = """
            Class Program { main() {} }
            Class C{
                e(){
                    Var a: Int = 0;
                    Val b: Int = 1;
                    Val c:Float = b+1;
                }
            }
            Class Car {
                Var a : Int = 10;
                foo() {
                    Var x : Int = Self.a;
                    Var y : Int = a;
                }
            }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_452(self):
        input = """
            Class Program { main() {} }
            Class Car {
                foo() {
                    Var a:Array[Int,2];
                    a = Array(1,2);
                    a = Array(1,2.3);
                }
            }"""
        expect = "Illegal Array Literal: [IntLit(1),FloatLit(2.3)]"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_453(self):
        input = """
        Class Program {
            foo() {
                Return 1;
            }
            main() {
                Var a:Int = Self.foo(1);
            }
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Self(),Id(foo),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_454(self):
        input = """
        Class Program {
            mainN() {
                Var a: Boolean = True || False;
            }
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_455(self):
        input = """
        Class E {
            func() {}
        }

        Class Program{
            test() {
                Var e: E = New E();
                Return e.func;
            }

            main() {}
        }"""
        expect = "Undeclared Attribute: func"
        self.assertTrue(TestChecker.test(input, expect, 455))

    # def test_456(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var arr: Array[Array[Int,2], 3];
    #             Var a: String = arr[1][2];
    #         }
    #     }"""
    #     expect = "Type Mismatch In Statement: VarDecl(Id(a),StringType,ArrayCell(Id(arr),[IntLit(1),IntLit(2)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 456))

    def test_457(self):
        input = """
        Class Program {
            main() {
                Var arr: Array[Array[Int,2], 3];
                Var a: Int = arr[1];
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,ArrayCell(Id(arr),[IntLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_458(self):
        input = """
        Class Program {
            main() {
                Var arr: Array[Int,2] = Array(1, 2);
                Var a: String = arr[1];
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),StringType,ArrayCell(Id(arr),[IntLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_459(self):
        input = """
        Class Program {
            main() {
                Var arr: Array[Int,2] = Array(1, 2, 3);
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(arr),ArrayType(2,IntType),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_460(self):
        input = """
        Class Program {
            main() {
                Return 1;
            }
        }"""
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_461(self):
        input = """
            Class A{
                $a(){
                    Return 1;
                }
                b(){
                    Return 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_462(self):
        input = """
            Class A{
                $a(){
                    Return 1;
                }
                b(){
                    Return 1;
                }
            }
            Class Program{
                c(){
                    Return 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_463(self):
        input = """
            Class A{
                $a(){
                    Return 1;
                }
                b(){
                    Return 1;
                }
            }
            Class Program{
                $main(){
                    Return 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_464(self):
        input = """
            Class A{
                $a(){
                    Return 1;
                }
                b(){
                    Return 1;
                }
            }
            Class Program{
                $main(a: Int){}
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_466(self):
        input = """
            Class Program { main() {} }
            Class A{
                Var a: Int = 1;
                foo(){
                    Var b: Int = Self.a;
                    Var c: Int = a;
                }
            }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 466))

    # def test_467(self):
    #     input = """
    #     Class O {
    #         Var $a: String = "1";
    #     }
    #     Class Program {
    #             main() {
    #                 Var b: Int = O.a;
    #             }
    #         }"""
    #     expect = "Illegal Member Access: FieldAccess(Id(O),Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, 467))

    def test_468(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var x: Int = 1;
                foo(){
                    Return 1;
                }
                func (){
                    Var a: Int = Self.x;
                    a = Self.foo();
                    Var b:String = Self.foo();
                }
            } """
        expect = "Type Mismatch In Statement: VarDecl(Id(b),StringType,CallExpr(Self(),Id(foo),[]))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_469(self):
        input = """
            Class Program { main() {} }
            Class B{
                Var x: Int = 1;
                foo(){
                    Return 1;
                }
                func (){
                    Var a: Int = Self.x;
                    a = Self.foo();
                    Var b:String = Self.foofoo();
                }
            } """
        expect = "Undeclared Method: foofoo"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_470(self):
        input = """
            Class Program { main() {} }
            Class E {
                func() {}
            }
            Class Test{
                test() {
                    Var e: E = New E();
                    Return e.func;
                }
            }"""
        expect = "Undeclared Attribute: func"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_471(self):
        input = """
            Class Program { main() {} }
            Class E {
                func() {}
                Constructor(a: Int){}
            }
            Class Test{
                Var e: E = New E(1);
                Var b: E = New E();
            }"""
        expect = "Type Mismatch In Expression: NewExpr(Id(E),[])"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_472(self):
        input = """
        Class O {}
        Class Program {
                main() {
                    Var a: O = New O(1);
                }
            }"""
        expect = "Type Mismatch In Expression: NewExpr(Id(O),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_473(self):
        input = """
        Class Program {
            mainN() {
                Var a: Boolean = 1 == 2;
            }
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_474(self):
        input = """
        Class Program {
            mainN() {
                Var a: Boolean = "True" ==. "True";
            }
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_475(self):
        input = """
            Class A {
                Var a: Int = 1;
            }
            Class B{
                Var b:A = New A();
            }
            Class C{
                foo(){
                    Var c:B = New B();
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_476(self):
        input = """
            Class A {
                Var a: Int = 1;
            }
            Class B{
                Var b:A = New A();
            }
            Class C{
                foo(){
                    Var c:B = New B();
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_477(self):
        input = """
            Class A {
                Var a: Int = 1;
            }
            Class B{
                Var $b:A = New A();
            }
            Class C{
                foo(){
                    Var c:B = New B();
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_478(self):
        input = """
            Class A {
                Var a: Int = 1;
            }
            Class B{
                Var $b:A = New A();
            }
            Class C{
                foo(){
                    Var c:B = New B();
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_479(self):
        input = """
            Class Program { main() {} }
            Class A {
                Var a: Int = 1;
                foo(){
                    Return 1;
                }
            }
            Class B{
                Var b:A = New A();
                foo(){
                    Return New A();
                }
            }
            Class C{
                foo(){
                    Var c:B = New B();
                    Var f: Int = c.foo();
                }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(f),IntType,CallExpr(Id(c),Id(foo),[]))"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_480(self):
        input = """
            Class A {
                Var a: Int = 1;
                foo(x:Float; y:String){}
            }
            Class B{
                Var b:A = New A();
                foo(){
                    Return New A();
                }
            }
            Class C{
                foo(){
                    Var c:B = New B();
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_481(self):
        input = """
            Class Program { main() {} }
            Class A {
                Var a: Int = 1;
                fooExp(x:Float; y:String){
                    Return 1;
                }
                fooCall(x:Float; y:String){}
            }
            Class B{
                Var b:A = New A();
                foo(){
                    Return New A();
                }
                foo2(){
                    Var e: Int = Self.b;
                }
            }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(e),IntType,FieldAccess(Self(),Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_482(self):
        input = """
        Class Program {
            foo() {
                Return 1;
            }
            main() {
                Var a:Int = Self.foo(1);
            }
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Self(),Id(foo),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 482))

    # def test_483(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a: Array[Array[Int, 2], 2] = Array(Array(1, 2), Array("1", "2"));
    #         }
    #     }"""
    #     expect = "Illegal Array Literal: [[IntLit(1),IntLit(2)],[StringLit(1),StringLit(2)]]"
    #     self.assertTrue(TestChecker.test(input, expect, 483))

    def test_484(self):
        input = """
        Class Program {
            main() {
                Var a: Array[Int, 2] = Array(1, "2");
            }
        }"""
        expect = "Illegal Array Literal: [IntLit(1),StringLit(2)]"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_485(self):
        input = """
        Class O {
            $foo() {}
        }
        Class Program {
            foo() {}
            main() {
                Var a: Int = O::$foo();
            }
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(O),Id($foo),[])"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_486(self):
        input = """
        Class Program {
            main() {
                Var i : Int;
                Foreach (i In 1 .. 100 By 2) {
                    Break;
                    Continue;
                    Var a: String = i;
                }
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),StringType,Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_487(self):
        input = """
        Class Program {
            main() {
                Var i : Int;
                Var a: String = "1";
                Foreach (i In 1 .. 100 By 2) {
                    Break;
                    Continue;
                    a = a + i;
                }
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_488(self):
        input = """
        Class Program {
            main() {
                Var i : Int;
                Var a: String = "1";
                Foreach (i In 1 .. 100 By 2) {
                    a = a + i;
                }
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_489(self):
        input = """
            Class Program { main() {} }
            Class A {
                $fooExp1(x:Float; y:String){
                Var a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1,"a"));
                }
            }"""
        expect = "Illegal Array Literal: [IntLit(1),IntLit(1),StringLit(a)]"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_490(self):
        input = """
            Class Program { main() {} }
            Class A {
                $fooExp1(){
                    Var a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                    a[1] = Array(1,1);
                    a[1][1] = 1;
                    a = 1;
                }
            }"""
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(1)]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_491(self):
        input = """
            Class Program { main() {} }
            Class A {
                $fooExp1(){
                    Val a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                    a[1] = Array(1,1);
                }
            }"""
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(Id(a),[IntLit(1)]),[IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_492(self):
        input = """
            Class Program { main() {} }
            Class A {
                Var a: Int = 2;
                fooExp1(){
                    Self.a = "abc";
                }
            }"""
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(a)),StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_493(self):
        input = """
            Class Program { main() {} }
            Class A {
                Var myArray: Array[Array[Array[Int,4],2],2] = Array(
                    Array(
                        Array(1,2,3,4),
                        Array(5,6,7,8)
                    ),
                    Array(
                        Array(1,2,3,4),
                        Array(5,6,7,False)
                    )
                );
            }
        """
        expect = "Illegal Array Literal: [IntLit(5),IntLit(6),IntLit(7),BooleanLit(False)]"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_494(self):
        input = """
            Class Program { main() {} }
            Class A {
                foo() {
                    Var a: Array[Array[Int, 3], 1] = Array(Array(1,2,3));
                    a[1][2] = 4;
                }
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_495(self):
        input = """
            Class Student {
                Var name: String;
                Var ID: Int;
                Constructor(newName: String; newID : Int) {
                    Self.name = "a";
                    Self.name = newName;
                    Self.ID = newID;
                }
            }
            Class Program {
                main() {
                    Var myStudent: Student = New Student ();
                }
            }
        """

        expect = "Type Mismatch In Expression: NewExpr(Id(Student),[])"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_496(self):
        input = """
            Class Program { main() {} }
            Class A {}
            Class B:A {
                Var a: A = New C();
            }
        """

        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_497(self):
        input = """
            Class A {}
            Class B:A {
                Var a: A = New B();
            }
            """

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_498(self):
        input = """
            Class Program{
                Val $someStatic : Int = 10;
                foo() {
                    Var Program : Float = 1.0;
                    Var x : Int = Program::$someStatic;
                }
            }
        """

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_499(self):
        input = """
            Class A {
                Var foo: Int = 1;
                foo() {}
            }
        """

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_500(self):
        input = """
            Class B {
                Var $a: Int = 1;
                Val $b: Int = 2;
                foo(){
                    Val c: Int = 1;
                    Return 1;
                }
            }
            """

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 500))
