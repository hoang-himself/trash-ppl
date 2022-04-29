import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_blank_program(self):
        input = r'''
Class Program {
    main() {
        a.foo(2+1);
    }
}
'''
        expect = r'successful'
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_blank_class(self):
        input = r'''
Class main {}
'''
        expect = r'successful'
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_inheritance(self):
        input = r'''
Class Rectangle: Shape {
    getArea() {
        Return Self.length * Self.width;
    }
}
'''
        expect = r'successful'
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_static_method(self):
        input = r'''
Class Shape {
    $getNumOfShape() {
        Return Self.length * Self.width;
    }
}
'''
        expect = r'successful'
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_wrong_miss_close(self):
        input = r'''
Class Program {
    main( {}
}'''
        expect = r'Error on line 3 col 10: {'
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_literal_attr(self):
        input = r'''
Class other {
    Var int_oct8: Int = 00357;
    Var int_hex16: Int = 0X_DEA_DBE_EF;
    Var int_bin2: Int = 0b0001_1100;
    Val fuck_10base: Int = 69_420;

    Val $goodFlag: Boolean = True;
    Val $badFlag: Boolean = False;
}
Class Program {
    Var norm_float: Float = 1.234;
    Var full_form_float: Float = 1.2e3;
    Var no_frac_float: Float = 7E-10;
    main() {
        Val good: String="Congratulations";
        Val bad: String = "Fuck off";
    }
}'''
        expect = r'successful'
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_multi_assign(self):
        input = r'''
Class Program {
    Val sample_array: Array[Int, 2] = (1, 2);
    Var a, $b: Int = 1, 2;
    main() {}
}'''
        expect = r'successful'
        self.assertTrue(TestParser.test(input, expect, 207))

    def normal_oop(self):
        input = r'''
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    $getNumOfShape() {
        Return $numOfShape;
    }
}
Class Rectangle: Shape {
    getArea() {
        Return Self.length * Self.width;
    }
}
Class Program {
    main() {
        Out.printInt(Shape::$numOfShape);
    }
}
'''
        expect = r'successful'
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_1(self):
        input = '''Class r:_q{}Class _B{}Class _6{}Class o{}Class a3S:_{}Class fv:L{Destructor (){}$28(C,__:Array [String ,68]){}$W8(){Val _,__:Float ;}$_Q_(_dy5__:Array [Array [String ,0x46],4_6]){}Var _m:rv;}Class E{}Class sx{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 401))

    def test_2(self):
        input = '''Class Y{Constructor (RY5:Array [Array [Array [Int ,0x50],051],04];Z:Boolean ;G_:String ;_:Boolean ){}Var $18H_95,$9,$T,__R,$_,$8_,$_699t:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 402))

    def test_3(self):
        input = '''Class X:bc5F7x_{}Class _:_{}Class WM{$r_(_:Boolean ;_:Array [Boolean ,0b1];_:_;__:String ;R_,_6,q:Array [Boolean ,010]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 403))

    def test_4(self):
        input = '''Class r:C{Constructor (_:Float ;Q_2:Boolean ;t_c:Array [Array [String ,0X3],5_7_1];QT,_,Cl_,__e8,_:String ){} }Class Y{}Class _m:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 404))

    def test_external_5(self):
        input = '''Class _{Val _:String ;Destructor (){}Val $1:Array [String ,0b1_1_1010];Val _,$__,Z_,_,U_:Array [Float ,92];Destructor (){} }Class _2:u6{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 405))

    def test_external_6(self):
        input = '''Class R:_{Val l,_:Int ;}Class Y:A{Constructor (_9,_:Array [Array [Array [Array [Array [Array [Float ,0x8_4_9],014],0B110000],06],014],38]){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 406))

    def test_external_7(self):
        input = '''Class o{}Class _:g_{Constructor (_,d:Array [Array [Float ,02_0],60]){}Val E,$6,_,$7,_:Boolean ;}Class zj:_gB_f{Val $_,$8S:Array [Array [Boolean ,2],0B1_00];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 407))

    def test_external_8(self):
        input = '''Class _{}Class _6_{Constructor (){}Constructor (x3,su5S_:Boolean ){}$h(){}H4(){}Var $_,$_V,$___:Array [Boolean ,0b1_0];Var l,$c_L_X:e_;}Class O{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 408))

    def test_external_9(self):
        input = '''Class ph:S{}Class __:G_0{Constructor (){Continue ;} }Class _{}Class _2hlA_{Var _A:_3;Val $5_:Array [String ,0X51];Val z:Int ;}Class X:R_{$y(P_:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 409))

    def test_external_10(self):
        input = '''Class f{Constructor (J,_9,v4:Array [Int ,0x47];_z,r_ApA_:Array [Int ,0B10_1];Z,g__,L:Array [Int ,8];_j,__,d3_m_:s07){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 410))

    def test_external_11(self):
        input = '''Class W_{}Class _:_{Val z0,_,I:Array [Array [Array [Array [Array [Boolean ,0x44],0xA_5_A],75],057],0XD];}Class g:e7{}Class _:a6_{}Class nO{}Class g:L_1{Val $b9,$Q,$__9:Boolean ;}Class f3:I_{}Class _0S_:SjT{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 411))

    def test_external_12(self):
        input = '''Class L:A_6A_{}Class d{Var _,$42,$_1D:Array [Array [String ,032],032];Val $J:Array [Float ,0b1100011];Val ___:Boolean ;}Class I:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 412))

    def test_external_13(self):
        input = '''Class p:S{}Class _{Destructor (){}_(_0_4_,f,_8,_,_y,F:Array [Array [Array [Boolean ,6],0140],0XAD_E8]){}Var K:Int ;}Class _{$K(_44,_z,_,_z_r:Array [String ,8_5_8];_1__,__:Boolean ;K:Array [Int ,0b111011]){}Constructor (){}Var $8_,__:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 413))

    def test_external_14(self):
        input = '''Class F{Constructor (){} }Class J{Destructor (){Var rc:String ;}Constructor (F1,Spj_:Int ;_H_0:Array [Array [String ,0x4],0x46]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 414))

    def test_external_15(self):
        input = '''Class Q{}Class _:q4{Constructor (C:Y){Continue ;}Destructor (){Val da,C:_y;} }Class H___61K:_{Constructor (){}Constructor (){}Constructor (_:Array [Float ,0B1010101];__l8,_:Int ){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 415))

    def test_external_16(self):
        input = '''Class h:Aam{Val _J:Array [Array [Array [Array [Int ,0X5D],0x63],01],6];Destructor (){} }Class _b_z__U:_gL{Destructor (){Break ;} }Class _X{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 416))

    def test_external_17(self):
        input = '''Class _{Val _:Array [Array [Boolean ,0b10101],3];}Class s:__{Val $R,$1:r;Constructor (_By ,j2:_;D,y,e744,_:Int ;Z,l,J_U,R___,R,Z_,C:Array [Array [Array [Array [String ,2],42],0137],0B1];c0,_:Int ;qH:Array [Int ,8_7_62_01];___,K:Array [Int ,0137]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 417))

    def test_external_18(self):
        input = '''Class __V_5_8:_H{Constructor (_:Boolean ){}Val $I,__,r__K:Array [Boolean ,07];}Class __{Var _:Array [Int ,0XF];Var $_:V__;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 418))

    def test_external_19(self):
        input = '''Class __{Constructor (){}Constructor (_,_,Q,_:Array [Array [Boolean ,062],64];_:Array [Array [Array [Boolean ,0X24],0b1011110],0x440_F];Om:Float ;x1:Array [String ,07407]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 419))

    def test_external_20(self):
        input = '''Class F_{Var _0,wkN,$5V:Array [String ,0x7_8];}Class __72{}Class _:_K___0{icC4(_51_,s,I:Array [Float ,0B11000]){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 420))

    def test_external_21(self):
        input = '''Class r9____O:g{$_(){}Var $__M6,$f,w9:Array [Array [Array [Int ,1_1],0b1001111],21];}Class h_q_:D{}Class R_:m{Var __,e:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 421))

    def test_external_22(self):
        input = '''Class g7{}Class ___:_L{s(C:_;_W_:Array [Array [Array [String ,3_02_5],0X2D],035]){}Var $V:Array [Array [Array [String ,88],88],0XF_6];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 422))

    def test_external_23(self):
        input = '''Class _{Val $p0Y6__S1,B:String ;}Class W{Constructor (S__6_J_:_;b:Array [Array [Array [Array [String ,031],031],4],3];__:Array [Boolean ,0B1100001]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 423))

    def test_external_24(self):
        input = '''Class __:_c{Var t:Array [Array [Array [Array [Array [Array [Array [Array [Int ,0b1010001],0x1F],0B10],0b1010001],047],0b11],0b10],0b1010001];$8(){Continue ;Continue ;{Break ;} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 424))

    def test_external_25(self):
        input = '''Class K_:h{Var k,$9,CB,Z,$_,F,$_,$_,$_V7o,m__:Array [Array [Array [Array [Float ,0b110011],0X10],02],0B1];}Class mh:UK{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 425))

    def test_external_26(self):
        input = '''Class __3_E1{Constructor (_,__P,_,R,vPg,z:Array [Array [Float ,0B1000101],0b1001110];_,_:String ;_o__0,_,_,Z_HM_4S,D3Y:Array [Boolean ,65]){Var X:String ;} }Class j5__{}Class V6:_50{Destructor (){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 426))

    def test_external_27(self):
        input = '''Class __:kM__A{Var _1_Z,_0:Int ;O9(___8l_:_e;V:h3;_N4_36,_,_X,On12:Int ;_P_:Int ){}$2_(P95,_,b,k829,_0d:Array [String ,0x1E];_w_,bL6,k:String ;_e4:Boolean ;Xr2,_axXfM_8:String ;_Iv,hGT_:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 427))

    def test_external_28(self):
        input = '''Class a{$_(){Return ;Break ;}Var $v,b_:_1;}Class _:_{Var O:Array [Array [Array [Array [Array [String ,0B1_0_0],02],5],020],020];Constructor (_,T:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 428))

    def test_external_29(self):
        input = '''Class QV:_0{Val _:__;Val c_72:Array [Array [Array [Array [Float ,92],047],0XC4BEE8],6_8];}Class N:_{Constructor (G,_,h_:Array [String ,0x8];__J:Boolean ;L,p_8_,_4:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 429))

    def test_external_30(self):
        input = '''Class _{}Class _R9{__9_(){}Destructor (){ {} }Var $__,$8,_,_S_59w,$e,$_b:Array [String ,0B1];_(_qGz,_:Float ){Val j,u:Boolean ;} }Class H:_0F55_{}Class N{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 430))

    def test_external_31(self):
        input = '''Class O_:_1{Destructor (){Continue ;} }Class i{_1_Ne7m__(L,_,N,S57eH366,m,r4:Int ;r1_d,_:b_R;_:_;K3:w;C:Array [Array [Float ,0X19],76]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 431))

    def test_external_32(self):
        input = '''Class _5_{Constructor (_4:Boolean ){}Var $_,__,__:String ;Val $_,_Y1:Array [Array [Boolean ,7],047];_(){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 432))

    def test_external_33(self):
        input = '''Class _:g_{}Class s{Constructor (w:a2){}Val xT_:Int ;Destructor (){}_4(d:String ){}Val l:e;}Class __6{Var $4,_:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 433))

    def test_external_34(self):
        input = '''Class h__:m{Val $_,_sK,$_,$4_:Array [Float ,03];Constructor (_R,_,_:Array [Array [Float ,0B1001100],1];J,UC_3:Float ;_,_,_:Array [Boolean ,0131]){}Constructor (_X,_,_:u_5_;T:Float ){}Var $L,$_X:_;}Class _{Destructor (){} }Class __{$_(a:Array [Float ,5];L,__c6:_s__T_2_){} }Class _:_CS{$_0(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 434))

    def test_external_35(self):
        input = '''Class _{}Class _:l___{Destructor (){}Constructor (_,I,c1:Array [Array [Float ,2_0],04];__,_W_v68,M1:u_H_2;_6_,M,_OF_56:String ){Break ;} }Class L:Vw{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 435))

    def test_external_36(self):
        input = '''Class ____{}Class F:_{}Class Tn:z{Destructor (){}Var e,im,$E,JO_b,$bSH7,M8:Array [Array [String ,0b1001010],4];}Class _L7{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 436))

    def test_external_37(self):
        input = '''Class l{Destructor (){} }Class s:_{Destructor (){}Constructor (d_m9:Array [Array [Array [Int ,03_5],0B1001],7_52];v_:Array [Array [String ,0B10],43]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 437))

    def test_external_38(self):
        input = '''Class S4:X{Constructor (W,n:X;t:Array [Float ,0136];vr,l:Float ;cP:Boolean ;_,A:Array [Int ,0136]){} }Class __{Constructor (){} }Class i1:_Q6{}Class r_7{Destructor (){Break ;}Var M:___;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 438))

    def test_external_39(self):
        input = '''Class _{Val $Q:Int ;Constructor (__i4:f;Ow_b6:_;S,_T8_495:Float ;Q_:Array [Array [Float ,26],0X9];X,___mB,M4U_,Q:Array [Array [Float ,0B1011101],0xC];q_:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 439))

    def test_external_40(self):
        input = '''Class _:E{Constructor (_,F:Array [Float ,056];c5:_U;X4p4f:_){}$g05_(){}V(_4b__9CP:Array [String ,0xD];c,aF6,c,_:cD27W;u,_,V:K_;T_:_;_E:Array [Array [Int ,0B1_0],0b110101]){}Constructor (){ {{} }} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 440))

    def test_external_41(self):
        input = '''Class _{$_(){Var Z,H:Array [Boolean ,0137];Continue ;} }Class y{$_7z(_,__:U7;_:_){}Destructor (){}Val $Cy_I_:Array [Array [Boolean ,0b110111],0x4];Var Dx_,i_a,$__q7_:Array [Int ,0137];G3(L3,_36:L;v_0:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 441))

    def test_external_42(self):
        input = '''Class n:_6_z{G2(_35,_0,_,z_s2_,_2:Array [Array [Array [Float ,0B1],84_3],0B110010];_to:Array [Array [Float ,02],0xF];B0:_;B:b_0;_,_,_,_,_,_v3XU0,B5_5:_;_TtN,j3t6,x_H74,Z0_4:Boolean ){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 442))

    def test_external_43(self):
        input = '''Class Z2J4:_{}Class a:_0{$M(M__3zA_,k,v,_7:String ;_2_4:Array [Array [Array [Array [Array [Array [String ,0B1_0_0],0B111011],0b101110],66],0X5],0B111011];_,P_W2__54A3,I,i_IAd__,_,_:Array [Int ,0b1_1]){} }Class __9__c4{Val e6,E:Array [Int ,0X5E];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 443))

    def test_external_44(self):
        input = '''Class Ok{Var P_1pI,Y,_:Array [Array [Array [Array [Array [Array [Int ,0b1010001],0b1010001],5_1],76],7_4_18_5_5],0B1_0];}Class V7{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 444))

    def test_external_45(self):
        input = '''Class _{q_2(_:Array [Boolean ,0b1];__,H:String ;_,__x,s_3:Int ;__0,X,_p,s__:_;RJ9:Array [Array [Array [Array [Array [Float ,0x7],37],0X2_4],05],0b1000011];z,l60,_T:Int ){Break ;}Val _,$1,$8,$L5:_D;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 445))

    def test_external_46(self):
        input = '''Class _{}Class y0:b{Var $__3,$2:Boolean ;}Class B{$4_X(G,U3m_26:Array [Array [Array [String ,0B1000110],0B1000110],02]){} }Class _D{Val _y:bi;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 446))

    def test_external_47(self):
        input = '''Class _{}Class _v3{Constructor (b_q_,G:Int ){}Constructor (O60_5,e,_K:Array [Array [Array [Array [Array [Array [Boolean ,0X9],9],72],0X9],72],3_3];_,_:_;M,_8:_B){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 447))

    def test_external_48(self):
        input = '''Class j{Constructor (__2:String ;_d,ZQf:Array [String ,0B10]){}Destructor (){Break ;}Destructor (){} }Class _:C_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 448))

    def test_external_49(self):
        input = '''Class _3{Constructor (F__P,Y:Array [Array [Array [Array [Float ,0b1010101],061],0X8],061]){Continue ;}Val A__:S;Val $o,$v_:Array [Array [String ,0b1010101],50];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 449))

    def test_external_50(self):
        input = '''Class k{Var _,$d3_V_:Array [String ,21];$d_(){} }Class e6:K{$5(G_6,___t3F_,_:Array [Array [Boolean ,0121],01_2];_,___,D:_;_,p:___9hV){} }Class _2{Val $1,_X0,k,_1:Float ;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 450))

    def test_external_51(self):
        input = '''Class _{Constructor (w4:String ){ {} }Val $3c:Array [Array [Float ,0b1],0x5_5_A];}Class ___s:qHg{}Class _:_{}Class __V:__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 451))

    def test_external_52(self):
        input = '''Class _:_b_x{}Class AZ{Destructor (){} }Class J{Val _,V19_D_f:Array [Boolean ,041];$5(_,_GY:Array [Array [Int ,8],0X43]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 452))

    def test_external_53(self):
        input = '''Class h:_{Constructor (_a9,_,_:Array [Int ,8];__6:Boolean ;q,_,h,_,_3_:Array [Float ,05_3];_9_,B__8,_1,_:Array [Int ,0b10]){} }Class U:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 453))

    def test_external_54(self):
        input = '''Class _D:w{Constructor (y,_,__:P_;Tl,__,v:Array [String ,0x49];l:Boolean ;A_w:__o;A:String ){}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 454))

    def test_external_55(self):
        input = '''Class __{Val $0,w:_;$5(b_,_6,__0,bv3__,r_,_,__:Int ;____:Int ;_J:Boolean ){}Val m5_J:Array [Array [Float ,0127],0X3D_A];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 455))

    def test_external_56(self):
        input = '''Class _5_3{}Class _42{}Class g:W_y{}Class _:_{K_(l,p7,p_:_;__:Array [Array [Float ,0x3F],0b101010];G933_1_2:Array [Array [Boolean ,0X7],041];v_8:Array [Float ,041]){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 456))

    def test_external_57(self):
        input = '''Class _{}Class d{Var $4,a:Pk76_;_y(B_,a9U4:a;m_8:Float ;eJ3:Boolean ){} }Class _lb6:_{Var $_:Array [Array [Array [Array [Int ,44_0],01_0_6],0XF],0XF1];}Class G:O{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 457))

    def test_external_58(self):
        input = '''Class _3:e_7hp{_0(w:Boolean ;_Aa:Array [Array [Int ,0x41],0x41];_28GOB,t,yb:j21t){Break ;Return ;Val _,f,_:v8;} }Class _:A_8{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 458))

    def test_external_59(self):
        input = '''Class i{}Class q3e_{}Class Ij_R_{Var $_:Array [Array [Array [String ,1],3_1],76_6_4_7];Constructor (KP,q__:Array [Int ,77]){} }Class _:_{X(){}Constructor (hl,V3:Array [Array [Array [Array [String ,0B1],82_2],0X63],77];o:X){}Val $Q,Z5:Array [String ,0xC];}Class __:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 459))

    def test_external_60(self):
        input = '''Class _:__{}Class N:JLO{$Ql(_,_:Int ){}Destructor (){} }Class R2_:_{$5(__,d:String ;_:Int ){}Val _9,_:Array [String ,53];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 460))

    def test_external_61(self):
        input = '''Class _{_g(t:Int ){ {} }k(_55_,q:Array [Array [Array [Array [Array [Int ,0B1_1],0B1011101],54],54],026]){} }Class _{$ij(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 461))

    def test_external_62(self):
        input = '''Class X{}Class __3{}Class w:_9{Val j___:_;Constructor (C:Ygx;_0,_b:Float ;_,_:Array [Float ,8];_:_4;_,u2_:Array [Array [Array [Int ,0B1000011],0B1000011],0b1_11_0]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 462))

    def test_external_63(self):
        input = '''Class K:E{}Class w_:j{Val $R:Array [Array [Array [Int ,18_3],9],06];$__(){}Destructor (){} }Class _{Destructor (){} }Class _a__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 463))

    def test_external_64(self):
        input = '''Class _7_0_{Constructor (){Continue ;} }Class _c:_{$_(){}_5(){Break ;Return ;}Destructor (){}Constructor (){}Val $7_3E:Array [Float ,48_4];}Class _E_{Val $__2Z_,h,$68,$g,$4:Array [Float ,0XE];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 464))

    def test_external_65(self):
        input = '''Class V{$_N7_c(v5:_150){Val _1_1:Array [String ,0B1];}Var j:Int ;$66_(_,_4l,m320:Int ;x__:Float ){sL::$__1_.nL();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 465))

    def test_external_66(self):
        input = '''Class __{Constructor (_v,gL4d:Array [Array [Array [Array [Int ,0B1_1101],58],0xC_7],03_2_7];_,L_3:nR__;_3__,O,O_:_4){ {} }Var $_:_d;$Y_(){Break ;}Constructor (_:N__;I:_t){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 466))

    def test_external_67(self):
        input = '''Class J30{Var _,$81,_,$6,_:r;Var _o6:_;}Class R{}Class _{Constructor (_,NJ:String ;_og:_){Break ;Continue ;} }Class m:c_p{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 467))

    def test_external_68(self):
        input = '''Class _v28:_{Destructor (){} }Class _{$88C_w(){}Constructor (O:_){}Var $xb0_N_17,$_2,_i,$6_,t,$8z,__:Boolean ;Var $4:Array [Array [Int ,72],0115];_(m,_,O,_,_J_,_,g,_:Boolean ;_y,L,_:s){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 468))

    def test_external_69(self):
        input = '''Class __{Val $k5,M0_:Boolean ;}Class _{Destructor (){} }Class _0{Var $_,$AY,$X:Float ;}Class _:_8{Constructor (){}Val $i:Array [Array [Boolean ,040],076];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 469))

    def test_external_70(self):
        input = '''Class w_{$fp_(J6,_p1,_:Array [Array [Array [Array [String ,0x11],0X21],0x11],10]){}Constructor (__9_:Array [Array [Array [Float ,0b1],0x11],0B100001]){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 470))

    def test_external_71(self):
        input = '''Class _:_{Constructor (){}_10(){}Var $J_,R0_u3:Boolean ;Destructor (){Break ;Continue ;Val _:_81;Var F,u:Int ;Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 471))

    def test_external_72(self):
        input = '''Class _{CLQ(_,t:Boolean ){Break ;} }Class _{Val $r,_:_;Constructor (){}Constructor (){Continue ;}Val $_:Int ;Destructor (){ {} }}Class _6_7{Destructor (){}$S(){} }Class F2r{}Class _e{}Class _{}Class bM:s{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 472))

    def test_external_73(self):
        input = '''Class __fl_p_:nU{Constructor (K8,_,o:Array [Array [Int ,066],014]){}Val _:Array [Array [Array [Int ,0x58],031],0B1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 473))

    def test_external_74(self):
        input = '''Class F6{Constructor (G_1:Float ;at:i;u,Oe30,_9_4,_Q:String ;_5:_;Jq___F:nb;__n75_p___:g){ {}Val y,I:Boolean ;}Val __,Sh:String ;Val $_,$_:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 474))

    def test_external_75(self):
        input = '''Class _a:_{Destructor (){}_(fv,_,_3:Int ;d,_G_0_2:Array [Array [Array [Int ,59],050_7],013];GC,V4_,_3I:Array [Array [Array [Int ,59],050],7];r_B4c,_z:_lB1I;Q_Q,_S_,_,_:String ){}Constructor (){Break ;}v(m:b){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 475))

    def test_external_76(self):
        input = '''Class H6Y4{Destructor (){} }Class _9:_{Constructor (k,_,d2,_:Int ){}Constructor (_:String ;_:String ){}Val ks_:za;}Class _g{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 476))

    def test_external_77(self):
        input = '''Class X5DT3{Constructor (O,_8:Array [Array [Float ,0X6E_3],07];E_:u;_:Float ){} }Class N{Val $_,$s:l;}Class F{Constructor (){}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 477))

    def test_external_78(self):
        input = '''Class __:_{}Class WV_9{eA2(){}Var $_8_:Array [Array [String ,0X4D],0B111110];Var $_:_1l;$2(dpdYF,_,MMZ___:Array [String ,0B111110]){}_(I,_,_A,J_:Array [Int ,06]){}Constructor (){} }Class Q7:_m_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 478))

    def test_external_79(self):
        input = '''Class UB3{}Class _4:_{}Class J{Destructor (){} }Class n:p{$7f8(){} }Class k{Destructor (){} }Class T3:__{}Class x{Val $Vn,h:__;}Class J:Cj058_g__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 479))

    def test_external_80(self):
        input = '''Class _:f{Constructor (u:_J_;_3:Array [Boolean ,0115];_,B:String ){}Constructor (){}D8(_:Zvq;_,E,__4:Array [Array [Array [String ,100],0X5E],0X5E];j5_:String ;_:Array [Int ,16_93];_:Array [Array [Float ,0B1100001],7];x:String ;__3:Array [Array [Float ,0B1],0115];p303_3_,_:Array [Array [Array [Boolean ,0115],0X7],0B1]){Return ;} }Class Qy_5{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 480))

    def test_external_81(self):
        input = '''Class O_:_{Val U,_:Boolean ;}Class fI{Val F:Array [Int ,0b1];__(d___5:_;__:Boolean ;W,_86_2c:Array [Float ,010]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 481))

    def test_external_82(self):
        input = '''Class _{$s5(_Zo:W;T6:Array [Array [Array [Float ,0x1_3],0B1],96];_,_F_c2,v:Array [Int ,0X63];___,j_:Float ;B:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 482))

    def test_external_83(self):
        input = '''Class _:____{Constructor (u7J3A:Array [Array [Int ,01_7_1],20];_,c4__:Boolean ){Continue ;}Val uy,wK,_,$4__v:Q;Constructor (){ {}{} }}Class v{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 483))

    def test_external_84(self):
        input = '''Class C{Destructor (){}Destructor (){Continue ;}Var $76_,$5:v__;}Class _{}Class G:_m{Constructor (I5:Array [Boolean ,0b1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 484))

    def test_external_85(self):
        input = '''Class f:w_r{Val $e,$_:Int ;Var $5,$U:___4;Var M,$_,$2,A:String ;Constructor (_,C5_87,_77r:_){} }Class _cC_691_T_C9:_{$s(_,L_,_:Array [Array [Array [Array [Int ,40],0b111110],0B1],0X1D];_j:Int ;_,_:H6){}Val _,H3,T6_,_,c31DM,_:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 485))

    def test_external_86(self):
        input = '''Class _{Val _,$___:String ;}Class CzP3:_C{}Class _3l:__5_o_k{Constructor (){}Val _:Array [Array [Array [Float ,91],0b110110],0xC];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 486))

    def test_external_87(self):
        input = '''Class I_g9{}Class __:__5{Constructor (_,b_P:_0){}Destructor (){} }Class X{Destructor (){} }Class rjV{}Class X8{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 487))

    def test_external_88(self):
        input = '''Class j:G80R{Constructor (_:fY;o,U_,_1:Array [Array [String ,0b111110],0x9_4]){If (-_4__::$07_3()){} }Val $P8:_50_;Val $_0:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 488))

    def test_external_89(self):
        input = '''Class _{r(_Mt2,_,_,_n,__:Array [Boolean ,0b11000];p1_,_ko_u3:Float ;_:Int ){} }Class p_{Val $4787_,$_0,_,$uo,$_,_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 489))

    def test_external_90(self):
        input = '''Class y{}Class T2:k{}Class _:_{$6F_(_v_,m,_8:Array [Boolean ,04];_4,a_,K,W5_:_){}$u(Z,_:c){m8_::$_();}Destructor (){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 490))

    def test_external_91(self):
        input = '''Class ___h_:NYy_o{Var p:N;$___(){Break ;} }Class m{}Class DO{}Class _{}Class _:_{Constructor (){ {} }Val _0:Int ;}Class x{Destructor (){Return ;}Val $_:W;Var $37_,$vB,L_9:Int ;Destructor (){Break ;Val _:s;} }Class __T{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 491))

    def test_external_92(self):
        input = '''Class ___4_{}Class _{$_(L:String ;H_:Array [Array [Array [String ,87],0x6],0x9];__,Q_,W,_,E,m,K,J:Array [Array [Array [Array [Array [Boolean ,0X46],87],0B101000],87],5]){Break ;}V(_3_AG:Array [Int ,0b100101]){Break ;}Var N,$v_,x_4,_rs:_;Var ____,_07:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 492))

    def test_external_93(self):
        input = '''Class d{Var __:i5_;Val f:Boolean ;_(z:Array [Int ,8];_6,_6,_f,_,_p,l:Array [String ,0x6];_07,_,R,_I,_,_,_L:Array [Array [Array [Array [Int ,02_6_4_5],01],032],032];E:Boolean ;_q,J:_){} }Class __:___8__{Constructor (__I6_96N:Array [Int ,5]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 493))
