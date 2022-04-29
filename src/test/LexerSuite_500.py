import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_0(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:Y{}Class _:_2{}Class D{Val z_:Float ;$F_R_D(_VQ:Int ;O:_;a,__,d,__0__5:_){}Val _7J7,$_:Boolean ;}Class A51:_{}''',
                '''Class,__,:,Y,{,},Class,_,:,_2,{,},Class,D,{,Val,z_,:,Float,;,$F_R_D,(,_VQ,:,Int,;,O,:,_,;,a,,,__,,,d,,,__0__5,:,_,),{,},Val,_7J7,,,$_,:,Boolean,;,},Class,A51,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:X7D__{Var $3,$L:Array [String ,80];Destructor (){ {{} }} }Class _c{Val $D0:_3;Val $_:Array [Boolean ,0XF_B5];}''',
                '''Class,_,:,X7D__,{,Var,$3,,,$L,:,Array,[,String,,,80,],;,Destructor,(,),{,{,{,},},},},Class,_c,{,Val,$D0,:,_3,;,Val,$_,:,Array,[,Boolean,,,0XFB5,],;,},<EOF>''',
                101
            )
        )

    def test_2(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Y:Z_pL74{Var _,$nV__W:_;}Class N:LG{Destructor (){}Var u:X;Constructor (_7:Array [Int ,6]){} }Class d:V8{}''',
                '''Class,Y,:,Z_pL74,{,Var,_,,,$nV__W,:,_,;,},Class,N,:,LG,{,Destructor,(,),{,},Var,u,:,X,;,Constructor,(,_7,:,Array,[,Int,,,6,],),{,},},Class,d,:,V8,{,},<EOF>''',
                101
            )
        )

    def test_3(self):
        self.assertTrue(
            TestLexer.test(
                '''Class WB{Constructor (){} }Class _:_{}Class k29{}Class _x8{}Class A3_z:_{$_(_4__4,ur3,JN:Array [String ,0123];e:Array [Array [Array [Array [Array [String ,07_3],0x3],0xC_5],0b1],0XC_F8]){} }''',
                '''Class,WB,{,Constructor,(,),{,},},Class,_,:,_,{,},Class,k29,{,},Class,_x8,{,},Class,A3_z,:,_,{,$_,(,_4__4,,,ur3,,,JN,:,Array,[,String,,,0123,],;,e,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,073,],,,0x3,],,,0xC5,],,,0b1,],,,0XCF8,],),{,},},<EOF>''',
                101
            )
        )

    def test_4(self):
        self.assertTrue(
            TestLexer.test(
                '''Class TG:__2_6_3{}Class d:a{Val $V_,_:Array [Array [Array [Float ,0x44],0x1],94_06_2];$O_5b(P_:_;_5:Array [Array [Float ,0B111100],1];_:Array [Float ,0X9_A];bx__:Array [Array [Array [Array [Boolean ,054],0B1_00],0x44],0B1_1];_,__:Boolean ){} }Class _6k{Destructor (){Return ;} }''',
                '''Class,TG,:,__2_6_3,{,},Class,d,:,a,{,Val,$V_,,,_,:,Array,[,Array,[,Array,[,Float,,,0x44,],,,0x1,],,,94062,],;,$O_5b,(,P_,:,_,;,_5,:,Array,[,Array,[,Float,,,0B111100,],,,1,],;,_,:,Array,[,Float,,,0X9A,],;,bx__,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,054,],,,0B100,],,,0x44,],,,0B11,],;,_,,,__,:,Boolean,),{,},},Class,_6k,{,Destructor,(,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_5(self):
        self.assertTrue(
            TestLexer.test(
                '''Class R:_{Var _2,c:Array [Array [Array [Array [Array [Array [Array [Int ,6],030_50],0X49],02],0X2F],055],02];}Class h{}''',
                '''Class,R,:,_,{,Var,_2,,,c,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,6,],,,03050,],,,0X49,],,,02,],,,0X2F,],,,055,],,,02,],;,},Class,h,{,},<EOF>''',
                101
            )
        )

    def test_6(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{$__(X,__3_5,m:String ;__,G_4,I,x:Boolean ;_,_,_e6,_2:K__;Y_85:Array [Boolean ,0111];b,RO,a:_;_,U:_){} }''',
                '''Class,_,{,$__,(,X,,,__3_5,,,m,:,String,;,__,,,G_4,,,I,,,x,:,Boolean,;,_,,,_,,,_e6,,,_2,:,K__,;,Y_85,:,Array,[,Boolean,,,0111,],;,b,,,RO,,,a,:,_,;,_,,,U,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_7(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o{Var _,__k,$n5:String ;}Class j{}Class c:BG{$_(v,_D:String ;_:_sp){}Constructor (){}Var $0,af,r,$9_e,$1,$2,__4P,g:p;}''',
                '''Class,o,{,Var,_,,,__k,,,$n5,:,String,;,},Class,j,{,},Class,c,:,BG,{,$_,(,v,,,_D,:,String,;,_,:,_sp,),{,},Constructor,(,),{,},Var,$0,,,af,,,r,,,$9_e,,,$1,,,$2,,,__4P,,,g,:,p,;,},<EOF>''',
                101
            )
        )

    def test_8(self):
        self.assertTrue(
            TestLexer.test(
                '''Class uG9{Val j,o_,_:Array [Array [Array [Int ,030],030],78];Destructor (){}Val A2:Array [Array [Array [Array [Float ,0B10110],0B10110],0xF5_5],0x37];}Class _{}''',
                '''Class,uG9,{,Val,j,,,o_,,,_,:,Array,[,Array,[,Array,[,Int,,,030,],,,030,],,,78,],;,Destructor,(,),{,},Val,A2,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B10110,],,,0B10110,],,,0xF55,],,,0x37,],;,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_9(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A_L08_77:_j{Constructor (KZ8_:Boolean ;O:Int ;_KX:Boolean ;___H_47f,l6:Array [Array [Array [Int ,0b1010010],04_2],0x4A];E,h_,KF,__:r_6Nl){} }''',
                '''Class,A_L08_77,:,_j,{,Constructor,(,KZ8_,:,Boolean,;,O,:,Int,;,_KX,:,Boolean,;,___H_47f,,,l6,:,Array,[,Array,[,Array,[,Int,,,0b1010010,],,,042,],,,0x4A,],;,E,,,h_,,,KF,,,__,:,r_6Nl,),{,},},<EOF>''',
                101
            )
        )

    def test_10(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n:_{Constructor (_,G5,_6,_:Array [Int ,0b111];Se_fz,_4L5_,A,_8:Array [Array [Float ,04],0B1010]){Continue ;} }''',
                '''Class,n,:,_,{,Constructor,(,_,,,G5,,,_6,,,_,:,Array,[,Int,,,0b111,],;,Se_fz,,,_4L5_,,,A,,,_8,:,Array,[,Array,[,Float,,,04,],,,0B1010,],),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_11(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b4_:h_4{Val _,$5_1:Array [Array [Array [Array [Array [Array [Array [Array [Int ,0B1010011],1_6],0B1_0],0x40],82],0X4A],0X4A],0X4A];}Class _:Y{}''',
                '''Class,b4_,:,h_4,{,Val,_,,,$5_1,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B1010011,],,,16,],,,0B10,],,,0x40,],,,82,],,,0X4A,],,,0X4A,],,,0X4A,],;,},Class,_,:,Y,{,},<EOF>''',
                101
            )
        )

    def test_12(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Zk{Constructor (_3_:Int ;_:Array [String ,86]){}Val $_:Array [Int ,0b1_10];$6(t,X,_:Array [Array [Array [Array [String ,0b1010000],060],2],0b1010000];_:String ){Return ;} }Class _7_02{}Class _5i5{Var C7,__,jpN,$W,$t:Array [Array [Int ,051_4_4_5_6_3],0XE_C];Destructor (){} }Class _:_3{}''',
                '''Class,Zk,{,Constructor,(,_3_,:,Int,;,_,:,Array,[,String,,,86,],),{,},Val,$_,:,Array,[,Int,,,0b110,],;,$6,(,t,,,X,,,_,:,Array,[,Array,[,Array,[,Array,[,String,,,0b1010000,],,,060,],,,2,],,,0b1010000,],;,_,:,String,),{,Return,;,},},Class,_7_02,{,},Class,_5i5,{,Var,C7,,,__,,,jpN,,,$W,,,$t,:,Array,[,Array,[,Int,,,05144563,],,,0XEC,],;,Destructor,(,),{,},},Class,_,:,_3,{,},<EOF>''',
                101
            )
        )

    def test_13(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _:C{Val $7:Array [Array [Array [Array [Array [Array [Array [Array [String ,5_7],4],0b1],8_2_1],0B1_1_0],6],8],0b1];}''',
                '''Class,_,{,},Class,_,:,C,{,Val,$7,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,57,],,,4,],,,0b1,],,,821,],,,0B110,],,,6,],,,8,],,,0b1,],;,},<EOF>''',
                101
            )
        )

    def test_14(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0__IO_5Y{}Class _{$_(B_:Boolean ){Continue ;} }Class h:O5_9{}Class _{Var _,$_41,$5fqj:Array [Array [Array [Array [String ,0b101000],012],0B100_0],012];}''',
                '''Class,_0__IO_5Y,{,},Class,_,{,$_,(,B_,:,Boolean,),{,Continue,;,},},Class,h,:,O5_9,{,},Class,_,{,Var,_,,,$_41,,,$5fqj,:,Array,[,Array,[,Array,[,Array,[,String,,,0b101000,],,,012,],,,0B1000,],,,012,],;,},<EOF>''',
                101
            )
        )

    def test_15(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __9_{$V(H,D:Boolean ;_:Float ;V_EK,f_2_n0p____5D_D:Array [Array [Array [Array [Array [String ,0B1100011],056],0b1_1],0B1100011],065];__,__,__,I:Int ;W_:Float ;___,_:Array [Array [Float ,0x4],02_7]){} }Class P_4{Constructor (_:TB1){} }''',
                '''Class,__9_,{,$V,(,H,,,D,:,Boolean,;,_,:,Float,;,V_EK,,,f_2_n0p____5D_D,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B1100011,],,,056,],,,0b11,],,,0B1100011,],,,065,],;,__,,,__,,,__,,,I,:,Int,;,W_,:,Float,;,___,,,_,:,Array,[,Array,[,Float,,,0x4,],,,027,],),{,},},Class,P_4,{,Constructor,(,_,:,TB1,),{,},},<EOF>''',
                101
            )
        )

    def test_16(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A:K{$_(){ {} }}Class ma{_(){Continue ;}Val W:Array [Float ,026];Constructor (__1,S,_p,E,M,r_D,o__1,_,_,_,_,M:String ;_,w,_1_6,_,_:Array [Array [Array [Array [Array [Array [String ,52],0X2F],0X2F],01],06],026]){}Val $M:String ;}''',
                '''Class,A,:,K,{,$_,(,),{,{,},},},Class,ma,{,_,(,),{,Continue,;,},Val,W,:,Array,[,Float,,,026,],;,Constructor,(,__1,,,S,,,_p,,,E,,,M,,,r_D,,,o__1,,,_,,,_,,,_,,,_,,,M,:,String,;,_,,,w,,,_1_6,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,52,],,,0X2F,],,,0X2F,],,,01,],,,06,],,,026,],),{,},Val,$M,:,String,;,},<EOF>''',
                101
            )
        )

    def test_17(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (){}Val $S_,$w,v,N66r38:Array [Array [Array [Array [String ,97],0X6_C_2_1_A_21FE],07_2],0b110011];}Class _4_3__{}''',
                '''Class,_,{,Constructor,(,),{,},Val,$S_,,,$w,,,v,,,N66r38,:,Array,[,Array,[,Array,[,Array,[,String,,,97,],,,0X6C21A21FE,],,,072,],,,0b110011,],;,},Class,_4_3__,{,},<EOF>''',
                101
            )
        )

    def test_18(self):
        self.assertTrue(
            TestLexer.test(
                '''Class c{$H(oP:Array [Array [Array [String ,0b1_00],04],05];z_27,m:String ){} }Class i_{}Class Vk:_{}Class _:_{}Class y_{}''',
                '''Class,c,{,$H,(,oP,:,Array,[,Array,[,Array,[,String,,,0b100,],,,04,],,,05,],;,z_27,,,m,:,String,),{,},},Class,i_,{,},Class,Vk,:,_,{,},Class,_,:,_,{,},Class,y_,{,},<EOF>''',
                101
            )
        )

    def test_19(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:Hj_{Val _:_1__;}Class _:T{Val $7,I,j_QY,s__,$_,$_,y_8,$L,$E1:M;}Class _9{}Class _{}Class c2:_Q9{Var $4,_:U;}''',
                '''Class,_,:,Hj_,{,Val,_,:,_1__,;,},Class,_,:,T,{,Val,$7,,,I,,,j_QY,,,s__,,,$_,,,$_,,,y_8,,,$L,,,$E1,:,M,;,},Class,_9,{,},Class,_,{,},Class,c2,:,_Q9,{,Var,$4,,,_,:,U,;,},<EOF>''',
                101
            )
        )

    def test_20(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7:_{Constructor (q6W31,__,_:Boolean ){}f_E977(_:Array [Boolean ,98];I:Array [Array [Array [Array [Int ,024],7],0X1B],5_801_2]){} }''',
                '''Class,_7,:,_,{,Constructor,(,q6W31,,,__,,,_,:,Boolean,),{,},f_E977,(,_,:,Array,[,Boolean,,,98,],;,I,:,Array,[,Array,[,Array,[,Array,[,Int,,,024,],,,7,],,,0X1B,],,,58012,],),{,},},<EOF>''',
                101
            )
        )

    def test_21(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Q_7_Or74:_{Val _,z9S____,$Y:Array [Array [Array [String ,0B10],0B101000],0X14];Val D:Array [Array [Float ,017],16];}''',
                '''Class,Q_7_Or74,:,_,{,Val,_,,,z9S____,,,$Y,:,Array,[,Array,[,Array,[,String,,,0B10,],,,0B101000,],,,0X14,],;,Val,D,:,Array,[,Array,[,Float,,,017,],,,16,],;,},<EOF>''',
                101
            )
        )

    def test_22(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _50:yb{Destructor (){Val __,h,r_:Float ;}Destructor (){}Constructor (_:Float ;x,I0,pi,Wa_9:Array [Array [Array [Int ,0X54],43],43];_:Int ){} }Class h{Val $6:String ;}''',
                '''Class,_50,:,yb,{,Destructor,(,),{,Val,__,,,h,,,r_,:,Float,;,},Destructor,(,),{,},Constructor,(,_,:,Float,;,x,,,I0,,,pi,,,Wa_9,:,Array,[,Array,[,Array,[,Int,,,0X54,],,,43,],,,43,],;,_,:,Int,),{,},},Class,h,{,Val,$6,:,String,;,},<EOF>''',
                101
            )
        )

    def test_23(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:R{Var k_1,$5:Array [Array [Array [Array [Array [Array [Array [String ,873],076],076],076],0b1_0_1],0xF_C],0B1000011];}''',
                '''Class,_,:,R,{,Var,k_1,,,$5,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,873,],,,076,],,,076,],,,076,],,,0b101,],,,0xFC,],,,0B1000011,],;,},<EOF>''',
                101
            )
        )

    def test_24(self):
        self.assertTrue(
            TestLexer.test(
                '''Class N_{Destructor (){Val r4:_;}Constructor (){}Constructor (_G:Boolean ){}Val $9,$_7,Z,$____,h,l_,$W:_hA;Var $y_:n;}''',
                '''Class,N_,{,Destructor,(,),{,Val,r4,:,_,;,},Constructor,(,),{,},Constructor,(,_G,:,Boolean,),{,},Val,$9,,,$_7,,,Z,,,$____,,,h,,,l_,,,$W,:,_hA,;,Var,$y_,:,n,;,},<EOF>''',
                101
            )
        )

    def test_25(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _5{Var F_:Array [Float ,027];Val _:Array [String ,0b1];$S(){} }Class _:_{Constructor (a__,b,_,T0,_,C,_,p_3:w;H5,vv_,G_:String ;_Y,_:Array [Array [Array [Array [Array [String ,6],0377],0x5A],0b1],22]){Continue ;Return ;} }''',
                '''Class,_5,{,Var,F_,:,Array,[,Float,,,027,],;,Val,_,:,Array,[,String,,,0b1,],;,$S,(,),{,},},Class,_,:,_,{,Constructor,(,a__,,,b,,,_,,,T0,,,_,,,C,,,_,,,p_3,:,w,;,H5,,,vv_,,,G_,:,String,;,_Y,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,6,],,,0377,],,,0x5A,],,,0b1,],,,22,],),{,Continue,;,Return,;,},},<EOF>''',
                101
            )
        )

    def test_26(self):
        self.assertTrue(
            TestLexer.test(
                '''Class p:_Z{}Class Ad8:_s_8_2j{$u98(_5_a:Array [Array [Array [Array [Float ,0B110010],0B110010],9_60_7],0x2D];__,__3:Array [Array [Array [Boolean ,0x2D],0X35],0b1]){Continue ;}Var g5:Int ;}''',
                '''Class,p,:,_Z,{,},Class,Ad8,:,_s_8_2j,{,$u98,(,_5_a,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B110010,],,,0B110010,],,,9607,],,,0x2D,],;,__,,,__3,:,Array,[,Array,[,Array,[,Boolean,,,0x2D,],,,0X35,],,,0b1,],),{,Continue,;,},Var,g5,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_27(self):
        self.assertTrue(
            TestLexer.test(
                '''Class D0{Var $4_:Array [Array [Array [Array [Array [Int ,4_2],03],03],0xE_92],01];Val Z6:Array [Float ,0B1];Val F:Array [String ,0B1];Val H:Array [Int ,03];Destructor (){} }''',
                '''Class,D0,{,Var,$4_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,42,],,,03,],,,03,],,,0xE92,],,,01,],;,Val,Z6,:,Array,[,Float,,,0B1,],;,Val,F,:,Array,[,String,,,0B1,],;,Val,H,:,Array,[,Int,,,03,],;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_28(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l__{Val $3,$a6k7:Array [Boolean ,0B1];Destructor (){Continue ;}Destructor (){}Constructor (){} }Class _z13:v0__9{}''',
                '''Class,l__,{,Val,$3,,,$a6k7,:,Array,[,Boolean,,,0B1,],;,Destructor,(,),{,Continue,;,},Destructor,(,),{,},Constructor,(,),{,},},Class,_z13,:,v0__9,{,},<EOF>''',
                101
            )
        )

    def test_29(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E:_o__{Constructor (F,R:Y0_;S2p,E,_m_7,c45:Array [Array [Array [Array [Array [Array [Boolean ,14],0B1],022],0x31],14],14];_,v:Float ){} }''',
                '''Class,E,:,_o__,{,Constructor,(,F,,,R,:,Y0_,;,S2p,,,E,,,_m_7,,,c45,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,14,],,,0B1,],,,022,],,,0x31,],,,14,],,,14,],;,_,,,v,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_30(self):
        self.assertTrue(
            TestLexer.test(
                '''Class v_{Var $_4_9,$37n,$6U,_:J;}Class _:W7{}Class h_o0V_{}Class b{}Class h6:L{RW(KS,s,J_:Array [Array [Boolean ,74],0xA];x,uW8,z0:Array [Array [Int ,0B11100],0X4_A_CC];_,YK952,_:a_){} }''',
                '''Class,v_,{,Var,$_4_9,,,$37n,,,$6U,,,_,:,J,;,},Class,_,:,W7,{,},Class,h_o0V_,{,},Class,b,{,},Class,h6,:,L,{,RW,(,KS,,,s,,,J_,:,Array,[,Array,[,Boolean,,,74,],,,0xA,],;,x,,,uW8,,,z0,:,Array,[,Array,[,Int,,,0B11100,],,,0X4ACC,],;,_,,,YK952,,,_,:,a_,),{,},},<EOF>''',
                101
            )
        )

    def test_31(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Tn{_(_,d_D2,wO,z,z__,_:Array [Array [Array [Array [Array [Int ,22],0x61],8_9],02],2_3_7_49];g,i,f_40:Array [Array [Array [Array [Array [Float ,0xF],0X5C],01113_0_3],0b1000110],0b1]){} }''',
                '''Class,Tn,{,_,(,_,,,d_D2,,,wO,,,z,,,z__,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,22,],,,0x61,],,,89,],,,02,],,,23749,],;,g,,,i,,,f_40,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0xF,],,,0X5C,],,,0111303,],,,0b1000110,],,,0b1,],),{,},},<EOF>''',
                101
            )
        )

    def test_32(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class s:__1{}Class _7{_(){} }Class __:_{}Class __:u{}Class _:_G_{Destructor (){Continue ;}g(y4:String ;c,__7:_;_,_:__){} }''',
                '''Class,_,{,},Class,s,:,__1,{,},Class,_7,{,_,(,),{,},},Class,__,:,_,{,},Class,__,:,u,{,},Class,_,:,_G_,{,Destructor,(,),{,Continue,;,},g,(,y4,:,String,;,c,,,__7,:,_,;,_,,,_,:,__,),{,},},<EOF>''',
                101
            )
        )

    def test_33(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:M{Constructor (){}$V(){} }Class _{Var b:Array [Array [Array [Array [Int ,0130],97],97],0x61];Var Vn,$4:s_;y(){} }''',
                '''Class,_,:,M,{,Constructor,(,),{,},$V,(,),{,},},Class,_,{,Var,b,:,Array,[,Array,[,Array,[,Array,[,Int,,,0130,],,,97,],,,97,],,,0x61,],;,Var,Vn,,,$4,:,s_,;,y,(,),{,},},<EOF>''',
                101
            )
        )

    def test_34(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___5_0{}Class u:Tz_{Var $42,$_:Array [Array [Array [Array [Array [Array [Array [Float ,35],0x60],0b10],35],0x60],35],0B110011];}''',
                '''Class,___5_0,{,},Class,u,:,Tz_,{,Var,$42,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,35,],,,0x60,],,,0b10,],,,35,],,,0x60,],,,35,],,,0B110011,],;,},<EOF>''',
                101
            )
        )

    def test_35(self):
        self.assertTrue(
            TestLexer.test(
                '''Class z{Val j___2:Boolean ;$_(){Break ;}$3(m_,_g:Array [Float ,0xA2]){}$f(){}Destructor (){Return ;} }Class Z30:_{Val _:J;Val j:Float ;}''',
                '''Class,z,{,Val,j___2,:,Boolean,;,$_,(,),{,Break,;,},$3,(,m_,,,_g,:,Array,[,Float,,,0xA2,],),{,},$f,(,),{,},Destructor,(,),{,Return,;,},},Class,Z30,:,_,{,Val,_,:,J,;,Val,j,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_36(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val _8,$p,$g1:Array [Int ,0x9];}Class C:D{Constructor (_:String ;_C,Q,__49b:Array [String ,64];__,_5_:g_;_,_7,_b_,_:_F){ {}Var A4,_8C:Boolean ;} }Class F_7{}''',
                '''Class,_,{,Val,_8,,,$p,,,$g1,:,Array,[,Int,,,0x9,],;,},Class,C,:,D,{,Constructor,(,_,:,String,;,_C,,,Q,,,__49b,:,Array,[,String,,,64,],;,__,,,_5_,:,g_,;,_,,,_7,,,_b_,,,_,:,_F,),{,{,},Var,A4,,,_8C,:,Boolean,;,},},Class,F_7,{,},<EOF>''',
                101
            )
        )

    def test_37(self):
        self.assertTrue(
            TestLexer.test(
                '''Class d5{$Z7(){} }Class _I:X9{}Class _5{Val $_0w___,_:String ;Var $5Z,__:Array [Array [Array [String ,0B10001],1],165166];}''',
                '''Class,d5,{,$Z7,(,),{,},},Class,_I,:,X9,{,},Class,_5,{,Val,$_0w___,,,_,:,String,;,Var,$5Z,,,__,:,Array,[,Array,[,Array,[,String,,,0B10001,],,,1,],,,165166,],;,},<EOF>''',
                101
            )
        )

    def test_38(self):
        self.assertTrue(
            TestLexer.test(
                '''Class e{}Class _:_{Constructor (u8:Array [Array [Array [Float ,06],0B1],0X3E];pO,H4:Float ;L:Array [Float ,0b1010];_,t_,cB_:Float ;kR,EJ_,_,c:Array [Float ,0x6];_,_:Array [Array [Boolean ,0B11101],62];_,_,S_:E){} }Class __5B_X{N(){} }Class _:__6438Iy{}Class _:w8BK_{}Class Au87:__50{}''',
                '''Class,e,{,},Class,_,:,_,{,Constructor,(,u8,:,Array,[,Array,[,Array,[,Float,,,06,],,,0B1,],,,0X3E,],;,pO,,,H4,:,Float,;,L,:,Array,[,Float,,,0b1010,],;,_,,,t_,,,cB_,:,Float,;,kR,,,EJ_,,,_,,,c,:,Array,[,Float,,,0x6,],;,_,,,_,:,Array,[,Array,[,Boolean,,,0B11101,],,,62,],;,_,,,_,,,S_,:,E,),{,},},Class,__5B_X,{,N,(,),{,},},Class,_,:,__6438Iy,{,},Class,_,:,w8BK_,{,},Class,Au87,:,__50,{,},<EOF>''',
                101
            )
        )

    def test_39(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Pk_94{Constructor (B,__4_2_:M60h;_,_4__:t_5){} }Class V:j_5_{}Class _{m(){} }Class a__9{Constructor (R_:Boolean ;s:String ){} }''',
                '''Class,Pk_94,{,Constructor,(,B,,,__4_2_,:,M60h,;,_,,,_4__,:,t_5,),{,},},Class,V,:,j_5_,{,},Class,_,{,m,(,),{,},},Class,a__9,{,Constructor,(,R_,:,Boolean,;,s,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_40(self):
        self.assertTrue(
            TestLexer.test(
                '''Class oU:_{Val _,g:Array [Float ,0B1001110];Var $_,$r4,kkY,$j_:Array [String ,82];}Class V:f4O_y{}Class _0_:_{Val f:Array [String ,0b111010];}Class E2:X{Val _,C7,lCP,h_:Int ;}Class N:w_{}''',
                '''Class,oU,:,_,{,Val,_,,,g,:,Array,[,Float,,,0B1001110,],;,Var,$_,,,$r4,,,kkY,,,$j_,:,Array,[,String,,,82,],;,},Class,V,:,f4O_y,{,},Class,_0_,:,_,{,Val,f,:,Array,[,String,,,0b111010,],;,},Class,E2,:,X,{,Val,_,,,C7,,,lCP,,,h_,:,Int,;,},Class,N,:,w_,{,},<EOF>''',
                101
            )
        )

    def test_41(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n2{$8__7(_2_Zyf0G7:Array [String ,609];_,_,_X__2:Array [Array [Boolean ,0b11],0B1011101]){Var ___:N;Break ;}Var g:V__;}''',
                '''Class,n2,{,$8__7,(,_2_Zyf0G7,:,Array,[,String,,,609,],;,_,,,_,,,_X__2,:,Array,[,Array,[,Boolean,,,0b11,],,,0B1011101,],),{,Var,___,:,N,;,Break,;,},Var,g,:,V__,;,},<EOF>''',
                101
            )
        )

    def test_42(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _E_{Var C2,$q8,_8:Boolean ;Var $6:Array [String ,0B1_11];Constructor (_4_,_F,c:_;_0:Boolean ;R_5_,__3:__){} }Class u{}''',
                '''Class,_E_,{,Var,C2,,,$q8,,,_8,:,Boolean,;,Var,$6,:,Array,[,String,,,0B111,],;,Constructor,(,_4_,,,_F,,,c,:,_,;,_0,:,Boolean,;,R_5_,,,__3,:,__,),{,},},Class,u,{,},<EOF>''',
                101
            )
        )

    def test_43(self):
        self.assertTrue(
            TestLexer.test(
                '''Class R{Constructor (ZUw,_KR:L;o,_:Array [Array [String ,1],033];D_,p,_:Array [Array [String ,8_90],033];HR:Array [Boolean ,0X3B]){Break ;{Break ;} }$u5L__(){} }''',
                '''Class,R,{,Constructor,(,ZUw,,,_KR,:,L,;,o,,,_,:,Array,[,Array,[,String,,,1,],,,033,],;,D_,,,p,,,_,:,Array,[,Array,[,String,,,890,],,,033,],;,HR,:,Array,[,Boolean,,,0X3B,],),{,Break,;,{,Break,;,},},$u5L__,(,),{,},},<EOF>''',
                101
            )
        )

    def test_44(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_ji66_L_E17{}Class _:_a_{Destructor (){Continue ;}Destructor (){}Destructor (){} }Class _:_g{_4Fh(_,_1,_93:Array [Array [Boolean ,0X33],0B1011101]){} }Class _q:e__{}Class _y:D{}''',
                '''Class,_,:,_ji66_L_E17,{,},Class,_,:,_a_,{,Destructor,(,),{,Continue,;,},Destructor,(,),{,},Destructor,(,),{,},},Class,_,:,_g,{,_4Fh,(,_,,,_1,,,_93,:,Array,[,Array,[,Boolean,,,0X33,],,,0B1011101,],),{,},},Class,_q,:,e__,{,},Class,_y,:,D,{,},<EOF>''',
                101
            )
        )

    def test_45(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V_{Constructor (HY_,J,_:Int ){} }Class X{Val $7,$_k,$2__L:O;Var _,_:Array [Array [Array [Array [Array [Array [Float ,9],03_6_4],07_6_4_2_2],033],033],44];}Class r{Constructor (_5d_r:Array [Array [Array [String ,0522],0b111001],0B1000001]){} }Class _ch{Val O:Array [Float ,868_2];}Class O{_(l,s_53,_n,_3:__;P,V:_8T;_7,_,_p_:GL_3_;S,_,n,T,_7,_,mSNMTN:Array [Int ,0x6];_7:Int ){}Var Ty6_:Array [Int ,0xA];$_z8_(_9,k,_,_:Array [Array [String ,0B11],3_2_02_9];m3_:Array [Array [Array [Int ,0b1_0],0X64],44];_:_7){}Val $_:Int ;}''',
                '''Class,V_,{,Constructor,(,HY_,,,J,,,_,:,Int,),{,},},Class,X,{,Val,$7,,,$_k,,,$2__L,:,O,;,Var,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,9,],,,0364,],,,076422,],,,033,],,,033,],,,44,],;,},Class,r,{,Constructor,(,_5d_r,:,Array,[,Array,[,Array,[,String,,,0522,],,,0b111001,],,,0B1000001,],),{,},},Class,_ch,{,Val,O,:,Array,[,Float,,,8682,],;,},Class,O,{,_,(,l,,,s_53,,,_n,,,_3,:,__,;,P,,,V,:,_8T,;,_7,,,_,,,_p_,:,GL_3_,;,S,,,_,,,n,,,T,,,_7,,,_,,,mSNMTN,:,Array,[,Int,,,0x6,],;,_7,:,Int,),{,},Var,Ty6_,:,Array,[,Int,,,0xA,],;,$_z8_,(,_9,,,k,,,_,,,_,:,Array,[,Array,[,String,,,0B11,],,,32029,],;,m3_,:,Array,[,Array,[,Array,[,Int,,,0b10,],,,0X64,],,,44,],;,_,:,_7,),{,},Val,$_,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_46(self):
        self.assertTrue(
            TestLexer.test(
                '''Class je{}Class FLr4:_{Val $r,_2:Array [Array [Boolean ,0X39],0b1];Constructor (L__0:Boolean ;R:Array [String ,0x12]){} }Class z_{}Class _{Constructor (){} }Class b:_{}''',
                '''Class,je,{,},Class,FLr4,:,_,{,Val,$r,,,_2,:,Array,[,Array,[,Boolean,,,0X39,],,,0b1,],;,Constructor,(,L__0,:,Boolean,;,R,:,Array,[,String,,,0x12,],),{,},},Class,z_,{,},Class,_,{,Constructor,(,),{,},},Class,b,:,_,{,},<EOF>''',
                101
            )
        )

    def test_47(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0:wr{Constructor (){}w(kH_h:Array [Array [Int ,0X5B],01_0_6];q,T,_f_2__7:k;W_,F0A5:Array [Array [Array [Array [Array [Int ,0X8BE],0x9],0xC_3],51],61]){} }Class y8_V{Constructor (){} }Class D{}Class j_9CM{Val c7,$47:c;}''',
                '''Class,_0,:,wr,{,Constructor,(,),{,},w,(,kH_h,:,Array,[,Array,[,Int,,,0X5B,],,,0106,],;,q,,,T,,,_f_2__7,:,k,;,W_,,,F0A5,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0X8BE,],,,0x9,],,,0xC3,],,,51,],,,61,],),{,},},Class,y8_V,{,Constructor,(,),{,},},Class,D,{,},Class,j_9CM,{,Val,c7,,,$47,:,c,;,},<EOF>''',
                101
            )
        )

    def test_48(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __H{$_oF3(h,_Z_,VL:String ;d:Int ){}Constructor (_,t2_,_:Boolean ){} }Class Eph:x_{Val $75,aZ:Float ;Var $_,$9:Boolean ;}Class _32{}''',
                '''Class,__H,{,$_oF3,(,h,,,_Z_,,,VL,:,String,;,d,:,Int,),{,},Constructor,(,_,,,t2_,,,_,:,Boolean,),{,},},Class,Eph,:,x_,{,Val,$75,,,aZ,:,Float,;,Var,$_,,,$9,:,Boolean,;,},Class,_32,{,},<EOF>''',
                101
            )
        )

    def test_49(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class _:_4{Destructor (){}Val _:Array [Boolean ,0x52];$L_(x:_i;j,w_r,x:Array [Float ,85_783];_1,_:Array [Boolean ,4];n,e_:Float ;_2__2:Array [Float ,49]){} }''',
                '''Class,__,{,},Class,_,:,_4,{,Destructor,(,),{,},Val,_,:,Array,[,Boolean,,,0x52,],;,$L_,(,x,:,_i,;,j,,,w_r,,,x,:,Array,[,Float,,,85783,],;,_1,,,_,:,Array,[,Boolean,,,4,],;,n,,,e_,:,Float,;,_2__2,:,Array,[,Float,,,49,],),{,},},<EOF>''',
                101
            )
        )

    def test_50(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ds_{Destructor (){}Destructor (){}Var s_,$1_04,_,$4Z,Ub_,$Y:_;_H(__:__X;t00,e___a_57:z){}Val $_:Array [Array [Array [String ,0X4],41],0B1000001];}''',
                '''Class,ds_,{,Destructor,(,),{,},Destructor,(,),{,},Var,s_,,,$1_04,,,_,,,$4Z,,,Ub_,,,$Y,:,_,;,_H,(,__,:,__X,;,t00,,,e___a_57,:,z,),{,},Val,$_,:,Array,[,Array,[,Array,[,String,,,0X4,],,,41,],,,0B1000001,],;,},<EOF>''',
                101
            )
        )

    def test_51(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _K7_:J{__B_b8(_Wh,_I9,O_,Sx0A:Float ;M___,EFX___,__T:_Do_3;_,_:i){}$__(_,_11:_;_5u8N9,h8_:_;_g,mvH__,_r,_7,_l:Array [Array [Boolean ,50],0x13];_0E_,_3s:Boolean ;_T:String ){} }''',
                '''Class,_K7_,:,J,{,__B_b8,(,_Wh,,,_I9,,,O_,,,Sx0A,:,Float,;,M___,,,EFX___,,,__T,:,_Do_3,;,_,,,_,:,i,),{,},$__,(,_,,,_11,:,_,;,_5u8N9,,,h8_,:,_,;,_g,,,mvH__,,,_r,,,_7,,,_l,:,Array,[,Array,[,Boolean,,,50,],,,0x13,],;,_0E_,,,_3s,:,Boolean,;,_T,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_52(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _61:_1{}Class __f{Var $o,$38I,$T7,$_H,$d:Array [Array [Array [Array [Array [Array [Array [Array [Int ,0b10],0b100],36],0x3],025],0B1],0B101000],0xB_A];}''',
                '''Class,_61,:,_1,{,},Class,__f,{,Var,$o,,,$38I,,,$T7,,,$_H,,,$d,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0b10,],,,0b100,],,,36,],,,0x3,],,,025,],,,0B1,],,,0B101000,],,,0xBA,],;,},<EOF>''',
                101
            )
        )

    def test_53(self):
        self.assertTrue(
            TestLexer.test(
                '''Class r:P{M7_(_:Array [String ,0X8];_,fL2,_u__f,s,y:Array [Array [Float ,0B1],0b1];x,_:Array [Array [Array [String ,0X6CC],0x1A],04];_5,_,Q:I_){} }''',
                '''Class,r,:,P,{,M7_,(,_,:,Array,[,String,,,0X8,],;,_,,,fL2,,,_u__f,,,s,,,y,:,Array,[,Array,[,Float,,,0B1,],,,0b1,],;,x,,,_,:,Array,[,Array,[,Array,[,String,,,0X6CC,],,,0x1A,],,,04,],;,_5,,,_,,,Q,:,I_,),{,},},<EOF>''',
                101
            )
        )

    def test_54(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class __123_:_c_8{_(V_I:_5Js4DE;n,_681:Array [Boolean ,06_6]){} }Class U:_{}Class K:T{Constructor (){}Destructor (){} }''',
                '''Class,__,{,},Class,__123_,:,_c_8,{,_,(,V_I,:,_5Js4DE,;,n,,,_681,:,Array,[,Boolean,,,066,],),{,},},Class,U,:,_,{,},Class,K,:,T,{,Constructor,(,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_55(self):
        self.assertTrue(
            TestLexer.test(
                '''Class U{Constructor (ED,_7n,_:Array [Array [Float ,0X39],0B100_1];I_,_:__;PK:Int ;J_,_,_:Array [Boolean ,0x5];Z_a:Float ){} }''',
                '''Class,U,{,Constructor,(,ED,,,_7n,,,_,:,Array,[,Array,[,Float,,,0X39,],,,0B1001,],;,I_,,,_,:,__,;,PK,:,Int,;,J_,,,_,,,_,:,Array,[,Boolean,,,0x5,],;,Z_a,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_56(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q64:i{Var F8,i:Array [Array [Array [Float ,0xD_C_3],6_705_1_5_8_19],47_9_5];}Class __:h{}Class d{Val $9:z;}''',
                '''Class,q64,:,i,{,Var,F8,,,i,:,Array,[,Array,[,Array,[,Float,,,0xDC3,],,,670515819,],,,4795,],;,},Class,__,:,h,{,},Class,d,{,Val,$9,:,z,;,},<EOF>''',
                101
            )
        )

    def test_57(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g5_9q_{}Class _d:y{Destructor (){Z::$4();}$5y5_(p,___,_13_p0J_1y4_:Array [Array [Array [String ,0105],0102],0XB];j:Array [Array [Array [Array [Array [Boolean ,0b100111],0B11],0B1011],4],0x46]){} }Class E8{}Class x71195:_{}''',
                '''Class,g5_9q_,{,},Class,_d,:,y,{,Destructor,(,),{,Z,::,$4,(,),;,},$5y5_,(,p,,,___,,,_13_p0J_1y4_,:,Array,[,Array,[,Array,[,String,,,0105,],,,0102,],,,0XB,],;,j,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b100111,],,,0B11,],,,0B1011,],,,4,],,,0x46,],),{,},},Class,E8,{,},Class,x71195,:,_,{,},<EOF>''',
                101
            )
        )

    def test_58(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b{}Class _:ao{Constructor (_,h_e,_Ih4S,_sH:Array [Float ,0x9];_72:Float ;cd,_:Array [Array [Float ,04],37806_6_3]){}$_1(p_:String ;__3,_:Int ;_9_:a_P3;C:Array [Array [Float ,05],0X4]){ {} }}Class O:_{}Class _{}''',
                '''Class,b,{,},Class,_,:,ao,{,Constructor,(,_,,,h_e,,,_Ih4S,,,_sH,:,Array,[,Float,,,0x9,],;,_72,:,Float,;,cd,,,_,:,Array,[,Array,[,Float,,,04,],,,3780663,],),{,},$_1,(,p_,:,String,;,__3,,,_,:,Int,;,_9_,:,a_P3,;,C,:,Array,[,Array,[,Float,,,05,],,,0X4,],),{,{,},},},Class,O,:,_,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_59(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_9{}Class _{}Class d:_{}Class _0:BZ{}Class _W{$5(m,F,d:Array [Array [Array [Array [Array [String ,8],0b11],61],7_21_897_13],05_3]){} }''',
                '''Class,_,:,_9,{,},Class,_,{,},Class,d,:,_,{,},Class,_0,:,BZ,{,},Class,_W,{,$5,(,m,,,F,,,d,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,8,],,,0b11,],,,61,],,,72189713,],,,053,],),{,},},<EOF>''',
                101
            )
        )

    def test_60(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P_:_{Constructor (){}Val $43V,_,_2,$_:Boolean ;Val W7,_1m:Array [Boolean ,0B11001];Constructor (R7:String ;_,c,_:_;m_,_Qs_z3:Array [Array [Array [Array [Int ,0X3D],0631_0],100],0B11001];k,NP45:M;_,_:Boolean ;u:V;__:Array [Boolean ,0b10]){} }''',
                '''Class,P_,:,_,{,Constructor,(,),{,},Val,$43V,,,_,,,_2,,,$_,:,Boolean,;,Val,W7,,,_1m,:,Array,[,Boolean,,,0B11001,],;,Constructor,(,R7,:,String,;,_,,,c,,,_,:,_,;,m_,,,_Qs_z3,:,Array,[,Array,[,Array,[,Array,[,Int,,,0X3D,],,,06310,],,,100,],,,0B11001,],;,k,,,NP45,:,M,;,_,,,_,:,Boolean,;,u,:,V,;,__,:,Array,[,Boolean,,,0b10,],),{,},},<EOF>''',
                101
            )
        )

    def test_61(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V1__f_:h_P2{_x4(no:Array [Int ,30];__:Int ;_c:U7u;_:Array [String ,0x93_3A5];pS__z,Z_,_,_z,i:Int ){} }Class N_J:_3_{}''',
                '''Class,V1__f_,:,h_P2,{,_x4,(,no,:,Array,[,Int,,,30,],;,__,:,Int,;,_c,:,U7u,;,_,:,Array,[,String,,,0x933A5,],;,pS__z,,,Z_,,,_,,,_z,,,i,:,Int,),{,},},Class,N_J,:,_3_,{,},<EOF>''',
                101
            )
        )

    def test_62(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:n48{Var dL,_:Float ;Var i___:Array [Boolean ,87];Var __:Array [Boolean ,87]=!-__::$___U._();__(_Zs27:_1;z:_;_:Array [Int ,046]){Continue ;Val Z,F_2:Boolean ;Break ;} }''',
                '''Class,_,:,n48,{,Var,dL,,,_,:,Float,;,Var,i___,:,Array,[,Boolean,,,87,],;,Var,__,:,Array,[,Boolean,,,87,],=,!,-,__,::,$___U,.,_,(,),;,__,(,_Zs27,:,_1,;,z,:,_,;,_,:,Array,[,Int,,,046,],),{,Continue,;,Val,Z,,,F_2,:,Boolean,;,Break,;,},},<EOF>''',
                101
            )
        )

    def test_63(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:m9b{}Class _R{Val k:C7_;}Class d{Destructor (){}Var $_,T,$1:Array [Array [Array [Array [Int ,054],0x3],0b11_0],0b1100001];_(){Var P,_,wO:J;} }''',
                '''Class,_,:,m9b,{,},Class,_R,{,Val,k,:,C7_,;,},Class,d,{,Destructor,(,),{,},Var,$_,,,T,,,$1,:,Array,[,Array,[,Array,[,Array,[,Int,,,054,],,,0x3,],,,0b110,],,,0b1100001,],;,_,(,),{,Var,P,,,_,,,wO,:,J,;,},},<EOF>''',
                101
            )
        )

    def test_64(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E__{__(__H,h,G_,D_6,__1i,_u_,_02gMj_:Float ;S,_:Array [Int ,033];K:Int ;f,r0,j4_,_:Boolean ;kl2,_7:a){} }''',
                '''Class,E__,{,__,(,__H,,,h,,,G_,,,D_6,,,__1i,,,_u_,,,_02gMj_,:,Float,;,S,,,_,:,Array,[,Int,,,033,],;,K,:,Int,;,f,,,r0,,,j4_,,,_,:,Boolean,;,kl2,,,_7,:,a,),{,},},<EOF>''',
                101
            )
        )

    def test_65(self):
        self.assertTrue(
            TestLexer.test(
                '''Class F:_{Constructor (u_A,i_2Co__,_,E_X:String ){} }Class U:h{}Class C:_{Val qc6f4,$__,$5:Float ;Destructor (){} }Class j6X{}Class _{}''',
                '''Class,F,:,_,{,Constructor,(,u_A,,,i_2Co__,,,_,,,E_X,:,String,),{,},},Class,U,:,h,{,},Class,C,:,_,{,Val,qc6f4,,,$__,,,$5,:,Float,;,Destructor,(,),{,},},Class,j6X,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_66(self):
        self.assertTrue(
            TestLexer.test(
                '''Class G7_F:m{Destructor (){}Var $W4__5:Float ;}Class __:_{}Class j92I_{a_(_:mkf){}Var x:Array [Array [Array [Int ,0xEF],052],052];}''',
                '''Class,G7_F,:,m,{,Destructor,(,),{,},Var,$W4__5,:,Float,;,},Class,__,:,_,{,},Class,j92I_,{,a_,(,_,:,mkf,),{,},Var,x,:,Array,[,Array,[,Array,[,Int,,,0xEF,],,,052,],,,052,],;,},<EOF>''',
                101
            )
        )

    def test_67(self):
        self.assertTrue(
            TestLexer.test(
                '''Class F{}Class m_6_Zk{Var _q0,Q,X:Boolean ;Constructor (xN8:s;u,k,c0_6:Array [String ,06];W,_Z,w__:Array [String ,0b111000]){} }''',
                '''Class,F,{,},Class,m_6_Zk,{,Var,_q0,,,Q,,,X,:,Boolean,;,Constructor,(,xN8,:,s,;,u,,,k,,,c0_6,:,Array,[,String,,,06,],;,W,,,_Z,,,w__,:,Array,[,String,,,0b111000,],),{,},},<EOF>''',
                101
            )
        )

    def test_68(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_5{Constructor (Q_,_8099z:Array [Array [Array [Array [Array [Array [Array [String ,0b110101],0x8],0102],0b1],49_4_1],0b110101],38]){} }Class I:_7{}''',
                '''Class,_,:,_5,{,Constructor,(,Q_,,,_8099z,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b110101,],,,0x8,],,,0102,],,,0b1,],,,4941,],,,0b110101,],,,38,],),{,},},Class,I,:,_7,{,},<EOF>''',
                101
            )
        )

    def test_69(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w:a{}Class _6:fY_{}Class _{Constructor (_,Z:_){Break ;Break ;Val l:Array [Float ,0b10];}Constructor (){} }''',
                '''Class,w,:,a,{,},Class,_6,:,fY_,{,},Class,_,{,Constructor,(,_,,,Z,:,_,),{,Break,;,Break,;,Val,l,:,Array,[,Float,,,0b10,],;,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_70(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Pt{}Class R:A_{Val $j,$6:Array [Array [Boolean ,0410_1_2],0302];Val l__:Array [Int ,0b1000];Val $LN_,_R,B_,P_l_g:_;}''',
                '''Class,Pt,{,},Class,R,:,A_,{,Val,$j,,,$6,:,Array,[,Array,[,Boolean,,,041012,],,,0302,],;,Val,l__,:,Array,[,Int,,,0b1000,],;,Val,$LN_,,,_R,,,B_,,,P_l_g,:,_,;,},<EOF>''',
                101
            )
        )

    def test_71(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __J:Xp{Var $q,_9:String ;Constructor (o03__:Array [Array [Array [Float ,0b101110],0b1_001],0X1];_,cw:String ){ {}_::$p._3337();} }''',
                '''Class,__J,:,Xp,{,Var,$q,,,_9,:,String,;,Constructor,(,o03__,:,Array,[,Array,[,Array,[,Float,,,0b101110,],,,0b1001,],,,0X1,],;,_,,,cw,:,String,),{,{,},_,::,$p,.,_3337,(,),;,},},<EOF>''',
                101
            )
        )

    def test_72(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0{}Class __:h{Val $_d:Array [Array [Int ,0B1],0X9_9_2];}Class L:_2{Constructor (_3,_:Int ;_:Array [String ,026]){} }''',
                '''Class,_0,{,},Class,__,:,h,{,Val,$_d,:,Array,[,Array,[,Int,,,0B1,],,,0X992,],;,},Class,L,:,_2,{,Constructor,(,_3,,,_,:,Int,;,_,:,Array,[,String,,,026,],),{,},},<EOF>''',
                101
            )
        )

    def test_73(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _5m{}Class ___:_{Val $2s_,F0,C1V,_,$e:Array [Array [String ,0x11],0b1011101];}Class _{Val $_:Int ;}Class g:K{}Class _{Val _:Array [String ,0x11];}Class v{}''',
                '''Class,_5m,{,},Class,___,:,_,{,Val,$2s_,,,F0,,,C1V,,,_,,,$e,:,Array,[,Array,[,String,,,0x11,],,,0b1011101,],;,},Class,_,{,Val,$_,:,Int,;,},Class,g,:,K,{,},Class,_,{,Val,_,:,Array,[,String,,,0x11,],;,},Class,v,{,},<EOF>''',
                101
            )
        )

    def test_74(self):
        self.assertTrue(
            TestLexer.test(
                '''Class DG{Var __:Array [Float ,0B1011001];Var _8:Array [Array [Array [Array [Array [String ,016],70],23_98],0B1],70];}Class _4hG_5:_{}''',
                '''Class,DG,{,Var,__,:,Array,[,Float,,,0B1011001,],;,Var,_8,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,016,],,,70,],,,2398,],,,0B1,],,,70,],;,},Class,_4hG_5,:,_,{,},<EOF>''',
                101
            )
        )

    def test_75(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _F4_19:__{$2(_:_1){}$h(_2,_12jx:Array [Array [Int ,04],0X4C];pX,V:Array [Array [Int ,0b1001010],75];_,_,_rm,HEm:Array [Array [Boolean ,4],75]){}Var Q_H2,$8,n:sSr;}Class _:_{Val Eb:Array [Array [Array [Array [Array [Array [Float ,0x5C],0X4C],03],75],02_5],0x2_5_F_2];}''',
                '''Class,_F4_19,:,__,{,$2,(,_,:,_1,),{,},$h,(,_2,,,_12jx,:,Array,[,Array,[,Int,,,04,],,,0X4C,],;,pX,,,V,:,Array,[,Array,[,Int,,,0b1001010,],,,75,],;,_,,,_,,,_rm,,,HEm,:,Array,[,Array,[,Boolean,,,4,],,,75,],),{,},Var,Q_H2,,,$8,,,n,:,sSr,;,},Class,_,:,_,{,Val,Eb,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x5C,],,,0X4C,],,,03,],,,75,],,,025,],,,0x25F2,],;,},<EOF>''',
                101
            )
        )

    def test_76(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E{h(_:Array [Boolean ,0x47]){} }Class I2_:p{Var x3,$a__,u:Array [Array [Array [String ,0XA],0B1],0b110010];Constructor (){Continue ;Continue ;}Var $_j_4:Array [Array [Array [Array [Array [Array [Float ,0b1],0B110010],025],0X38],0b110010],025];}''',
                '''Class,E,{,h,(,_,:,Array,[,Boolean,,,0x47,],),{,},},Class,I2_,:,p,{,Var,x3,,,$a__,,,u,:,Array,[,Array,[,Array,[,String,,,0XA,],,,0B1,],,,0b110010,],;,Constructor,(,),{,Continue,;,Continue,;,},Var,$_j_4,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1,],,,0B110010,],,,025,],,,0X38,],,,0b110010,],,,025,],;,},<EOF>''',
                101
            )
        )

    def test_77(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X{}Class ____{Destructor (){ {} }}Class g5:H{}Class _:_{Val $_T,_77,$__6,$_:Array [Float ,010];}Class ____9:_{}''',
                '''Class,X,{,},Class,____,{,Destructor,(,),{,{,},},},Class,g5,:,H,{,},Class,_,:,_,{,Val,$_T,,,_77,,,$__6,,,$_,:,Array,[,Float,,,010,],;,},Class,____9,:,_,{,},<EOF>''',
                101
            )
        )

    def test_78(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __15:r{Destructor (){}$5___(){}Constructor (KV,Tz:Array [Array [Array [Array [Array [Boolean ,3],03_0],033],5],0x5_A]){} }Class _{}''',
                '''Class,__15,:,r,{,Destructor,(,),{,},$5___,(,),{,},Constructor,(,KV,,,Tz,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,3,],,,030,],,,033,],,,5,],,,0x5A,],),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_79(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:e_{__c(c9_:Float ;Q,_GrW,_2Y,_:String ;N:String ){}$h(H,c5HE,jv:Array [Int ,0B1];__9:Float ){Break ;} }''',
                '''Class,_,:,e_,{,__c,(,c9_,:,Float,;,Q,,,_GrW,,,_2Y,,,_,:,String,;,N,:,String,),{,},$h,(,H,,,c5HE,,,jv,:,Array,[,Int,,,0B1,],;,__9,:,Float,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_80(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:_{}Class _:_{Constructor (_:Array [Int ,0XE_6];_:Array [Array [Array [Boolean ,2_7],0B1100_0],0103];_:_X){} }Class E{Destructor (){Return ;} }Class _oE_:Ew{}Class __{}Class b:_{}Class _{}Class _{Val $_8,$F3_,f8:_0;}Class _P_x55_{}Class f:b{}''',
                '''Class,__,:,_,{,},Class,_,:,_,{,Constructor,(,_,:,Array,[,Int,,,0XE6,],;,_,:,Array,[,Array,[,Array,[,Boolean,,,27,],,,0B11000,],,,0103,],;,_,:,_X,),{,},},Class,E,{,Destructor,(,),{,Return,;,},},Class,_oE_,:,Ew,{,},Class,__,{,},Class,b,:,_,{,},Class,_,{,},Class,_,{,Val,$_8,,,$F3_,,,f8,:,_0,;,},Class,_P_x55_,{,},Class,f,:,b,{,},<EOF>''',
                101
            )
        )

    def test_81(self):
        self.assertTrue(
            TestLexer.test(
                '''Class v491:y6l_1{Var $F_rk:String ;}Class a_t{Val $_:Array [Array [Float ,73_823_5_0],0x3E_7];}Class _{Var c:Int ;}''',
                '''Class,v491,:,y6l_1,{,Var,$F_rk,:,String,;,},Class,a_t,{,Val,$_,:,Array,[,Array,[,Float,,,7382350,],,,0x3E7,],;,},Class,_,{,Var,c,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_82(self):
        self.assertTrue(
            TestLexer.test(
                '''Class kw0:f2{Var l:_;Val _7_,b,m:_;Constructor (_:__;C:Array [Array [Int ,0B110_00_1],81]){} }Class _:_{}Class d6:_{}''',
                '''Class,kw0,:,f2,{,Var,l,:,_,;,Val,_7_,,,b,,,m,:,_,;,Constructor,(,_,:,__,;,C,:,Array,[,Array,[,Int,,,0B110001,],,,81,],),{,},},Class,_,:,_,{,},Class,d6,:,_,{,},<EOF>''',
                101
            )
        )

    def test_83(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _y3__A_{}Class _{$21_(upN_26g4__,__,_:Boolean ;l37z,_Y_S,___:_8;V,l_,O:String ;_7:Boolean ){} }Class A_:la{}''',
                '''Class,_y3__A_,{,},Class,_,{,$21_,(,upN_26g4__,,,__,,,_,:,Boolean,;,l37z,,,_Y_S,,,___,:,_8,;,V,,,l_,,,O,:,String,;,_7,:,Boolean,),{,},},Class,A_,:,la,{,},<EOF>''',
                101
            )
        )

    def test_84(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Q9_{Constructor (_:Float ;_:x;_U1:String ;O,z:Y;c,X:_;A8,_,x:Array [Array [Array [Boolean ,0B100011],0b111110],0b111_1]){} }''',
                '''Class,Q9_,{,Constructor,(,_,:,Float,;,_,:,x,;,_U1,:,String,;,O,,,z,:,Y,;,c,,,X,:,_,;,A8,,,_,,,x,:,Array,[,Array,[,Array,[,Boolean,,,0B100011,],,,0b111110,],,,0b1111,],),{,},},<EOF>''',
                101
            )
        )

    def test_85(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class __{Var $_:Array [String ,3];}Class a_{Var $S,v__d:N1O5;Constructor (h,____,_,_,W,k_:String ){} }''',
                '''Class,__,{,},Class,__,{,Var,$_,:,Array,[,String,,,3,],;,},Class,a_,{,Var,$S,,,v__d,:,N1O5,;,Constructor,(,h,,,____,,,_,,,_,,,W,,,k_,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_86(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T__16{Constructor (w_:String ){_B9::$5_4();}Constructor (AG4,_,J_,S,_:_9b;__,_:Array [Array [Array [Boolean ,0B1000110],0X2],022];a_,_,E:String ){} }''',
                '''Class,T__16,{,Constructor,(,w_,:,String,),{,_B9,::,$5_4,(,),;,},Constructor,(,AG4,,,_,,,J_,,,S,,,_,:,_9b,;,__,,,_,:,Array,[,Array,[,Array,[,Boolean,,,0B1000110,],,,0X2,],,,022,],;,a_,,,_,,,E,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_87(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m{}Class W{}Class F{}Class _:G{}Class _:_R{}Class _:_1{}Class _{__(_PN:Array [Float ,39_4]){}Destructor (){Break ;} }''',
                '''Class,m,{,},Class,W,{,},Class,F,{,},Class,_,:,G,{,},Class,_,:,_R,{,},Class,_,:,_1,{,},Class,_,{,__,(,_PN,:,Array,[,Float,,,394,],),{,},Destructor,(,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_88(self):
        self.assertTrue(
            TestLexer.test(
                '''Class lR{Destructor (){} }Class _J{}Class IK:y{Destructor (){Break ;}Val $_1:Array [Array [Boolean ,0b1_00],0105];}''',
                '''Class,lR,{,Destructor,(,),{,},},Class,_J,{,},Class,IK,:,y,{,Destructor,(,),{,Break,;,},Val,$_1,:,Array,[,Array,[,Boolean,,,0b100,],,,0105,],;,},<EOF>''',
                101
            )
        )

    def test_89(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __Q{Val cD_,_:_;}Class L:_{}Class _:_{}Class _40{Destructor (){}Val $j_7S_,$0_:jfl;}Class g{Destructor (){} }''',
                '''Class,__Q,{,Val,cD_,,,_,:,_,;,},Class,L,:,_,{,},Class,_,:,_,{,},Class,_40,{,Destructor,(,),{,},Val,$j_7S_,,,$0_,:,jfl,;,},Class,g,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_90(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _Zd8:dbm{Constructor (_:Array [Array [Int ,061],0X48];v2320_:Array [Array [Array [Array [Boolean ,02],15_7],0X48],64];_:Float ){} }''',
                '''Class,_Zd8,:,dbm,{,Constructor,(,_,:,Array,[,Array,[,Int,,,061,],,,0X48,],;,v2320_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,02,],,,157,],,,0X48,],,,64,],;,_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_91(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k:Pc{Val $f:String ;}Class _:__5_f{Destructor (){n8::$6_6_.v();Break ;} }Class G__{Var $2:Array [Float ,037];}''',
                '''Class,k,:,Pc,{,Val,$f,:,String,;,},Class,_,:,__5_f,{,Destructor,(,),{,n8,::,$6_6_,.,v,(,),;,Break,;,},},Class,G__,{,Var,$2,:,Array,[,Float,,,037,],;,},<EOF>''',
                101
            )
        )

    def test_92(self):
        self.assertTrue(
            TestLexer.test(
                '''Class d:_{}Class _{}Class _{$62H(_v:Array [Float ,0X2D]){Return ;{Continue ;Val __,_w:Array [Array [Float ,0xC],31];}Return ;Break ;}$a(){}Val $j0,a_:Array [Boolean ,0b1000];}''',
                '''Class,d,:,_,{,},Class,_,{,},Class,_,{,$62H,(,_v,:,Array,[,Float,,,0X2D,],),{,Return,;,{,Continue,;,Val,__,,,_w,:,Array,[,Array,[,Float,,,0xC,],,,31,],;,},Return,;,Break,;,},$a,(,),{,},Val,$j0,,,a_,:,Array,[,Boolean,,,0b1000,],;,},<EOF>''',
                101
            )
        )

    def test_93(self):
        self.assertTrue(
            TestLexer.test(
                '''Class O_0{Var ZAN6:_;Constructor (_0,_g:_;_:Int ;V:Array [Array [Boolean ,0b10],0X5_62_11]){}_5(){}Destructor (){y::$z8_();} }''',
                '''Class,O_0,{,Var,ZAN6,:,_,;,Constructor,(,_0,,,_g,:,_,;,_,:,Int,;,V,:,Array,[,Array,[,Boolean,,,0b10,],,,0X56211,],),{,},_5,(,),{,},Destructor,(,),{,y,::,$z8_,(,),;,},},<EOF>''',
                101
            )
        )

    def test_94(self):
        self.assertTrue(
            TestLexer.test(
                '''Class x:fk0_{}Class o_{Var T2v7:String ;}Class _{Constructor (H_:Boolean ){}Constructor (){Continue ;Var t,__g,j,QbP__l:k;} }Class j:b{}''',
                '''Class,x,:,fk0_,{,},Class,o_,{,Var,T2v7,:,String,;,},Class,_,{,Constructor,(,H_,:,Boolean,),{,},Constructor,(,),{,Continue,;,Var,t,,,__g,,,j,,,QbP__l,:,k,;,},},Class,j,:,b,{,},<EOF>''',
                101
            )
        )

    def test_95(self):
        self.assertTrue(
            TestLexer.test(
                '''Class kM:_3{}Class __{Val d,$__:Array [Array [Array [Float ,61],61],0B1];Var $_,f3__,g:Array [Boolean ,0X1_37_D];}''',
                '''Class,kM,:,_3,{,},Class,__,{,Val,d,,,$__,:,Array,[,Array,[,Array,[,Float,,,61,],,,61,],,,0B1,],;,Var,$_,,,f3__,,,g,:,Array,[,Boolean,,,0X137D,],;,},<EOF>''',
                101
            )
        )

    def test_96(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _:v{$S(B:Array [String ,0x43];t_,Ii,_N,G:__;y:Array [Array [Array [Int ,0b1],2],01]){Continue ;}Destructor (){}Var $618,_8:Float ;}''',
                '''Class,_,{,},Class,_,:,v,{,$S,(,B,:,Array,[,String,,,0x43,],;,t_,,,Ii,,,_N,,,G,:,__,;,y,:,Array,[,Array,[,Array,[,Int,,,0b1,],,,2,],,,01,],),{,Continue,;,},Destructor,(,),{,},Var,$618,,,_8,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_97(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __5:x_{Constructor (){}$5(__:M;z53:N;_,H4,s9M,w_7,t,__,_9,_:Array [Array [Array [Array [Boolean ,0B10000],4_9],0B1],0B1];_:Array [Int ,4]){} }''',
                '''Class,__5,:,x_,{,Constructor,(,),{,},$5,(,__,:,M,;,z53,:,N,;,_,,,H4,,,s9M,,,w_7,,,t,,,__,,,_9,,,_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B10000,],,,49,],,,0B1,],,,0B1,],;,_,:,Array,[,Int,,,4,],),{,},},<EOF>''',
                101
            )
        )

    def test_98(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n{Var l___a62H__,_,O,r_8k:n;Val Ra__:Int ;}Class j7:___L{}Class V{}Class _{}Class __z9:_{Val $__:String ;Destructor (){Break ;Break ;} }''',
                '''Class,n,{,Var,l___a62H__,,,_,,,O,,,r_8k,:,n,;,Val,Ra__,:,Int,;,},Class,j7,:,___L,{,},Class,V,{,},Class,_,{,},Class,__z9,:,_,{,Val,$__,:,String,;,Destructor,(,),{,Break,;,Break,;,},},<EOF>''',
                101
            )
        )

    def test_99(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var _:Array [Array [Float ,2_9],5_3];}Class Lz{Destructor (){Break ;} }
            Class Y_ee{}
            Class _Y:_it0_{
                Constructor (w,f:Array [Array [Array [Array [Array [Array [Float ,0xF],54],0x3B],8],0B100000],0xC];___:_s;Q:Array [String ,0X4A]){} }Class _U:__Z{Val F_8_:String ;}''',
                '''Class,_,{,Var,_,:,Array,[,Array,[,Float,,,29,],,,53,],;,},Class,Lz,{,Destructor,(,),{,Break,;,},},Class,Y_ee,{,},Class,_Y,:,_it0_,{,Constructor,(,w,,,f,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0xF,],,,54,],,,0x3B,],,,8,],,,0B100000,],,,0xC,],;,___,:,_s,;,Q,:,Array,[,String,,,0X4A,],),{,},},Class,_U,:,__Z,{,Val,F_8_,:,String,;,},<EOF>''',
                101
            )
        )

    def test_100(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Ra:lk{S(h,S9k1:Float ;_9,b:kM;_:Boolean ;_,u,jn,h,_:Boolean ){Continue ;Xi::$6_3();}Val $xt_1,$R_5_:Boolean ;}''',
                '''Class,Ra,:,lk,{,S,(,h,,,S9k1,:,Float,;,_9,,,b,:,kM,;,_,:,Boolean,;,_,,,u,,,jn,,,h,,,_,:,Boolean,),{,Continue,;,Xi,::,$6_3,(,),;,},Val,$xt_1,,,$R_5_,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_101(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __q:mV{_(){}Var _,$_j,_8:String ;b6(_h0,_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,3],0X27],0X27],0436],07],07],0125],3],4];_,_:Array [Array [String ,0x23],0x7];z,_,_,_8q8:Boolean ;_:Array [Boolean ,0X27];h,Q,_:Boolean ){} }''',
                '''Class,__q,:,mV,{,_,(,),{,},Var,_,,,$_j,,,_8,:,String,;,b6,(,_h0,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,3,],,,0X27,],,,0X27,],,,0436,],,,07,],,,07,],,,0125,],,,3,],,,4,],;,_,,,_,:,Array,[,Array,[,String,,,0x23,],,,0x7,],;,z,,,_,,,_,,,_8q8,:,Boolean,;,_,:,Array,[,Boolean,,,0X27,],;,h,,,Q,,,_,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_102(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J{}Class x{}Class _{}Class _8:_{}Class _298:__{Val rCS,$_1,$_1,$_2,$55,_:Array [Array [Array [Array [Array [Float ,8_51],87],0116],06],02_7];}''',
                '''Class,J,{,},Class,x,{,},Class,_,{,},Class,_8,:,_,{,},Class,_298,:,__,{,Val,rCS,,,$_1,,,$_1,,,$_2,,,$55,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,851,],,,87,],,,0116,],,,06,],,,027,],;,},<EOF>''',
                101
            )
        )

    def test_103(self):
        self.assertTrue(
            TestLexer.test(
                '''Class D:v_{Constructor (_3R:Array [Array [Array [Array [Boolean ,017],05],0X63],50]){Var GM,E:String ;} }Class J:f4_3_{}''',
                '''Class,D,:,v_,{,Constructor,(,_3R,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,017,],,,05,],,,0X63,],,,50,],),{,Var,GM,,,E,:,String,;,},},Class,J,:,f4_3_,{,},<EOF>''',
                101
            )
        )

    def test_104(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:N6{Destructor (){Val __S:Array [Float ,80];Val I,_0,Tn057Vr:Array [Int ,9_8];} }Class s03:_3____{}Class __1{}''',
                '''Class,_,:,N6,{,Destructor,(,),{,Val,__S,:,Array,[,Float,,,80,],;,Val,I,,,_0,,,Tn057Vr,:,Array,[,Int,,,98,],;,},},Class,s03,:,_3____,{,},Class,__1,{,},<EOF>''',
                101
            )
        )

    def test_105(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val _,_,O4:Array [Array [String ,21],06];Val _:String ;Val _Q,$05:String ;Val $J,$7qw_4:String ;C(_,_:Int ){}Constructor (){}Destructor (){} }Class RR4{}''',
                '''Class,_,{,Val,_,,,_,,,O4,:,Array,[,Array,[,String,,,21,],,,06,],;,Val,_,:,String,;,Val,_Q,,,$05,:,String,;,Val,$J,,,$7qw_4,:,String,;,C,(,_,,,_,:,Int,),{,},Constructor,(,),{,},Destructor,(,),{,},},Class,RR4,{,},<EOF>''',
                101
            )
        )

    def test_106(self):
        self.assertTrue(
            TestLexer.test(
                '''Class U5E_85_:_Y{Destructor (){}Constructor (o,_:Array [Array [Float ,0xC_1],0b10000]){}Val $M__:_;}Class wa9{}Class _{}''',
                '''Class,U5E_85_,:,_Y,{,Destructor,(,),{,},Constructor,(,o,,,_,:,Array,[,Array,[,Float,,,0xC1,],,,0b10000,],),{,},Val,$M__,:,_,;,},Class,wa9,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_107(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0:b{Destructor (){}Destructor (){} }Class _53:G{__(_:Int ){}_(i,__:String ;_:Int ;j2_,_fN8V,CBu:_ok){} }Class _:FI{}''',
                '''Class,_0,:,b,{,Destructor,(,),{,},Destructor,(,),{,},},Class,_53,:,G,{,__,(,_,:,Int,),{,},_,(,i,,,__,:,String,;,_,:,Int,;,j2_,,,_fN8V,,,CBu,:,_ok,),{,},},Class,_,:,FI,{,},<EOF>''',
                101
            )
        )

    def test_108(self):
        self.assertTrue(
            TestLexer.test(
                '''Class d{_(_1f__,A,_D_l:_;_,_4:ZB_;L,w2:Int ;w,L35,i_:Array [Array [Array [Array [Boolean ,5],725_5],0B101100],0x4_FA_F_F_BB99];h:Array [Boolean ,0X8B]){} }''',
                '''Class,d,{,_,(,_1f__,,,A,,,_D_l,:,_,;,_,,,_4,:,ZB_,;,L,,,w2,:,Int,;,w,,,L35,,,i_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,5,],,,7255,],,,0B101100,],,,0x4FAFFBB99,],;,h,:,Array,[,Boolean,,,0X8B,],),{,},},<EOF>''',
                101
            )
        )

    def test_109(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8{Constructor (E,_,_Oy_,_g:Array [Array [Array [Array [Int ,0x55],0xE5],0x821],0b1011110];d:Array [Array [Int ,23],23]){} }''',
                '''Class,_8,{,Constructor,(,E,,,_,,,_Oy_,,,_g,:,Array,[,Array,[,Array,[,Array,[,Int,,,0x55,],,,0xE5,],,,0x821,],,,0b1011110,],;,d,:,Array,[,Array,[,Int,,,23,],,,23,],),{,},},<EOF>''',
                101
            )
        )

    def test_110(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _4:_3{}Class _1_:_3JN_{Val $8,$9r8m:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0xE],0X2_8],3_7],44],032],0X2E],94],032],0x4A],050];}Class g{}Class __D:f{Constructor (){} }''',
                '''Class,_4,:,_3,{,},Class,_1_,:,_3JN_,{,Val,$8,,,$9r8m,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0xE,],,,0X28,],,,37,],,,44,],,,032,],,,0X2E,],,,94,],,,032,],,,0x4A,],,,050,],;,},Class,g,{,},Class,__D,:,f,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_111(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _A:X_CD{Val _:Array [Array [Int ,68],35];Val $6a,k,$y:Array [Array [Array [Array [Array [Float ,0X3C],025],025],0B1],0XA_39];k(){}Var $__,$_:Float ;Val ym634:String ;}''',
                '''Class,_A,:,X_CD,{,Val,_,:,Array,[,Array,[,Int,,,68,],,,35,],;,Val,$6a,,,k,,,$y,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X3C,],,,025,],,,025,],,,0B1,],,,0XA39,],;,k,(,),{,},Var,$__,,,$_,:,Float,;,Val,ym634,:,String,;,},<EOF>''',
                101
            )
        )

    def test_112(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0_s_4:i{Destructor (){}Constructor (_S4,y:Array [Float ,0xE_E];O__I9P8,F,p53Q,E,_,_6,_:__;r:ZGB){} }Class t_3u8:_66{J(){Val B,_Y,_,W,_S:Boolean ;Continue ;{} }}''',
                '''Class,_0_s_4,:,i,{,Destructor,(,),{,},Constructor,(,_S4,,,y,:,Array,[,Float,,,0xEE,],;,O__I9P8,,,F,,,p53Q,,,E,,,_,,,_6,,,_,:,__,;,r,:,ZGB,),{,},},Class,t_3u8,:,_66,{,J,(,),{,Val,B,,,_Y,,,_,,,W,,,_S,:,Boolean,;,Continue,;,{,},},},<EOF>''',
                101
            )
        )

    def test_113(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_J_{Constructor (){}$_(_,_,_A_,_5:Float ){_::$___();} }Class __IA:V{}Class Lo6{Destructor (){Break ;Return ;}Var O:Array [Boolean ,4_15_5_1];}Class R:g3{_mMF(y:Boolean ;Wik5,__E:_D;_3:jd;_,M8ZRc9:H){Continue ;} }''',
                '''Class,_,:,_J_,{,Constructor,(,),{,},$_,(,_,,,_,,,_A_,,,_5,:,Float,),{,_,::,$___,(,),;,},},Class,__IA,:,V,{,},Class,Lo6,{,Destructor,(,),{,Break,;,Return,;,},Var,O,:,Array,[,Boolean,,,41551,],;,},Class,R,:,g3,{,_mMF,(,y,:,Boolean,;,Wik5,,,__E,:,_D,;,_3,:,jd,;,_,,,M8ZRc9,:,H,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_114(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _6{Destructor (){}Constructor (G_4y,_:_;__,v4:Boolean ;SF_X:Boolean ;_:_a;cY_y_:__;Z:_;k,_:Int ;H,f:Array [Array [String ,0B11001],8];_GI5:String ){Return ;} }Class _{Val $p:String ;$_5(){}Constructor (){} }''',
                '''Class,_6,{,Destructor,(,),{,},Constructor,(,G_4y,,,_,:,_,;,__,,,v4,:,Boolean,;,SF_X,:,Boolean,;,_,:,_a,;,cY_y_,:,__,;,Z,:,_,;,k,,,_,:,Int,;,H,,,f,:,Array,[,Array,[,String,,,0B11001,],,,8,],;,_GI5,:,String,),{,Return,;,},},Class,_,{,Val,$p,:,String,;,$_5,(,),{,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_115(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _o:___{}Class _:_G{}Class __8:dr_{Var _,Zd5G____:String ;}Class _{}Class _2:__{Val g_T_h8_:_RA;}Class _0_8{}''',
                '''Class,_o,:,___,{,},Class,_,:,_G,{,},Class,__8,:,dr_,{,Var,_,,,Zd5G____,:,String,;,},Class,_,{,},Class,_2,:,__,{,Val,g_T_h8_,:,_RA,;,},Class,_0_8,{,},<EOF>''',
                101
            )
        )

    def test_116(self):
        self.assertTrue(
            TestLexer.test(
                '''Class GO:_1{}Class q:b6{_W(G_P:Float ;___:_){}Constructor (_,F_486,_,j:_;_0PmU1,G1_,_5__:Float ;R,_,_,_3:Boolean ){} }Class Z_0_{}Class z:_{Constructor (Bc:Fp0__){} }''',
                '''Class,GO,:,_1,{,},Class,q,:,b6,{,_W,(,G_P,:,Float,;,___,:,_,),{,},Constructor,(,_,,,F_486,,,_,,,j,:,_,;,_0PmU1,,,G1_,,,_5__,:,Float,;,R,,,_,,,_,,,_3,:,Boolean,),{,},},Class,Z_0_,{,},Class,z,:,_,{,Constructor,(,Bc,:,Fp0__,),{,},},<EOF>''',
                101
            )
        )

    def test_117(self):
        self.assertTrue(
            TestLexer.test(
                '''Class z_:Wc{Constructor (_,_O__:e;_c:Array [Array [Boolean ,0x3],0b1010110];_1_x_7f:Array [String ,0B11000];W:Array [Array [Array [Array [Array [Boolean ,0126],0x62],0B1],04],0XD]){} }Class _fK{}Class D:_{}Class T0{Val H:Array [Boolean ,0x7];}''',
                '''Class,z_,:,Wc,{,Constructor,(,_,,,_O__,:,e,;,_c,:,Array,[,Array,[,Boolean,,,0x3,],,,0b1010110,],;,_1_x_7f,:,Array,[,String,,,0B11000,],;,W,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0126,],,,0x62,],,,0B1,],,,04,],,,0XD,],),{,},},Class,_fK,{,},Class,D,:,_,{,},Class,T0,{,Val,H,:,Array,[,Boolean,,,0x7,],;,},<EOF>''',
                101
            )
        )

    def test_118(self):
        self.assertTrue(
            TestLexer.test(
                '''Class e0_z:O{Val $_,$8,$p,$G4:Float ;Destructor (){}H(_:_;e,j_,_z,f,_:Array [String ,64];mT,Q,t:Boolean ;_O,F,Pu,__V:Float ;__:Array [Float ,65]){} }Class K{}Class __:H{}Class ___y_F_Z{}''',
                '''Class,e0_z,:,O,{,Val,$_,,,$8,,,$p,,,$G4,:,Float,;,Destructor,(,),{,},H,(,_,:,_,;,e,,,j_,,,_z,,,f,,,_,:,Array,[,String,,,64,],;,mT,,,Q,,,t,:,Boolean,;,_O,,,F,,,Pu,,,__V,:,Float,;,__,:,Array,[,Float,,,65,],),{,},},Class,K,{,},Class,__,:,H,{,},Class,___y_F_Z,{,},<EOF>''',
                101
            )
        )

    def test_119(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o:P{Val r_,_Z:C_;Var __,_25:Array [Array [Array [Array [Array [Boolean ,05],0B11011],0B1],01],3];Constructor (){}Val __,$_8_6,$_,_,$0g,_,_:Boolean ;Destructor (){Break ;} }Class _8Ag_:h_{}''',
                '''Class,o,:,P,{,Val,r_,,,_Z,:,C_,;,Var,__,,,_25,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,05,],,,0B11011,],,,0B1,],,,01,],,,3,],;,Constructor,(,),{,},Val,__,,,$_8_6,,,$_,,,_,,,$0g,,,_,,,_,:,Boolean,;,Destructor,(,),{,Break,;,},},Class,_8Ag_,:,h_,{,},<EOF>''',
                101
            )
        )

    def test_120(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Ly:_{Val _:Array [Boolean ,0b10100];}Class ____SI4{Constructor (xYA:Array [String ,06_4];_,B5_,_:_Di;__,_125,_8M3:Int ){} }''',
                '''Class,Ly,:,_,{,Val,_,:,Array,[,Boolean,,,0b10100,],;,},Class,____SI4,{,Constructor,(,xYA,:,Array,[,String,,,064,],;,_,,,B5_,,,_,:,_Di,;,__,,,_125,,,_8M3,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_121(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J{Destructor (){}Constructor (){} }Class _8_:LA{}Class F_:_{Var _F0_:Array [Array [Int ,0xC],0b1010100];Destructor (){}e(T4:J__;J__:Array [Float ,0b1_01]){} }''',
                '''Class,J,{,Destructor,(,),{,},Constructor,(,),{,},},Class,_8_,:,LA,{,},Class,F_,:,_,{,Var,_F0_,:,Array,[,Array,[,Int,,,0xC,],,,0b1010100,],;,Destructor,(,),{,},e,(,T4,:,J__,;,J__,:,Array,[,Float,,,0b101,],),{,},},<EOF>''',
                101
            )
        )

    def test_122(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T:_2__{}Class _:_{}Class _2Hg_:W{Val _:Array [Array [Boolean ,0b1011],82_9];Val $d,$89_k:String ;Destructor (){}$br2(_:___m4_id;_T,L_,Hn,_,w:_;_:Array [Boolean ,02]){} }''',
                '''Class,T,:,_2__,{,},Class,_,:,_,{,},Class,_2Hg_,:,W,{,Val,_,:,Array,[,Array,[,Boolean,,,0b1011,],,,829,],;,Val,$d,,,$89_k,:,String,;,Destructor,(,),{,},$br2,(,_,:,___m4_id,;,_T,,,L_,,,Hn,,,_,,,w,:,_,;,_,:,Array,[,Boolean,,,02,],),{,},},<EOF>''',
                101
            )
        )

    def test_123(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Mw_M{Ys(b:Int ;_H:Float ){}Constructor (){} }Class __:_{}Class dr:J{Var O_Y0:Array [Array [Int ,0XF3_7],0b110100];}''',
                '''Class,Mw_M,{,Ys,(,b,:,Int,;,_H,:,Float,),{,},Constructor,(,),{,},},Class,__,:,_,{,},Class,dr,:,J,{,Var,O_Y0,:,Array,[,Array,[,Int,,,0XF37,],,,0b110100,],;,},<EOF>''',
                101
            )
        )

    def test_124(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class _{Val ui5_,$V_,$05Y,z,_,$20P,$pjr,$9bvy_,Mgd:Array [Float ,0X52];}Class V___{$0N(D_,I,f,_,__:Array [Array [String ,0X52],100]){Break ;}Var _,$C5:String ;}Class w:k{}Class __Q:_i{}''',
                '''Class,_,:,_,{,},Class,_,{,Val,ui5_,,,$V_,,,$05Y,,,z,,,_,,,$20P,,,$pjr,,,$9bvy_,,,Mgd,:,Array,[,Float,,,0X52,],;,},Class,V___,{,$0N,(,D_,,,I,,,f,,,_,,,__,:,Array,[,Array,[,String,,,0X52,],,,100,],),{,Break,;,},Var,_,,,$C5,:,String,;,},Class,w,:,k,{,},Class,__Q,:,_i,{,},<EOF>''',
                101
            )
        )

    def test_125(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val k:Array [Int ,80];Constructor (_:Array [Array [Float ,0b10_101_11],78]){} }Class Q:a{}Class L{}Class __:_{}Class a:a{}Class A5_67_N2{}''',
                '''Class,_,{,Val,k,:,Array,[,Int,,,80,],;,Constructor,(,_,:,Array,[,Array,[,Float,,,0b1010111,],,,78,],),{,},},Class,Q,:,a,{,},Class,L,{,},Class,__,:,_,{,},Class,a,:,a,{,},Class,A5_67_N2,{,},<EOF>''',
                101
            )
        )

    def test_126(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2__{g(Q:Array [Array [Array [Array [Array [Float ,95],0B1001100],0x18],0B1001100],03];DU,A_,Ps,_7,_,s,_,y:Array [Array [Int ,5],0b1];K,Z,_,L,_x:o){}Val __v,$_,$h:Array [Array [Array [Float ,0B1001100],0104],0x2];Destructor (){}W(J,Z73:String ;_,_:String ){} }Class Dd808{}Class _H7{Var $__,_b,C:_3;}Class ph:F{}''',
                '''Class,_2__,{,g,(,Q,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,95,],,,0B1001100,],,,0x18,],,,0B1001100,],,,03,],;,DU,,,A_,,,Ps,,,_7,,,_,,,s,,,_,,,y,:,Array,[,Array,[,Int,,,5,],,,0b1,],;,K,,,Z,,,_,,,L,,,_x,:,o,),{,},Val,__v,,,$_,,,$h,:,Array,[,Array,[,Array,[,Float,,,0B1001100,],,,0104,],,,0x2,],;,Destructor,(,),{,},W,(,J,,,Z73,:,String,;,_,,,_,:,String,),{,},},Class,Dd808,{,},Class,_H7,{,Var,$__,,,_b,,,C,:,_3,;,},Class,ph,:,F,{,},<EOF>''',
                101
            )
        )

    def test_127(self):
        self.assertTrue(
            TestLexer.test(
                '''Class LC_B:V73{Constructor (__:Array [Array [Array [Array [String ,0104],0104],04],0B1];_,_,_,W7,_:Array [Float ,0x3B]){}Constructor (_:t46__5_S;m,__,L,E,C,_:Array [Boolean ,0x632E7]){}$_(){} }''',
                '''Class,LC_B,:,V73,{,Constructor,(,__,:,Array,[,Array,[,Array,[,Array,[,String,,,0104,],,,0104,],,,04,],,,0B1,],;,_,,,_,,,_,,,W7,,,_,:,Array,[,Float,,,0x3B,],),{,},Constructor,(,_,:,t46__5_S,;,m,,,__,,,L,,,E,,,C,,,_,:,Array,[,Boolean,,,0x632E7,],),{,},$_,(,),{,},},<EOF>''',
                101
            )
        )

    def test_128(self):
        self.assertTrue(
            TestLexer.test(
                '''Class DT:_7{}Class P2Zx_4{Constructor (_,q,w7:Array [Array [Boolean ,6],0b1100];_:Array [Array [Array [String ,0x2],1],95_2_4_6_22];_:Z;Q6_,X:Array [Array [Array [String ,1],0B10],0X2F]){} }''',
                '''Class,DT,:,_7,{,},Class,P2Zx_4,{,Constructor,(,_,,,q,,,w7,:,Array,[,Array,[,Boolean,,,6,],,,0b1100,],;,_,:,Array,[,Array,[,Array,[,String,,,0x2,],,,1,],,,9524622,],;,_,:,Z,;,Q6_,,,X,:,Array,[,Array,[,Array,[,String,,,1,],,,0B10,],,,0X2F,],),{,},},<EOF>''',
                101
            )
        )

    def test_129(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _X{Var W3,$q,H:Array [Array [String ,040],0b1_1_0];k(R,F8,_3,tO,N:Boolean ;i__,p6TD:Array [Array [Int ,0X6_C],0B10_0]){} }''',
                '''Class,_X,{,Var,W3,,,$q,,,H,:,Array,[,Array,[,String,,,040,],,,0b110,],;,k,(,R,,,F8,,,_3,,,tO,,,N,:,Boolean,;,i__,,,p6TD,:,Array,[,Array,[,Int,,,0X6C,],,,0B100,],),{,},},<EOF>''',
                101
            )
        )

    def test_130(self):
        self.assertTrue(
            TestLexer.test(
                '''Class D:_f7{Constructor (__O0,_,s,z:__;x__:_;vTg__:Array [Array [Array [Array [String ,43],0xF2],056],056]){Continue ;} }''',
                '''Class,D,:,_f7,{,Constructor,(,__O0,,,_,,,s,,,z,:,__,;,x__,:,_,;,vTg__,:,Array,[,Array,[,Array,[,Array,[,String,,,43,],,,0xF2,],,,056,],,,056,],),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_131(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _1{}Class z_8{Constructor (){}Var _3,$__1s1r:Float ;PO00(_:Int ){} }Class _Ae6:y__{Constructor (){Break ;}Constructor (_,t4:Boolean ){} }''',
                '''Class,_,{,},Class,_1,{,},Class,z_8,{,Constructor,(,),{,},Var,_3,,,$__1s1r,:,Float,;,PO00,(,_,:,Int,),{,},},Class,_Ae6,:,y__,{,Constructor,(,),{,Break,;,},Constructor,(,_,,,t4,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_132(self):
        self.assertTrue(
            TestLexer.test(
                '''Class d{Constructor (_O:Array [Array [Array [Array [Array [Float ,37],1],0x5C],15],0b1];L,_,_,_:Boolean ;f0k2:Boolean ){} }Class Vx{}''',
                '''Class,d,{,Constructor,(,_O,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,37,],,,1,],,,0x5C,],,,15,],,,0b1,],;,L,,,_,,,_,,,_,:,Boolean,;,f0k2,:,Boolean,),{,},},Class,Vx,{,},<EOF>''',
                101
            )
        )

    def test_133(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E:_{}Class W_:s{}Class I_:C{}Class u1:A{Var __:Boolean ;Var $1,$5:d_;Var $13,$_57d,$_:Boolean ;Destructor (){} }Class m4{}''',
                '''Class,E,:,_,{,},Class,W_,:,s,{,},Class,I_,:,C,{,},Class,u1,:,A,{,Var,__,:,Boolean,;,Var,$1,,,$5,:,d_,;,Var,$13,,,$_57d,,,$_,:,Boolean,;,Destructor,(,),{,},},Class,m4,{,},<EOF>''',
                101
            )
        )

    def test_134(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _p4:i{}Class _:v{Constructor (e:Boolean ;c,e2,aX,Z,_,x1:__;__,_:Boolean ){}Val $a,$Q:Boolean ;}Class _:_92c0{}''',
                '''Class,_p4,:,i,{,},Class,_,:,v,{,Constructor,(,e,:,Boolean,;,c,,,e2,,,aX,,,Z,,,_,,,x1,:,__,;,__,,,_,:,Boolean,),{,},Val,$a,,,$Q,:,Boolean,;,},Class,_,:,_92c0,{,},<EOF>''',
                101
            )
        )

    def test_135(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P{Var _4,$B:Array [Int ,0xF];}Class S_:_2_{Var U0,$Y__,$5___,y,$Q_:Boolean ;}Class s7_3R{}Class M:N{}Class l3:_{}''',
                '''Class,P,{,Var,_4,,,$B,:,Array,[,Int,,,0xF,],;,},Class,S_,:,_2_,{,Var,U0,,,$Y__,,,$5___,,,y,,,$Q_,:,Boolean,;,},Class,s7_3R,{,},Class,M,:,N,{,},Class,l3,:,_,{,},<EOF>''',
                101
            )
        )

    def test_136(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A:_86p{Constructor (Nw:Array [Array [Array [Array [Array [String ,0XB],0X4C],0x5_8_7_9],043],070]){}Var $0:Int ;Val $_w:v;}''',
                '''Class,A,:,_86p,{,Constructor,(,Nw,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0XB,],,,0X4C,],,,0x5879,],,,043,],,,070,],),{,},Var,$0,:,Int,;,Val,$_w,:,v,;,},<EOF>''',
                101
            )
        )

    def test_137(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _h:_5486{}Class Me5_T3{Constructor (T__5:Int ;_20_,_:Array [Array [String ,0XA],0B111110];___:_7Ps;_,V__,_Wn0r,_,_:Array [Array [Float ,054],0XA];_3:_y;v:Float ;g:Boolean ){}Destructor (){} }''',
                '''Class,_h,:,_5486,{,},Class,Me5_T3,{,Constructor,(,T__5,:,Int,;,_20_,,,_,:,Array,[,Array,[,String,,,0XA,],,,0B111110,],;,___,:,_7Ps,;,_,,,V__,,,_Wn0r,,,_,,,_,:,Array,[,Array,[,Float,,,054,],,,0XA,],;,_3,:,_y,;,v,:,Float,;,g,:,Boolean,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_138(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _P{Destructor (){Return ;}Var u0_:Array [Array [Boolean ,8],026];}Class _:_{Destructor (){} }Class _:_{Constructor (){}Var x,c8:Array [Float ,026];}''',
                '''Class,_P,{,Destructor,(,),{,Return,;,},Var,u0_,:,Array,[,Array,[,Boolean,,,8,],,,026,],;,},Class,_,:,_,{,Destructor,(,),{,},},Class,_,:,_,{,Constructor,(,),{,},Var,x,,,c8,:,Array,[,Float,,,026,],;,},<EOF>''',
                101
            )
        )

    def test_139(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y:s__{Destructor (){}Destructor (){}Val $___0_f,_,K9n,_5,C:Array [Array [Boolean ,9],0xA2_D];Val I_r,$_8P:Int ;}''',
                '''Class,y,:,s__,{,Destructor,(,),{,},Destructor,(,),{,},Val,$___0_f,,,_,,,K9n,,,_5,,,C,:,Array,[,Array,[,Boolean,,,9,],,,0xA2D,],;,Val,I_r,,,$_8P,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_140(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _6:_{}Class _A9:_X_{}Class _y__{}Class _{Val $62,$_:Float ;Val _,G6,g,$Rv:Array [Array [Array [Array [Array [Float ,0X1],0b1_00_0_0_0_110],0X1],05],0B1100100];}''',
                '''Class,_,{,},Class,_6,:,_,{,},Class,_A9,:,_X_,{,},Class,_y__,{,},Class,_,{,Val,$62,,,$_,:,Float,;,Val,_,,,G6,,,g,,,$Rv,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X1,],,,0b100000110,],,,0X1,],,,05,],,,0B1100100,],;,},<EOF>''',
                101
            )
        )

    def test_141(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2:_{$g60_(_622:__;h:String ;lm,t,_:_f){Return ;Continue ;}Var $b:Array [Float ,0b1_1];}Class p:__{}Class w4C:u{}''',
                '''Class,_2,:,_,{,$g60_,(,_622,:,__,;,h,:,String,;,lm,,,t,,,_,:,_f,),{,Return,;,Continue,;,},Var,$b,:,Array,[,Float,,,0b11,],;,},Class,p,:,__,{,},Class,w4C,:,u,{,},<EOF>''',
                101
            )
        )

    def test_142(self):
        self.assertTrue(
            TestLexer.test(
                '''Class s:_{$1eYE(t,_,l:_e;_,o0:Array [Int ,4];_:Float ;_:Array [String ,0B1_1];u,jj:Array [Array [Array [Array [Int ,0B1],0b1],0b1],0b110101];_8:_){}$58pl(){}$_(){} }Class __74:_5807D{}Class u:____{}''',
                '''Class,s,:,_,{,$1eYE,(,t,,,_,,,l,:,_e,;,_,,,o0,:,Array,[,Int,,,4,],;,_,:,Float,;,_,:,Array,[,String,,,0B11,],;,u,,,jj,:,Array,[,Array,[,Array,[,Array,[,Int,,,0B1,],,,0b1,],,,0b1,],,,0b110101,],;,_8,:,_,),{,},$58pl,(,),{,},$_,(,),{,},},Class,__74,:,_5807D,{,},Class,u,:,____,{,},<EOF>''',
                101
            )
        )

    def test_143(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __36{}Class _{Constructor (n7,_,I,_,Tu_:Float ;Q:Array [Array [Int ,0x3],80]){}Var $_d:Array [String ,0x24];}''',
                '''Class,__36,{,},Class,_,{,Constructor,(,n7,,,_,,,I,,,_,,,Tu_,:,Float,;,Q,:,Array,[,Array,[,Int,,,0x3,],,,80,],),{,},Var,$_d,:,Array,[,String,,,0x24,],;,},<EOF>''',
                101
            )
        )

    def test_144(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ku{Var $46_,$__,__2eY:Array [Boolean ,0B111010];$yHS_Px(___,_:Float ;_F:_M__){ {} }}Class _K2:o{Constructor (){} }''',
                '''Class,ku,{,Var,$46_,,,$__,,,__2eY,:,Array,[,Boolean,,,0B111010,],;,$yHS_Px,(,___,,,_,:,Float,;,_F,:,_M__,),{,{,},},},Class,_K2,:,o,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_145(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _a:_1{}Class z{Var o,_:Array [String ,8750];Val $0:Int ;}Class m{}Class D_:U{Constructor (){}Constructor (){Break ;} }''',
                '''Class,_a,:,_1,{,},Class,z,{,Var,o,,,_,:,Array,[,String,,,8750,],;,Val,$0,:,Int,;,},Class,m,{,},Class,D_,:,U,{,Constructor,(,),{,},Constructor,(,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_146(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:B{Val k:Array [String ,96];}Class _:_{Val F:String ;}Class __h{_(j9,_fj:Float ){} }Class _:N{Destructor (){}Constructor (a,r,___,_69,_6_,_6:Boolean ){ {} }Val $1q7,$_2:Boolean ;}''',
                '''Class,_,:,B,{,Val,k,:,Array,[,String,,,96,],;,},Class,_,:,_,{,Val,F,:,String,;,},Class,__h,{,_,(,j9,,,_fj,:,Float,),{,},},Class,_,:,N,{,Destructor,(,),{,},Constructor,(,a,,,r,,,___,,,_69,,,_6_,,,_6,:,Boolean,),{,{,},},Val,$1q7,,,$_2,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_147(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _4:Rm{}Class _{}Class _O0:G{_(_kv:Int ){Return ;}Constructor (_7_,____8_6,_:s_1w2){___::$6();} }Class p8O4:_K{}''',
                '''Class,_4,:,Rm,{,},Class,_,{,},Class,_O0,:,G,{,_,(,_kv,:,Int,),{,Return,;,},Constructor,(,_7_,,,____8_6,,,_,:,s_1w2,),{,___,::,$6,(,),;,},},Class,p8O4,:,_K,{,},<EOF>''',
                101
            )
        )

    def test_148(self):
        self.assertTrue(
            TestLexer.test(
                '''Class M_l{_(a,_05,_:Array [Array [Array [Float ,6],680_1],9];D_2_:Array [Int ,0B110001];__D,a:Array [Array [Array [Int ,0B110001],8],04];j:Array [Array [Boolean ,0b1],0x47]){}Destructor (){} }''',
                '''Class,M_l,{,_,(,a,,,_05,,,_,:,Array,[,Array,[,Array,[,Float,,,6,],,,6801,],,,9,],;,D_2_,:,Array,[,Int,,,0B110001,],;,__D,,,a,:,Array,[,Array,[,Array,[,Int,,,0B110001,],,,8,],,,04,],;,j,:,Array,[,Array,[,Boolean,,,0b1,],,,0x47,],),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_149(self):
        self.assertTrue(
            TestLexer.test(
                '''Class i:_{Constructor (_:Array [Array [Int ,0b1],024];__:Array [Int ,0b1];_,___1:Int ;H87,O_n___,_1x__:h){Continue ;}Var $013,$9:Boolean ;}''',
                '''Class,i,:,_,{,Constructor,(,_,:,Array,[,Array,[,Int,,,0b1,],,,024,],;,__,:,Array,[,Int,,,0b1,],;,_,,,___1,:,Int,;,H87,,,O_n___,,,_1x__,:,h,),{,Continue,;,},Var,$013,,,$9,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_150(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var $4,$Q_O,J,y__R:Boolean ;$_(){Continue ;Array ()._0();}Var $6:Array [Int ,3_57_6_9_5_20];}Class r__1:_{}Class I1{}Class _3:_{}''',
                '''Class,_,{,Var,$4,,,$Q_O,,,J,,,y__R,:,Boolean,;,$_,(,),{,Continue,;,Array,(,),.,_0,(,),;,},Var,$6,:,Array,[,Int,,,35769520,],;,},Class,r__1,:,_,{,},Class,I1,{,},Class,_3,:,_,{,},<EOF>''',
                101
            )
        )

    def test_151(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _V{}Class _{Q06(_U3_:Array [Array [Array [Array [Int ,075_3],07],0b1],071];__,_G0__:___3a;p,x:_){}Destructor (){} }''',
                '''Class,_V,{,},Class,_,{,Q06,(,_U3_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0753,],,,07,],,,0b1,],,,071,],;,__,,,_G0__,:,___3a,;,p,,,x,:,_,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_152(self):
        self.assertTrue(
            TestLexer.test(
                '''Class K:_{Var _jc,P_,h_,Nt:Array [Array [Array [Array [Array [Boolean ,0B1001011],0141],06],07030_7],0x4];}Class B:__L{}Class h1_:a{}Class D_6{}''',
                '''Class,K,:,_,{,Var,_jc,,,P_,,,h_,,,Nt,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1001011,],,,0141,],,,06,],,,070307,],,,0x4,],;,},Class,B,:,__L,{,},Class,h1_,:,a,{,},Class,D_6,{,},<EOF>''',
                101
            )
        )

    def test_153(self):
        self.assertTrue(
            TestLexer.test(
                '''Class e{Constructor (){}Var _9u,$__gH__:Boolean ;Constructor (_,M_:Array [Float ,0B10];_:_){_0::$Gq6();}_Wa(_:B5){}Constructor (){} }''',
                '''Class,e,{,Constructor,(,),{,},Var,_9u,,,$__gH__,:,Boolean,;,Constructor,(,_,,,M_,:,Array,[,Float,,,0B10,],;,_,:,_,),{,_0,::,$Gq6,(,),;,},_Wa,(,_,:,B5,),{,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_154(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _H:K3AQnI{}Class Zo2k{Constructor (__:Array [Boolean ,8]){} }Class _:_{$___(I_,_,i:Array [Array [Float ,4],0X31]){} }''',
                '''Class,_H,:,K3AQnI,{,},Class,Zo2k,{,Constructor,(,__,:,Array,[,Boolean,,,8,],),{,},},Class,_,:,_,{,$___,(,I_,,,_,,,i,:,Array,[,Array,[,Float,,,4,],,,0X31,],),{,},},<EOF>''',
                101
            )
        )

    def test_155(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (__5,i85_,_1:Int ;_b7,_7,_66:Array [Float ,37];_2B_O,_,An:Array [Boolean ,5];_:_5V){ {{} }} }Class ZC___4:_t{Constructor (R__:Int ){}Destructor (){} }''',
                '''Class,_,{,Constructor,(,__5,,,i85_,,,_1,:,Int,;,_b7,,,_7,,,_66,:,Array,[,Float,,,37,],;,_2B_O,,,_,,,An,:,Array,[,Boolean,,,5,],;,_,:,_5V,),{,{,{,},},},},Class,ZC___4,:,_t,{,Constructor,(,R__,:,Int,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_156(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _d{}Class n:t{$_(r_MhY,_:Int ;f,__6,G:Array [Array [Array [Array [Boolean ,04],0B1],04],0x23]){} }Class ___8:_{Constructor (){} }''',
                '''Class,_d,{,},Class,n,:,t,{,$_,(,r_MhY,,,_,:,Int,;,f,,,__6,,,G,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,04,],,,0B1,],,,04,],,,0x23,],),{,},},Class,___8,:,_,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_157(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _31v_{}Class Q_4O{Var _,cE:Array [Array [Int ,2_74],03];}Class _:Z{}Class h_107__:p{Val ___:_gp;}Class h_{}''',
                '''Class,_31v_,{,},Class,Q_4O,{,Var,_,,,cE,:,Array,[,Array,[,Int,,,274,],,,03,],;,},Class,_,:,Z,{,},Class,h_107__,:,p,{,Val,___,:,_gp,;,},Class,h_,{,},<EOF>''',
                101
            )
        )

    def test_158(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Td8_{}Class G_BI3{Val kn_,__W:Boolean ;}Class q_:K{Destructor (){Return ;}Var $___:Boolean ;}Class e:kA{Var $_,$e,_:Int ;}''',
                '''Class,Td8_,{,},Class,G_BI3,{,Val,kn_,,,__W,:,Boolean,;,},Class,q_,:,K,{,Destructor,(,),{,Return,;,},Var,$___,:,Boolean,;,},Class,e,:,kA,{,Var,$_,,,$e,,,_,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_159(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Constructor (P0:Boolean ){Val T:Array [String ,0xC];} }Class _4k{Constructor (Z1_,_,m:Boolean ){} }Class _{}Class v0:_{}''',
                '''Class,_,:,_,{,Constructor,(,P0,:,Boolean,),{,Val,T,:,Array,[,String,,,0xC,],;,},},Class,_4k,{,Constructor,(,Z1_,,,_,,,m,:,Boolean,),{,},},Class,_,{,},Class,v0,:,_,{,},<EOF>''',
                101
            )
        )

    def test_160(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _U8:__{$_(X,_:Array [Array [Array [Array [Float ,021],02],0B11],0b1];_,f:_;f,av:Boolean ){} }Class __{$6hn(){} }''',
                '''Class,_U8,:,__,{,$_,(,X,,,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,021,],,,02,],,,0B11,],,,0b1,],;,_,,,f,:,_,;,f,,,av,:,Boolean,),{,},},Class,__,{,$6hn,(,),{,},},<EOF>''',
                101
            )
        )

    def test_161(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:F{Val x:Array [String ,0X8_7];Destructor (){}Var $K:Array [Array [Array [Array [Array [Int ,0B1],13],0130],0130],0x4E];}''',
                '''Class,_,:,F,{,Val,x,:,Array,[,String,,,0X87,],;,Destructor,(,),{,},Var,$K,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B1,],,,13,],,,0130,],,,0130,],,,0x4E,],;,},<EOF>''',
                101
            )
        )

    def test_162(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Ym{Val O:B;}Class e6dR:_{$h(__,u62U,Y9:_;_6_:Array [Boolean ,0B1_00_11]){Return ;} }Class d:_b_ak07{}Class _:P{}''',
                '''Class,Ym,{,Val,O,:,B,;,},Class,e6dR,:,_,{,$h,(,__,,,u62U,,,Y9,:,_,;,_6_,:,Array,[,Boolean,,,0B10011,],),{,Return,;,},},Class,d,:,_b_ak07,{,},Class,_,:,P,{,},<EOF>''',
                101
            )
        )

    def test_163(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:Z_{}Class _t{}Class __:t_9i__{Val $H,_,q8:Y06;}Class B:Q2s{Destructor (){}$1(){} }Class _8__N{}Class C{}''',
                '''Class,_,:,Z_,{,},Class,_t,{,},Class,__,:,t_9i__,{,Val,$H,,,_,,,q8,:,Y06,;,},Class,B,:,Q2s,{,Destructor,(,),{,},$1,(,),{,},},Class,_8__N,{,},Class,C,{,},<EOF>''',
                101
            )
        )

    def test_164(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _6{}Class _{GAY0_6(C,_:Boolean ;_,__ja_6_,P6,_Q,_,_:Array [Array [Array [Array [Int ,0x3_9],01],1],02];C,_8:_){} }''',
                '''Class,_6,{,},Class,_,{,GAY0_6,(,C,,,_,:,Boolean,;,_,,,__ja_6_,,,P6,,,_Q,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0x39,],,,01,],,,1,],,,02,],;,C,,,_8,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_165(self):
        self.assertTrue(
            TestLexer.test(
                '''Class pla_:X_{Destructor (){}Constructor (y:_4;_U:_;w34:Array [Array [Int ,0xF],071];t:Int ;_,_O,o,____:Array [Array [Array [Array [Array [Int ,0B101],4],03],04],28]){Continue ;} }''',
                '''Class,pla_,:,X_,{,Destructor,(,),{,},Constructor,(,y,:,_4,;,_U,:,_,;,w34,:,Array,[,Array,[,Int,,,0xF,],,,071,],;,t,:,Int,;,_,,,_O,,,o,,,____,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B101,],,,4,],,,03,],,,04,],,,28,],),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_166(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9{}Class H:y{Val $K6__wxW,$_:String ;Var $OdBg,W,$4,_,_1:Array [Array [Array [Array [Array [Array [Array [Int ,0b110101],0xC],44],0B10_1],0107],0B1],0107];Constructor (){} }''',
                '''Class,_9,{,},Class,H,:,y,{,Val,$K6__wxW,,,$_,:,String,;,Var,$OdBg,,,W,,,$4,,,_,,,_1,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0b110101,],,,0xC,],,,44,],,,0B101,],,,0107,],,,0B1,],,,0107,],;,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_167(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b{}Class P:_6_{}Class uw:Y_w{Val $c:S;}Class y1{Var S83_:Array [Array [Array [Boolean ,0X9],0B1],0X9_B_1];}''',
                '''Class,b,{,},Class,P,:,_6_,{,},Class,uw,:,Y_w,{,Val,$c,:,S,;,},Class,y1,{,Var,S83_,:,Array,[,Array,[,Array,[,Boolean,,,0X9,],,,0B1,],,,0X9B1,],;,},<EOF>''',
                101
            )
        )

    def test_168(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2:_6{Val _s:Array [Array [Array [Array [Float ,051],0X3],051],34];}Class p:_O_oV{Val A__C_:Array [Array [Array [Array [Boolean ,0x21],03_1],0x21],0b1];$4r(){} }''',
                '''Class,_2,:,_6,{,Val,_s,:,Array,[,Array,[,Array,[,Array,[,Float,,,051,],,,0X3,],,,051,],,,34,],;,},Class,p,:,_O_oV,{,Val,A__C_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x21,],,,031,],,,0x21,],,,0b1,],;,$4r,(,),{,},},<EOF>''',
                101
            )
        )

    def test_169(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Val $4__j_U3:Float ;Var t__,$E,_94:___i;Constructor (__5:Int ;_z:Float ){}Var _8y_3T78,____:Array [Array [Array [String ,0B111_1],0116],71];Constructor (){}Destructor (){} }''',
                '''Class,_,:,_,{,Val,$4__j_U3,:,Float,;,Var,t__,,,$E,,,_94,:,___i,;,Constructor,(,__5,:,Int,;,_z,:,Float,),{,},Var,_8y_3T78,,,____,:,Array,[,Array,[,Array,[,String,,,0B1111,],,,0116,],,,71,],;,Constructor,(,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_170(self):
        self.assertTrue(
            TestLexer.test(
                '''Class D_0{}Class _:D5G{Var I___,__:Array [Array [Array [Array [Array [Array [Array [Array [String ,0B1011110],82],034],0x10],6_3_1],066_1067_2],034],04_1];}Class __M5US{}Class Z{$D(){} }''',
                '''Class,D_0,{,},Class,_,:,D5G,{,Var,I___,,,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B1011110,],,,82,],,,034,],,,0x10,],,,631,],,,06610672,],,,034,],,,041,],;,},Class,__M5US,{,},Class,Z,{,$D,(,),{,},},<EOF>''',
                101
            )
        )

    def test_171(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _P:h{}Class _{}Class M:nW{Var __:Array [Array [Array [Array [Array [Float ,0X10],015],0xF],0X10],0xB_6_D07];}''',
                '''Class,_P,:,h,{,},Class,_,{,},Class,M,:,nW,{,Var,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X10,],,,015,],,,0xF,],,,0X10,],,,0xB6D07,],;,},<EOF>''',
                101
            )
        )

    def test_172(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0:_{}Class K_{Constructor (){Val _,__O:N;}Var $n:Array [Array [Float ,41],0B1];}Class N9:e{Val $0Y:Int ;}Class X{}Class _:Z_7B{}''',
                '''Class,_0,:,_,{,},Class,K_,{,Constructor,(,),{,Val,_,,,__O,:,N,;,},Var,$n,:,Array,[,Array,[,Float,,,41,],,,0B1,],;,},Class,N9,:,e,{,Val,$0Y,:,Int,;,},Class,X,{,},Class,_,:,Z_7B,{,},<EOF>''',
                101
            )
        )

    def test_173(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val f:Array [Array [Array [Float ,0xF],59_2],7_6]=!-_::$_.I_._88()._j().iv89.o8362._0()._G.s+!!!!!!!!!!!!__::$1()._w();}Class T{}''',
                '''Class,_,{,Val,f,:,Array,[,Array,[,Array,[,Float,,,0xF,],,,592,],,,76,],=,!,-,_,::,$_,.,I_,.,_88,(,),.,_j,(,),.,iv89,.,o8362,.,_0,(,),.,_G,.,s,+,!,!,!,!,!,!,!,!,!,!,!,!,__,::,$1,(,),.,_w,(,),;,},Class,T,{,},<EOF>''',
                101
            )
        )

    def test_174(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class o1P:X_z{Constructor (){}Var _,_:Boolean ;Val $L_J,$1,$C:Array [Int ,5];}Class u{Destructor (){} }''',
                '''Class,_,:,_,{,},Class,o1P,:,X_z,{,Constructor,(,),{,},Var,_,,,_,:,Boolean,;,Val,$L_J,,,$1,,,$C,:,Array,[,Int,,,5,],;,},Class,u,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_175(self):
        self.assertTrue(
            TestLexer.test(
                '''Class B8t5X_{Destructor (){}$Y98(_,__:_;_R,_FoZ1Z5_,qK_:Array [Array [Boolean ,0x40],05_5]){}Destructor (){} }''',
                '''Class,B8t5X_,{,Destructor,(,),{,},$Y98,(,_,,,__,:,_,;,_R,,,_FoZ1Z5_,,,qK_,:,Array,[,Array,[,Boolean,,,0x40,],,,055,],),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_176(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _Q:_{$617__5(u7:Array [Array [Array [Int ,0X77_4_5EE_2],01_6522],0x57];H,_i,___,x,kz3_0_,_:_0;Z_:l){Continue ;{} }}''',
                '''Class,_Q,:,_,{,$617__5,(,u7,:,Array,[,Array,[,Array,[,Int,,,0X7745EE2,],,,016522,],,,0x57,],;,H,,,_i,,,___,,,x,,,kz3_0_,,,_,:,_0,;,Z_,:,l,),{,Continue,;,{,},},},<EOF>''',
                101
            )
        )

    def test_177(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _G7_:e{}Class T:Xp{Constructor (_6M:Boolean ;B,_,_,F,_j0:Array [Array [Boolean ,3_36_3],0XC];Q,y,_,F_,o:O;_v,_l:l_4){ {} }}Class P{}Class vJ050{}''',
                '''Class,_G7_,:,e,{,},Class,T,:,Xp,{,Constructor,(,_6M,:,Boolean,;,B,,,_,,,_,,,F,,,_j0,:,Array,[,Array,[,Boolean,,,3363,],,,0XC,],;,Q,,,y,,,_,,,F_,,,o,:,O,;,_v,,,_l,:,l_4,),{,{,},},},Class,P,{,},Class,vJ050,{,},<EOF>''',
                101
            )
        )

    def test_178(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:n{Val _,$w:Array [String ,0B10];Constructor (___,e,_,_,l_,_e7,o:Array [Boolean ,44];_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,0X5F],0X46],970_0],0xA_9],0b11],0X46],3_39_2],076],44],04_2],0x7E_30_D],44]){}Destructor (){}Destructor (){} }''',
                '''Class,_,:,n,{,Val,_,,,$w,:,Array,[,String,,,0B10,],;,Constructor,(,___,,,e,,,_,,,_,,,l_,,,_e7,,,o,:,Array,[,Boolean,,,44,],;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X5F,],,,0X46,],,,9700,],,,0xA9,],,,0b11,],,,0X46,],,,3392,],,,076,],,,44,],,,042,],,,0x7E30D,],,,44,],),{,},Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_179(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _1__Y:N{Destructor (){}Destructor (){} }Class Y{Var $WT,$v__M,$434:_;Var f:Int ;Val z:Array [Array [Float ,156],39];}Class _:_{Destructor (){} }''',
                '''Class,_1__Y,:,N,{,Destructor,(,),{,},Destructor,(,),{,},},Class,Y,{,Var,$WT,,,$v__M,,,$434,:,_,;,Var,f,:,Int,;,Val,z,:,Array,[,Array,[,Float,,,156,],,,39,],;,},Class,_,:,_,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_180(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A:m{Var $43:Array [Array [Array [Array [Array [Array [Array [Boolean ,05],0x45],05_3],3_9_7],0b10],0B1],0B1001111];$6(A__,XJ:__){Var _2F,w:Float ;} }Class b:_{}Class _18:_i_{}Class w{}''',
                '''Class,A,:,m,{,Var,$43,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,05,],,,0x45,],,,053,],,,397,],,,0b10,],,,0B1,],,,0B1001111,],;,$6,(,A__,,,XJ,:,__,),{,Var,_2F,,,w,:,Float,;,},},Class,b,:,_,{,},Class,_18,:,_i_,{,},Class,w,{,},<EOF>''',
                101
            )
        )

    def test_181(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k:k{}Class __8_{Destructor (){_::$_5_.S.c();}Val H9:Int ;Destructor (){}Destructor (){} }Class sh{}Class Rx__6:__{$r(_2:Array [Int ,6_2]){} }Class D{}''',
                '''Class,k,:,k,{,},Class,__8_,{,Destructor,(,),{,_,::,$_5_,.,S,.,c,(,),;,},Val,H9,:,Int,;,Destructor,(,),{,},Destructor,(,),{,},},Class,sh,{,},Class,Rx__6,:,__,{,$r,(,_2,:,Array,[,Int,,,62,],),{,},},Class,D,{,},<EOF>''',
                101
            )
        )

    def test_182(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __y:g{$c19(_57_8,_,_,_,_0:Array [String ,0X3_3];x:Boolean ;f_V,C,__4:_y;_,__,__:Int ){}Val $4:Boolean ;}''',
                '''Class,__y,:,g,{,$c19,(,_57_8,,,_,,,_,,,_,,,_0,:,Array,[,String,,,0X33,],;,x,:,Boolean,;,f_V,,,C,,,__4,:,_y,;,_,,,__,,,__,:,Int,),{,},Val,$4,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_183(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:C_{_E(){} }Class _{z_(_Q,n_,y,_S63,_,_,_,c,rA4,V,_4:Array [Array [Array [String ,0B101011],0b1],0B1];x1:Float ;v_:h){}Var O:N;}Class _:c{Var $_,_X9q:_F;}''',
                '''Class,_,:,C_,{,_E,(,),{,},},Class,_,{,z_,(,_Q,,,n_,,,y,,,_S63,,,_,,,_,,,_,,,c,,,rA4,,,V,,,_4,:,Array,[,Array,[,Array,[,String,,,0B101011,],,,0b1,],,,0B1,],;,x1,:,Float,;,v_,:,h,),{,},Var,O,:,N,;,},Class,_,:,c,{,Var,$_,,,_X9q,:,_F,;,},<EOF>''',
                101
            )
        )

    def test_184(self):
        self.assertTrue(
            TestLexer.test(
                '''Class L:U{Var $S:Array [Array [Array [Array [Array [Array [Int ,0733],0x3],05],0x56],6],73_55];Constructor (){Return ;} }''',
                '''Class,L,:,U,{,Var,$S,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0733,],,,0x3,],,,05,],,,0x56,],,,6,],,,7355,],;,Constructor,(,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_185(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _G{}Class ____:a20{Val __:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,011],2],85],2],016],85],85],011],0x1A],85];}''',
                '''Class,_G,{,},Class,____,:,a20,{,Val,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,011,],,,2,],,,85,],,,2,],,,016,],,,85,],,,85,],,,011,],,,0x1A,],,,85,],;,},<EOF>''',
                101
            )
        )

    def test_186(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{Var $1,$_:Array [Array [Array [Boolean ,0x25],96],0b11000];}Class _h___:_{Val __G7_X,$v_,$5:Int ;}Class I2:Z_C{}''',
                '''Class,__,{,Var,$1,,,$_,:,Array,[,Array,[,Array,[,Boolean,,,0x25,],,,96,],,,0b11000,],;,},Class,_h___,:,_,{,Val,__G7_X,,,$v_,,,$5,:,Int,;,},Class,I2,:,Z_C,{,},<EOF>''',
                101
            )
        )

    def test_187(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:_{Constructor (_:Float ;Ui2_,u:Array [Array [Array [Array [Boolean ,057],0b1],0b1000],0B111110];j0,j,B,r_1,_,__:H_){} }''',
                '''Class,__,:,_,{,Constructor,(,_,:,Float,;,Ui2_,,,u,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,057,],,,0b1,],,,0b1000,],,,0B111110,],;,j0,,,j,,,B,,,r_1,,,_,,,__,:,H_,),{,},},<EOF>''',
                101
            )
        )

    def test_188(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o_1Yh__1{}Class f{Val eR4_O_,$V:Array [Array [String ,0b11101],0B110110];}Class Y{$V_4_(K:Array [Array [Array [Array [Int ,0X1C],0xC_7F6_7],0X1C],1]){}Val __:I_;}''',
                '''Class,o_1Yh__1,{,},Class,f,{,Val,eR4_O_,,,$V,:,Array,[,Array,[,String,,,0b11101,],,,0B110110,],;,},Class,Y,{,$V_4_,(,K,:,Array,[,Array,[,Array,[,Array,[,Int,,,0X1C,],,,0xC7F67,],,,0X1C,],,,1,],),{,},Val,__,:,I_,;,},<EOF>''',
                101
            )
        )

    def test_189(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Val _0,__R:Array [Array [Array [Array [Boolean ,073],0b1000001],073],0X5C_0_2A];Destructor (){}$G(_y:Array [Array [Array [Int ,0xB_E_B_D14E_A_2],0x17_4],01];___41_,_,_,V:__b1_5;_D,Y4,__:Array [Boolean ,0B1]){}i(){} }''',
                '''Class,_,:,_,{,Val,_0,,,__R,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,073,],,,0b1000001,],,,073,],,,0X5C02A,],;,Destructor,(,),{,},$G,(,_y,:,Array,[,Array,[,Array,[,Int,,,0xBEBD14EA2,],,,0x174,],,,01,],;,___41_,,,_,,,_,,,V,:,__b1_5,;,_D,,,Y4,,,__,:,Array,[,Boolean,,,0B1,],),{,},i,(,),{,},},<EOF>''',
                101
            )
        )

    def test_190(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __B{}Class r_{Destructor (){}Var $6Kb4,$L_8,$_:String ;Var S,$_f00_t,_,$N_,f:Array [Float ,03];}Class __7{Val _4z,$g_,y_,$_,$M,$_:_;}''',
                '''Class,__B,{,},Class,r_,{,Destructor,(,),{,},Var,$6Kb4,,,$L_8,,,$_,:,String,;,Var,S,,,$_f00_t,,,_,,,$N_,,,f,:,Array,[,Float,,,03,],;,},Class,__7,{,Val,_4z,,,$g_,,,y_,,,$_,,,$M,,,$_,:,_,;,},<EOF>''',
                101
            )
        )

    def test_191(self):
        self.assertTrue(
            TestLexer.test(
                '''Class U7572:E{}Class H{_(A_,n1,T_,_7P,YSY_B,_t:Array [Array [Array [Array [String ,0b1100001],0B10_1],0b1100001],05_6_1]){}$2_y(_0:g;_9:Array [Int ,012];xW:H_R9_){Break ;}Constructor (_598,__:Int ;_,e,I8,p:l;_,Q_:Array [Int ,051];D2,_v,_2:Float ){}x_(V:Boolean ;A_,TL:P;__4JX9,h_,A_,O,_xbS:M;_jwM:Int ){Return ;} }''',
                '''Class,U7572,:,E,{,},Class,H,{,_,(,A_,,,n1,,,T_,,,_7P,,,YSY_B,,,_t,:,Array,[,Array,[,Array,[,Array,[,String,,,0b1100001,],,,0B101,],,,0b1100001,],,,0561,],),{,},$2_y,(,_0,:,g,;,_9,:,Array,[,Int,,,012,],;,xW,:,H_R9_,),{,Break,;,},Constructor,(,_598,,,__,:,Int,;,_,,,e,,,I8,,,p,:,l,;,_,,,Q_,:,Array,[,Int,,,051,],;,D2,,,_v,,,_2,:,Float,),{,},x_,(,V,:,Boolean,;,A_,,,TL,:,P,;,__4JX9,,,h_,,,A_,,,O,,,_xbS,:,M,;,_jwM,:,Int,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_192(self):
        self.assertTrue(
            TestLexer.test(
                '''Class s:U_{Var _,$_,$__:Boolean ;}Class M{Constructor (____0_,_s,D,i:Array [Array [Array [Array [String ,0X54],59_7],061],9];_P,L,_0,__I_:Int ){Val _,_,_:Boolean ;Continue ;Return ;Continue ;} }Class __M__:_{}Class w_{}''',
                '''Class,s,:,U_,{,Var,_,,,$_,,,$__,:,Boolean,;,},Class,M,{,Constructor,(,____0_,,,_s,,,D,,,i,:,Array,[,Array,[,Array,[,Array,[,String,,,0X54,],,,597,],,,061,],,,9,],;,_P,,,L,,,_0,,,__I_,:,Int,),{,Val,_,,,_,,,_,:,Boolean,;,Continue,;,Return,;,Continue,;,},},Class,__M__,:,_,{,},Class,w_,{,},<EOF>''',
                101
            )
        )

    def test_193(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_7{}Class q{}Class z:_{}Class i:_jy1{}Class _:_9{}Class __49{Constructor (){}Destructor (){} }Class _{}''',
                '''Class,_,:,_7,{,},Class,q,{,},Class,z,:,_,{,},Class,i,:,_jy1,{,},Class,_,:,_9,{,},Class,__49,{,Constructor,(,),{,},Destructor,(,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_194(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class _:__{I(__:_;o_lu:Array [Boolean ,0x39F4]){New _().b.__.J().cl().i();}Destructor (){} }Class __{Val _:_3;$b0_(p,h,_9:Boolean ;O,G_yO5g4:Boolean ){}Constructor (){Continue ;} }''',
                '''Class,_,:,_,{,},Class,_,:,__,{,I,(,__,:,_,;,o_lu,:,Array,[,Boolean,,,0x39F4,],),{,New,_,(,),.,b,.,__,.,J,(,),.,cl,(,),.,i,(,),;,},Destructor,(,),{,},},Class,__,{,Val,_,:,_3,;,$b0_,(,p,,,h,,,_9,:,Boolean,;,O,,,G_yO5g4,:,Boolean,),{,},Constructor,(,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_195(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y:__z9{Constructor (Y_8n_:Array [Array [Int ,0X5_CCA],066]){}Val G:String ;Var $H,cYt439_:W1;Val $0:Array [String ,0b10110];Var $5,_:V_;Destructor (){ {} }}Class L{}''',
                '''Class,y,:,__z9,{,Constructor,(,Y_8n_,:,Array,[,Array,[,Int,,,0X5CCA,],,,066,],),{,},Val,G,:,String,;,Var,$H,,,cYt439_,:,W1,;,Val,$0,:,Array,[,String,,,0b10110,],;,Var,$5,,,_,:,V_,;,Destructor,(,),{,{,},},},Class,L,{,},<EOF>''',
                101
            )
        )

    def test_196(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _6_:D{}Class t6{Val $4:Array [Boolean ,0x7_C];Var H1f8L1R,l,p:c_y;$__q_(_u:Array [String ,63]){Break ;_::$Pw();} }Class _e0_{}''',
                '''Class,_6_,:,D,{,},Class,t6,{,Val,$4,:,Array,[,Boolean,,,0x7C,],;,Var,H1f8L1R,,,l,,,p,:,c_y,;,$__q_,(,_u,:,Array,[,String,,,63,],),{,Break,;,_,::,$Pw,(,),;,},},Class,_e0_,{,},<EOF>''',
                101
            )
        )

    def test_197(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _4{}Class _:r{Val x,w_24,$0_,_3,_L,$J,NZ4,_,$5_,_68:Array [Array [Array [String ,0X33],0373],7_4_6_2];}Class _{}Class S{}Class _:_{}''',
                '''Class,_4,{,},Class,_,:,r,{,Val,x,,,w_24,,,$0_,,,_3,,,_L,,,$J,,,NZ4,,,_,,,$5_,,,_68,:,Array,[,Array,[,Array,[,String,,,0X33,],,,0373,],,,7462,],;,},Class,_,{,},Class,S,{,},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_198(self):
        self.assertTrue(
            TestLexer.test(
                '''Class KI{Val _4,$_:Array [Array [Array [Array [Array [Array [String ,2_0_7_0],03],0B111110],03],76],89_3];Constructor (){} }Class B_4:_5{}Class g{}''',
                '''Class,KI,{,Val,_4,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,2070,],,,03,],,,0B111110,],,,03,],,,76,],,,893,],;,Constructor,(,),{,},},Class,B_4,:,_5,{,},Class,g,{,},<EOF>''',
                101
            )
        )

    def test_199(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _1_1_6:_{Val $_:_;$f(_:Array [Array [Float ,0b110001],06_7];_O_,Y_6:Array [Array [Array [Float ,07_6_0_2_04],0B11111],0xBD]){Return ;} }Class wJ{Destructor (){}Q_3(E_:Array [Array [Boolean ,0B1_0_0],0b101];_v:Int ){} }''',
                '''Class,_1_1_6,:,_,{,Val,$_,:,_,;,$f,(,_,:,Array,[,Array,[,Float,,,0b110001,],,,067,],;,_O_,,,Y_6,:,Array,[,Array,[,Array,[,Float,,,0760204,],,,0B11111,],,,0xBD,],),{,Return,;,},},Class,wJ,{,Destructor,(,),{,},Q_3,(,E_,:,Array,[,Array,[,Boolean,,,0B100,],,,0b101,],;,_v,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_200(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __4{}Class _{Val HG:Array [Array [Array [Int ,0XE8],0b100100],0x5F];}Class _{Val h:Int ;Destructor (){Return ;} }Class _:mJ_2{}''',
                '''Class,__4,{,},Class,_,{,Val,HG,:,Array,[,Array,[,Array,[,Int,,,0XE8,],,,0b100100,],,,0x5F,],;,},Class,_,{,Val,h,:,Int,;,Destructor,(,),{,Return,;,},},Class,_,:,mJ_2,{,},<EOF>''',
                101
            )
        )

    def test_201(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o{$_(_7,H,_,G_1:Boolean ;z:Float ;_,_5_:Array [Array [Array [Array [Array [String ,56],987],0b1],05_6],0X6F_A]){} }''',
                '''Class,o,{,$_,(,_7,,,H,,,_,,,G_1,:,Boolean,;,z,:,Float,;,_,,,_5_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,56,],,,987,],,,0b1,],,,056,],,,0X6FA,],),{,},},<EOF>''',
                101
            )
        )

    def test_202(self):
        self.assertTrue(
            TestLexer.test(
                '''Class B{Var _:Array [Array [Array [Array [Array [Int ,060],0x55],5_9_5],060],6];Constructor (){}Destructor (){} }Class _i{}''',
                '''Class,B,{,Var,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,060,],,,0x55,],,,595,],,,060,],,,6,],;,Constructor,(,),{,},Destructor,(,),{,},},Class,_i,{,},<EOF>''',
                101
            )
        )

    def test_203(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:X{Constructor (i2,N__7:Array [Array [Boolean ,01],0X7_D_9F_D];V:Int ;__:Array [Array [Int ,93],0b101110]){} }Class x:_{}Class a9{Constructor (){} }Class U{Destructor (){}_4(B_LI:Array [Int ,66]){} }Class R_P{}''',
                '''Class,_,:,X,{,Constructor,(,i2,,,N__7,:,Array,[,Array,[,Boolean,,,01,],,,0X7D9FD,],;,V,:,Int,;,__,:,Array,[,Array,[,Int,,,93,],,,0b101110,],),{,},},Class,x,:,_,{,},Class,a9,{,Constructor,(,),{,},},Class,U,{,Destructor,(,),{,},_4,(,B_LI,:,Array,[,Int,,,66,],),{,},},Class,R_P,{,},<EOF>''',
                101
            )
        )

    def test_204(self):
        self.assertTrue(
            TestLexer.test(
                '''Class v6_{Constructor (){} }Class T{Constructor (){} }Class l5J:WI{Var $v,$t9:__i_;Constructor (){}Var _1____,$19:_;}Class wm{}''',
                '''Class,v6_,{,Constructor,(,),{,},},Class,T,{,Constructor,(,),{,},},Class,l5J,:,WI,{,Var,$v,,,$t9,:,__i_,;,Constructor,(,),{,},Var,_1____,,,$19,:,_,;,},Class,wm,{,},<EOF>''',
                101
            )
        )

    def test_205(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Rc___2W_{}Class e6_{$j(_,U0,X_n,_6_7:v0;_:Array [Boolean ,0112];_,S_82_G5:Array [Array [Float ,05_4776_0],0X10]){} }''',
                '''Class,Rc___2W_,{,},Class,e6_,{,$j,(,_,,,U0,,,X_n,,,_6_7,:,v0,;,_,:,Array,[,Boolean,,,0112,],;,_,,,S_82_G5,:,Array,[,Array,[,Float,,,0547760,],,,0X10,],),{,},},<EOF>''',
                101
            )
        )

    def test_206(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _b:_{Destructor (){ {{ {Val p:Array [String ,030];} }} }_P(p,__3,_0:Array [Float ,0B1]){} }Class _A{Val $_:f;Var u7i,_26,t,_,_l:Array [Array [Float ,010_667],0b111010];}Class _8:_{}''',
                '''Class,_b,:,_,{,Destructor,(,),{,{,{,{,Val,p,:,Array,[,String,,,030,],;,},},},},_P,(,p,,,__3,,,_0,:,Array,[,Float,,,0B1,],),{,},},Class,_A,{,Val,$_,:,f,;,Var,u7i,,,_26,,,t,,,_,,,_l,:,Array,[,Array,[,Float,,,010667,],,,0b111010,],;,},Class,_8,:,_,{,},<EOF>''',
                101
            )
        )

    def test_207(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Gj{Val Zu_0:Boolean ;Var X:Array [Array [Array [Array [Array [Array [String ,05],0X60],0b1100010],0B10010],0b1100010],6_26];}''',
                '''Class,Gj,{,Val,Zu_0,:,Boolean,;,Var,X,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,05,],,,0X60,],,,0b1100010,],,,0B10010,],,,0b1100010,],,,626,],;,},<EOF>''',
                101
            )
        )

    def test_208(self):
        self.assertTrue(
            TestLexer.test(
                '''Class L1{}Class z:_{}Class _{Val $y,_f8:Array [Array [Array [Array [Array [Array [Array [Boolean ,0b1010],0144],0X44],0B101],0b1010],0x32],0x32];}Class X:b_m____{Val $F:Float ;Var y,_:L;Var $55:Boolean ;}Class B{}Class g:A6{}''',
                '''Class,L1,{,},Class,z,:,_,{,},Class,_,{,Val,$y,,,_f8,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1010,],,,0144,],,,0X44,],,,0B101,],,,0b1010,],,,0x32,],,,0x32,],;,},Class,X,:,b_m____,{,Val,$F,:,Float,;,Var,y,,,_,:,L,;,Var,$55,:,Boolean,;,},Class,B,{,},Class,g,:,A6,{,},<EOF>''',
                101
            )
        )

    def test_209(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l_{Constructor (_,_:Array [Array [String ,0B11],0B1001110];R,K78:yh_2__){}$6_T(){Break ;}Val __,$1:Array [Array [Array [Array [Float ,0xA],03],0X9],296];}''',
                '''Class,l_,{,Constructor,(,_,,,_,:,Array,[,Array,[,String,,,0B11,],,,0B1001110,],;,R,,,K78,:,yh_2__,),{,},$6_T,(,),{,Break,;,},Val,__,,,$1,:,Array,[,Array,[,Array,[,Array,[,Float,,,0xA,],,,03,],,,0X9,],,,296,],;,},<EOF>''',
                101
            )
        )

    def test_210(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l{Constructor (){Break ;}$b(M,_,gZ_:Array [String ,8_2_48_7384_51]){}Constructor (K__,_3:_Q){} }Class _{}Class _{Var $_1O:Boolean ;}''',
                '''Class,l,{,Constructor,(,),{,Break,;,},$b,(,M,,,_,,,gZ_,:,Array,[,String,,,8248738451,],),{,},Constructor,(,K__,,,_3,:,_Q,),{,},},Class,_,{,},Class,_,{,Var,$_1O,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_211(self):
        self.assertTrue(
            TestLexer.test(
                '''Class D:_{Constructor (){} }Class _{Val t1,$5,$l14_:Array [Boolean ,0b1111];Destructor (){}Var _:Array [String ,0B1_1];Val p:Y;}''',
                '''Class,D,:,_,{,Constructor,(,),{,},},Class,_,{,Val,t1,,,$5,,,$l14_,:,Array,[,Boolean,,,0b1111,],;,Destructor,(,),{,},Var,_,:,Array,[,String,,,0B11,],;,Val,p,:,Y,;,},<EOF>''',
                101
            )
        )

    def test_212(self):
        self.assertTrue(
            TestLexer.test(
                '''Class N5__1_:__4_{}Class w:_{}Class _{Constructor (){}Val $o,R,$G:Array [Array [Array [Array [Float ,0B1],9],0107],0B1];}Class _:tZ{}Class B{}Class K{Val $bc:Int ;}Class __C:_s{}''',
                '''Class,N5__1_,:,__4_,{,},Class,w,:,_,{,},Class,_,{,Constructor,(,),{,},Val,$o,,,R,,,$G,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B1,],,,9,],,,0107,],,,0B1,],;,},Class,_,:,tZ,{,},Class,B,{,},Class,K,{,Val,$bc,:,Int,;,},Class,__C,:,_s,{,},<EOF>''',
                101
            )
        )

    def test_213(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9G05{Constructor (Wd_g,_9,Qyi7_,Q__66_,Z:Array [Int ,053];__:String ;_:Array [String ,0X18];v__3:Boolean ;_:Int ;P4,_,k7,vt_,j,l9,g_Q,jh2:_;_,_,g__:m){} }Class A{}''',
                '''Class,_9G05,{,Constructor,(,Wd_g,,,_9,,,Qyi7_,,,Q__66_,,,Z,:,Array,[,Int,,,053,],;,__,:,String,;,_,:,Array,[,String,,,0X18,],;,v__3,:,Boolean,;,_,:,Int,;,P4,,,_,,,k7,,,vt_,,,j,,,l9,,,g_Q,,,jh2,:,_,;,_,,,_,,,g__,:,m,),{,},},Class,A,{,},<EOF>''',
                101
            )
        )

    def test_214(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8:x{}Class Lw_9__:V_{Destructor (){} }Class z_:c{Constructor (_H:Array [Array [Array [Array [Array [Float ,0122],0122],0b101],0B1],40];_8:Int ;R,B,Z,_:String ;y1:__){} }Class L:Ki{}''',
                '''Class,_8,:,x,{,},Class,Lw_9__,:,V_,{,Destructor,(,),{,},},Class,z_,:,c,{,Constructor,(,_H,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0122,],,,0122,],,,0b101,],,,0B1,],,,40,],;,_8,:,Int,;,R,,,B,,,Z,,,_,:,String,;,y1,:,__,),{,},},Class,L,:,Ki,{,},<EOF>''',
                101
            )
        )

    def test_215(self):
        self.assertTrue(
            TestLexer.test(
                '''Class K4____2{Constructor (_Z,s6:String ;t:Int ;_IO53_8:Int ){ {}__Y7b__::$ww();}Destructor (){Var x1Jrwj,t:Array [Boolean ,0b1_1_01];}Constructor (){Return ;} }''',
                '''Class,K4____2,{,Constructor,(,_Z,,,s6,:,String,;,t,:,Int,;,_IO53_8,:,Int,),{,{,},__Y7b__,::,$ww,(,),;,},Destructor,(,),{,Var,x1Jrwj,,,t,:,Array,[,Boolean,,,0b1101,],;,},Constructor,(,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_216(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q0o:_G{}Class _3:___{Constructor (vs_,_,__:__T18;s,Ay,xA,zn,_,D:V;H94,D0O_:Array [Array [Int ,56],0x12];D:Array [Array [Float ,3_8],0x12]){Break ;}Var _e:_;}''',
                '''Class,q0o,:,_G,{,},Class,_3,:,___,{,Constructor,(,vs_,,,_,,,__,:,__T18,;,s,,,Ay,,,xA,,,zn,,,_,,,D,:,V,;,H94,,,D0O_,:,Array,[,Array,[,Int,,,56,],,,0x12,],;,D,:,Array,[,Array,[,Float,,,38,],,,0x12,],),{,Break,;,},Var,_e,:,_,;,},<EOF>''',
                101
            )
        )

    def test_217(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E:_{}Class e_A:__{$C_3(H,lW3,_,c:Array [Array [String ,51],0x2];_L0:R_;_2:N51_pM;_,_H:Array [Boolean ,03_2_5];__23,m_,_FU:Int ;mR,_A:Boolean ;_:String ;_,_714:s){} }Class J:_{}''',
                '''Class,E,:,_,{,},Class,e_A,:,__,{,$C_3,(,H,,,lW3,,,_,,,c,:,Array,[,Array,[,String,,,51,],,,0x2,],;,_L0,:,R_,;,_2,:,N51_pM,;,_,,,_H,:,Array,[,Boolean,,,0325,],;,__23,,,m_,,,_FU,:,Int,;,mR,,,_A,:,Boolean,;,_,:,String,;,_,,,_714,:,s,),{,},},Class,J,:,_,{,},<EOF>''',
                101
            )
        )

    def test_218(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (s,_1_,_,k:Int ;L4:Array [Array [Array [Array [Array [Array [Array [Array [String ,0B1],0b11],6_62],0B111110],0B10],92],92],0X5_1_5B_5];_,Y__:Array [Array [Array [Boolean ,0B1],0b111110],7_6]){} }''',
                '''Class,_,{,Constructor,(,s,,,_1_,,,_,,,k,:,Int,;,L4,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B1,],,,0b11,],,,662,],,,0B111110,],,,0B10,],,,92,],,,92,],,,0X515B5,],;,_,,,Y__,:,Array,[,Array,[,Array,[,Boolean,,,0B1,],,,0b111110,],,,76,],),{,},},<EOF>''',
                101
            )
        )

    def test_219(self):
        self.assertTrue(
            TestLexer.test(
                '''Class zcJ_{Var _,$jr:String ;}Class o{Constructor (O,__4,J:Array [Float ,0B110101]){N::$_();Break ;} }Class _:_{Val $69_,_:_7_U_9;}Class __h{}''',
                '''Class,zcJ_,{,Var,_,,,$jr,:,String,;,},Class,o,{,Constructor,(,O,,,__4,,,J,:,Array,[,Float,,,0B110101,],),{,N,::,$_,(,),;,Break,;,},},Class,_,:,_,{,Val,$69_,,,_,:,_7_U_9,;,},Class,__h,{,},<EOF>''',
                101
            )
        )

    def test_220(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0_AT:g_{}Class _64{}Class Z___:__{Var $9_:__;Val _:Array [Array [Array [Array [Array [Float ,2],0x6],0B1_1_1_1],06],38];}''',
                '''Class,_0_AT,:,g_,{,},Class,_64,{,},Class,Z___,:,__,{,Var,$9_,:,__,;,Val,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,2,],,,0x6,],,,0B1111,],,,06,],,,38,],;,},<EOF>''',
                101
            )
        )

    def test_221(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{Var $0_:Array [Array [Array [Boolean ,0b1],0XF_5C26],023];Destructor (){_::$5();}Constructor (){}Val __:Array [Boolean ,0X26];Val $l,_:__;Destructor (){Continue ;}Var $V,_49:Float ;Constructor (){} }''',
                '''Class,__,{,Var,$0_,:,Array,[,Array,[,Array,[,Boolean,,,0b1,],,,0XF5C26,],,,023,],;,Destructor,(,),{,_,::,$5,(,),;,},Constructor,(,),{,},Val,__,:,Array,[,Boolean,,,0X26,],;,Val,$l,,,_,:,__,;,Destructor,(,),{,Continue,;,},Var,$V,,,_49,:,Float,;,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_222(self):
        self.assertTrue(
            TestLexer.test(
                '''Class s_0{Constructor (_:Boolean ;_,S:Array [Array [Int ,0XD],0b1000011]){}Val $sS:X;}Class _:__{}Class __:G{Destructor (){}$_i2T(){}Destructor (){} }Class B{}''',
                '''Class,s_0,{,Constructor,(,_,:,Boolean,;,_,,,S,:,Array,[,Array,[,Int,,,0XD,],,,0b1000011,],),{,},Val,$sS,:,X,;,},Class,_,:,__,{,},Class,__,:,G,{,Destructor,(,),{,},$_i2T,(,),{,},Destructor,(,),{,},},Class,B,{,},<EOF>''',
                101
            )
        )

    def test_223(self):
        self.assertTrue(
            TestLexer.test(
                '''Class M4:u{Destructor (){}Destructor (){}Val $b,_:s;}Class U{}Class d{}Class _:j04Tx_{}Class _{Val $5:__h;}Class Vv{}Class __{Constructor (){Continue ;} }''',
                '''Class,M4,:,u,{,Destructor,(,),{,},Destructor,(,),{,},Val,$b,,,_,:,s,;,},Class,U,{,},Class,d,{,},Class,_,:,j04Tx_,{,},Class,_,{,Val,$5,:,__h,;,},Class,Vv,{,},Class,__,{,Constructor,(,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_224(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P{Constructor (r__9,N:w4;I,z_,_,q_6__,l:Float ){}$I(){}Var L,$_,w:Boolean ;_6_(){} }Class __:_{}Class _{Val E4,___I,_o,$_,$vAA:Array [Array [Boolean ,0xF_1FA],67];}''',
                '''Class,P,{,Constructor,(,r__9,,,N,:,w4,;,I,,,z_,,,_,,,q_6__,,,l,:,Float,),{,},$I,(,),{,},Var,L,,,$_,,,w,:,Boolean,;,_6_,(,),{,},},Class,__,:,_,{,},Class,_,{,Val,E4,,,___I,,,_o,,,$_,,,$vAA,:,Array,[,Array,[,Boolean,,,0xF1FA,],,,67,],;,},<EOF>''',
                101
            )
        )

    def test_225(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C{}Class _0lf{Constructor (){Continue ;}Constructor (z,OX:Array [Array [Array [Int ,0XC],2],0x2A]){}Val $G,$2a__,__9:Array [Boolean ,03];Val _,$1:Array [Array [String ,0b1],0B110001];}Class _:trJS{}Class k{}Class n:_{}''',
                '''Class,C,{,},Class,_0lf,{,Constructor,(,),{,Continue,;,},Constructor,(,z,,,OX,:,Array,[,Array,[,Array,[,Int,,,0XC,],,,2,],,,0x2A,],),{,},Val,$G,,,$2a__,,,__9,:,Array,[,Boolean,,,03,],;,Val,_,,,$1,:,Array,[,Array,[,String,,,0b1,],,,0B110001,],;,},Class,_,:,trJS,{,},Class,k,{,},Class,n,:,_,{,},<EOF>''',
                101
            )
        )

    def test_226(self):
        self.assertTrue(
            TestLexer.test(
                '''Class lL_{Constructor (B:Int ;o3C,p:ILW_3){Continue ;Continue ;} }Class __9{__(_,_,_:Array [Boolean ,0b1]){}v(_2_,z__:Array [Int ,0b1];_p:Array [Array [String ,0x1],0B101];_:_B;C,eS,W,K,A80:String ){}Constructor (){} }''',
                '''Class,lL_,{,Constructor,(,B,:,Int,;,o3C,,,p,:,ILW_3,),{,Continue,;,Continue,;,},},Class,__9,{,__,(,_,,,_,,,_,:,Array,[,Boolean,,,0b1,],),{,},v,(,_2_,,,z__,:,Array,[,Int,,,0b1,],;,_p,:,Array,[,Array,[,String,,,0x1,],,,0B101,],;,_,:,_B,;,C,,,eS,,,W,,,K,,,A80,:,String,),{,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_227(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A_{}Class _{}Class S{_(x,G,_,_:Array [Array [Float ,0X28],05];__:_c6_){Break ;Break ;} }Class O_:__74w_{Val $Y,CK_6:Array [Array [Array [Float ,077],05],0xB];}''',
                '''Class,A_,{,},Class,_,{,},Class,S,{,_,(,x,,,G,,,_,,,_,:,Array,[,Array,[,Float,,,0X28,],,,05,],;,__,:,_c6_,),{,Break,;,Break,;,},},Class,O_,:,__74w_,{,Val,$Y,,,CK_6,:,Array,[,Array,[,Array,[,Float,,,077,],,,05,],,,0xB,],;,},<EOF>''',
                101
            )
        )

    def test_228(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m:f_{$x(_,p:Int ;_,_,_,t,F,_:Boolean ){Var l9o_i:Array [Float ,0X9];}Destructor (){Continue ;} }Class _{}Class g:__{}''',
                '''Class,m,:,f_,{,$x,(,_,,,p,:,Int,;,_,,,_,,,_,,,t,,,F,,,_,:,Boolean,),{,Var,l9o_i,:,Array,[,Float,,,0X9,],;,},Destructor,(,),{,Continue,;,},},Class,_,{,},Class,g,:,__,{,},<EOF>''',
                101
            )
        )

    def test_229(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Fg:RP5v{Var $5___n,O2g:Boolean ;Var $4n:l1;}Class Q:__{$v_0_(){}Val $4:Int ;Constructor (){}$_5(I,_,__,Z_:Array [Float ,0XF];B,_,__B:qT_804;y,V_7:Int ;I,l,_7:String ;_6,_6,K,_1,z9j:Boolean ){} }Class H_7_{}Class f:L{$_7(){} }''',
                '''Class,Fg,:,RP5v,{,Var,$5___n,,,O2g,:,Boolean,;,Var,$4n,:,l1,;,},Class,Q,:,__,{,$v_0_,(,),{,},Val,$4,:,Int,;,Constructor,(,),{,},$_5,(,I,,,_,,,__,,,Z_,:,Array,[,Float,,,0XF,],;,B,,,_,,,__B,:,qT_804,;,y,,,V_7,:,Int,;,I,,,l,,,_7,:,String,;,_6,,,_6,,,K,,,_1,,,z9j,:,Boolean,),{,},},Class,H_7_,{,},Class,f,:,L,{,$_7,(,),{,},},<EOF>''',
                101
            )
        )

    def test_230(self):
        self.assertTrue(
            TestLexer.test(
                '''Class rw_:__9h_{Val _:Float ;}Class _:_{}Class ZFyz__:EO{}Class _:__0{Constructor (___:Int ;i:String ;J__4:Array [Array [Array [String ,5],3_5],02]){} }''',
                '''Class,rw_,:,__9h_,{,Val,_,:,Float,;,},Class,_,:,_,{,},Class,ZFyz__,:,EO,{,},Class,_,:,__0,{,Constructor,(,___,:,Int,;,i,:,String,;,J__4,:,Array,[,Array,[,Array,[,String,,,5,],,,35,],,,02,],),{,},},<EOF>''',
                101
            )
        )

    def test_231(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m1{Var N:G1;Constructor (zM,t,_:Array [Float ,7];t:Float ;_:Array [Array [Array [Array [Array [Float ,0B1_11],040],040],44],0B101]){} }''',
                '''Class,m1,{,Var,N,:,G1,;,Constructor,(,zM,,,t,,,_,:,Array,[,Float,,,7,],;,t,:,Float,;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B111,],,,040,],,,040,],,,44,],,,0B101,],),{,},},<EOF>''',
                101
            )
        )

    def test_232(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _p:S{Val U:Float ;}Class _:Q____{G_7(_JN,_:Array [Float ,076]){} }Class _:_{}Class l_{}Class b_78{Val $2_,$_,$M6:Array [Array [Array [Float ,0b1_0_0_0],72],0X5F];}''',
                '''Class,_p,:,S,{,Val,U,:,Float,;,},Class,_,:,Q____,{,G_7,(,_JN,,,_,:,Array,[,Float,,,076,],),{,},},Class,_,:,_,{,},Class,l_,{,},Class,b_78,{,Val,$2_,,,$_,,,$M6,:,Array,[,Array,[,Array,[,Float,,,0b1000,],,,72,],,,0X5F,],;,},<EOF>''',
                101
            )
        )

    def test_233(self):
        self.assertTrue(
            TestLexer.test(
                '''Class M{Constructor (D7:String ){}$A_U7_kc5(__94:Array [Array [Array [Array [Array [Array [Float ,7],0123],0B11100],0B1],0X3],275];_:Float ;_:_){Break ;Break ;} }''',
                '''Class,M,{,Constructor,(,D7,:,String,),{,},$A_U7_kc5,(,__94,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,7,],,,0123,],,,0B11100,],,,0B1,],,,0X3,],,,275,],;,_,:,Float,;,_,:,_,),{,Break,;,Break,;,},},<EOF>''',
                101
            )
        )

    def test_234(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class _:J5{Var $09,_,_:Int ;Var _M_7,$2_:_1;Val $3k0:Array [Array [Array [Array [Boolean ,07],12],0x74_9_3],0B1];}Class _:Z_5{}''',
                '''Class,_,:,_,{,},Class,_,:,J5,{,Var,$09,,,_,,,_,:,Int,;,Var,_M_7,,,$2_,:,_1,;,Val,$3k0,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,07,],,,12,],,,0x7493,],,,0B1,],;,},Class,_,:,Z_5,{,},<EOF>''',
                101
            )
        )

    def test_235(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:Xcd{Var J2,_,_,$_2:String ;$S2_(Gp,m,eu,_,m,F:M7_){}Val $_Q_2:_;}Class _:h6a{Destructor (){Val _,_F:Float ;}Var $8,_8,$_,$6:K5;}''',
                '''Class,_,:,Xcd,{,Var,J2,,,_,,,_,,,$_2,:,String,;,$S2_,(,Gp,,,m,,,eu,,,_,,,m,,,F,:,M7_,),{,},Val,$_Q_2,:,_,;,},Class,_,:,h6a,{,Destructor,(,),{,Val,_,,,_F,:,Float,;,},Var,$8,,,_8,,,$_,,,$6,:,K5,;,},<EOF>''',
                101
            )
        )

    def test_236(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A_:B_63{}Class ___1h:__{_(){Return ;Continue ;} }Class _:_{Constructor (_k82:Boolean ;Y_,N,wh:C;_X75K5,Q_2:_){Return ;Break ;Continue ;} }Class _:E_{}''',
                '''Class,A_,:,B_63,{,},Class,___1h,:,__,{,_,(,),{,Return,;,Continue,;,},},Class,_,:,_,{,Constructor,(,_k82,:,Boolean,;,Y_,,,N,,,wh,:,C,;,_X75K5,,,Q_2,:,_,),{,Return,;,Break,;,Continue,;,},},Class,_,:,E_,{,},<EOF>''',
                101
            )
        )

    def test_237(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P{Destructor (){}Var $_,Z__:Array [Array [Array [Array [Array [Float ,0b1],0b1001111],0B1],03_6],539_6];Constructor (_,_,_43,_,__:Array [Boolean ,0b100_1];__,y_Y3:_;G:Int ;k:String ){} }''',
                '''Class,P,{,Destructor,(,),{,},Var,$_,,,Z__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1,],,,0b1001111,],,,0B1,],,,036,],,,5396,],;,Constructor,(,_,,,_,,,_43,,,_,,,__,:,Array,[,Boolean,,,0b1001,],;,__,,,y_Y3,:,_,;,G,:,Int,;,k,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_238(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t{}Class j:i{}Class H:e__K{}Class g{}Class __t:_{}Class _5S42S{Constructor (){} }Class __dGZ{}Class _{Val $6y9,$V,$i,_1:Int ;}''',
                '''Class,t,{,},Class,j,:,i,{,},Class,H,:,e__K,{,},Class,g,{,},Class,__t,:,_,{,},Class,_5S42S,{,Constructor,(,),{,},},Class,__dGZ,{,},Class,_,{,Val,$6y9,,,$V,,,$i,,,_1,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_239(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _8{}Class _:_{}Class _64x{Destructor (){Var _,f:Array [Array [Boolean ,1],0446_4];Var U_:Int ;}Val _H,$20,X:Array [String ,06_62_0];Destructor (){}Val $r:Array [Int ,0B100110];}''',
                '''Class,_,{,},Class,_8,{,},Class,_,:,_,{,},Class,_64x,{,Destructor,(,),{,Var,_,,,f,:,Array,[,Array,[,Boolean,,,1,],,,04464,],;,Var,U_,:,Int,;,},Val,_H,,,$20,,,X,:,Array,[,String,,,06620,],;,Destructor,(,),{,},Val,$r,:,Array,[,Int,,,0B100110,],;,},<EOF>''',
                101
            )
        )

    def test_240(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __3AI{Destructor (){}Val __u7C:Array [Array [Array [Int ,0xCA_8_D5],076],3];Var $__:_Fe;Destructor (){Break ;}Var _:Array [Array [String ,413],0B1_10];}Class m:_4{}Class i78_{Constructor (h:Int ;_:m){}Var $_,_,_9,$9_0f84h,$E,$9_,$U6:Int ;Destructor (){Break ;} }Class _:Y{}Class _:_16{}Class F_DY{}''',
                '''Class,__3AI,{,Destructor,(,),{,},Val,__u7C,:,Array,[,Array,[,Array,[,Int,,,0xCA8D5,],,,076,],,,3,],;,Var,$__,:,_Fe,;,Destructor,(,),{,Break,;,},Var,_,:,Array,[,Array,[,String,,,413,],,,0B110,],;,},Class,m,:,_4,{,},Class,i78_,{,Constructor,(,h,:,Int,;,_,:,m,),{,},Var,$_,,,_,,,_9,,,$9_0f84h,,,$E,,,$9_,,,$U6,:,Int,;,Destructor,(,),{,Break,;,},},Class,_,:,Y,{,},Class,_,:,_16,{,},Class,F_DY,{,},<EOF>''',
                101
            )
        )

    def test_241(self):
        self.assertTrue(
            TestLexer.test(
                '''Class mM{Val $_,$_1,$_,Q_s,_,l:Array [Array [Array [Array [Array [Array [Boolean ,0B1_1],0B10111],031],87],8_6],0b1_1_0_0_1];}Class _:_{}''',
                '''Class,mM,{,Val,$_,,,$_1,,,$_,,,Q_s,,,_,,,l,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B11,],,,0B10111,],,,031,],,,87,],,,86,],,,0b11001,],;,},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_242(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_5{}Class _:_b{Constructor (){}Val m:Float ;Constructor (C_o,_:_3;_C:Array [Array [Int ,16],056]){}Val f:Float ;}''',
                '''Class,_,:,_5,{,},Class,_,:,_b,{,Constructor,(,),{,},Val,m,:,Float,;,Constructor,(,C_o,,,_,:,_3,;,_C,:,Array,[,Array,[,Int,,,16,],,,056,],),{,},Val,f,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_243(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _U{Val $_,C,__q:String ;}Class _:_m_2{Constructor (_D:__o76__;c,v,_a:Int ;y,O:Float ){}Destructor (){}Destructor (){Continue ;} }''',
                '''Class,_U,{,Val,$_,,,C,,,__q,:,String,;,},Class,_,:,_m_2,{,Constructor,(,_D,:,__o76__,;,c,,,v,,,_a,:,Int,;,y,,,O,:,Float,),{,},Destructor,(,),{,},Destructor,(,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_244(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0{Val i:Float ;Constructor (B9f:Float ;Yi_n_7:Array [Int ,0XEA_B8];B,_4YG,VK:Array [Boolean ,73];y:Array [String ,0x3_4]){} }''',
                '''Class,_0,{,Val,i,:,Float,;,Constructor,(,B9f,:,Float,;,Yi_n_7,:,Array,[,Int,,,0XEAB8,],;,B,,,_4YG,,,VK,:,Array,[,Boolean,,,73,],;,y,:,Array,[,String,,,0x34,],),{,},},<EOF>''',
                101
            )
        )

    def test_245(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A_8_4_60__1wt{}Class _:Y_A91{Constructor (){} }Class J0{}Class d:l_KV{Val _120:Boolean ;Destructor (){Var _,_,___,_6b:Z;} }''',
                '''Class,A_8_4_60__1wt,{,},Class,_,:,Y_A91,{,Constructor,(,),{,},},Class,J0,{,},Class,d,:,l_KV,{,Val,_120,:,Boolean,;,Destructor,(,),{,Var,_,,,_,,,___,,,_6b,:,Z,;,},},<EOF>''',
                101
            )
        )

    def test_246(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __zx{}Class p83:b{Var $8,_g:__;Val $8,Y:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,0B10],0b111001],0B1001001],0x2_88_8_2_0],053],0123],0123],0B11001],0xF],0xC],0B1001001];Destructor (){}Val __:kW;}''',
                '''Class,__zx,{,},Class,p83,:,b,{,Var,$8,,,_g,:,__,;,Val,$8,,,Y,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B10,],,,0b111001,],,,0B1001001,],,,0x288820,],,,053,],,,0123,],,,0123,],,,0B11001,],,,0xF,],,,0xC,],,,0B1001001,],;,Destructor,(,),{,},Val,__,:,kW,;,},<EOF>''',
                101
            )
        )

    def test_247(self):
        self.assertTrue(
            TestLexer.test(
                '''Class GT{Var $_:x;Constructor (_9,O2,Y,N,vM:Array [Boolean ,0X42]){}Var X:Boolean ;}Class yq_0:__{Var $B,$0:String ;}''',
                '''Class,GT,{,Var,$_,:,x,;,Constructor,(,_9,,,O2,,,Y,,,N,,,vM,:,Array,[,Boolean,,,0X42,],),{,},Var,X,:,Boolean,;,},Class,yq_0,:,__,{,Var,$B,,,$0,:,String,;,},<EOF>''',
                101
            )
        )

    def test_248(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Q:_3{Constructor (_6_,e,Rr:String ;k_,n,_L_4:Array [Float ,58];n1VE,_:Boolean ;_5:Int ){}Val _,V:Array [Float ,07];}Class Y{}''',
                '''Class,Q,:,_3,{,Constructor,(,_6_,,,e,,,Rr,:,String,;,k_,,,n,,,_L_4,:,Array,[,Float,,,58,],;,n1VE,,,_,:,Boolean,;,_5,:,Int,),{,},Val,_,,,V,:,Array,[,Float,,,07,],;,},Class,Y,{,},<EOF>''',
                101
            )
        )

    def test_249(self):
        self.assertTrue(
            TestLexer.test(
                '''Class YcX{Val g:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,04_6],65],02_2],28],0x56],0x56],65],0x8],0B111110],04];}''',
                '''Class,YcX,{,Val,g,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,046,],,,65,],,,022,],,,28,],,,0x56,],,,0x56,],,,65,],,,0x8,],,,0B111110,],,,04,],;,},<EOF>''',
                101
            )
        )

    def test_250(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var $___,$3,_e:Array [Int ,0B111001];Val T:jP;Var $_h_1,$__t0:Array [Array [Array [Float ,0B10_101_0],5],0B111001];}Class v{}''',
                '''Class,_,{,Var,$___,,,$3,,,_e,:,Array,[,Int,,,0B111001,],;,Val,T,:,jP,;,Var,$_h_1,,,$__t0,:,Array,[,Array,[,Array,[,Float,,,0B101010,],,,5,],,,0B111001,],;,},Class,v,{,},<EOF>''',
                101
            )
        )

    def test_251(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class D_{}Class Z:___{}Class I:d3{}Class _aJ5B{}Class h:d{Destructor (){}Val _,$T,$_K:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0x45],0144],0b1100010],0x45],2],91],05],0B1000011];}Class s:E{}''',
                '''Class,_,{,},Class,D_,{,},Class,Z,:,___,{,},Class,I,:,d3,{,},Class,_aJ5B,{,},Class,h,:,d,{,Destructor,(,),{,},Val,_,,,$T,,,$_K,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x45,],,,0144,],,,0b1100010,],,,0x45,],,,2,],,,91,],,,05,],,,0B1000011,],;,},Class,s,:,E,{,},<EOF>''',
                101
            )
        )

    def test_252(self):
        self.assertTrue(
            TestLexer.test(
                '''Class p5AT{Var $6,$582:Float ;Constructor (A,_,_:Array [Array [Array [Float ,39],0XF],7];o:Array [Array [Array [Array [Int ,0x6_A_7],3_2],0xA],0XF];N_,V,VC7,_,_W,_84:Array [Int ,0b1001110]){} }Class _qp{$_(){Var _,q,_OB:Array [Float ,0x23];}Var ____3:o_;}''',
                '''Class,p5AT,{,Var,$6,,,$582,:,Float,;,Constructor,(,A,,,_,,,_,:,Array,[,Array,[,Array,[,Float,,,39,],,,0XF,],,,7,],;,o,:,Array,[,Array,[,Array,[,Array,[,Int,,,0x6A7,],,,32,],,,0xA,],,,0XF,],;,N_,,,V,,,VC7,,,_,,,_W,,,_84,:,Array,[,Int,,,0b1001110,],),{,},},Class,_qp,{,$_,(,),{,Var,_,,,q,,,_OB,:,Array,[,Float,,,0x23,],;,},Var,____3,:,o_,;,},<EOF>''',
                101
            )
        )

    def test_253(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___:_D09jV6{Constructor (){} }Class _:GG8{Val $7,$_68:Array [Int ,3];}Class e:_p_{Var $1Q,$_,$5fR,$5,t:U;Var $s:Float ;}''',
                '''Class,___,:,_D09jV6,{,Constructor,(,),{,},},Class,_,:,GG8,{,Val,$7,,,$_68,:,Array,[,Int,,,3,],;,},Class,e,:,_p_,{,Var,$1Q,,,$_,,,$5fR,,,$5,,,t,:,U,;,Var,$s,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_254(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var _:Array [Array [Array [Array [Array [Array [Array [Array [Int ,041],0B1011001],17],17],17],0b1010011],041],0b1010011];}Class _{Constructor (v,_:String ){} }''',
                '''Class,_,{,Var,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,041,],,,0B1011001,],,,17,],,,17,],,,17,],,,0b1010011,],,,041,],,,0b1010011,],;,},Class,_,{,Constructor,(,v,,,_,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_255(self):
        self.assertTrue(
            TestLexer.test(
                '''Class i:_1D{Constructor (u:Y_1;_:_1_;_0,_h_f,_w:__6;_,_:__;Ck,_:String ;_r:_;_,e,Ff_,_:Array [Array [Boolean ,0b100],0X51];_4,jyp:EV){} }''',
                '''Class,i,:,_1D,{,Constructor,(,u,:,Y_1,;,_,:,_1_,;,_0,,,_h_f,,,_w,:,__6,;,_,,,_,:,__,;,Ck,,,_,:,String,;,_r,:,_,;,_,,,e,,,Ff_,,,_,:,Array,[,Array,[,Boolean,,,0b100,],,,0X51,],;,_4,,,jyp,:,EV,),{,},},<EOF>''',
                101
            )
        )

    def test_256(self):
        self.assertTrue(
            TestLexer.test(
                '''Class x0{Constructor (m:_;_A62,S__k,AW:Array [Array [Int ,015_1],9_778]){}Destructor (){Val C1W,A3837,q,_:Array [Boolean ,0X61];} }Class _:t{}Class _:J{}Class _{}Class H5{}Class __4:_{}''',
                '''Class,x0,{,Constructor,(,m,:,_,;,_A62,,,S__k,,,AW,:,Array,[,Array,[,Int,,,0151,],,,9778,],),{,},Destructor,(,),{,Val,C1W,,,A3837,,,q,,,_,:,Array,[,Boolean,,,0X61,],;,},},Class,_,:,t,{,},Class,_,:,J,{,},Class,_,{,},Class,H5,{,},Class,__4,:,_,{,},<EOF>''',
                101
            )
        )

    def test_257(self):
        self.assertTrue(
            TestLexer.test(
                '''Class F:M{Constructor (__,_O3,D,A,b,D:Array [Array [String ,33],33]){}Destructor (){} }Class _3ZB{Val $_0,_H,$_:String ;}''',
                '''Class,F,:,M,{,Constructor,(,__,,,_O3,,,D,,,A,,,b,,,D,:,Array,[,Array,[,String,,,33,],,,33,],),{,},Destructor,(,),{,},},Class,_3ZB,{,Val,$_0,,,_H,,,$_,:,String,;,},<EOF>''',
                101
            )
        )

    def test_258(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Jm_{Var D,F:Boolean ;Val $___K:Array [Int ,0B10_1];}Class m:_{}Class C_:c7{}Class x{Var _,$Y,_:Array [Int ,044];}Class c:N5{}''',
                '''Class,Jm_,{,Var,D,,,F,:,Boolean,;,Val,$___K,:,Array,[,Int,,,0B101,],;,},Class,m,:,_,{,},Class,C_,:,c7,{,},Class,x,{,Var,_,,,$Y,,,_,:,Array,[,Int,,,044,],;,},Class,c,:,N5,{,},<EOF>''',
                101
            )
        )

    def test_259(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Z31h_{Val $4_:Array [Array [Float ,023],0XB];$_6_6p(_X,f,__D_3,hg,_7,_K:Array [Array [Array [Float ,0X60],0b1111],06_63];_6___,__S:_;_69_:gMX){} }Class A1Fm:_9{_0a(J,pb,c,n:Array [Array [Array [Boolean ,0X60],0x4],549];K:Int ;__:W0_){Break ;}Val __,O,n_9:Array [Array [Array [Float ,0B1001101],56],9_0_4];}''',
                '''Class,Z31h_,{,Val,$4_,:,Array,[,Array,[,Float,,,023,],,,0XB,],;,$_6_6p,(,_X,,,f,,,__D_3,,,hg,,,_7,,,_K,:,Array,[,Array,[,Array,[,Float,,,0X60,],,,0b1111,],,,0663,],;,_6___,,,__S,:,_,;,_69_,:,gMX,),{,},},Class,A1Fm,:,_9,{,_0a,(,J,,,pb,,,c,,,n,:,Array,[,Array,[,Array,[,Boolean,,,0X60,],,,0x4,],,,549,],;,K,:,Int,;,__,:,W0_,),{,Break,;,},Val,__,,,O,,,n_9,:,Array,[,Array,[,Array,[,Float,,,0B1001101,],,,56,],,,904,],;,},<EOF>''',
                101
            )
        )

    def test_260(self):
        self.assertTrue(
            TestLexer.test(
                '''Class S_{Constructor (x7b:Array [Float ,03_15]){} }Class _8{Val E:Array [Array [Float ,0X8_8_1B],0x6];Destructor (){O::$7();}Var $_I__K,$_7N:Array [Array [Boolean ,0b1],0b11_1];}''',
                '''Class,S_,{,Constructor,(,x7b,:,Array,[,Float,,,0315,],),{,},},Class,_8,{,Val,E,:,Array,[,Array,[,Float,,,0X881B,],,,0x6,],;,Destructor,(,),{,O,::,$7,(,),;,},Var,$_I__K,,,$_7N,:,Array,[,Array,[,Boolean,,,0b1,],,,0b111,],;,},<EOF>''',
                101
            )
        )

    def test_261(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n:N{Var h5la__,d,F_0n_,$f_:Array [Array [Array [Array [String ,36],0b11100],021],02];Constructor (_,s:M){}Constructor (){Return ;} }Class ___7{}Class __7{}''',
                '''Class,n,:,N,{,Var,h5la__,,,d,,,F_0n_,,,$f_,:,Array,[,Array,[,Array,[,Array,[,String,,,36,],,,0b11100,],,,021,],,,02,],;,Constructor,(,_,,,s,:,M,),{,},Constructor,(,),{,Return,;,},},Class,___7,{,},Class,__7,{,},<EOF>''',
                101
            )
        )

    def test_262(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{$L_6d(L,_9t:Array [Boolean ,0125];_,gH__:Boolean ;WY,__,_0W:__;l,_:Array [String ,0125];_1h_,__:Array [Array [Array [Boolean ,4_0_36],0X2E],0B1010001];__,m_,_5,_3L:_w){Continue ;Continue ;}Destructor (){} }''',
                '''Class,_,:,_,{,$L_6d,(,L,,,_9t,:,Array,[,Boolean,,,0125,],;,_,,,gH__,:,Boolean,;,WY,,,__,,,_0W,:,__,;,l,,,_,:,Array,[,String,,,0125,],;,_1h_,,,__,:,Array,[,Array,[,Array,[,Boolean,,,4036,],,,0X2E,],,,0B1010001,],;,__,,,m_,,,_5,,,_3L,:,_w,),{,Continue,;,Continue,;,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_263(self):
        self.assertTrue(
            TestLexer.test(
                '''Class H4____:S{_(_6_8_:t;__,X:Array [Boolean ,0b1011];_:n_9_p_;gV:Array [Int ,0X10];t:Array [Int ,93]){}Val $jP_:Array [Array [Array [Int ,71],0B1001000],2_5];Constructor (){Val q,n:_F;} }Class _:_{}''',
                '''Class,H4____,:,S,{,_,(,_6_8_,:,t,;,__,,,X,:,Array,[,Boolean,,,0b1011,],;,_,:,n_9_p_,;,gV,:,Array,[,Int,,,0X10,],;,t,:,Array,[,Int,,,93,],),{,},Val,$jP_,:,Array,[,Array,[,Array,[,Int,,,71,],,,0B1001000,],,,25,],;,Constructor,(,),{,Val,q,,,n,:,_F,;,},},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_264(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class NW7o_{Constructor (Yz:Array [Array [Array [Array [String ,39],0B100_0],39],072];n:Array [Array [Array [Int ,0b1],0X6],05];_i:Float ){} }Class q4{}''',
                '''Class,_,{,},Class,NW7o_,{,Constructor,(,Yz,:,Array,[,Array,[,Array,[,Array,[,String,,,39,],,,0B1000,],,,39,],,,072,],;,n,:,Array,[,Array,[,Array,[,Int,,,0b1,],,,0X6,],,,05,],;,_i,:,Float,),{,},},Class,q4,{,},<EOF>''',
                101
            )
        )

    def test_265(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g:E{}Class _m3_{Constructor (V,__0:_){} }Class g:_3E{}Class N0{g(_,e_,ZE_:Array [Array [Array [Int ,0136],0X6],0B101001];_:Boolean ;E_:_){}_Hu_k5(i5_:q;In :l__;i1:Float ;zZ,_,O,_0_p:Array [String ,07_3]){} }''',
                '''Class,g,:,E,{,},Class,_m3_,{,Constructor,(,V,,,__0,:,_,),{,},},Class,g,:,_3E,{,},Class,N0,{,g,(,_,,,e_,,,ZE_,:,Array,[,Array,[,Array,[,Int,,,0136,],,,0X6,],,,0B101001,],;,_,:,Boolean,;,E_,:,_,),{,},_Hu_k5,(,i5_,:,q,;,In,:,l__,;,i1,:,Float,;,zZ,,,_,,,O,,,_0_p,:,Array,[,String,,,073,],),{,},},<EOF>''',
                101
            )
        )

    def test_266(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _3_:_5{}Class _{Constructor (I:String ;Q:_;Z,_5:Array [Array [Array [Array [Boolean ,90],04],0x16],0X3B];_,z_:E;m_,_F,d86,_,_:Float ){} }''',
                '''Class,_3_,:,_5,{,},Class,_,{,Constructor,(,I,:,String,;,Q,:,_,;,Z,,,_5,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,90,],,,04,],,,0x16,],,,0X3B,],;,_,,,z_,:,E,;,m_,,,_F,,,d86,,,_,,,_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_267(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b:Y{Constructor (ckA,g___:Array [Array [String ,0b10011],0X61];__:Array [Array [Array [Float ,0x6_3],04],052];___,_:Array [Float ,052];zi4,P:_H0){_::$____M8g_();}Val $_,_:_;}''',
                '''Class,b,:,Y,{,Constructor,(,ckA,,,g___,:,Array,[,Array,[,String,,,0b10011,],,,0X61,],;,__,:,Array,[,Array,[,Array,[,Float,,,0x63,],,,04,],,,052,],;,___,,,_,:,Array,[,Float,,,052,],;,zi4,,,P,:,_H0,),{,_,::,$____M8g_,(,),;,},Val,$_,,,_,:,_,;,},<EOF>''',
                101
            )
        )

    def test_268(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _w{}Class __{Var _9,m,$0:_;Var $0,$vN_X:Array [String ,067];$O6(_W,_:Array [Int ,0B1000100];A,T_x1,_Z:_98){Continue ;} }''',
                '''Class,_w,{,},Class,__,{,Var,_9,,,m,,,$0,:,_,;,Var,$0,,,$vN_X,:,Array,[,String,,,067,],;,$O6,(,_W,,,_,:,Array,[,Int,,,0B1000100,],;,A,,,T_x1,,,_Z,:,_98,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_269(self):
        self.assertTrue(
            TestLexer.test(
                '''Class W_{}Class M:__8T{$yj_(){}$__(__1,___4,j1,_5j4,_:Array [Array [Boolean ,40],0B1000101];__,B_7:Array [Array [Array [Int ,0b101001],9_36_8],0b1];_:String ;__,__I:Array [Int ,05]){} }''',
                '''Class,W_,{,},Class,M,:,__8T,{,$yj_,(,),{,},$__,(,__1,,,___4,,,j1,,,_5j4,,,_,:,Array,[,Array,[,Boolean,,,40,],,,0B1000101,],;,__,,,B_7,:,Array,[,Array,[,Array,[,Int,,,0b101001,],,,9368,],,,0b1,],;,_,:,String,;,__,,,__I,:,Array,[,Int,,,05,],),{,},},<EOF>''',
                101
            )
        )

    def test_270(self):
        self.assertTrue(
            TestLexer.test(
                '''Class I:Z{Constructor (_:B;_:Array [Array [Array [Array [String ,0xD75],05],0x44],0b1];_,w,_:Array [Boolean ,03_5];o,__zx,___:Array [Array [Array [String ,0B1],0b10_00],0B100111];_03gL,L:Int ;T,_,P:Boolean ;Ra4,y,J_:Boolean ;_:_;_5,qN_:Boolean ;G:Array [Array [Array [String ,02_6_0],05],072_7_5];Te_:Array [Array [String ,06_4_62],4]){}Destructor (){}Destructor (){Continue ;} }''',
                '''Class,I,:,Z,{,Constructor,(,_,:,B,;,_,:,Array,[,Array,[,Array,[,Array,[,String,,,0xD75,],,,05,],,,0x44,],,,0b1,],;,_,,,w,,,_,:,Array,[,Boolean,,,035,],;,o,,,__zx,,,___,:,Array,[,Array,[,Array,[,String,,,0B1,],,,0b1000,],,,0B100111,],;,_03gL,,,L,:,Int,;,T,,,_,,,P,:,Boolean,;,Ra4,,,y,,,J_,:,Boolean,;,_,:,_,;,_5,,,qN_,:,Boolean,;,G,:,Array,[,Array,[,Array,[,String,,,0260,],,,05,],,,07275,],;,Te_,:,Array,[,Array,[,String,,,06462,],,,4,],),{,},Destructor,(,),{,},Destructor,(,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_271(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_:Array [Boolean ,065];_,_,m_:Array [Array [Array [Array [Int ,91],0X1A],01],065]){Continue ;}_sC(){} }''',
                '''Class,_,{,Constructor,(,_,:,Array,[,Boolean,,,065,],;,_,,,_,,,m_,:,Array,[,Array,[,Array,[,Array,[,Int,,,91,],,,0X1A,],,,01,],,,065,],),{,Continue,;,},_sC,(,),{,},},<EOF>''',
                101
            )
        )

    def test_272(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V{}Class x_3_j:t7{Constructor (B4:Array [Array [Int ,0b101100],0B1010110];_,_:Float ){Var Y:Array [Array [Array [Array [Int ,0x4A],0x4A],0x1],06];} }''',
                '''Class,V,{,},Class,x_3_j,:,t7,{,Constructor,(,B4,:,Array,[,Array,[,Int,,,0b101100,],,,0B1010110,],;,_,,,_,:,Float,),{,Var,Y,:,Array,[,Array,[,Array,[,Array,[,Int,,,0x4A,],,,0x4A,],,,0x1,],,,06,],;,},},<EOF>''',
                101
            )
        )

    def test_273(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_,T,W55__gE_Z2:Float ){Val aB,_,y:String ;_45_7::$01();}Destructor (){}$_(_z,_,_W:HG_R;_:Int ;F,O:String ;a:Int ;U:Array [Array [Array [Float ,0x7_29],30_8],0B100]){} }Class j{}''',
                '''Class,_,{,Constructor,(,_,,,T,,,W55__gE_Z2,:,Float,),{,Val,aB,,,_,,,y,:,String,;,_45_7,::,$01,(,),;,},Destructor,(,),{,},$_,(,_z,,,_,,,_W,:,HG_R,;,_,:,Int,;,F,,,O,:,String,;,a,:,Int,;,U,:,Array,[,Array,[,Array,[,Float,,,0x729,],,,308,],,,0B100,],),{,},},Class,j,{,},<EOF>''',
                101
            )
        )

    def test_274(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{$_(__,_,_:Float ;__,_i,_:Boolean ;Y,e,S_4,_,_:Array [Array [Int ,0x2A],72];_:Boolean ;_:Int ){}_O__L1(){} }''',
                '''Class,_,{,$_,(,__,,,_,,,_,:,Float,;,__,,,_i,,,_,:,Boolean,;,Y,,,e,,,S_4,,,_,,,_,:,Array,[,Array,[,Int,,,0x2A,],,,72,],;,_,:,Boolean,;,_,:,Int,),{,},_O__L1,(,),{,},},<EOF>''',
                101
            )
        )

    def test_275(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __7:_{Constructor (){}a80_(_,C:Array [Array [Array [Array [Float ,0x63],04],8_0313_1],1];T,_:_;N:Array [Float ,0b11_10];qJ,S_:L15){} }Class d_8{Constructor (){} }''',
                '''Class,__7,:,_,{,Constructor,(,),{,},a80_,(,_,,,C,:,Array,[,Array,[,Array,[,Array,[,Float,,,0x63,],,,04,],,,803131,],,,1,],;,T,,,_,:,_,;,N,:,Array,[,Float,,,0b1110,],;,qJ,,,S_,:,L15,),{,},},Class,d_8,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_276(self):
        self.assertTrue(
            TestLexer.test(
                '''Class c67{$5v_(_,_Xg3b:Array [Float ,3];l6_:Array [Array [Array [String ,0X2],0B1],0b111110]){}Var $65_T7___,D:Array [Float ,10];}''',
                '''Class,c67,{,$5v_,(,_,,,_Xg3b,:,Array,[,Float,,,3,],;,l6_,:,Array,[,Array,[,Array,[,String,,,0X2,],,,0B1,],,,0b111110,],),{,},Var,$65_T7___,,,D,:,Array,[,Float,,,10,],;,},<EOF>''',
                101
            )
        )

    def test_277(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _1:d_{}Class _:f{Val _Ct,a:Array [Array [Array [Array [Array [Int ,0x2],0x2],034],0x33],0x33];Constructor (){} }Class q5{}''',
                '''Class,_1,:,d_,{,},Class,_,:,f,{,Val,_Ct,,,a,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x2,],,,0x2,],,,034,],,,0x33,],,,0x33,],;,Constructor,(,),{,},},Class,q5,{,},<EOF>''',
                101
            )
        )

    def test_278(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Var Mr4,J0W_u0_C:Float ;}Class _{Constructor (t1,_:Array [Int ,03];_,_10,_,__:Array [Array [Array [Int ,54],0b1100011],0x30]){} }Class GV{}''',
                '''Class,_,:,_,{,Var,Mr4,,,J0W_u0_C,:,Float,;,},Class,_,{,Constructor,(,t1,,,_,:,Array,[,Int,,,03,],;,_,,,_10,,,_,,,__,:,Array,[,Array,[,Array,[,Int,,,54,],,,0b1100011,],,,0x30,],),{,},},Class,GV,{,},<EOF>''',
                101
            )
        )

    def test_279(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m_:R{Val $_,$_,$9:Array [Int ,40];}Class _C1__7:b{Val K,B,$k_S82_6_,_Q,_:Boolean ;$9(){Val G__:Array [Boolean ,0B1];} }''',
                '''Class,m_,:,R,{,Val,$_,,,$_,,,$9,:,Array,[,Int,,,40,],;,},Class,_C1__7,:,b,{,Val,K,,,B,,,$k_S82_6_,,,_Q,,,_,:,Boolean,;,$9,(,),{,Val,G__,:,Array,[,Boolean,,,0B1,],;,},},<EOF>''',
                101
            )
        )

    def test_280(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2_{Var $o,f,_,$6Fg97X:_94w;}Class I_:_{}Class _3{}Class _:_{}Class AYm{Constructor (_:Array [Array [Array [Array [Array [Float ,0x3A],18],0B1_01],6_1_45],0b1_10_0];_Z:String ;_,_9_b,H_S:Array [Array [Array [Boolean ,18],0b100111],06_3_7_5_0_3_2]){Continue ;Break ;} }Class d{}Class D{}''',
                '''Class,_2_,{,Var,$o,,,f,,,_,,,$6Fg97X,:,_94w,;,},Class,I_,:,_,{,},Class,_3,{,},Class,_,:,_,{,},Class,AYm,{,Constructor,(,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x3A,],,,18,],,,0B101,],,,6145,],,,0b1100,],;,_Z,:,String,;,_,,,_9_b,,,H_S,:,Array,[,Array,[,Array,[,Boolean,,,18,],,,0b100111,],,,06375032,],),{,Continue,;,Break,;,},},Class,d,{,},Class,D,{,},<EOF>''',
                101
            )
        )

    def test_281(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $15:Boolean ;}Class I{Val $_:Array [String ,0B1];Constructor (s_:Float ;cF:Array [Array [Boolean ,0X3_06_B],057]){} }Class _:f6{}Class _4:WV_0{}''',
                '''Class,_,{,Val,$15,:,Boolean,;,},Class,I,{,Val,$_,:,Array,[,String,,,0B1,],;,Constructor,(,s_,:,Float,;,cF,:,Array,[,Array,[,Boolean,,,0X306B,],,,057,],),{,},},Class,_,:,f6,{,},Class,_4,:,WV_0,{,},<EOF>''',
                101
            )
        )

    def test_282(self):
        self.assertTrue(
            TestLexer.test(
                '''Class s:_W{Val $__:Array [Array [Array [Array [Array [Int ,03],0xF],0b100010],0x9],0b100010];$v(__v,_:mY_;__,_:Array [Boolean ,60];m_:b1){Break ;}$_F5(_eJ:String ){Continue ;} }Class __{Val $g:Int ;}''',
                '''Class,s,:,_W,{,Val,$__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,03,],,,0xF,],,,0b100010,],,,0x9,],,,0b100010,],;,$v,(,__v,,,_,:,mY_,;,__,,,_,:,Array,[,Boolean,,,60,],;,m_,:,b1,),{,Break,;,},$_F5,(,_eJ,:,String,),{,Continue,;,},},Class,__,{,Val,$g,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_283(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class __{Constructor (_4:Float ;u:Array [Boolean ,0B100];Y__:Boolean ;_4:Array [Boolean ,6_48];_R:Array [Array [Float ,19],0B100];y,z:Boolean ){}p_(_,_:Float ;_b,__:Array [Float ,19];V6s_:__i__q_;Q:String ;_7,i7_:_4_){ {Return ;} }}Class p7:__e{}''',
                '''Class,_,:,_,{,},Class,__,{,Constructor,(,_4,:,Float,;,u,:,Array,[,Boolean,,,0B100,],;,Y__,:,Boolean,;,_4,:,Array,[,Boolean,,,648,],;,_R,:,Array,[,Array,[,Float,,,19,],,,0B100,],;,y,,,z,:,Boolean,),{,},p_,(,_,,,_,:,Float,;,_b,,,__,:,Array,[,Float,,,19,],;,V6s_,:,__i__q_,;,Q,:,String,;,_7,,,i7_,:,_4_,),{,{,Return,;,},},},Class,p7,:,__e,{,},<EOF>''',
                101
            )
        )

    def test_284(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_b_x02{Constructor (_:Array [Boolean ,0b1001000];Ny,_:Array [String ,9];_r6,xL:Boolean ){}Destructor (){} }Class _86_{}Class __{}''',
                '''Class,_,:,_b_x02,{,Constructor,(,_,:,Array,[,Boolean,,,0b1001000,],;,Ny,,,_,:,Array,[,String,,,9,],;,_r6,,,xL,:,Boolean,),{,},Destructor,(,),{,},},Class,_86_,{,},Class,__,{,},<EOF>''',
                101
            )
        )

    def test_285(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _51{}Class kp{}Class _7_:_A{Var _:Int ;Val $P:_;_2_RF_(_,_8,_,_s_L_,B:Array [Array [Array [String ,0B10000],060],1_3_4_9];_,_4Z_:L_;M2X:Boolean ){} }Class w{}''',
                '''Class,_51,{,},Class,kp,{,},Class,_7_,:,_A,{,Var,_,:,Int,;,Val,$P,:,_,;,_2_RF_,(,_,,,_8,,,_,,,_s_L_,,,B,:,Array,[,Array,[,Array,[,String,,,0B10000,],,,060,],,,1349,],;,_,,,_4Z_,:,L_,;,M2X,:,Boolean,),{,},},Class,w,{,},<EOF>''',
                101
            )
        )

    def test_286(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V:C4{Val o,$_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0B11101],0xB],0B11101],9_7],01],04],5_7],0x10],0b1];}''',
                '''Class,V,:,C4,{,Val,o,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B11101,],,,0xB,],,,0B11101,],,,97,],,,01,],,,04,],,,57,],,,0x10,],,,0b1,],;,},<EOF>''',
                101
            )
        )

    def test_287(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _3p{Constructor (){}Var __,__,$0,$20,_,$_G_,$m:Array [Int ,0X22];}Class s{}Class Y:s{$H(_x,_,_:Array [Boolean ,0B1_1_0_0];v:_;S:Array [Int ,1];P_K,_,_,p,___,_6s,_:y9;h_:Float ){ {{} }} }''',
                '''Class,_3p,{,Constructor,(,),{,},Var,__,,,__,,,$0,,,$20,,,_,,,$_G_,,,$m,:,Array,[,Int,,,0X22,],;,},Class,s,{,},Class,Y,:,s,{,$H,(,_x,,,_,,,_,:,Array,[,Boolean,,,0B1100,],;,v,:,_,;,S,:,Array,[,Int,,,1,],;,P_K,,,_,,,_,,,p,,,___,,,_6s,,,_,:,y9,;,h_,:,Float,),{,{,{,},},},},<EOF>''',
                101
            )
        )

    def test_288(self):
        self.assertTrue(
            TestLexer.test(
                '''Class v{_(l4:Array [Float ,18];_:Array [String ,0X6];M4:_;__:Array [Array [Boolean ,46],24];_K:__){}Val $0,$3_,R_2q:Array [Int ,0X4_0];}''',
                '''Class,v,{,_,(,l4,:,Array,[,Float,,,18,],;,_,:,Array,[,String,,,0X6,],;,M4,:,_,;,__,:,Array,[,Array,[,Boolean,,,46,],,,24,],;,_K,:,__,),{,},Val,$0,,,$3_,,,R_2q,:,Array,[,Int,,,0X40,],;,},<EOF>''',
                101
            )
        )

    def test_289(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t5_{Constructor (_:Array [Array [Array [String ,01_2],03],7];_0,_,__,_I:Array [Array [Array [Float ,0X5D],56_2_4],0x6D];__:Array [Array [Array [Array [Boolean ,0x2],0104],0b10000],0x5E_9DA_0C]){}Val $_,g:Int ;}Class Z{}''',
                '''Class,t5_,{,Constructor,(,_,:,Array,[,Array,[,Array,[,String,,,012,],,,03,],,,7,],;,_0,,,_,,,__,,,_I,:,Array,[,Array,[,Array,[,Float,,,0X5D,],,,5624,],,,0x6D,],;,__,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x2,],,,0104,],,,0b10000,],,,0x5E9DA0C,],),{,},Val,$_,,,g,:,Int,;,},Class,Z,{,},<EOF>''',
                101
            )
        )

    def test_290(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9{}Class _:_{}Class v6:w9PH_s_{_(__8:Array [Array [Array [Int ,0124],0B1011011],0B1_11_01_10];_O9DM,_:Int ){} }''',
                '''Class,_9,{,},Class,_,:,_,{,},Class,v6,:,w9PH_s_,{,_,(,__8,:,Array,[,Array,[,Array,[,Int,,,0124,],,,0B1011011,],,,0B1110110,],;,_O9DM,,,_,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_291(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _H{hm_6(D,_,Hb:mY_j;_:Array [String ,57];la:Array [Float ,04];_H:Boolean ;M:Array [Array [String ,0X11],0x5];__,b5,E:Boolean ;__8_Q:Array [Array [String ,0b1],0xC];p4:Array [Array [Array [Float ,0xC],96_24_6_85],0B1_10_1]){} }''',
                '''Class,_H,{,hm_6,(,D,,,_,,,Hb,:,mY_j,;,_,:,Array,[,String,,,57,],;,la,:,Array,[,Float,,,04,],;,_H,:,Boolean,;,M,:,Array,[,Array,[,String,,,0X11,],,,0x5,],;,__,,,b5,,,E,:,Boolean,;,__8_Q,:,Array,[,Array,[,String,,,0b1,],,,0xC,],;,p4,:,Array,[,Array,[,Array,[,Float,,,0xC,],,,9624685,],,,0B1101,],),{,},},<EOF>''',
                101
            )
        )

    def test_292(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Ng55:D81r{_(W82:Int ;_4_:_0A;_:_){}Constructor (__:i;__q6:Array [String ,0126];_,_:Array [Array [Array [String ,0X63],0B1_1_01],0b1]){} }''',
                '''Class,Ng55,:,D81r,{,_,(,W82,:,Int,;,_4_,:,_0A,;,_,:,_,),{,},Constructor,(,__,:,i,;,__q6,:,Array,[,String,,,0126,],;,_,,,_,:,Array,[,Array,[,Array,[,String,,,0X63,],,,0B1101,],,,0b1,],),{,},},<EOF>''',
                101
            )
        )

    def test_293(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _q:_45{Destructor (){}Val _,zg,$k:String ;Destructor (){}Destructor (){} }Class NAS{$5(__:Boolean ;g8:_;_23,oJ_:_){} }''',
                '''Class,_q,:,_45,{,Destructor,(,),{,},Val,_,,,zg,,,$k,:,String,;,Destructor,(,),{,},Destructor,(,),{,},},Class,NAS,{,$5,(,__,:,Boolean,;,g8,:,_,;,_23,,,oJ_,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_294(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_x__{}Class q:_{_(o,_ZV:u4_;X_f2_,N,b5_v_:Zh_M_;__1,_:Float ;_,x:Int ){}Var $q8:Array [Array [Int ,0B1],38];Var $4_:_;Destructor (){ {} }}''',
                '''Class,_,:,_x__,{,},Class,q,:,_,{,_,(,o,,,_ZV,:,u4_,;,X_f2_,,,N,,,b5_v_,:,Zh_M_,;,__1,,,_,:,Float,;,_,,,x,:,Int,),{,},Var,$q8,:,Array,[,Array,[,Int,,,0B1,],,,38,],;,Var,$4_,:,_,;,Destructor,(,),{,{,},},},<EOF>''',
                101
            )
        )

    def test_295(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V:__{}Class _{}Class _3R43:b{$211T(x:Float ){}Var _X:_;Val $T,p2Z,$0,_,$_,_,$_5_3:_4;Destructor (){Break ;Continue ;} }''',
                '''Class,V,:,__,{,},Class,_,{,},Class,_3R43,:,b,{,$211T,(,x,:,Float,),{,},Var,_X,:,_,;,Val,$T,,,p2Z,,,$0,,,_,,,$_,,,_,,,$_5_3,:,_4,;,Destructor,(,),{,Break,;,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_296(self):
        self.assertTrue(
            TestLexer.test(
                '''Class K{}Class zP{Val $671D:Array [Array [Array [Array [Array [Array [Int ,0b1],074],92],0X2],0B11_01_11_1_1],074];}Class W{}''',
                '''Class,K,{,},Class,zP,{,Val,$671D,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0b1,],,,074,],,,92,],,,0X2,],,,0B11011111,],,,074,],;,},Class,W,{,},<EOF>''',
                101
            )
        )

    def test_297(self):
        self.assertTrue(
            TestLexer.test(
                '''Class c:q{Var $o:_;Var $_:Q__;}Class _:_{}Class _:f0_{Val $_:Array [Array [Array [Array [Array [Array [Float ,8_6],56],0X8_9E1_F_C_92_8_1],06],48],0x55];}''',
                '''Class,c,:,q,{,Var,$o,:,_,;,Var,$_,:,Q__,;,},Class,_,:,_,{,},Class,_,:,f0_,{,Val,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,86,],,,56,],,,0X89E1FC9281,],,,06,],,,48,],,,0x55,],;,},<EOF>''',
                101
            )
        )

    def test_298(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ld_k:M{Destructor (){}Var __,$dM7H4J_7:Array [Array [Float ,0x1A],0137];}Class F:_{Var $_:m_;Val V:Array [Int ,07];}Class C{}''',
                '''Class,ld_k,:,M,{,Destructor,(,),{,},Var,__,,,$dM7H4J_7,:,Array,[,Array,[,Float,,,0x1A,],,,0137,],;,},Class,F,:,_,{,Var,$_,:,m_,;,Val,V,:,Array,[,Int,,,07,],;,},Class,C,{,},<EOF>''',
                101
            )
        )

    def test_299(self):
        self.assertTrue(
            TestLexer.test(
                '''Class mN:__{_i(l_____:Array [Array [Float ,0x21],0XC2A];_j,A7:String ;_2:_;_,_c:Float ;_2,A,n_,_:_;_,q_,_,_:Array [Array [Array [Array [Float ,0b11010],8_6],0X61],06_0]){} }Class T_:_{}''',
                '''Class,mN,:,__,{,_i,(,l_____,:,Array,[,Array,[,Float,,,0x21,],,,0XC2A,],;,_j,,,A7,:,String,;,_2,:,_,;,_,,,_c,:,Float,;,_2,,,A,,,n_,,,_,:,_,;,_,,,q_,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0b11010,],,,86,],,,0X61,],,,060,],),{,},},Class,T_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_300(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _28:X_84{Var _4:Array [Array [Array [Array [Float ,0b10010],0B1101],0B1101],28];Destructor (){} }Class __Iv_7{}Class _:__{Constructor (){}_(e:String ){}_IsQ(){} }''',
                '''Class,_28,:,X_84,{,Var,_4,:,Array,[,Array,[,Array,[,Array,[,Float,,,0b10010,],,,0B1101,],,,0B1101,],,,28,],;,Destructor,(,),{,},},Class,__Iv_7,{,},Class,_,:,__,{,Constructor,(,),{,},_,(,e,:,String,),{,},_IsQ,(,),{,},},<EOF>''',
                101
            )
        )

    def test_301(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E_z:J{Val _0,_Ph06,$0:j;Constructor (R,g_:Array [Array [String ,0XC_A92_D_A],0X17]){}Destructor (){}Constructor (Z_,_:_;_,_:__){} }Class __7Y:R{}Class J_:_s__{Constructor (_,z:String ;t:String ;__4_:X){} }''',
                '''Class,E_z,:,J,{,Val,_0,,,_Ph06,,,$0,:,j,;,Constructor,(,R,,,g_,:,Array,[,Array,[,String,,,0XCA92DA,],,,0X17,],),{,},Destructor,(,),{,},Constructor,(,Z_,,,_,:,_,;,_,,,_,:,__,),{,},},Class,__7Y,:,R,{,},Class,J_,:,_s__,{,Constructor,(,_,,,z,:,String,;,t,:,String,;,__4_,:,X,),{,},},<EOF>''',
                101
            )
        )

    def test_302(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _3{Val c8,$_:_;Constructor (_:Array [Array [Float ,054],06];w70,_:_;D,_,z0,j:String ;_:Int ;n,_:Int ;m2,_,W_,_,Uyo:Array [Boolean ,054]){} }''',
                '''Class,_3,{,Val,c8,,,$_,:,_,;,Constructor,(,_,:,Array,[,Array,[,Float,,,054,],,,06,],;,w70,,,_,:,_,;,D,,,_,,,z0,,,j,:,String,;,_,:,Int,;,n,,,_,:,Int,;,m2,,,_,,,W_,,,_,,,Uyo,:,Array,[,Boolean,,,054,],),{,},},<EOF>''',
                101
            )
        )

    def test_303(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class X_H_8{}Class __1CO:_{}Class _:g{}Class Xn:__f{}Class __1:Q2{Constructor (B5_,_:_6;yH_3:U){}Constructor (r___u:Array [String ,0x7]){}Val $_:Array [Array [Int ,0b1],2_4];}''',
                '''Class,_,{,},Class,X_H_8,{,},Class,__1CO,:,_,{,},Class,_,:,g,{,},Class,Xn,:,__f,{,},Class,__1,:,Q2,{,Constructor,(,B5_,,,_,:,_6,;,yH_3,:,U,),{,},Constructor,(,r___u,:,Array,[,String,,,0x7,],),{,},Val,$_,:,Array,[,Array,[,Int,,,0b1,],,,24,],;,},<EOF>''',
                101
            )
        )

    def test_304(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g8:i{Constructor (__:V){Return ;}Var $_,P:Array [Boolean ,0xB_B];A6_(_:__u7;l3,q8h:Array [Boolean ,4];BS_,D,H5,m,hH:Array [Array [Boolean ,4],056];M_,g0_,e:Float ;R:hH;Q_:g_Q_;PZ__Zg8,y_,_6,u_:_3){}Constructor (kR:Int ){} }''',
                '''Class,g8,:,i,{,Constructor,(,__,:,V,),{,Return,;,},Var,$_,,,P,:,Array,[,Boolean,,,0xBB,],;,A6_,(,_,:,__u7,;,l3,,,q8h,:,Array,[,Boolean,,,4,],;,BS_,,,D,,,H5,,,m,,,hH,:,Array,[,Array,[,Boolean,,,4,],,,056,],;,M_,,,g0_,,,e,:,Float,;,R,:,hH,;,Q_,:,g_Q_,;,PZ__Zg8,,,y_,,,_6,,,u_,:,_3,),{,},Constructor,(,kR,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_305(self):
        self.assertTrue(
            TestLexer.test(
                '''Class M_9z2z{Constructor (__,l,W,_:Int ;Xa_,Sc6_,W:Int ;_,N_:q_;_:Array [Array [Array [Array [String ,47],0X4],47],04]){} }''',
                '''Class,M_9z2z,{,Constructor,(,__,,,l,,,W,,,_,:,Int,;,Xa_,,,Sc6_,,,W,:,Int,;,_,,,N_,:,q_,;,_,:,Array,[,Array,[,Array,[,Array,[,String,,,47,],,,0X4,],,,47,],,,04,],),{,},},<EOF>''',
                101
            )
        )

    def test_306(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __dM:h{Var $_:A;Constructor (___t:Boolean ){Val __Q:Array [Array [Array [Array [Int ,0x55],0B101001],83],0b10];} }Class Zi_8{Var $9:_;Destructor (){ {} }}''',
                '''Class,__dM,:,h,{,Var,$_,:,A,;,Constructor,(,___t,:,Boolean,),{,Val,__Q,:,Array,[,Array,[,Array,[,Array,[,Int,,,0x55,],,,0B101001,],,,83,],,,0b10,],;,},},Class,Zi_8,{,Var,$9,:,_,;,Destructor,(,),{,{,},},},<EOF>''',
                101
            )
        )

    def test_307(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P{Val _C:Float ;Constructor (__,o4:String ){}B(P4:Boolean ;l1,JF:_t;f,__7O:Float ;_H,_:Boolean ){Var _,dk8:Int ;} }''',
                '''Class,P,{,Val,_C,:,Float,;,Constructor,(,__,,,o4,:,String,),{,},B,(,P4,:,Boolean,;,l1,,,JF,:,_t,;,f,,,__7O,:,Float,;,_H,,,_,:,Boolean,),{,Var,_,,,dk8,:,Int,;,},},<EOF>''',
                101
            )
        )

    def test_308(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Destructor (){}Var g:G9;}Class _f:_R_{Var _,c,$_13__v1H_j,_:Array [String ,3];}Class X:G{Constructor (){} }Class x85R3{}''',
                '''Class,_,{,Destructor,(,),{,},Var,g,:,G9,;,},Class,_f,:,_R_,{,Var,_,,,c,,,$_13__v1H_j,,,_,:,Array,[,String,,,3,],;,},Class,X,:,G,{,Constructor,(,),{,},},Class,x85R3,{,},<EOF>''',
                101
            )
        )

    def test_309(self):
        self.assertTrue(
            TestLexer.test(
                '''Class S_:z4{Constructor (){}_5b0(u_8,qj7,dv,p:Array [Array [Float ,0B10],0X3];_A:Float ;_,y,Nw:Array [Boolean ,41];_jM,F29,_,Nx,__5H9__t:y6){}Constructor (){}B9(_,_:g){ {} }}''',
                '''Class,S_,:,z4,{,Constructor,(,),{,},_5b0,(,u_8,,,qj7,,,dv,,,p,:,Array,[,Array,[,Float,,,0B10,],,,0X3,],;,_A,:,Float,;,_,,,y,,,Nw,:,Array,[,Boolean,,,41,],;,_jM,,,F29,,,_,,,Nx,,,__5H9__t,:,y6,),{,},Constructor,(,),{,},B9,(,_,,,_,:,g,),{,{,},},},<EOF>''',
                101
            )
        )

    def test_310(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l:_{}Class T{Destructor (){ {} }Val _:r;$Se(){} }Class _{_1(v,_,w,_:Boolean ;_D,u:Array [Array [Int ,07],0xA_9]){} }Class _{}''',
                '''Class,l,:,_,{,},Class,T,{,Destructor,(,),{,{,},},Val,_,:,r,;,$Se,(,),{,},},Class,_,{,_1,(,v,,,_,,,w,,,_,:,Boolean,;,_D,,,u,:,Array,[,Array,[,Int,,,07,],,,0xA9,],),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_311(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P:J_9___{Val $j:d;Var m:Int ;}Class Qs{}Class _{}Class f:D{Constructor (l27S32:Int ;eC,_:v;l:_v4;__7q86:Array [String ,0b1010]){Continue ;{Var _2_E_Z:_;} }Val $Tb:D;}''',
                '''Class,P,:,J_9___,{,Val,$j,:,d,;,Var,m,:,Int,;,},Class,Qs,{,},Class,_,{,},Class,f,:,D,{,Constructor,(,l27S32,:,Int,;,eC,,,_,:,v,;,l,:,_v4,;,__7q86,:,Array,[,String,,,0b1010,],),{,Continue,;,{,Var,_2_E_Z,:,_,;,},},Val,$Tb,:,D,;,},<EOF>''',
                101
            )
        )

    def test_312(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:d_X8{Destructor (){} }Class _{Val O:s;}Class _{Destructor (){Continue ;} }Class q_{}Class _Z_0_:_{}Class _728R{}''',
                '''Class,_,:,d_X8,{,Destructor,(,),{,},},Class,_,{,Val,O,:,s,;,},Class,_,{,Destructor,(,),{,Continue,;,},},Class,q_,{,},Class,_Z_0_,:,_,{,},Class,_728R,{,},<EOF>''',
                101
            )
        )

    def test_313(self):
        self.assertTrue(
            TestLexer.test(
                '''Class UL{$2_(_,R:Array [Float ,0xE_E_95];_fO:v){Continue ;}Constructor (_g,L,_,__,x:Int ;_,X1,u,_38q,g:Array [Float ,0X40]){}Val $YX:Z6G;}Class J_4{}''',
                '''Class,UL,{,$2_,(,_,,,R,:,Array,[,Float,,,0xEE95,],;,_fO,:,v,),{,Continue,;,},Constructor,(,_g,,,L,,,_,,,__,,,x,:,Int,;,_,,,X1,,,u,,,_38q,,,g,:,Array,[,Float,,,0X40,],),{,},Val,$YX,:,Z6G,;,},Class,J_4,{,},<EOF>''',
                101
            )
        )

    def test_314(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _3Q3Y:_Do_{}Class _20:__{}Class _q9P:L{}Class Do{Constructor (_,__4,v,m0h,L:Array [Array [Float ,0142],0xED2_4DB]){} }Class Z:M{}Class i{Destructor (){} }''',
                '''Class,_3Q3Y,:,_Do_,{,},Class,_20,:,__,{,},Class,_q9P,:,L,{,},Class,Do,{,Constructor,(,_,,,__4,,,v,,,m0h,,,L,:,Array,[,Array,[,Float,,,0142,],,,0xED24DB,],),{,},},Class,Z,:,M,{,},Class,i,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_315(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _k6{}Class _V:_Ba100{Constructor (_,R_,_D,d3_,_6__,Q_,_:Float ){ {_::$3();} }}Class s32{}Class tP3:X{}Class QAS3:__402{Destructor (){}Destructor (){} }''',
                '''Class,_k6,{,},Class,_V,:,_Ba100,{,Constructor,(,_,,,R_,,,_D,,,d3_,,,_6__,,,Q_,,,_,:,Float,),{,{,_,::,$3,(,),;,},},},Class,s32,{,},Class,tP3,:,X,{,},Class,QAS3,:,__402,{,Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_316(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __2{}Class W{Constructor (){}_0(__,i:_;y,_,_5,f:Float ;Q9_,_2:String ){} }Class _3l:__{}Class _{Constructor (_2,sJ,N8,_:Int ){} }''',
                '''Class,__2,{,},Class,W,{,Constructor,(,),{,},_0,(,__,,,i,:,_,;,y,,,_,,,_5,,,f,:,Float,;,Q9_,,,_2,:,String,),{,},},Class,_3l,:,__,{,},Class,_,{,Constructor,(,_2,,,sJ,,,N8,,,_,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_317(self):
        self.assertTrue(
            TestLexer.test(
                '''Class R4:_{}Class c_l1a_{Constructor (){} }Class px{Constructor (){} }Class B:_{Val r4Qx:Array [Array [Int ,0XC_E_5],0B11011];}Class w{}''',
                '''Class,R4,:,_,{,},Class,c_l1a_,{,Constructor,(,),{,},},Class,px,{,Constructor,(,),{,},},Class,B,:,_,{,Val,r4Qx,:,Array,[,Array,[,Int,,,0XCE5,],,,0B11011,],;,},Class,w,{,},<EOF>''',
                101
            )
        )

    def test_318(self):
        self.assertTrue(
            TestLexer.test(
                '''Class B93:Jlv{Constructor (l_:Array [Array [Array [Array [Float ,0xC],0B11],31],62];S1,_:Array [Array [Float ,0xB],53];_Hey:l;w_,___:_){} }Class U_{}''',
                '''Class,B93,:,Jlv,{,Constructor,(,l_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0xC,],,,0B11,],,,31,],,,62,],;,S1,,,_,:,Array,[,Array,[,Float,,,0xB,],,,53,],;,_Hey,:,l,;,w_,,,___,:,_,),{,},},Class,U_,{,},<EOF>''',
                101
            )
        )

    def test_319(self):
        self.assertTrue(
            TestLexer.test(
                '''Class i:Tj{Var a4s,$q,$O3,I:Int ;}Class ____:_{}Class _5{Constructor (){} }Class e{}Class x2:Z{Var $_:Array [Float ,0X8];}''',
                '''Class,i,:,Tj,{,Var,a4s,,,$q,,,$O3,,,I,:,Int,;,},Class,____,:,_,{,},Class,_5,{,Constructor,(,),{,},},Class,e,{,},Class,x2,:,Z,{,Var,$_,:,Array,[,Float,,,0X8,],;,},<EOF>''',
                101
            )
        )

    def test_320(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C:_{$6G6(n,t:Array [Array [Array [Array [Array [Array [Int ,0x5],0B1_1],51],0B1011111],0X40],0X40];u:z;m_:_X){}Destructor (){} }''',
                '''Class,C,:,_,{,$6G6,(,n,,,t,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x5,],,,0B11,],,,51,],,,0B1011111,],,,0X40,],,,0X40,],;,u,:,z,;,m_,:,_X,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_321(self):
        self.assertTrue(
            TestLexer.test(
                '''Class D_9:__656{$c__(_:Array [Array [Int ,0B10111],0x14];___50:Array [String ,12];__,__J,kt,_i6_3,B2,_:Boolean ){Return ;} }''',
                '''Class,D_9,:,__656,{,$c__,(,_,:,Array,[,Array,[,Int,,,0B10111,],,,0x14,],;,___50,:,Array,[,String,,,12,],;,__,,,__J,,,kt,,,_i6_3,,,B2,,,_,:,Boolean,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_322(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_9_{Destructor (){} }Class _{Constructor (_:_;Q:O){ {}Continue ;}_Nm5(){Return ;}Val _m,$A,$m:_U4;Val $K,_,M,$R7,_1:C;}''',
                '''Class,_,:,_9_,{,Destructor,(,),{,},},Class,_,{,Constructor,(,_,:,_,;,Q,:,O,),{,{,},Continue,;,},_Nm5,(,),{,Return,;,},Val,_m,,,$A,,,$m,:,_U4,;,Val,$K,,,_,,,M,,,$R7,,,_1,:,C,;,},<EOF>''',
                101
            )
        )

    def test_323(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var $_,_:Float ;}Class i1{$f8oI7(_,O_,F,_:Array [Array [Array [Boolean ,0b1100000],06],0B101101]){}Var $8,$_45LK57:Float ;Destructor (){} }Class P{}''',
                '''Class,_,{,Var,$_,,,_,:,Float,;,},Class,i1,{,$f8oI7,(,_,,,O_,,,F,,,_,:,Array,[,Array,[,Array,[,Boolean,,,0b1100000,],,,06,],,,0B101101,],),{,},Var,$8,,,$_45LK57,:,Float,;,Destructor,(,),{,},},Class,P,{,},<EOF>''',
                101
            )
        )

    def test_324(self):
        self.assertTrue(
            TestLexer.test(
                '''Class F84l1i:_{}Class _:q{}Class U:d{$72(j,_,_,tO0:_;__,_:_;Kjt:Q){}$u(){} }Class __Y:_{Constructor (__:_0_){Return ;Return ;} }''',
                '''Class,F84l1i,:,_,{,},Class,_,:,q,{,},Class,U,:,d,{,$72,(,j,,,_,,,_,,,tO0,:,_,;,__,,,_,:,_,;,Kjt,:,Q,),{,},$u,(,),{,},},Class,__Y,:,_,{,Constructor,(,__,:,_0_,),{,Return,;,Return,;,},},<EOF>''',
                101
            )
        )

    def test_325(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class _43_fQ6:_{Val $__:Int ;Val o_:Array [String ,16_07];Val $n_1__:S6;Constructor (_,__9,Y:_){Val v_h,_,__:Float ;{}Continue ;}Destructor (){}Val _,_A,$oH72:_4;}''',
                '''Class,__,{,},Class,_43_fQ6,:,_,{,Val,$__,:,Int,;,Val,o_,:,Array,[,String,,,1607,],;,Val,$n_1__,:,S6,;,Constructor,(,_,,,__9,,,Y,:,_,),{,Val,v_h,,,_,,,__,:,Float,;,{,},Continue,;,},Destructor,(,),{,},Val,_,,,_A,,,$oH72,:,_4,;,},<EOF>''',
                101
            )
        )

    def test_326(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_V{Constructor (w6_h,W,d,N:Array [Int ,0X35];_,y_2__,W,_0,Cou:Float ){}_I8L_8W(){} }Class _6:_{}Class u9:_{}''',
                '''Class,_,:,_V,{,Constructor,(,w6_h,,,W,,,d,,,N,:,Array,[,Int,,,0X35,],;,_,,,y_2__,,,W,,,_0,,,Cou,:,Float,),{,},_I8L_8W,(,),{,},},Class,_6,:,_,{,},Class,u9,:,_,{,},<EOF>''',
                101
            )
        )

    def test_327(self):
        self.assertTrue(
            TestLexer.test(
                '''Class HX:I{}Class _J{}Class Ju:_{}Class _:_{Constructor (i:Array [Int ,61];c,_:Array [Array [Array [Boolean ,0X4],035],0135];_j:Array [Int ,0X34]){}Var $C_,_,$h:Float ;Val __B:ZD;Val P9,$_,p:Boolean ;}Class b{}''',
                '''Class,HX,:,I,{,},Class,_J,{,},Class,Ju,:,_,{,},Class,_,:,_,{,Constructor,(,i,:,Array,[,Int,,,61,],;,c,,,_,:,Array,[,Array,[,Array,[,Boolean,,,0X4,],,,035,],,,0135,],;,_j,:,Array,[,Int,,,0X34,],),{,},Var,$C_,,,_,,,$h,:,Float,;,Val,__B,:,ZD,;,Val,P9,,,$_,,,p,:,Boolean,;,},Class,b,{,},<EOF>''',
                101
            )
        )

    def test_328(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _P6_59V_{Destructor (){}Constructor (){}z_n01R(){Return ;J::$__16();Break ;Var l,I,_,_:Int ;}Var r:Boolean ;}Class wcN{}''',
                '''Class,_P6_59V_,{,Destructor,(,),{,},Constructor,(,),{,},z_n01R,(,),{,Return,;,J,::,$__16,(,),;,Break,;,Var,l,,,I,,,_,,,_,:,Int,;,},Var,r,:,Boolean,;,},Class,wcN,{,},<EOF>''',
                101
            )
        )

    def test_329(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:o_{Bu(){} }Class _{Constructor (){}Val bF:Array [Int ,0B1];}Class g5_{}Class B{}Class q4:A610_5_A{_(){Return ;} }''',
                '''Class,_,:,o_,{,Bu,(,),{,},},Class,_,{,Constructor,(,),{,},Val,bF,:,Array,[,Int,,,0B1,],;,},Class,g5_,{,},Class,B,{,},Class,q4,:,A610_5_A,{,_,(,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_330(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___J4__:H{}Class q:_6{}Class wvZ7{Var $0:Boolean ;}Class _:_{}Class _w{}Class _{Destructor (){} }Class e:L4t534{}''',
                '''Class,___J4__,:,H,{,},Class,q,:,_6,{,},Class,wvZ7,{,Var,$0,:,Boolean,;,},Class,_,:,_,{,},Class,_w,{,},Class,_,{,Destructor,(,),{,},},Class,e,:,L4t534,{,},<EOF>''',
                101
            )
        )

    def test_331(self):
        self.assertTrue(
            TestLexer.test(
                '''Class fg{}Class _:j{}Class Y{Var __:m;}Class j_{}Class _g{Destructor (){Val T:Array [Array [Array [Array [Array [String ,033],0b1000000],0x18],0B10010],0X4];{} }}''',
                '''Class,fg,{,},Class,_,:,j,{,},Class,Y,{,Var,__,:,m,;,},Class,j_,{,},Class,_g,{,Destructor,(,),{,Val,T,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,033,],,,0b1000000,],,,0x18,],,,0B10010,],,,0X4,],;,{,},},},<EOF>''',
                101
            )
        )

    def test_332(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o__:M_{Var $G,Ir,$_,$5_,R4,e2H:Array [Array [Boolean ,057],0XD_0];Constructor (dMp:k_9;_,Co__:Array [Array [Float ,0x7],0B10];_5,_B:Array [Array [Array [Array [Boolean ,070],7],0142],0142]){}Destructor (){} }''',
                '''Class,o__,:,M_,{,Var,$G,,,Ir,,,$_,,,$5_,,,R4,,,e2H,:,Array,[,Array,[,Boolean,,,057,],,,0XD0,],;,Constructor,(,dMp,:,k_9,;,_,,,Co__,:,Array,[,Array,[,Float,,,0x7,],,,0B10,],;,_5,,,_B,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,070,],,,7,],,,0142,],,,0142,],),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_333(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _23_{Constructor (SZ__d_,_,G43,__8,_Gu:Array [Boolean ,026]){}_(xF_,z7_5,cU:Int ;l_:Y425;c:Array [Int ,0B1]){ {} }}Class _0_{}Class W{}''',
                '''Class,_23_,{,Constructor,(,SZ__d_,,,_,,,G43,,,__8,,,_Gu,:,Array,[,Boolean,,,026,],),{,},_,(,xF_,,,z7_5,,,cU,:,Int,;,l_,:,Y425,;,c,:,Array,[,Int,,,0B1,],),{,{,},},},Class,_0_,{,},Class,W,{,},<EOF>''',
                101
            )
        )

    def test_334(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:_4_28{}Class _:_{}Class b:z_0Z9v{Constructor (_,T,__U,R_:_;L_:String ;_C:UGG_){Return ;} }Class _:_{Val $_9:Int ;}''',
                '''Class,__,:,_4_28,{,},Class,_,:,_,{,},Class,b,:,z_0Z9v,{,Constructor,(,_,,,T,,,__U,,,R_,:,_,;,L_,:,String,;,_C,:,UGG_,),{,Return,;,},},Class,_,:,_,{,Val,$_9,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_335(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _g:_Z4W{Z48j8(q,_6_,w__,_kCh:Array [String ,15];bRR:Array [String ,0b11111];_:Boolean ;___j:Array [Boolean ,04_3]){} }''',
                '''Class,_g,:,_Z4W,{,Z48j8,(,q,,,_6_,,,w__,,,_kCh,:,Array,[,String,,,15,],;,bRR,:,Array,[,String,,,0b11111,],;,_,:,Boolean,;,___j,:,Array,[,Boolean,,,043,],),{,},},<EOF>''',
                101
            )
        )

    def test_336(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Kk{}Class X:r{Constructor (_3m:Float ){}Var r,__:Array [Array [Array [Array [Array [Array [Boolean ,04],0b10_10],0x24],93],0b1011010],0b1_0_11_1];}Class g{}Class __Fy{Constructor (){} }''',
                '''Class,Kk,{,},Class,X,:,r,{,Constructor,(,_3m,:,Float,),{,},Var,r,,,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,04,],,,0b1010,],,,0x24,],,,93,],,,0b1011010,],,,0b10111,],;,},Class,g,{,},Class,__Fy,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_337(self):
        self.assertTrue(
            TestLexer.test(
                '''Class K:_k2_{Constructor (H,_53_qI0H6_p8_,z,_,sEY,_R3:j5;__:d;_y,C,V:Boolean ;__7_:r6;_L34:_q_){} }Class _:J{H(l5:Boolean ;s6_,__:Float ){Break ;_9_::$_u();} }''',
                '''Class,K,:,_k2_,{,Constructor,(,H,,,_53_qI0H6_p8_,,,z,,,_,,,sEY,,,_R3,:,j5,;,__,:,d,;,_y,,,C,,,V,:,Boolean,;,__7_,:,r6,;,_L34,:,_q_,),{,},},Class,_,:,J,{,H,(,l5,:,Boolean,;,s6_,,,__,:,Float,),{,Break,;,_9_,::,$_u,(,),;,},},<EOF>''',
                101
            )
        )

    def test_338(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class hH{Constructor (_,H,_,sb,_92I92_m,K:Boolean ;Uth:Boolean ;T_:Boolean ;_bF:_;_:String ){}Destructor (){} }Class _{}Class b:l__{}''',
                '''Class,_,{,},Class,hH,{,Constructor,(,_,,,H,,,_,,,sb,,,_92I92_m,,,K,:,Boolean,;,Uth,:,Boolean,;,T_,:,Boolean,;,_bF,:,_,;,_,:,String,),{,},Destructor,(,),{,},},Class,_,{,},Class,b,:,l__,{,},<EOF>''',
                101
            )
        )

    def test_339(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Aw__0{Constructor (_,_,_:Array [Array [Array [Array [String ,053],5_9_47_65],0B10],04];Qr7,_,__,___,j,_C_e02:Float ;__:Array [Boolean ,0x43_E]){}____V1A(){} }''',
                '''Class,Aw__0,{,Constructor,(,_,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,String,,,053,],,,594765,],,,0B10,],,,04,],;,Qr7,,,_,,,__,,,___,,,j,,,_C_e02,:,Float,;,__,:,Array,[,Boolean,,,0x43E,],),{,},____V1A,(,),{,},},<EOF>''',
                101
            )
        )

    def test_340(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class q:_D{Val $q8,$4,$_,Y:J;Destructor (){Var uOum,_:Array [Array [String ,05],54];} }Class __:_xR5V{}Class y:_{}''',
                '''Class,__,{,},Class,q,:,_D,{,Val,$q8,,,$4,,,$_,,,Y,:,J,;,Destructor,(,),{,Var,uOum,,,_,:,Array,[,Array,[,String,,,05,],,,54,],;,},},Class,__,:,_xR5V,{,},Class,y,:,_,{,},<EOF>''',
                101
            )
        )

    def test_341(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A8_72{Var $6:Array [Array [Array [Array [Array [Array [Array [Float ,030],030],0xEF_5_9],0x61],0B11],0b1011000],0b11_1_0];}''',
                '''Class,A8_72,{,Var,$6,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,030,],,,030,],,,0xEF59,],,,0x61,],,,0B11,],,,0b1011000,],,,0b1110,],;,},<EOF>''',
                101
            )
        )

    def test_342(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:tl{$k(I:_;z3X4:Array [Array [Array [Array [Array [String ,022_0_1_6_4],0b11010],59],67_3_3],59]){} }Class e1_:_BJ{}Class _{}''',
                '''Class,_,:,tl,{,$k,(,I,:,_,;,z3X4,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0220164,],,,0b11010,],,,59,],,,6733,],,,59,],),{,},},Class,e1_,:,_BJ,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_343(self):
        self.assertTrue(
            TestLexer.test(
                '''Class R{$4(_,A,_:Array [Array [Array [Boolean ,14],0x1_C_1_D],14];_Fl:Array [Array [Array [Array [Array [Float ,0b100001],14],0x61],0b100001],6];zj872,g2,_f_:j94;C:y_;AU3Q,_,_D,s7,Q,_:_D;_:D;_2,n0_Z64L,fY_w:K_;_8S_9:j__){} }''',
                '''Class,R,{,$4,(,_,,,A,,,_,:,Array,[,Array,[,Array,[,Boolean,,,14,],,,0x1C1D,],,,14,],;,_Fl,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b100001,],,,14,],,,0x61,],,,0b100001,],,,6,],;,zj872,,,g2,,,_f_,:,j94,;,C,:,y_,;,AU3Q,,,_,,,_D,,,s7,,,Q,,,_,:,_D,;,_,:,D,;,_2,,,n0_Z64L,,,fY_w,:,K_,;,_8S_9,:,j__,),{,},},<EOF>''',
                101
            )
        )

    def test_344(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var TC,$q_y,f,$_,a:Array [Array [Array [Array [Array [Array [Array [Boolean ,03],0x47],044],05],0b10],0X9_8_9_1],0b1_10];}''',
                '''Class,_,{,Var,TC,,,$q_y,,,f,,,$_,,,a,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,03,],,,0x47,],,,044,],,,05,],,,0b10,],,,0X9891,],,,0b110,],;,},<EOF>''',
                101
            )
        )

    def test_345(self):
        self.assertTrue(
            TestLexer.test(
                '''Class fHjv{Constructor (_:Array [Boolean ,1];_1,_:Float ;s:String ;dZb,w,_:_h_4_;_:EA;izO:Array [Boolean ,0X77]){Return ;} }Class M:M1{R_(){} }''',
                '''Class,fHjv,{,Constructor,(,_,:,Array,[,Boolean,,,1,],;,_1,,,_,:,Float,;,s,:,String,;,dZb,,,w,,,_,:,_h_4_,;,_,:,EA,;,izO,:,Array,[,Boolean,,,0X77,],),{,Return,;,},},Class,M,:,M1,{,R_,(,),{,},},<EOF>''',
                101
            )
        )

    def test_346(self):
        self.assertTrue(
            TestLexer.test(
                '''Class f:Y7S4l_{Constructor (_:Array [Array [Float ,0X1D],0x46];w,J:_4_;E:Array [Array [Array [Boolean ,0XB_352],056],0B1];l:Array [String ,0B111110];J,b,F:Boolean ;_:_;jJ:Array [Int ,0b1_1]){} }Class __{}''',
                '''Class,f,:,Y7S4l_,{,Constructor,(,_,:,Array,[,Array,[,Float,,,0X1D,],,,0x46,],;,w,,,J,:,_4_,;,E,:,Array,[,Array,[,Array,[,Boolean,,,0XB352,],,,056,],,,0B1,],;,l,:,Array,[,String,,,0B111110,],;,J,,,b,,,F,:,Boolean,;,_,:,_,;,jJ,:,Array,[,Int,,,0b11,],),{,},},Class,__,{,},<EOF>''',
                101
            )
        )

    def test_347(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___d:_{Val $7:Array [Array [Array [Array [Array [Array [Int ,6_9],0b1011010],14],0B10_0_110],0B11_1_011],14];Destructor (){ {Break ;}h9__::$U_();} }Class r:a{}Class hdXx:p_oG{}''',
                '''Class,___d,:,_,{,Val,$7,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,69,],,,0b1011010,],,,14,],,,0B100110,],,,0B111011,],,,14,],;,Destructor,(,),{,{,Break,;,},h9__,::,$U_,(,),;,},},Class,r,:,a,{,},Class,hdXx,:,p_oG,{,},<EOF>''',
                101
            )
        )

    def test_348(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Q_{r(__,m:J022){} }Class Vt{Constructor (){} }Class C:_{Destructor (){}h(F:Array [Array [Array [Array [Int ,02],0x10],0b10],64]){} }Class __:__{}''',
                '''Class,Q_,{,r,(,__,,,m,:,J022,),{,},},Class,Vt,{,Constructor,(,),{,},},Class,C,:,_,{,Destructor,(,),{,},h,(,F,:,Array,[,Array,[,Array,[,Array,[,Int,,,02,],,,0x10,],,,0b10,],,,64,],),{,},},Class,__,:,__,{,},<EOF>''',
                101
            )
        )

    def test_349(self):
        self.assertTrue(
            TestLexer.test(
                '''Class G6:m97{}Class g:_J{}Class _l8:_W{Val _2:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0X9],0x5],0126],1],0x9],0126],0126],7_9_4_1];_(){} }Class _{}Class K3{}''',
                '''Class,G6,:,m97,{,},Class,g,:,_J,{,},Class,_l8,:,_W,{,Val,_2,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X9,],,,0x5,],,,0126,],,,1,],,,0x9,],,,0126,],,,0126,],,,7941,],;,_,(,),{,},},Class,_,{,},Class,K3,{,},<EOF>''',
                101
            )
        )

    def test_350(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:__{Destructor (){Break ;}$__f_(___1:U){Break ;}Constructor (){} }Class y{Var H_4:Array [Array [Array [Boolean ,91],0xB],0655_6];}Class ___{Var X5:_;}''',
                '''Class,_,:,__,{,Destructor,(,),{,Break,;,},$__f_,(,___1,:,U,),{,Break,;,},Constructor,(,),{,},},Class,y,{,Var,H_4,:,Array,[,Array,[,Array,[,Boolean,,,91,],,,0xB,],,,06556,],;,},Class,___,{,Var,X5,:,_,;,},<EOF>''',
                101
            )
        )

    def test_351(self):
        self.assertTrue(
            TestLexer.test(
                '''Class h:Z{}Class _9:w{Var $1__4__,_,$8:_;}Class f_7:_{Constructor (){}Constructor (){} }Class VVUP{}Class n:_{}''',
                '''Class,h,:,Z,{,},Class,_9,:,w,{,Var,$1__4__,,,_,,,$8,:,_,;,},Class,f_7,:,_,{,Constructor,(,),{,},Constructor,(,),{,},},Class,VVUP,{,},Class,n,:,_,{,},<EOF>''',
                101
            )
        )

    def test_352(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Z:d{Destructor (){}Destructor (){} }Class _1{Val $A__0_,$_,__,_:Float ;Var I_,$8,U,_L:Array [String ,0xF_5_09];Constructor (){Break ;} }Class dW0{}Class w:b{y_6_(){L::$H.O_4_2658_().Lu();} }''',
                '''Class,Z,:,d,{,Destructor,(,),{,},Destructor,(,),{,},},Class,_1,{,Val,$A__0_,,,$_,,,__,,,_,:,Float,;,Var,I_,,,$8,,,U,,,_L,:,Array,[,String,,,0xF509,],;,Constructor,(,),{,Break,;,},},Class,dW0,{,},Class,w,:,b,{,y_6_,(,),{,L,::,$H,.,O_4_2658_,(,),.,Lu,(,),;,},},<EOF>''',
                101
            )
        )

    def test_353(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _6:V_{_(){} }Class _j:_A{Constructor (A:String ){}Constructor (nM___:Array [Array [Array [Array [Array [Boolean ,45],0127],0b1],05_175_0],0b1];_,z,_:Array [Array [Int ,0B1110],02_0_2];C:Array [Array [Array [Array [String ,0b1010011],0B1],0b1_00],0127]){}Val $J:V;}Class _{Var $3M,u:__G;Destructor (){} }Class _:C{}Class I{}''',
                '''Class,_6,:,V_,{,_,(,),{,},},Class,_j,:,_A,{,Constructor,(,A,:,String,),{,},Constructor,(,nM___,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,45,],,,0127,],,,0b1,],,,051750,],,,0b1,],;,_,,,z,,,_,:,Array,[,Array,[,Int,,,0B1110,],,,0202,],;,C,:,Array,[,Array,[,Array,[,Array,[,String,,,0b1010011,],,,0B1,],,,0b100,],,,0127,],),{,},Val,$J,:,V,;,},Class,_,{,Var,$3M,,,u,:,__G,;,Destructor,(,),{,},},Class,_,:,C,{,},Class,I,{,},<EOF>''',
                101
            )
        )

    def test_354(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C6S{$3FX(_G,bML,s:Int ;K:Array [Array [Array [Array [Array [Array [Float ,0x57],0x57],05],03],0B1000001],0x8]){} }Class _:Wp_{}''',
                '''Class,C6S,{,$3FX,(,_G,,,bML,,,s,:,Int,;,K,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x57,],,,0x57,],,,05,],,,03,],,,0B1000001,],,,0x8,],),{,},},Class,_,:,Wp_,{,},<EOF>''',
                101
            )
        )

    def test_355(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __yx_:V_C{O(_2O3:Array [String ,0b1001001]){Return ;}Constructor (_I,K,_,_,_:Array [Array [Array [Array [Array [Float ,06],01_21_6_4],0x4E],0X25],0b1_0]){Y::$_();} }''',
                '''Class,__yx_,:,V_C,{,O,(,_2O3,:,Array,[,String,,,0b1001001,],),{,Return,;,},Constructor,(,_I,,,K,,,_,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,06,],,,012164,],,,0x4E,],,,0X25,],,,0b10,],),{,Y,::,$_,(,),;,},},<EOF>''',
                101
            )
        )

    def test_356(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ycm__:n{Val $e5__zk,$9_M3__,u:Array [Array [Array [Array [Array [String ,36],0127],0b1_1],0x19],0B1_1_1];}Class T:_{}Class _Z:_{Constructor (C50,e,h_:Array [Array [Array [String ,0xE],0x19],4]){} }''',
                '''Class,ycm__,:,n,{,Val,$e5__zk,,,$9_M3__,,,u,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,36,],,,0127,],,,0b11,],,,0x19,],,,0B111,],;,},Class,T,:,_,{,},Class,_Z,:,_,{,Constructor,(,C50,,,e,,,h_,:,Array,[,Array,[,Array,[,String,,,0xE,],,,0x19,],,,4,],),{,},},<EOF>''',
                101
            )
        )

    def test_357(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m:s_W3_{Var o,$_:_x;Var s:Array [Array [Int ,4_4],0xB_A];}Class j:C{Val _3,k9,o__,$9x:Boolean ;Constructor (){Return ;}Val _:Float ;}Class r_0_:_3004{}''',
                '''Class,m,:,s_W3_,{,Var,o,,,$_,:,_x,;,Var,s,:,Array,[,Array,[,Int,,,44,],,,0xBA,],;,},Class,j,:,C,{,Val,_3,,,k9,,,o__,,,$9x,:,Boolean,;,Constructor,(,),{,Return,;,},Val,_,:,Float,;,},Class,r_0_,:,_3004,{,},<EOF>''',
                101
            )
        )

    def test_358(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _03_{Constructor (_Qz,_H,PDlX_Q8:_){}Constructor (u:__){}$_(){}Destructor (){}Destructor (){} }''',
                '''Class,_,{,},Class,_03_,{,Constructor,(,_Qz,,,_H,,,PDlX_Q8,:,_,),{,},Constructor,(,u,:,__,),{,},$_,(,),{,},Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_359(self):
        self.assertTrue(
            TestLexer.test(
                '''Class c6{}Class _{Constructor (n:_;___W,__:l_0;F,L_:Float ;_:_;_w,_,__:Array [Array [String ,0x57],0X22F2_D5]){}Var _A1:Array [Array [Array [Float ,0B101011],0B1],0B11_1_00];}''',
                '''Class,c6,{,},Class,_,{,Constructor,(,n,:,_,;,___W,,,__,:,l_0,;,F,,,L_,:,Float,;,_,:,_,;,_w,,,_,,,__,:,Array,[,Array,[,String,,,0x57,],,,0X22F2D5,],),{,},Var,_A1,:,Array,[,Array,[,Array,[,Float,,,0B101011,],,,0B1,],,,0B11100,],;,},<EOF>''',
                101
            )
        )

    def test_360(self):
        self.assertTrue(
            TestLexer.test(
                '''Class v:_{Destructor (){Continue ;Break ;}Var j:Array [String ,44];}Class __:_{Constructor (s0q3,__,_,_,Su,t_s,_,_:Array [Array [Array [String ,0B100101],9_926_0],0B11];e5__,_,__8c:_2d_1__j){} }Class _{}''',
                '''Class,v,:,_,{,Destructor,(,),{,Continue,;,Break,;,},Var,j,:,Array,[,String,,,44,],;,},Class,__,:,_,{,Constructor,(,s0q3,,,__,,,_,,,_,,,Su,,,t_s,,,_,,,_,:,Array,[,Array,[,Array,[,String,,,0B100101,],,,99260,],,,0B11,],;,e5__,,,_,,,__8c,:,_2d_1__j,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_361(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Constructor (_,W7____Ra,E,___1:u__;b,_:_;___l:_vg){} }Class Z:_K_th{Destructor (){}Val S9,$3,$__P0:Int ;Destructor (){Break ;} }''',
                '''Class,_,:,_,{,Constructor,(,_,,,W7____Ra,,,E,,,___1,:,u__,;,b,,,_,:,_,;,___l,:,_vg,),{,},},Class,Z,:,_K_th,{,Destructor,(,),{,},Val,S9,,,$3,,,$__P0,:,Int,;,Destructor,(,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_362(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Rr{}Class _{Constructor (){} }Class _{$_(_,J,_81:Array [String ,0B1];e__,_,__81G9:Boolean ;w_z,_:Array [Boolean ,04_436]){} }Class E{}''',
                '''Class,Rr,{,},Class,_,{,Constructor,(,),{,},},Class,_,{,$_,(,_,,,J,,,_81,:,Array,[,String,,,0B1,],;,e__,,,_,,,__81G9,:,Boolean,;,w_z,,,_,:,Array,[,Boolean,,,04436,],),{,},},Class,E,{,},<EOF>''',
                101
            )
        )

    def test_363(self):
        self.assertTrue(
            TestLexer.test(
                '''Class WE_6:_w{Destructor (){}Var d:_;Val Fc:Boolean ;Val W_:Array [Array [String ,0b1100100],062];p(d,___6:Boolean ){} }Class _:x_{}''',
                '''Class,WE_6,:,_w,{,Destructor,(,),{,},Var,d,:,_,;,Val,Fc,:,Boolean,;,Val,W_,:,Array,[,Array,[,String,,,0b1100100,],,,062,],;,p,(,d,,,___6,:,Boolean,),{,},},Class,_,:,x_,{,},<EOF>''',
                101
            )
        )

    def test_364(self):
        self.assertTrue(
            TestLexer.test(
                '''Class d742{Constructor (_,_,_:Boolean ;d:Array [Int ,0x3F]){ {} }Destructor (){Return ;Break ;} }Class p:_{Var $3:_;}Class _{Var _,$V_l6X_Z,$3T:__R1;}''',
                '''Class,d742,{,Constructor,(,_,,,_,,,_,:,Boolean,;,d,:,Array,[,Int,,,0x3F,],),{,{,},},Destructor,(,),{,Return,;,Break,;,},},Class,p,:,_,{,Var,$3,:,_,;,},Class,_,{,Var,_,,,$V_l6X_Z,,,$3T,:,__R1,;,},<EOF>''',
                101
            )
        )

    def test_365(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _:_{}Class _:y{}Class jc9{Val $V:B2;}Class _{Constructor (){}Constructor (h,Ic_:String ){Continue ;} }''',
                '''Class,_,{,},Class,_,:,_,{,},Class,_,:,y,{,},Class,jc9,{,Val,$V,:,B2,;,},Class,_,{,Constructor,(,),{,},Constructor,(,h,,,Ic_,:,String,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_366(self):
        self.assertTrue(
            TestLexer.test(
                '''Class F1{$a(){Var _0:Array [Boolean ,0110];Var R5:Array [Array [Float ,0B1000111],0110];} }Class __4_{Val _,_U9,_,_:_;}Class N_yeF17tc{Constructor (){}Var $__,w,_8:_;}''',
                '''Class,F1,{,$a,(,),{,Var,_0,:,Array,[,Boolean,,,0110,],;,Var,R5,:,Array,[,Array,[,Float,,,0B1000111,],,,0110,],;,},},Class,__4_,{,Val,_,,,_U9,,,_,,,_,:,_,;,},Class,N_yeF17tc,{,Constructor,(,),{,},Var,$__,,,w,,,_8,:,_,;,},<EOF>''',
                101
            )
        )

    def test_367(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val _q_,h,$q_:Array [Float ,0b1011];}Class e{}Class _:_{}Class f_g_8_120_{}Class R{$8(){}Constructor (){}Val $_:Array [Array [Int ,0b1],0xA1_8];}''',
                '''Class,_,{,Val,_q_,,,h,,,$q_,:,Array,[,Float,,,0b1011,],;,},Class,e,{,},Class,_,:,_,{,},Class,f_g_8_120_,{,},Class,R,{,$8,(,),{,},Constructor,(,),{,},Val,$_,:,Array,[,Array,[,Int,,,0b1,],,,0xA18,],;,},<EOF>''',
                101
            )
        )

    def test_368(self):
        self.assertTrue(
            TestLexer.test(
                '''Class U{Var g:Array [Float ,0x4_E5_56];Constructor (kR:Array [Int ,0b1011001];E,__F:_){}Var $_z:Float ;Var $ZC__m,$0_,ibH:Array [Array [Array [Boolean ,0B110010],0b1],0B1];}Class __:_17__{}''',
                '''Class,U,{,Var,g,:,Array,[,Float,,,0x4E556,],;,Constructor,(,kR,:,Array,[,Int,,,0b1011001,],;,E,,,__F,:,_,),{,},Var,$_z,:,Float,;,Var,$ZC__m,,,$0_,,,ibH,:,Array,[,Array,[,Array,[,Boolean,,,0B110010,],,,0b1,],,,0B1,],;,},Class,__,:,_17__,{,},<EOF>''',
                101
            )
        )

    def test_369(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_D_{}Class __855:_{Constructor (x:String ;_,F,t:Array [Float ,0xA]){Var V:Float ;}Destructor (){}$9(V:String ;E:Array [Boolean ,013]){Var c3,W:Int ;} }''',
                '''Class,_,:,_D_,{,},Class,__855,:,_,{,Constructor,(,x,:,String,;,_,,,F,,,t,:,Array,[,Float,,,0xA,],),{,Var,V,:,Float,;,},Destructor,(,),{,},$9,(,V,:,String,;,E,:,Array,[,Boolean,,,013,],),{,Var,c3,,,W,:,Int,;,},},<EOF>''',
                101
            )
        )

    def test_370(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _A_0n:_{Destructor (){}I(_g:Array [Array [Array [Float ,03],0b1_1],1];_5:Array [Array [Float ,11_3_3_3],0X7];D_b,_71,V,_,I_m_:Int ){} }''',
                '''Class,_A_0n,:,_,{,Destructor,(,),{,},I,(,_g,:,Array,[,Array,[,Array,[,Float,,,03,],,,0b11,],,,1,],;,_5,:,Array,[,Array,[,Float,,,11333,],,,0X7,],;,D_b,,,_71,,,V,,,_,,,I_m_,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_371(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0{Constructor (_v3_F3Z0:Array [Array [Array [Array [Int ,04],31],0B100110],0B100110];VAD,h,_:Wl4o;M2:Array [Array [Float ,0x3D],0X25]){} }''',
                '''Class,_0,{,Constructor,(,_v3_F3Z0,:,Array,[,Array,[,Array,[,Array,[,Int,,,04,],,,31,],,,0B100110,],,,0B100110,],;,VAD,,,h,,,_,:,Wl4o,;,M2,:,Array,[,Array,[,Float,,,0x3D,],,,0X25,],),{,},},<EOF>''',
                101
            )
        )

    def test_372(self):
        self.assertTrue(
            TestLexer.test(
                '''Class x4:u{Var $_41,_7_,$t,$4,$H4_:Array [Array [Array [Array [Array [Float ,06],67],67],0XF],0B1000010];}Class _:Hn{}''',
                '''Class,x4,:,u,{,Var,$_41,,,_7_,,,$t,,,$4,,,$H4_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,06,],,,67,],,,67,],,,0XF,],,,0B1000010,],;,},Class,_,:,Hn,{,},<EOF>''',
                101
            )
        )

    def test_373(self):
        self.assertTrue(
            TestLexer.test(
                '''Class F_1:_{_22(_:Ro8;_3Q,_,C_,__:Array [Array [Array [String ,0x83],0X43],0X43]){}Var $_78_,$3_:nKo;}Class X:_s{Val _:We927;}''',
                '''Class,F_1,:,_,{,_22,(,_,:,Ro8,;,_3Q,,,_,,,C_,,,__,:,Array,[,Array,[,Array,[,String,,,0x83,],,,0X43,],,,0X43,],),{,},Var,$_78_,,,$3_,:,nKo,;,},Class,X,:,_s,{,Val,_,:,We927,;,},<EOF>''',
                101
            )
        )

    def test_374(self):
        self.assertTrue(
            TestLexer.test(
                '''Class K{Val $3_:Boolean ;}Class _g:S4{Constructor (_,X:_;u:Array [Boolean ,0x17];_:Float ;z:Array [Boolean ,9];_,k7:Int ){}Constructor (T_7:String ){}Destructor (){} }''',
                '''Class,K,{,Val,$3_,:,Boolean,;,},Class,_g,:,S4,{,Constructor,(,_,,,X,:,_,;,u,:,Array,[,Boolean,,,0x17,],;,_,:,Float,;,z,:,Array,[,Boolean,,,9,],;,_,,,k7,:,Int,),{,},Constructor,(,T_7,:,String,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_375(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y{Constructor (_:Array [Array [String ,0b1011000],040];_,r,E,F,_,__:Es;C:Array [Int ,040]){}Var $_03w:Array [Boolean ,0b100];Constructor (){}Destructor (){} }''',
                '''Class,y,{,Constructor,(,_,:,Array,[,Array,[,String,,,0b1011000,],,,040,],;,_,,,r,,,E,,,F,,,_,,,__,:,Es,;,C,:,Array,[,Int,,,040,],),{,},Var,$_03w,:,Array,[,Boolean,,,0b100,],;,Constructor,(,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_376(self):
        self.assertTrue(
            TestLexer.test(
                '''Class K_13__n3R9oz{Constructor (G,i,Ru,G_C_7_:Array [Array [Int ,0xF],0XD]){Return ;} }Class __y:_{}Class _5_:A3{}''',
                '''Class,K_13__n3R9oz,{,Constructor,(,G,,,i,,,Ru,,,G_C_7_,:,Array,[,Array,[,Int,,,0xF,],,,0XD,],),{,Return,;,},},Class,__y,:,_,{,},Class,_5_,:,A3,{,},<EOF>''',
                101
            )
        )

    def test_377(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g{Val _y8_6,$D4__4_:_L;}Class l5_{}Class f{}Class D:R7{Var e9:Int ;Var $_:_;}Class _0{}Class _:_{}Class _{}Class G_:__5y{}''',
                '''Class,g,{,Val,_y8_6,,,$D4__4_,:,_L,;,},Class,l5_,{,},Class,f,{,},Class,D,:,R7,{,Var,e9,:,Int,;,Var,$_,:,_,;,},Class,_0,{,},Class,_,:,_,{,},Class,_,{,},Class,G_,:,__5y,{,},<EOF>''',
                101
            )
        )

    def test_378(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:g{}Class m_{Constructor (yZ,_,_626:Array [Array [Float ,023],0B1]){} }Class n{}Class QS{Val t,$l8jq_:Array [Array [String ,0xE],3];}''',
                '''Class,_,:,g,{,},Class,m_,{,Constructor,(,yZ,,,_,,,_626,:,Array,[,Array,[,Float,,,023,],,,0B1,],),{,},},Class,n,{,},Class,QS,{,Val,t,,,$l8jq_,:,Array,[,Array,[,String,,,0xE,],,,3,],;,},<EOF>''',
                101
            )
        )

    def test_379(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y_:_{B(__:_Jd_l;M4:_6w;_,c_8:Array [Boolean ,0106];_:Array [Array [Array [Array [Float ,07],0B1000010],06],04]){}Constructor (_AZc1:Array [Int ,0x46];T708:_E;q,h:xO;o:Int ;_,_k_,_,f:Array [Array [Array [Array [Int ,05_4],0106],060],03];b,L:Float ){}Val __4:_x;Constructor (){Continue ;} }Class QY:Gd6{}Class _{Val _:Boolean ;Constructor (){} }''',
                '''Class,y_,:,_,{,B,(,__,:,_Jd_l,;,M4,:,_6w,;,_,,,c_8,:,Array,[,Boolean,,,0106,],;,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,07,],,,0B1000010,],,,06,],,,04,],),{,},Constructor,(,_AZc1,:,Array,[,Int,,,0x46,],;,T708,:,_E,;,q,,,h,:,xO,;,o,:,Int,;,_,,,_k_,,,_,,,f,:,Array,[,Array,[,Array,[,Array,[,Int,,,054,],,,0106,],,,060,],,,03,],;,b,,,L,:,Float,),{,},Val,__4,:,_x,;,Constructor,(,),{,Continue,;,},},Class,QY,:,Gd6,{,},Class,_,{,Val,_,:,Boolean,;,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_380(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t:V{Val _:_;Var $62430,_9,$__:Int ;Val $8I7,_,$_p9__T,$9:Array [Int ,03];$Y(){}Val $4i1_,b:String ;}Class Yj{}''',
                '''Class,t,:,V,{,Val,_,:,_,;,Var,$62430,,,_9,,,$__,:,Int,;,Val,$8I7,,,_,,,$_p9__T,,,$9,:,Array,[,Int,,,03,],;,$Y,(,),{,},Val,$4i1_,,,b,:,String,;,},Class,Yj,{,},<EOF>''',
                101
            )
        )

    def test_381(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{_(_9x,V_:Array [Array [Array [Float ,0x48],0B1],0X44]){Return ;} }Class af{Destructor (){} }Class _{Var Fv4,_,_8:Int ;}''',
                '''Class,_,{,_,(,_9x,,,V_,:,Array,[,Array,[,Array,[,Float,,,0x48,],,,0B1,],,,0X44,],),{,Return,;,},},Class,af,{,Destructor,(,),{,},},Class,_,{,Var,Fv4,,,_,,,_8,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_382(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m{}Class _y{Var v_4,$_3,_,$_,_,__h6:Array [Array [Array [Array [Int ,07],24],24],1];}Class __:___T{}Class _{Destructor (){_j::$_48()._();} }''',
                '''Class,m,{,},Class,_y,{,Var,v_4,,,$_3,,,_,,,$_,,,_,,,__h6,:,Array,[,Array,[,Array,[,Array,[,Int,,,07,],,,24,],,,24,],,,1,],;,},Class,__,:,___T,{,},Class,_,{,Destructor,(,),{,_j,::,$_48,(,),.,_,(,),;,},},<EOF>''',
                101
            )
        )

    def test_383(self):
        self.assertTrue(
            TestLexer.test(
                '''Class R__{$6_MhA_(_:Array [Array [Array [Array [String ,01_3],4],07],24]){Break ;lut3t::$_();} }Class __{Destructor (){} }Class _:l3{}''',
                '''Class,R__,{,$6_MhA_,(,_,:,Array,[,Array,[,Array,[,Array,[,String,,,013,],,,4,],,,07,],,,24,],),{,Break,;,lut3t,::,$_,(,),;,},},Class,__,{,Destructor,(,),{,},},Class,_,:,l3,{,},<EOF>''',
                101
            )
        )

    def test_384(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _{Destructor (){}Var d__4:Array [Int ,0B1011];Var $t,_:j;}Class _:F0{_(xUN,_,hG:Array [Array [Array [Array [String ,0X28],011],011],0b1000011]){} }''',
                '''Class,_,{,},Class,_,{,Destructor,(,),{,},Var,d__4,:,Array,[,Int,,,0B1011,],;,Var,$t,,,_,:,j,;,},Class,_,:,F0,{,_,(,xUN,,,_,,,hG,:,Array,[,Array,[,Array,[,Array,[,String,,,0X28,],,,011,],,,011,],,,0b1000011,],),{,},},<EOF>''',
                101
            )
        )

    def test_385(self):
        self.assertTrue(
            TestLexer.test(
                '''Class r:z3_{$P(____,__3_:Float ;_,A:J;_:Boolean ;T:Boolean ;__0E,h_,_Ijc,Q:D){}Destructor (){} }Class _:_{}Class _2_S:_{Destructor (){Return ;} }Class n:_{Var _37_:c;}''',
                '''Class,r,:,z3_,{,$P,(,____,,,__3_,:,Float,;,_,,,A,:,J,;,_,:,Boolean,;,T,:,Boolean,;,__0E,,,h_,,,_Ijc,,,Q,:,D,),{,},Destructor,(,),{,},},Class,_,:,_,{,},Class,_2_S,:,_,{,Destructor,(,),{,Return,;,},},Class,n,:,_,{,Var,_37_,:,c,;,},<EOF>''',
                101
            )
        )

    def test_386(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J__{$_(rl__:Array [Array [Float ,27],56_66];W,_K:Array [Boolean ,032];_,c,R_84f9,_:Boolean ){}Constructor (k_82,V4,_67:Array [Array [Array [Array [Boolean ,0x7],6],33],27];__,_J,M_7_O,_Q:Int ;_:Float ){} }Class Q0W{}''',
                '''Class,J__,{,$_,(,rl__,:,Array,[,Array,[,Float,,,27,],,,5666,],;,W,,,_K,:,Array,[,Boolean,,,032,],;,_,,,c,,,R_84f9,,,_,:,Boolean,),{,},Constructor,(,k_82,,,V4,,,_67,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x7,],,,6,],,,33,],,,27,],;,__,,,_J,,,M_7_O,,,_Q,:,Int,;,_,:,Float,),{,},},Class,Q0W,{,},<EOF>''',
                101
            )
        )

    def test_387(self):
        self.assertTrue(
            TestLexer.test(
                '''Class U{Val $L,____,_40,$1_:Array [Array [Boolean ,0B10],0b11];Destructor (){Continue ;}Destructor (){}Var _2G_:Array [Array [Boolean ,63],0xC_CC];Val $8:Int ;Constructor (w_:String ){} }''',
                '''Class,U,{,Val,$L,,,____,,,_40,,,$1_,:,Array,[,Array,[,Boolean,,,0B10,],,,0b11,],;,Destructor,(,),{,Continue,;,},Destructor,(,),{,},Var,_2G_,:,Array,[,Array,[,Boolean,,,63,],,,0xCCC,],;,Val,$8,:,Int,;,Constructor,(,w_,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_388(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y:_{Destructor (){}Val _,$_i_,_z_V6,_,$5,$3,$_:_;}Class __x{}Class _{}Class H_{Destructor (){}$_Y(){} }''',
                '''Class,y,:,_,{,Destructor,(,),{,},Val,_,,,$_i_,,,_z_V6,,,_,,,$5,,,$3,,,$_,:,_,;,},Class,__x,{,},Class,_,{,},Class,H_,{,Destructor,(,),{,},$_Y,(,),{,},},<EOF>''',
                101
            )
        )

    def test_389(self):
        self.assertTrue(
            TestLexer.test(
                '''Class W{Val _:Array [Int ,93];Constructor (w_,p_4C4,i:Array [Array [Array [Float ,0X8],0xF2_20],93]){ {Continue ;} }}Class z:_{Var $U,$0:dG;Var I__0,$8_10_u,_2s,_:Float ;Val dP__,$_i:Array [Array [Array [Array [Int ,93],93],93],05];}''',
                '''Class,W,{,Val,_,:,Array,[,Int,,,93,],;,Constructor,(,w_,,,p_4C4,,,i,:,Array,[,Array,[,Array,[,Float,,,0X8,],,,0xF220,],,,93,],),{,{,Continue,;,},},},Class,z,:,_,{,Var,$U,,,$0,:,dG,;,Var,I__0,,,$8_10_u,,,_2s,,,_,:,Float,;,Val,dP__,,,$_i,:,Array,[,Array,[,Array,[,Array,[,Int,,,93,],,,93,],,,93,],,,05,],;,},<EOF>''',
                101
            )
        )

    def test_390(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (z,HN6,p:String ;p2,_:Array [String ,0x5A];__,__,m_,_,_8__:Int ){}Var $5:Array [String ,0b110110];}Class _:q_K{Val $QM,$__:Boolean ;Destructor (){} }''',
                '''Class,_,{,Constructor,(,z,,,HN6,,,p,:,String,;,p2,,,_,:,Array,[,String,,,0x5A,],;,__,,,__,,,m_,,,_,,,_8__,:,Int,),{,},Var,$5,:,Array,[,String,,,0b110110,],;,},Class,_,:,q_K,{,Val,$QM,,,$__,:,Boolean,;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_391(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _5{m(X,_Lv9I_q_,_:Int ;_9z,_g,ad7Kr:Array [Boolean ,0B10000];h_F_:Array [String ,31_8]){} }Class _{Var $0,_9A_,$A:Array [Array [Array [Array [Boolean ,8],0xC],0B1010110],0XC];}''',
                '''Class,_5,{,m,(,X,,,_Lv9I_q_,,,_,:,Int,;,_9z,,,_g,,,ad7Kr,:,Array,[,Boolean,,,0B10000,],;,h_F_,:,Array,[,String,,,318,],),{,},},Class,_,{,Var,$0,,,_9A_,,,$A,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,8,],,,0xC,],,,0B1010110,],,,0XC,],;,},<EOF>''',
                101
            )
        )

    def test_392(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V:_3{}Class S{e7(X_S,_:Array [Float ,95]){} }Class Y1___{Var b:Int ;$v(_p3T:W_){Continue ;z_8_::$_().T_a.AE.__D();} }''',
                '''Class,V,:,_3,{,},Class,S,{,e7,(,X_S,,,_,:,Array,[,Float,,,95,],),{,},},Class,Y1___,{,Var,b,:,Int,;,$v,(,_p3T,:,W_,),{,Continue,;,z_8_,::,$_,(,),.,T_a,.,AE,.,__D,(,),;,},},<EOF>''',
                101
            )
        )

    def test_393(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y{}Class _:_17jO{Var I,Is9,_n,$61_:Array [Array [String ,0x37],0X27];}Class P:E{Destructor (){}Destructor (){} }''',
                '''Class,y,{,},Class,_,:,_17jO,{,Var,I,,,Is9,,,_n,,,$61_,:,Array,[,Array,[,String,,,0x37,],,,0X27,],;,},Class,P,:,E,{,Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_394(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E:_{}Class f_L{}Class z__:_2{Val $__:_;Var _,$2,T:Array [Int ,0x6];}Class _a3__{Constructor (_:Array [Array [Float ,021],05_5];_:_y){} }''',
                '''Class,E,:,_,{,},Class,f_L,{,},Class,z__,:,_2,{,Val,$__,:,_,;,Var,_,,,$2,,,T,:,Array,[,Int,,,0x6,],;,},Class,_a3__,{,Constructor,(,_,:,Array,[,Array,[,Float,,,021,],,,055,],;,_,:,_y,),{,},},<EOF>''',
                101
            )
        )

    def test_395(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Pv{Destructor (){}Constructor (){}Destructor (){ {}{}Continue ;Var _0:__;}_(O_:E62;_24_,___,Z1:Boolean ;L,j_1,_,_,_L32:Array [Float ,55]){} }Class _:C{}''',
                '''Class,Pv,{,Destructor,(,),{,},Constructor,(,),{,},Destructor,(,),{,{,},{,},Continue,;,Var,_0,:,__,;,},_,(,O_,:,E62,;,_24_,,,___,,,Z1,:,Boolean,;,L,,,j_1,,,_,,,_,,,_L32,:,Array,[,Float,,,55,],),{,},},Class,_,:,C,{,},<EOF>''',
                101
            )
        )

    def test_396(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0{Var K:_;IK_(n:Array [Array [Array [Array [Float ,07_0],061],0b10010],0B10010];__:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,32],0B10010],9],061],0B1],0b10010],04],0b10010],0x26],508_4]){} }''',
                '''Class,_0,{,Var,K,:,_,;,IK_,(,n,:,Array,[,Array,[,Array,[,Array,[,Float,,,070,],,,061,],,,0b10010,],,,0B10010,],;,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,32,],,,0B10010,],,,9,],,,061,],,,0B1,],,,0b10010,],,,04,],,,0b10010,],,,0x26,],,,5084,],),{,},},<EOF>''',
                101
            )
        )

    def test_397(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $H,_0_U:Array [Array [Boolean ,0B100001],022_6_11];}Class _1_3W{}Class _7t_S{Constructor (_,M_:String ;_:Float ;_A,e_Y,p_,xh:R;E,q__5,d1_Nf_,X08:Array [Array [Array [Int ,0b1],0xE],0140];pe_:Array [Float ,0X3_2]){} }''',
                '''Class,_,{,Val,$H,,,_0_U,:,Array,[,Array,[,Boolean,,,0B100001,],,,022611,],;,},Class,_1_3W,{,},Class,_7t_S,{,Constructor,(,_,,,M_,:,String,;,_,:,Float,;,_A,,,e_Y,,,p_,,,xh,:,R,;,E,,,q__5,,,d1_Nf_,,,X08,:,Array,[,Array,[,Array,[,Int,,,0b1,],,,0xE,],,,0140,],;,pe_,:,Array,[,Float,,,0X32,],),{,},},<EOF>''',
                101
            )
        )

    def test_398(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k:_{}Class _s{_(rR,q_7s_,O1__:Array [Array [Array [Boolean ,0x8],25],0b101011];_:Array [Float ,80]){}$_0_1(){} }Class m:_{Val $6,$2a_,_,M2K:Array [Array [Boolean ,04],1];}Class _3:E{}''',
                '''Class,k,:,_,{,},Class,_s,{,_,(,rR,,,q_7s_,,,O1__,:,Array,[,Array,[,Array,[,Boolean,,,0x8,],,,25,],,,0b101011,],;,_,:,Array,[,Float,,,80,],),{,},$_0_1,(,),{,},},Class,m,:,_,{,Val,$6,,,$2a_,,,_,,,M2K,:,Array,[,Array,[,Boolean,,,04,],,,1,],;,},Class,_3,:,E,{,},<EOF>''',
                101
            )
        )

    def test_399(self):
        self.assertTrue(
            TestLexer.test(
                '''Class tX_U__{Constructor (_:Array [Array [Array [Array [Int ,033],50],033],7767]){}j(_c9:Array [Float ,7];__,_:Float ){} }''',
                '''Class,tX_U__,{,Constructor,(,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,033,],,,50,],,,033,],,,7767,],),{,},j,(,_c9,:,Array,[,Float,,,7,],;,__,,,_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_400(self):
        self.assertTrue(
            TestLexer.test(
                '''Class s__{Var $0,$__e:Float ;}Class __:_{Destructor (){} }Class M3_{_(w6k:Array [Boolean ,0B11]){}Constructor (){}Constructor (){} }Class _{Var $8:Int ;Constructor (L9,_:Int ){}Constructor (){} }Class _{Destructor (){}Val $zJ9,i:Array [Boolean ,100];}Class _7:__oZS{}''',
                '''Class,s__,{,Var,$0,,,$__e,:,Float,;,},Class,__,:,_,{,Destructor,(,),{,},},Class,M3_,{,_,(,w6k,:,Array,[,Boolean,,,0B11,],),{,},Constructor,(,),{,},Constructor,(,),{,},},Class,_,{,Var,$8,:,Int,;,Constructor,(,L9,,,_,:,Int,),{,},Constructor,(,),{,},},Class,_,{,Destructor,(,),{,},Val,$zJ9,,,i,:,Array,[,Boolean,,,100,],;,},Class,_7,:,__oZS,{,},<EOF>''',
                101
            )
        )

    def test_401(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:_{Var $_6A_e:String ;Var $W2_T,_,_8:Boolean ;Val $y_:Array [Array [Int ,0x41],0X6];}Class _{Constructor (){Return ;}Val s,l33r:_;}''',
                '''Class,__,:,_,{,Var,$_6A_e,:,String,;,Var,$W2_T,,,_,,,_8,:,Boolean,;,Val,$y_,:,Array,[,Array,[,Int,,,0x41,],,,0X6,],;,},Class,_,{,Constructor,(,),{,Return,;,},Val,s,,,l33r,:,_,;,},<EOF>''',
                101
            )
        )

    def test_402(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __Z:___{Constructor (){} }Class s3A9U{}Class _{Constructor (){Val _:Float ;}Val $i2_,$9:Array [Array [Array [Boolean ,0B1],01_45],0x1];}''',
                '''Class,__Z,:,___,{,Constructor,(,),{,},},Class,s3A9U,{,},Class,_,{,Constructor,(,),{,Val,_,:,Float,;,},Val,$i2_,,,$9,:,Array,[,Array,[,Array,[,Boolean,,,0B1,],,,0145,],,,0x1,],;,},<EOF>''',
                101
            )
        )

    def test_403(self):
        self.assertTrue(
            TestLexer.test(
                '''Class z{}Class E5:u{Var $uft_Q_:Float ;Destructor (){Break ;}Destructor (){}Constructor (_,_N_85_,T_w:_9e;_:Array [Array [String ,0X8C5],97];K,JK:Boolean ){} }''',
                '''Class,z,{,},Class,E5,:,u,{,Var,$uft_Q_,:,Float,;,Destructor,(,),{,Break,;,},Destructor,(,),{,},Constructor,(,_,,,_N_85_,,,T_w,:,_9e,;,_,:,Array,[,Array,[,String,,,0X8C5,],,,97,],;,K,,,JK,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_404(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:d_j{Constructor (p:Array [Array [Int ,4],05];V8,_:String ;_,_GC:Array [Int ,010_5];___A__,r,I:String ;_:Array [String ,0b11_11_0];zA4_:String ;b:Boolean ;_X_w:Boolean ){Continue ;} }''',
                '''Class,_,:,d_j,{,Constructor,(,p,:,Array,[,Array,[,Int,,,4,],,,05,],;,V8,,,_,:,String,;,_,,,_GC,:,Array,[,Int,,,0105,],;,___A__,,,r,,,I,:,String,;,_,:,Array,[,String,,,0b11110,],;,zA4_,:,String,;,b,:,Boolean,;,_X_w,:,Boolean,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_405(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X:M{Val $9:Float ;Val _:Int ;$77_(_2_:Array [Array [Array [Float ,0X26],066],0x2A];u:Float ;_,tp,_:H){Val Bp2Q:Float ;} }Class G__{}''',
                '''Class,X,:,M,{,Val,$9,:,Float,;,Val,_,:,Int,;,$77_,(,_2_,:,Array,[,Array,[,Array,[,Float,,,0X26,],,,066,],,,0x2A,],;,u,:,Float,;,_,,,tp,,,_,:,H,),{,Val,Bp2Q,:,Float,;,},},Class,G__,{,},<EOF>''',
                101
            )
        )

    def test_406(self):
        self.assertTrue(
            TestLexer.test(
                '''Class h:P{}Class _:__{}Class Z_B{}Class _1I{Constructor (l_,_4:Array [Array [Float ,040_2],0xB];_,y:Boolean ){} }Class _ky2_V7{}''',
                '''Class,h,:,P,{,},Class,_,:,__,{,},Class,Z_B,{,},Class,_1I,{,Constructor,(,l_,,,_4,:,Array,[,Array,[,Float,,,0402,],,,0xB,],;,_,,,y,:,Boolean,),{,},},Class,_ky2_V7,{,},<EOF>''',
                101
            )
        )

    def test_407(self):
        self.assertTrue(
            TestLexer.test(
                '''Class O{Var $N7,_:_7__;Val L,$d,$7,$U:Array [Array [Int ,0X3B],11];Var $6:Int ;Var $_:_X;}Class _l_U0A{Val $Z,$r:Int ;Var $W:Array [Array [Array [Array [Array [Int ,07],03_1],0133],04_10_1],0B101001];Val k:Boolean ;Destructor (){Break ;Continue ;} }''',
                '''Class,O,{,Var,$N7,,,_,:,_7__,;,Val,L,,,$d,,,$7,,,$U,:,Array,[,Array,[,Int,,,0X3B,],,,11,],;,Var,$6,:,Int,;,Var,$_,:,_X,;,},Class,_l_U0A,{,Val,$Z,,,$r,:,Int,;,Var,$W,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,07,],,,031,],,,0133,],,,04101,],,,0B101001,],;,Val,k,:,Boolean,;,Destructor,(,),{,Break,;,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_408(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class F:_z_11A__E{Var $_:Array [Boolean ,03_5_2];}Class ____{}Class ggAU_4H_:_z{Val E:Float ;Var $_:Array [Array [Float ,3],0x9];}''',
                '''Class,__,{,},Class,F,:,_z_11A__E,{,Var,$_,:,Array,[,Boolean,,,0352,],;,},Class,____,{,},Class,ggAU_4H_,:,_z,{,Val,E,:,Float,;,Var,$_,:,Array,[,Array,[,Float,,,3,],,,0x9,],;,},<EOF>''',
                101
            )
        )

    def test_409(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t_:_{Var $4dJ7598,$_K:Float ;g80(_,W:Array [Array [String ,0b1],30];_,_,T,h_,NQ:Boolean ;Pu_:__;gb6X09W61e,_:AGE2){} }Class Ws{}''',
                '''Class,t_,:,_,{,Var,$4dJ7598,,,$_K,:,Float,;,g80,(,_,,,W,:,Array,[,Array,[,String,,,0b1,],,,30,],;,_,,,_,,,T,,,h_,,,NQ,:,Boolean,;,Pu_,:,__,;,gb6X09W61e,,,_,:,AGE2,),{,},},Class,Ws,{,},<EOF>''',
                101
            )
        )

    def test_410(self):
        self.assertTrue(
            TestLexer.test(
                '''Class W1{}Class _{$__(_,M:Int ;W_,t:Array [Boolean ,0B1001101];l5_,_4_,_:Array [Array [Array [Array [Int ,02],021],59],0x5A]){}Destructor (){} }''',
                '''Class,W1,{,},Class,_,{,$__,(,_,,,M,:,Int,;,W_,,,t,:,Array,[,Boolean,,,0B1001101,],;,l5_,,,_4_,,,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,02,],,,021,],,,59,],,,0x5A,],),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_411(self):
        self.assertTrue(
            TestLexer.test(
                '''Class h_:y3{Constructor (MJ,x,_71:_Mc;W,c:R;_43C8_2_,_5,K:__;p2__LL:Boolean ;J_,_,_7_2__:Array [Array [Array [Array [Float ,0X37],02_7],7],02_4];H:Array [Int ,014];O:Int ;m:Int ){}Constructor (){}Constructor (){Continue ;}Var N,_,_3_,_:Array [Array [Boolean ,0x8_73_21_459],0XE];}''',
                '''Class,h_,:,y3,{,Constructor,(,MJ,,,x,,,_71,:,_Mc,;,W,,,c,:,R,;,_43C8_2_,,,_5,,,K,:,__,;,p2__LL,:,Boolean,;,J_,,,_,,,_7_2__,:,Array,[,Array,[,Array,[,Array,[,Float,,,0X37,],,,027,],,,7,],,,024,],;,H,:,Array,[,Int,,,014,],;,O,:,Int,;,m,:,Int,),{,},Constructor,(,),{,},Constructor,(,),{,Continue,;,},Var,N,,,_,,,_3_,,,_,:,Array,[,Array,[,Boolean,,,0x87321459,],,,0XE,],;,},<EOF>''',
                101
            )
        )

    def test_412(self):
        self.assertTrue(
            TestLexer.test(
                '''Class U{Constructor (__RL7__,T5_7,_,kH,_1,c_:Array [Array [Int ,0B1001111],0b1_0];A__:String ;O_:Array [Array [Boolean ,6],07];_,V__S,__m:Boolean ;W,z:Array [Array [Float ,0113],0B11_1];_:_){ {} }}Class __Y:X3{}''',
                '''Class,U,{,Constructor,(,__RL7__,,,T5_7,,,_,,,kH,,,_1,,,c_,:,Array,[,Array,[,Int,,,0B1001111,],,,0b10,],;,A__,:,String,;,O_,:,Array,[,Array,[,Boolean,,,6,],,,07,],;,_,,,V__S,,,__m,:,Boolean,;,W,,,z,:,Array,[,Array,[,Float,,,0113,],,,0B111,],;,_,:,_,),{,{,},},},Class,__Y,:,X3,{,},<EOF>''',
                101
            )
        )

    def test_413(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X:D{_d_N(){Break ;Continue ;Break ;}Constructor (w,_,w_:Array [Array [Array [Boolean ,04],060],0XF_4]){} }''',
                '''Class,X,:,D,{,_d_N,(,),{,Break,;,Continue,;,Break,;,},Constructor,(,w,,,_,,,w_,:,Array,[,Array,[,Array,[,Boolean,,,04,],,,060,],,,0XF4,],),{,},},<EOF>''',
                101
            )
        )

    def test_414(self):
        self.assertTrue(
            TestLexer.test(
                '''Class WV{Constructor (__:h;_,U,_1,_V,_CX,A_:Int ;O,z:Boolean ;_,_:Array [Boolean ,0B1_0_01_0];_69v_B3_,DR,_4_3_tF:_6;o6,_:Boolean ;sT__9O:Array [Array [Array [Array [Int ,62],03],034],0B1];J:Array [Boolean ,0x2_6_D]){} }Class s_{Var z_9td:Array [Array [Array [Array [String ,4_9_7],62],04],6];}Class _{Var w79,oO:_;Val $U,_s,$4,$_e,m:Array [Array [Int ,0X1],0b1];Var $7x:__8;}''',
                '''Class,WV,{,Constructor,(,__,:,h,;,_,,,U,,,_1,,,_V,,,_CX,,,A_,:,Int,;,O,,,z,:,Boolean,;,_,,,_,:,Array,[,Boolean,,,0B10010,],;,_69v_B3_,,,DR,,,_4_3_tF,:,_6,;,o6,,,_,:,Boolean,;,sT__9O,:,Array,[,Array,[,Array,[,Array,[,Int,,,62,],,,03,],,,034,],,,0B1,],;,J,:,Array,[,Boolean,,,0x26D,],),{,},},Class,s_,{,Var,z_9td,:,Array,[,Array,[,Array,[,Array,[,String,,,497,],,,62,],,,04,],,,6,],;,},Class,_,{,Var,w79,,,oO,:,_,;,Val,$U,,,_s,,,$4,,,$_e,,,m,:,Array,[,Array,[,Int,,,0X1,],,,0b1,],;,Var,$7x,:,__8,;,},<EOF>''',
                101
            )
        )

    def test_415(self):
        self.assertTrue(
            TestLexer.test(
                '''Class r:_{Constructor (__xae_7:Array [Array [Boolean ,90],1];_,_:Array [Int ,5];__,_,_G,_,G17:Array [Array [Array [Array [Array [Int ,0b1001110],9],90],0b1001110],90]){}Val __v,___:_0;Var _us:Float ;}''',
                '''Class,r,:,_,{,Constructor,(,__xae_7,:,Array,[,Array,[,Boolean,,,90,],,,1,],;,_,,,_,:,Array,[,Int,,,5,],;,__,,,_,,,_G,,,_,,,G17,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0b1001110,],,,9,],,,90,],,,0b1001110,],,,90,],),{,},Val,__v,,,___,:,_0,;,Var,_us,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_416(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t5:_3{}Class _{Var $6CgJ1,$1s,$Y:Array [Array [Int ,0XA_9_4_9],0b1];$_(){}Val $_9,w,w_:Array [Int ,33_3];}Class _{}''',
                '''Class,t5,:,_3,{,},Class,_,{,Var,$6CgJ1,,,$1s,,,$Y,:,Array,[,Array,[,Int,,,0XA949,],,,0b1,],;,$_,(,),{,},Val,$_9,,,w,,,w_,:,Array,[,Int,,,333,],;,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_417(self):
        self.assertTrue(
            TestLexer.test(
                '''Class e1:y{Val _:Float ;}Class z{}Class _H:t{}Class _41_7f_6_y_:_{Constructor (q,__:Array [Float ,68];A,__:Array [Array [String ,68],0x2F]){} }''',
                '''Class,e1,:,y,{,Val,_,:,Float,;,},Class,z,{,},Class,_H,:,t,{,},Class,_41_7f_6_y_,:,_,{,Constructor,(,q,,,__,:,Array,[,Float,,,68,],;,A,,,__,:,Array,[,Array,[,String,,,68,],,,0x2F,],),{,},},<EOF>''',
                101
            )
        )

    def test_418(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Destructor (){Val _:Array [Array [Array [Array [Float ,0B1],0B1],4],8];} }Class L7:_{}Class _k:_{Destructor (){}Var _:_S__;}''',
                '''Class,_,{,Destructor,(,),{,Val,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B1,],,,0B1,],,,4,],,,8,],;,},},Class,L7,:,_,{,},Class,_k,:,_,{,Destructor,(,),{,},Var,_,:,_S__,;,},<EOF>''',
                101
            )
        )

    def test_419(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:y{}Class _:k{}Class Y_:Q{Destructor (){}Constructor (p6:Array [String ,0xE2_8_6]){Break ;}Destructor (){} }''',
                '''Class,_,:,y,{,},Class,_,:,k,{,},Class,Y_,:,Q,{,Destructor,(,),{,},Constructor,(,p6,:,Array,[,String,,,0xE286,],),{,Break,;,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_420(self):
        self.assertTrue(
            TestLexer.test(
                '''Class S:Z_y{Destructor (){} }Class q_{}Class q{Var $9:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,0115],0X5],0b11],67],0XB_0],033],0B101],6],02_13],5],0B100011],0115];}''',
                '''Class,S,:,Z_y,{,Destructor,(,),{,},},Class,q_,{,},Class,q,{,Var,$9,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0115,],,,0X5,],,,0b11,],,,67,],,,0XB0,],,,033,],,,0B101,],,,6,],,,0213,],,,5,],,,0B100011,],,,0115,],;,},<EOF>''',
                101
            )
        )

    def test_421(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:lr{}Class _L_68y_{$0(L:_2Z;_:Int ){_4::$T_();Return ;}uL(){} }Class u___7m{}Class _:TFm{}Class _4s:n8{}''',
                '''Class,_,:,lr,{,},Class,_L_68y_,{,$0,(,L,:,_2Z,;,_,:,Int,),{,_4,::,$T_,(,),;,Return,;,},uL,(,),{,},},Class,u___7m,{,},Class,_,:,TFm,{,},Class,_4s,:,n8,{,},<EOF>''',
                101
            )
        )

    def test_422(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_,_8_:Array [Array [Int ,0X8],0X8]){} }Class _:P{$8_F(_:_;__7_p:Boolean ;o,s,_C:H_;h,__,__,WX,Q,_:Boolean ;a8_:Boolean ;__:Boolean ;_:p8bz){} }''',
                '''Class,_,{,Constructor,(,_,,,_8_,:,Array,[,Array,[,Int,,,0X8,],,,0X8,],),{,},},Class,_,:,P,{,$8_F,(,_,:,_,;,__7_p,:,Boolean,;,o,,,s,,,_C,:,H_,;,h,,,__,,,__,,,WX,,,Q,,,_,:,Boolean,;,a8_,:,Boolean,;,__,:,Boolean,;,_,:,p8bz,),{,},},<EOF>''',
                101
            )
        )

    def test_423(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_9_E,_8Cn,_8,z:Array [Array [Float ,0125],0xC];_:Array [Array [Float ,0B11_1],0125];p,_R47:Array [Array [Int ,92],0x10];j,q4:Array [Float ,92]){} }Class Vm5:A{Val $_,eG_:Array [Array [Array [Int ,92],1],0X3_B_D_D];Constructor (s9:Array [Float ,03];_,_:Boolean ){} }''',
                '''Class,_,{,Constructor,(,_9_E,,,_8Cn,,,_8,,,z,:,Array,[,Array,[,Float,,,0125,],,,0xC,],;,_,:,Array,[,Array,[,Float,,,0B111,],,,0125,],;,p,,,_R47,:,Array,[,Array,[,Int,,,92,],,,0x10,],;,j,,,q4,:,Array,[,Float,,,92,],),{,},},Class,Vm5,:,A,{,Val,$_,,,eG_,:,Array,[,Array,[,Array,[,Int,,,92,],,,1,],,,0X3BDD,],;,Constructor,(,s9,:,Array,[,Float,,,03,],;,_,,,_,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_424(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{_(l:D4;__:Int ;_:Array [Array [Array [Array [Array [Array [Float ,03],0x6],0X47],0b10_01],020],4];K,_5:Boolean ;ELjor__,L_:Array [Array [String ,0b1],0X47]){} }''',
                '''Class,_,{,_,(,l,:,D4,;,__,:,Int,;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,03,],,,0x6,],,,0X47,],,,0b1001,],,,020,],,,4,],;,K,,,_5,:,Boolean,;,ELjor__,,,L_,:,Array,[,Array,[,String,,,0b1,],,,0X47,],),{,},},<EOF>''',
                101
            )
        )

    def test_425(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Iv{Var iM1_69_:m_;}Class i:__C_ZCOW{}Class _:w_{Val $2:Array [String ,06]="'"";Val A:Array [Boolean ,0x58];}''',
                '''Class,Iv,{,Var,iM1_69_,:,m_,;,},Class,i,:,__C_ZCOW,{,},Class,_,:,w_,{,Val,$2,:,Array,[,String,,,06,],=,'",;,Val,A,:,Array,[,Boolean,,,0x58,],;,},<EOF>''',
                101
            )
        )

    def test_426(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J:M5nH6{Constructor (){Break ;}Constructor (){}Constructor (){Break ;}Var vc__9__:m;}Class b:_{}Class _:Q_{}''',
                '''Class,J,:,M5nH6,{,Constructor,(,),{,Break,;,},Constructor,(,),{,},Constructor,(,),{,Break,;,},Var,vc__9__,:,m,;,},Class,b,:,_,{,},Class,_,:,Q_,{,},<EOF>''',
                101
            )
        )

    def test_427(self):
        self.assertTrue(
            TestLexer.test(
                '''Class G_{Var _1Q:Array [Boolean ,0X10];Val m_l7y:u;}Class hvj{Constructor (M:Int ;_:Boolean ;I4H_,pr:Int ;__oO46,c0,a_,n_,I_7_2,_6U__l0_:Array [Array [Array [Boolean ,42],0120],0x10];n:_2){} }Class _{}Class __{}Class z:__{}''',
                '''Class,G_,{,Var,_1Q,:,Array,[,Boolean,,,0X10,],;,Val,m_l7y,:,u,;,},Class,hvj,{,Constructor,(,M,:,Int,;,_,:,Boolean,;,I4H_,,,pr,:,Int,;,__oO46,,,c0,,,a_,,,n_,,,I_7_2,,,_6U__l0_,:,Array,[,Array,[,Array,[,Boolean,,,42,],,,0120,],,,0x10,],;,n,:,_2,),{,},},Class,_,{,},Class,__,{,},Class,z,:,__,{,},<EOF>''',
                101
            )
        )

    def test_428(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7_l{Destructor (){Break ;}Var $Vyx:Array [Array [Array [Array [Array [Boolean ,05_2],82],0X57],040],82];Var $M,J,_u:Array [Array [Array [Array [Array [Int ,8],8],3_9_3],0B11111],045];}Class _:W{}Class p2:xB4OivF_{Constructor (){} }''',
                '''Class,_7_l,{,Destructor,(,),{,Break,;,},Var,$Vyx,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,052,],,,82,],,,0X57,],,,040,],,,82,],;,Var,$M,,,J,,,_u,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,8,],,,8,],,,393,],,,0B11111,],,,045,],;,},Class,_,:,W,{,},Class,p2,:,xB4OivF_,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_429(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8jw_{_U(_2_9,F,_F6K_,_t_,P,_,j:Int ;M2_,s,vmW,Dw_:Array [Boolean ,0xB_5_8_8];QX_,V:__;c_,d:__;r__:String ){} }''',
                '''Class,_8jw_,{,_U,(,_2_9,,,F,,,_F6K_,,,_t_,,,P,,,_,,,j,:,Int,;,M2_,,,s,,,vmW,,,Dw_,:,Array,[,Boolean,,,0xB588,],;,QX_,,,V,:,__,;,c_,,,d,:,__,;,r__,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_430(self):
        self.assertTrue(
            TestLexer.test(
                '''Class I{Val $m:Array [Float ,9];}Class _:_{}Class i:_{}Class _:__{_(_,_E,R:Array [Int ,061];M,l,ns_l,_1_Q,_,h__:Array [Int ,27];__o,_,n:Array [Array [Boolean ,0X9],0b111001]){} }''',
                '''Class,I,{,Val,$m,:,Array,[,Float,,,9,],;,},Class,_,:,_,{,},Class,i,:,_,{,},Class,_,:,__,{,_,(,_,,,_E,,,R,:,Array,[,Int,,,061,],;,M,,,l,,,ns_l,,,_1_Q,,,_,,,h__,:,Array,[,Int,,,27,],;,__o,,,_,,,n,:,Array,[,Array,[,Boolean,,,0X9,],,,0b111001,],),{,},},<EOF>''',
                101
            )
        )

    def test_431(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Q:_{Val $l9:e__;}Class D{}Class Y:_{Constructor (RI:VV;o:ww7;_o94,_n_L:Array [Array [Boolean ,034],25];Z,_:Float ;_:Float ){ {} }}''',
                '''Class,Q,:,_,{,Val,$l9,:,e__,;,},Class,D,{,},Class,Y,:,_,{,Constructor,(,RI,:,VV,;,o,:,ww7,;,_o94,,,_n_L,:,Array,[,Array,[,Boolean,,,034,],,,25,],;,Z,,,_,:,Float,;,_,:,Float,),{,{,},},},<EOF>''',
                101
            )
        )

    def test_432(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _9:I_EY_89_u6_{$_(_,_2,_E:Float ){}Var $v,_d,$Ju__70:Array [Array [Float ,82],0b111110];Constructor (_:_M;_:rw;N_M_ja_,_,_:l_){w::$_()._X9_();} }''',
                '''Class,_,{,},Class,_9,:,I_EY_89_u6_,{,$_,(,_,,,_2,,,_E,:,Float,),{,},Var,$v,,,_d,,,$Ju__70,:,Array,[,Array,[,Float,,,82,],,,0b111110,],;,Constructor,(,_,:,_M,;,_,:,rw,;,N_M_ja_,,,_,,,_,:,l_,),{,w,::,$_,(,),.,_X9_,(,),;,},},<EOF>''',
                101
            )
        )

    def test_433(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Constructor (_6,_,_,_8,_iA:Array [Boolean ,0144];j,a_,_:Array [Array [Array [String ,0b101],5],7_0];_,_,_5,_T,_0,z_,__5:Int ;F_w,J:a0h85;_8:Array [String ,0x4D];g85x:String ){}Var $4:Float ;}''',
                '''Class,_,:,_,{,Constructor,(,_6,,,_,,,_,,,_8,,,_iA,:,Array,[,Boolean,,,0144,],;,j,,,a_,,,_,:,Array,[,Array,[,Array,[,String,,,0b101,],,,5,],,,70,],;,_,,,_,,,_5,,,_T,,,_0,,,z_,,,__5,:,Int,;,F_w,,,J,:,a0h85,;,_8,:,Array,[,String,,,0x4D,],;,g85x,:,String,),{,},Var,$4,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_434(self):
        self.assertTrue(
            TestLexer.test(
                '''Class u{Val $k9,$Y,$_6:Array [Array [Array [Array [Array [String ,0X4],0X4B],14],0b1],14];}Class _1{J7__5(){} }Class _{}Class Zfw:_{}''',
                '''Class,u,{,Val,$k9,,,$Y,,,$_6,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X4,],,,0X4B,],,,14,],,,0b1,],,,14,],;,},Class,_1,{,J7__5,(,),{,},},Class,_,{,},Class,Zfw,:,_,{,},<EOF>''',
                101
            )
        )

    def test_435(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:zD{Constructor (){}Val $_,A__q,p:_;Var $D,$__2v,$8:String ;m(){} }Class _{}Class Nd_{Constructor (){}Destructor (){} }''',
                '''Class,_,:,zD,{,Constructor,(,),{,},Val,$_,,,A__q,,,p,:,_,;,Var,$D,,,$__2v,,,$8,:,String,;,m,(,),{,},},Class,_,{,},Class,Nd_,{,Constructor,(,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_436(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class __9i:A{Val k:_____;}Class _2{Constructor (_2,_,_:Array [Array [Int ,050],2];m6,_3:___;T8:_;_,_:u;__,_13:Array [Float ,04_53_4];gS_5,m,_:V__;f9,W8:Array [Int ,1_1_71];g:k__){}$P_(_:Array [Array [Array [Float ,48],0xC],7]){} }''',
                '''Class,_,{,},Class,__9i,:,A,{,Val,k,:,_____,;,},Class,_2,{,Constructor,(,_2,,,_,,,_,:,Array,[,Array,[,Int,,,050,],,,2,],;,m6,,,_3,:,___,;,T8,:,_,;,_,,,_,:,u,;,__,,,_13,:,Array,[,Float,,,04534,],;,gS_5,,,m,,,_,:,V__,;,f9,,,W8,:,Array,[,Int,,,1171,],;,g,:,k__,),{,},$P_,(,_,:,Array,[,Array,[,Array,[,Float,,,48,],,,0xC,],,,7,],),{,},},<EOF>''',
                101
            )
        )

    def test_437(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:__{Constructor (_,s_,K9:Array [Float ,0x11];S:Int ;n_V,K__8,J5,_,_4M__4___,a,_VB:Int ){} }Class _I:V28{}''',
                '''Class,_,:,__,{,Constructor,(,_,,,s_,,,K9,:,Array,[,Float,,,0x11,],;,S,:,Int,;,n_V,,,K__8,,,J5,,,_,,,_4M__4___,,,a,,,_VB,:,Int,),{,},},Class,_I,:,V28,{,},<EOF>''',
                101
            )
        )

    def test_438(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C{}Class t{p(_:Array [Array [Float ,020],0b1011011]){} }Class _:_{}Class _eo_7__{Destructor (){}Constructor (_8:_X;__,_,f3:Array [Array [Array [Array [Array [Array [Array [Boolean ,0b1],0B101001],0x9],020],95],0b1_1],95];_F_,_,k,S:Boolean ;_5D,_,o,X7:Boolean ){} }Class _{Q_3ai(_:Int ){} }''',
                '''Class,C,{,},Class,t,{,p,(,_,:,Array,[,Array,[,Float,,,020,],,,0b1011011,],),{,},},Class,_,:,_,{,},Class,_eo_7__,{,Destructor,(,),{,},Constructor,(,_8,:,_X,;,__,,,_,,,f3,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1,],,,0B101001,],,,0x9,],,,020,],,,95,],,,0b11,],,,95,],;,_F_,,,_,,,k,,,S,:,Boolean,;,_5D,,,_,,,o,,,X7,:,Boolean,),{,},},Class,_,{,Q_3ai,(,_,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_439(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m:_18{}Class f{}Class _8_:__{Constructor (Jo,_G,t,D:Array [Array [Float ,0b100010],0B1];__T:_;__8:A_){} }Class L8{}Class q0:yc{}''',
                '''Class,m,:,_18,{,},Class,f,{,},Class,_8_,:,__,{,Constructor,(,Jo,,,_G,,,t,,,D,:,Array,[,Array,[,Float,,,0b100010,],,,0B1,],;,__T,:,_,;,__8,:,A_,),{,},},Class,L8,{,},Class,q0,:,yc,{,},<EOF>''',
                101
            )
        )

    def test_440(self):
        self.assertTrue(
            TestLexer.test(
                '''Class z:_{Val $2,Z:Float ;}Class nB:_{}Class N{}Class u_Y:oH07_{Val R:String ;Var $03:Float =r._Gx;}Class f__:y{}''',
                '''Class,z,:,_,{,Val,$2,,,Z,:,Float,;,},Class,nB,:,_,{,},Class,N,{,},Class,u_Y,:,oH07_,{,Val,R,:,String,;,Var,$03,:,Float,=,r,.,_Gx,;,},Class,f__,:,y,{,},<EOF>''',
                101
            )
        )

    def test_441(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T:_{Constructor (){}$_(){} }Class ____:u__{}Class L7{Val $i,__ll_:Float ;Destructor (){} }Class v225W0:_{$73(){} }''',
                '''Class,T,:,_,{,Constructor,(,),{,},$_,(,),{,},},Class,____,:,u__,{,},Class,L7,{,Val,$i,,,__ll_,:,Float,;,Destructor,(,),{,},},Class,v225W0,:,_,{,$73,(,),{,},},<EOF>''',
                101
            )
        )

    def test_442(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___3{Constructor (_JwW,_:Array [Array [Array [Float ,0B1],0B100],077]){} }Class _4rLf{Var $8c8,A:String ;}''',
                '''Class,___3,{,Constructor,(,_JwW,,,_,:,Array,[,Array,[,Array,[,Float,,,0B1,],,,0B100,],,,077,],),{,},},Class,_4rLf,{,Var,$8c8,,,A,:,String,;,},<EOF>''',
                101
            )
        )

    def test_443(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_:U;x,_U,Z:p2;_,_,k,AM:Array [Boolean ,04];_S:_x){}Constructor (){} }Class H__{}Class cP_0_Pe:vb{}''',
                '''Class,_,{,Constructor,(,_,:,U,;,x,,,_U,,,Z,:,p2,;,_,,,_,,,k,,,AM,:,Array,[,Boolean,,,04,],;,_S,:,_x,),{,},Constructor,(,),{,},},Class,H__,{,},Class,cP_0_Pe,:,vb,{,},<EOF>''',
                101
            )
        )

    def test_444(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (R,B_8:Boolean ;_,_,_:Array [Array [Boolean ,0B1001101],8];K__5:Boolean ;q:Int ;_P,I_zPB8_:Array [Array [Float ,0b1],8]){} }''',
                '''Class,_,{,Constructor,(,R,,,B_8,:,Boolean,;,_,,,_,,,_,:,Array,[,Array,[,Boolean,,,0B1001101,],,,8,],;,K__5,:,Boolean,;,q,:,Int,;,_P,,,I_zPB8_,:,Array,[,Array,[,Float,,,0b1,],,,8,],),{,},},<EOF>''',
                101
            )
        )

    def test_445(self):
        self.assertTrue(
            TestLexer.test(
                '''Class I_R_6_:I7_q_d_y{Destructor (){Var d:Array [Array [Array [Array [Array [Int ,0x1D8_D_E],0x5],044],0x1],84];{} }}''',
                '''Class,I_R_6_,:,I7_q_d_y,{,Destructor,(,),{,Var,d,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x1D8DE,],,,0x5,],,,044,],,,0x1,],,,84,],;,{,},},},<EOF>''',
                101
            )
        )

    def test_446(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Dv{}Class Q:P6{}Class B:_R4_{}Class kO{$_m(_,V_4,_3M3_F,_:N){} }Class k5:g{Var $X_:Array [Boolean ,9];Destructor (){} }''',
                '''Class,Dv,{,},Class,Q,:,P6,{,},Class,B,:,_R4_,{,},Class,kO,{,$_m,(,_,,,V_4,,,_3M3_F,,,_,:,N,),{,},},Class,k5,:,g,{,Var,$X_,:,Array,[,Boolean,,,9,],;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_447(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y{$4(_:M35;P,_:Boolean ;___,_9,o_xD_3_3:Int ;Y:C1;e5,j:Boolean ;_,q_,Wu_,a:String ;_,__:Array [Int ,1_36_0_0];_:String ){} }''',
                '''Class,y,{,$4,(,_,:,M35,;,P,,,_,:,Boolean,;,___,,,_9,,,o_xD_3_3,:,Int,;,Y,:,C1,;,e5,,,j,:,Boolean,;,_,,,q_,,,Wu_,,,a,:,String,;,_,,,__,:,Array,[,Int,,,13600,],;,_,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_448(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{b(N5,_7,_q,U:Float ){}Constructor (i31P58,_Z_3:___;t__3,v_,y:z){} }Class D_{Var __,_,$V7:_;$Z3L(c:y){ {} }}Class N{Var $P:String ;}''',
                '''Class,_,{,b,(,N5,,,_7,,,_q,,,U,:,Float,),{,},Constructor,(,i31P58,,,_Z_3,:,___,;,t__3,,,v_,,,y,:,z,),{,},},Class,D_,{,Var,__,,,_,,,$V7,:,_,;,$Z3L,(,c,:,y,),{,{,},},},Class,N,{,Var,$P,:,String,;,},<EOF>''',
                101
            )
        )

    def test_449(self):
        self.assertTrue(
            TestLexer.test(
                '''Class LC8{Constructor (__:Array [Array [Array [Array [Array [Float ,0B111],62],04],0B1],0X4B];TG,Xl7R,____o:Array [Boolean ,0b1];ao210:Boolean ;p7:String ;_1:String ){}$q_(_3_c7:Boolean ;_2m,__8,r4,PW:Float ;J:_){}Val $_:_;}Class _Bn_{Constructor (){} }''',
                '''Class,LC8,{,Constructor,(,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B111,],,,62,],,,04,],,,0B1,],,,0X4B,],;,TG,,,Xl7R,,,____o,:,Array,[,Boolean,,,0b1,],;,ao210,:,Boolean,;,p7,:,String,;,_1,:,String,),{,},$q_,(,_3_c7,:,Boolean,;,_2m,,,__8,,,r4,,,PW,:,Float,;,J,:,_,),{,},Val,$_,:,_,;,},Class,_Bn_,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_450(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Y9_U__:_4{y87(){Break ;} }Class _{}Class _{Destructor (){}$_(){} }Class s{Var $Zd__v:W;Constructor (){}Constructor (X:Array [Boolean ,4]){} }''',
                '''Class,Y9_U__,:,_4,{,y87,(,),{,Break,;,},},Class,_,{,},Class,_,{,Destructor,(,),{,},$_,(,),{,},},Class,s,{,Var,$Zd__v,:,W,;,Constructor,(,),{,},Constructor,(,X,:,Array,[,Boolean,,,4,],),{,},},<EOF>''',
                101
            )
        )

    def test_451(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Z:_m1C9{Constructor (_,t,J4aZ_T0,c84:Int ;___,_,_,l_:Array [Array [Array [Array [Array [Array [Float ,5],1],0x27],0B110100],57],0B110100]){}_6v2(T:Array [Int ,57];c8_S:Array [Int ,57]){} }Class _{Val $a:String ;}''',
                '''Class,Z,:,_m1C9,{,Constructor,(,_,,,t,,,J4aZ_T0,,,c84,:,Int,;,___,,,_,,,_,,,l_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,5,],,,1,],,,0x27,],,,0B110100,],,,57,],,,0B110100,],),{,},_6v2,(,T,:,Array,[,Int,,,57,],;,c8_S,:,Array,[,Int,,,57,],),{,},},Class,_,{,Val,$a,:,String,;,},<EOF>''',
                101
            )
        )

    def test_452(self):
        self.assertTrue(
            TestLexer.test(
                '''Class K{}Class __s{Var g_,$h:Array [String ,0xB];_S(){Val S,EQ5:Array [Array [Array [Array [String ,4],0XB_6_C_4],71],0b100110];} }''',
                '''Class,K,{,},Class,__s,{,Var,g_,,,$h,:,Array,[,String,,,0xB,],;,_S,(,),{,Val,S,,,EQ5,:,Array,[,Array,[,Array,[,Array,[,String,,,4,],,,0XB6C4,],,,71,],,,0b100110,],;,},},<EOF>''',
                101
            )
        )

    def test_453(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_M__R{Destructor (){} }Class _:d{Constructor (_:_4_U;j:H9;vw9__,_,l,s,a:Boolean ;_m_,_Xg,_,__E__QL4,kD,_,_:Array [Int ,2]){}Constructor (_:Int ;_M2H__:Array [Array [Int ,0b1],17]){}Val $3,$__R:p7;Constructor (LCWf,t_9:Array [Array [Array [Int ,0b1010100],0B1010110],0X25]){} }Class _n_:_5{}''',
                '''Class,_,:,_M__R,{,Destructor,(,),{,},},Class,_,:,d,{,Constructor,(,_,:,_4_U,;,j,:,H9,;,vw9__,,,_,,,l,,,s,,,a,:,Boolean,;,_m_,,,_Xg,,,_,,,__E__QL4,,,kD,,,_,,,_,:,Array,[,Int,,,2,],),{,},Constructor,(,_,:,Int,;,_M2H__,:,Array,[,Array,[,Int,,,0b1,],,,17,],),{,},Val,$3,,,$__R,:,p7,;,Constructor,(,LCWf,,,t_9,:,Array,[,Array,[,Array,[,Int,,,0b1010100,],,,0B1010110,],,,0X25,],),{,},},Class,_n_,:,_5,{,},<EOF>''',
                101
            )
        )

    def test_454(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P:__v_{Constructor (_,_4_:Float ;x:String ;_7:j;_,_5Z,d,_:Boolean ;__N_:P;_8:Array [Int ,07]){} }Class L_z{Constructor (_,z,a_:Array [Array [Array [Array [Boolean ,3_5],0xF],7],27];a,t,_c:String ;T,P:_;bd_3O_:u;d8_:F_){} }Class I{}''',
                '''Class,P,:,__v_,{,Constructor,(,_,,,_4_,:,Float,;,x,:,String,;,_7,:,j,;,_,,,_5Z,,,d,,,_,:,Boolean,;,__N_,:,P,;,_8,:,Array,[,Int,,,07,],),{,},},Class,L_z,{,Constructor,(,_,,,z,,,a_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,35,],,,0xF,],,,7,],,,27,],;,a,,,t,,,_c,:,String,;,T,,,P,:,_,;,bd_3O_,:,u,;,d8_,:,F_,),{,},},Class,I,{,},<EOF>''',
                101
            )
        )

    def test_455(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class n:J{Constructor (_0,__,_,Y:Float ;F_:String ;_p__:Array [String ,0X2]){ {} }Var $1_4__P,_,_6:String ;I4_2(g,_3_e,_,v,_:Boolean ){}Val $__:Array [Array [Array [Array [Boolean ,0b1],0B110001],0x60],54_9_52];Destructor (){} }''',
                '''Class,_,:,_,{,},Class,n,:,J,{,Constructor,(,_0,,,__,,,_,,,Y,:,Float,;,F_,:,String,;,_p__,:,Array,[,String,,,0X2,],),{,{,},},Var,$1_4__P,,,_,,,_6,:,String,;,I4_2,(,g,,,_3_e,,,_,,,v,,,_,:,Boolean,),{,},Val,$__,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1,],,,0B110001,],,,0x60,],,,54952,],;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_456(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:Ke_{Constructor (q,U8v:Array [Array [Array [Array [Float ,070],0xD_4],070],0B11]){Return ;Break ;}Var __,_6,_:Int ;}''',
                '''Class,_,:,Ke_,{,Constructor,(,q,,,U8v,:,Array,[,Array,[,Array,[,Array,[,Float,,,070,],,,0xD4,],,,070,],,,0B11,],),{,Return,;,Break,;,},Var,__,,,_6,,,_,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_457(self):
        self.assertTrue(
            TestLexer.test(
                '''Class z_w:X3_{Var H235,_,$3_:Boolean ;}Class _f:_{Constructor (k6J,X_7_,A4:String ){Val __Z:Array [Float ,25];} }''',
                '''Class,z_w,:,X3_,{,Var,H235,,,_,,,$3_,:,Boolean,;,},Class,_f,:,_,{,Constructor,(,k6J,,,X_7_,,,A4,:,String,),{,Val,__Z,:,Array,[,Float,,,25,],;,},},<EOF>''',
                101
            )
        )

    def test_458(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o7{Val $_5_,$_:z93;Val $34_P,_,$_5El:Array [Float ,03_5_2];Var $_m:Float ;Val $B:Array [Array [String ,0B11001],0XA];$g(j:Array [Array [Array [Array [Float ,0B1],0xE],3],0b1]){} }''',
                '''Class,o7,{,Val,$_5_,,,$_,:,z93,;,Val,$34_P,,,_,,,$_5El,:,Array,[,Float,,,0352,],;,Var,$_m,:,Float,;,Val,$B,:,Array,[,Array,[,String,,,0B11001,],,,0XA,],;,$g,(,j,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B1,],,,0xE,],,,3,],,,0b1,],),{,},},<EOF>''',
                101
            )
        )

    def test_459(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V9:W_n{Destructor (){}Var $_,$b5,$72__4__2_:String ;}Class _:u{Destructor (){Var _8_5,l_6:String ;}Var __:Array [Int ,0b11100];}''',
                '''Class,V9,:,W_n,{,Destructor,(,),{,},Var,$_,,,$b5,,,$72__4__2_,:,String,;,},Class,_,:,u,{,Destructor,(,),{,Var,_8_5,,,l_6,:,String,;,},Var,__,:,Array,[,Int,,,0b11100,],;,},<EOF>''',
                101
            )
        )

    def test_460(self):
        self.assertTrue(
            TestLexer.test(
                '''Class F{Var $4__:Q;}Class k:_{Var _,_29,_29,q,U:r;}Class gS{Constructor (){Return ;} }Class _9{}Class _9_4N_:h8Y{}''',
                '''Class,F,{,Var,$4__,:,Q,;,},Class,k,:,_,{,Var,_,,,_29,,,_29,,,q,,,U,:,r,;,},Class,gS,{,Constructor,(,),{,Return,;,},},Class,_9,{,},Class,_9_4N_,:,h8Y,{,},<EOF>''',
                101
            )
        )

    def test_461(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A:__{}Class _{}Class I9_:_{Destructor (){} }Class BZ{Constructor (){}Var $9_F:Array [Array [Array [Array [Boolean ,0XE],51],0B1_0],0XE];Destructor (){Val T3,M:Int ;} }''',
                '''Class,A,:,__,{,},Class,_,{,},Class,I9_,:,_,{,Destructor,(,),{,},},Class,BZ,{,Constructor,(,),{,},Var,$9_F,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0XE,],,,51,],,,0B10,],,,0XE,],;,Destructor,(,),{,Val,T3,,,M,:,Int,;,},},<EOF>''',
                101
            )
        )

    def test_462(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:B8{Val if,b:Array [Boolean ,0b11000];Var $4W6s__:_;}Class _2:dd{Constructor (__,s:Array [Int ,0x4F];u,Vm:Array [Array [Boolean ,0X55],062]){}Var h:Array [Array [Array [Array [Array [Array [Float ,02_52],99],0XD_F],0x3],0x8],05056];}Class __z:_{}''',
                '''Class,_,:,B8,{,Val,if,,,b,:,Array,[,Boolean,,,0b11000,],;,Var,$4W6s__,:,_,;,},Class,_2,:,dd,{,Constructor,(,__,,,s,:,Array,[,Int,,,0x4F,],;,u,,,Vm,:,Array,[,Array,[,Boolean,,,0X55,],,,062,],),{,},Var,h,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0252,],,,99,],,,0XDF,],,,0x3,],,,0x8,],,,05056,],;,},Class,__z,:,_,{,},<EOF>''',
                101
            )
        )

    def test_463(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Y:_6e8{}Class _{$J(_,_:Array [Array [Array [Boolean ,0xD],0B10],0112];_:Int ;__,_j3:Array [Array [Array [String ,65],0X4D],0B1]){Val M1:T;} }''',
                '''Class,Y,:,_6e8,{,},Class,_,{,$J,(,_,,,_,:,Array,[,Array,[,Array,[,Boolean,,,0xD,],,,0B10,],,,0112,],;,_,:,Int,;,__,,,_j3,:,Array,[,Array,[,Array,[,String,,,65,],,,0X4D,],,,0B1,],),{,Val,M1,:,T,;,},},<EOF>''',
                101
            )
        )

    def test_464(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:__d{}Class x{}Class _B20{Destructor (){Continue ;}Var $_s__3:Array [Int ,0B1];E(){}$__Zh(_:_;Q:X145){} }Class ___0{}''',
                '''Class,_,:,__d,{,},Class,x,{,},Class,_B20,{,Destructor,(,),{,Continue,;,},Var,$_s__3,:,Array,[,Int,,,0B1,],;,E,(,),{,},$__Zh,(,_,:,_,;,Q,:,X145,),{,},},Class,___0,{,},<EOF>''',
                101
            )
        )

    def test_465(self):
        self.assertTrue(
            TestLexer.test(
                '''Class v{Constructor (w,c,_08P,r2:Float ;kk:Array [Array [Int ,0b1_10],0x36];__,wt,P__7:Boolean ){}Var $3:Boolean ;}''',
                '''Class,v,{,Constructor,(,w,,,c,,,_08P,,,r2,:,Float,;,kk,:,Array,[,Array,[,Int,,,0b110,],,,0x36,],;,__,,,wt,,,P__7,:,Boolean,),{,},Var,$3,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_466(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:N_{}Class _:_{}Class j_:_{}Class _:z7{}Class S{Val $__8_r,_8CG,$12,d:Array [Array [Array [Array [Array [Array [Boolean ,40],0X12_7_DA],0B111110],0b1000111],0b1000111],0xD];}''',
                '''Class,_,:,N_,{,},Class,_,:,_,{,},Class,j_,:,_,{,},Class,_,:,z7,{,},Class,S,{,Val,$__8_r,,,_8CG,,,$12,,,d,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,40,],,,0X127DA,],,,0B111110,],,,0b1000111,],,,0b1000111,],,,0xD,],;,},<EOF>''',
                101
            )
        )

    def test_467(self):
        self.assertTrue(
            TestLexer.test(
                '''Class O_:o_1_8{Constructor (_:Array [Int ,015];___:Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,0b110001],0xE_5B],0x9],0b110001],47],0b1],0b1],1],0X64];__:Array [String ,015];G,_:String ){Break ;} }''',
                '''Class,O_,:,o_1_8,{,Constructor,(,_,:,Array,[,Int,,,015,],;,___,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b110001,],,,0xE5B,],,,0x9,],,,0b110001,],,,47,],,,0b1,],,,0b1,],,,1,],,,0X64,],;,__,:,Array,[,String,,,015,],;,G,,,_,:,String,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_468(self):
        self.assertTrue(
            TestLexer.test(
                '''Class W3{}Class _9_9t_063_:_{Val O:Array [Array [Float ,02],0X28];}Class y3k{}Class s_7_:KJ2{}Class Y_:_{}Class _4{$WJ(){} }''',
                '''Class,W3,{,},Class,_9_9t_063_,:,_,{,Val,O,:,Array,[,Array,[,Float,,,02,],,,0X28,],;,},Class,y3k,{,},Class,s_7_,:,KJ2,{,},Class,Y_,:,_,{,},Class,_4,{,$WJ,(,),{,},},<EOF>''',
                101
            )
        )

    def test_469(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _6:__{}Class B{Constructor (U:Array [Array [Boolean ,3],0X9];x,_u,_6088xy:c_;_W_6:Boolean ;q:Array [Array [Array [Float ,040],0b10],6_9]){} }Class __{}Class _d1{Constructor (_:Float ;_X:C27;e,eu__n:Array [Array [Boolean ,0b10_1_10_1110],77];l:Array [Boolean ,0B1000011]){} }''',
                '''Class,_6,:,__,{,},Class,B,{,Constructor,(,U,:,Array,[,Array,[,Boolean,,,3,],,,0X9,],;,x,,,_u,,,_6088xy,:,c_,;,_W_6,:,Boolean,;,q,:,Array,[,Array,[,Array,[,Float,,,040,],,,0b10,],,,69,],),{,},},Class,__,{,},Class,_d1,{,Constructor,(,_,:,Float,;,_X,:,C27,;,e,,,eu__n,:,Array,[,Array,[,Boolean,,,0b101101110,],,,77,],;,l,:,Array,[,Boolean,,,0B1000011,],),{,},},<EOF>''',
                101
            )
        )

    def test_470(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:C{v3_1(X:Boolean ;s:_0__a;L,y_,_:Array [Array [Array [String ,032],0b10],87];Q:_G___c){}$_(){}Var $_A,$_4,$bd,$2V,U:Array [Boolean ,0xA];Constructor (Z__:Array [Array [Array [Boolean ,046],1761_8_4_8788],87];__:Array [Float ,05];_,l,_37__,_,_H:Boolean ;I,J8,___1,_:_S){} }''',
                '''Class,_,:,C,{,v3_1,(,X,:,Boolean,;,s,:,_0__a,;,L,,,y_,,,_,:,Array,[,Array,[,Array,[,String,,,032,],,,0b10,],,,87,],;,Q,:,_G___c,),{,},$_,(,),{,},Var,$_A,,,$_4,,,$bd,,,$2V,,,U,:,Array,[,Boolean,,,0xA,],;,Constructor,(,Z__,:,Array,[,Array,[,Array,[,Boolean,,,046,],,,1761848788,],,,87,],;,__,:,Array,[,Float,,,05,],;,_,,,l,,,_37__,,,_,,,_H,:,Boolean,;,I,,,J8,,,___1,,,_,:,_S,),{,},},<EOF>''',
                101
            )
        )

    def test_471(self):
        self.assertTrue(
            TestLexer.test(
                '''Class xjW_{}Class Z__:__{Var $1:Int ;Constructor (_,_:Boolean ;N_:Int ;Y,_R_,__2I:Array [Array [Int ,0X64],27]){} }''',
                '''Class,xjW_,{,},Class,Z__,:,__,{,Var,$1,:,Int,;,Constructor,(,_,,,_,:,Boolean,;,N_,:,Int,;,Y,,,_R_,,,__2I,:,Array,[,Array,[,Int,,,0X64,],,,27,],),{,},},<EOF>''',
                101
            )
        )

    def test_472(self):
        self.assertTrue(
            TestLexer.test(
                '''Class XEM_:_x{Constructor (R_:Array [Boolean ,0B111001];i,I,_,_:_;h1:Array [Boolean ,037];Z,H8_1t6_:_;J:Boolean ;__,A,P0:Float ){} }Class _b{Constructor (K5_:Boolean ;_4:Array [Boolean ,0xE]){ {} }}''',
                '''Class,XEM_,:,_x,{,Constructor,(,R_,:,Array,[,Boolean,,,0B111001,],;,i,,,I,,,_,,,_,:,_,;,h1,:,Array,[,Boolean,,,037,],;,Z,,,H8_1t6_,:,_,;,J,:,Boolean,;,__,,,A,,,P0,:,Float,),{,},},Class,_b,{,Constructor,(,K5_,:,Boolean,;,_4,:,Array,[,Boolean,,,0xE,],),{,{,},},},<EOF>''',
                101
            )
        )

    def test_473(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A{}Class z:X4{_(_8_:Array [Float ,0b1_1];_7qhz:Boolean ;X_e,_,_:Boolean ;q,d:Int ;fxR,_:String ;k,_:Boolean ;L:Array [Array [Float ,12],2_4]){Break ;} }''',
                '''Class,A,{,},Class,z,:,X4,{,_,(,_8_,:,Array,[,Float,,,0b11,],;,_7qhz,:,Boolean,;,X_e,,,_,,,_,:,Boolean,;,q,,,d,:,Int,;,fxR,,,_,:,String,;,k,,,_,:,Boolean,;,L,:,Array,[,Array,[,Float,,,12,],,,24,],),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_474(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X71{Constructor (n,X,s,hM:Array [Array [String ,0b11],9];__p,m,B,_,_:G;zPCh_n,_,i:Array [Array [String ,7],0b11_01];_:Array [Array [Array [Float ,4],0x39],0x39]){} }''',
                '''Class,X71,{,Constructor,(,n,,,X,,,s,,,hM,:,Array,[,Array,[,String,,,0b11,],,,9,],;,__p,,,m,,,B,,,_,,,_,:,G,;,zPCh_n,,,_,,,i,:,Array,[,Array,[,String,,,7,],,,0b1101,],;,_,:,Array,[,Array,[,Array,[,Float,,,4,],,,0x39,],,,0x39,],),{,},},<EOF>''',
                101
            )
        )

    def test_475(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _84{}Class _{Var $7,_,$9,W1_0,t,t:Array [Array [Float ,2_46],24];}Class _{Val T,T:Array [Int ,8];}Class G_q{}''',
                '''Class,_84,{,},Class,_,{,Var,$7,,,_,,,$9,,,W1_0,,,t,,,t,:,Array,[,Array,[,Float,,,246,],,,24,],;,},Class,_,{,Val,T,,,T,:,Array,[,Int,,,8,],;,},Class,G_q,{,},<EOF>''',
                101
            )
        )

    def test_476(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T:V__{}Class __{Val $wz:Array [Float ,071];Destructor (){} }Class _:_B_i1{}Class _:_2JQ_1_{Destructor (){}Var C:Array [Array [String ,03441_3_51_1_0],89];}Class R53{}''',
                '''Class,T,:,V__,{,},Class,__,{,Val,$wz,:,Array,[,Float,,,071,],;,Destructor,(,),{,},},Class,_,:,_B_i1,{,},Class,_,:,_2JQ_1_,{,Destructor,(,),{,},Var,C,:,Array,[,Array,[,String,,,0344135110,],,,89,],;,},Class,R53,{,},<EOF>''',
                101
            )
        )

    def test_477(self):
        self.assertTrue(
            TestLexer.test(
                '''Class F:P_18r{}Class _r{}Class C{Val _v,$_7:Array [Array [String ,053],06_0_43];$F4(){_GL4::$2y().__x();} }Class _{Var _,_N,_,$7,F_:Float ;Constructor (_,P,n,N,_3,_:Array [Array [String ,8_9],638]){} }Class _:_{}''',
                '''Class,F,:,P_18r,{,},Class,_r,{,},Class,C,{,Val,_v,,,$_7,:,Array,[,Array,[,String,,,053,],,,06043,],;,$F4,(,),{,_GL4,::,$2y,(,),.,__x,(,),;,},},Class,_,{,Var,_,,,_N,,,_,,,$7,,,F_,:,Float,;,Constructor,(,_,,,P,,,n,,,N,,,_3,,,_,:,Array,[,Array,[,String,,,89,],,,638,],),{,},},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_478(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n{w(L:Array [Array [Array [Array [Array [Int ,04],0x5_7],40],0B1_1],0B10111];p,Q:Array [Array [Boolean ,0X5B],40];__,_,vw:Array [String ,0144];R:Int ;_,A,V:Int ){} }Class L_b:_b{}Class __3_{}''',
                '''Class,n,{,w,(,L,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,04,],,,0x57,],,,40,],,,0B11,],,,0B10111,],;,p,,,Q,:,Array,[,Array,[,Boolean,,,0X5B,],,,40,],;,__,,,_,,,vw,:,Array,[,String,,,0144,],;,R,:,Int,;,_,,,A,,,V,:,Int,),{,},},Class,L_b,:,_b,{,},Class,__3_,{,},<EOF>''',
                101
            )
        )

    def test_479(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y{Destructor (){}$4(_0,_5,__:_8;_,__,_,__:_A___;v:Array [Array [Array [Array [Array [Boolean ,0B10000],0111],0X8],0X2F_F],7]){}Constructor (_:Array [Boolean ,0111];a,H,G_:Array [Array [Array [Array [Float ,0B110_0],1],3],2_6];___,e_:Int ;A,_,N65,U_,rF:Array [Array [Float ,0xC_7],64_0_7];_7,_,__6,M:Array [Array [Array [Int ,67],0B10000],67]){Continue ;}$03_s8_(){}Var L,Q:Array [Array [Array [Array [Array [Float ,0b1000001],07],0111],4],0111];z(fx977,u:Array [Int ,36_7];R:String ){} }''',
                '''Class,y,{,Destructor,(,),{,},$4,(,_0,,,_5,,,__,:,_8,;,_,,,__,,,_,,,__,:,_A___,;,v,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B10000,],,,0111,],,,0X8,],,,0X2FF,],,,7,],),{,},Constructor,(,_,:,Array,[,Boolean,,,0111,],;,a,,,H,,,G_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B1100,],,,1,],,,3,],,,26,],;,___,,,e_,:,Int,;,A,,,_,,,N65,,,U_,,,rF,:,Array,[,Array,[,Float,,,0xC7,],,,6407,],;,_7,,,_,,,__6,,,M,:,Array,[,Array,[,Array,[,Int,,,67,],,,0B10000,],,,67,],),{,Continue,;,},$03_s8_,(,),{,},Var,L,,,Q,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1000001,],,,07,],,,0111,],,,4,],,,0111,],;,z,(,fx977,,,u,:,Array,[,Int,,,367,],;,R,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_480(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m4D_:Rbw{}Class W{_(){Val _,_,_,_:Array [Boolean ,07];} }Class R2:_{Constructor (_,L_s,_:_6_67_){Continue ;} }''',
                '''Class,m4D_,:,Rbw,{,},Class,W,{,_,(,),{,Val,_,,,_,,,_,,,_,:,Array,[,Boolean,,,07,],;,},},Class,R2,:,_,{,Constructor,(,_,,,L_s,,,_,:,_6_67_,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_481(self):
        self.assertTrue(
            TestLexer.test(
                '''Class U{}Class _{Constructor (){}Constructor (l1:Array [Int ,0X3];_c:Float ){} }Class _I:_{}Class _{}Class Jn_{}''',
                '''Class,U,{,},Class,_,{,Constructor,(,),{,},Constructor,(,l1,:,Array,[,Int,,,0X3,],;,_c,:,Float,),{,},},Class,_I,:,_,{,},Class,_,{,},Class,Jn_,{,},<EOF>''',
                101
            )
        )

    def test_482(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_1{Constructor (M,E,r2,_9,P,_q,_:Array [Array [Array [Array [Boolean ,0b1011011],0623_5_65],0X5D],70]){Break ;} }''',
                '''Class,_,:,_1,{,Constructor,(,M,,,E,,,r2,,,_9,,,P,,,_q,,,_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1011011,],,,0623565,],,,0X5D,],,,70,],),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_483(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b1_4{Val b:_;Destructor (){Return ;}Var $_,ap,Z2_,o:Array [Array [Array [Array [String ,5_1],0b1_1],0X12],0B1];}Class _{Destructor (){} }''',
                '''Class,b1_4,{,Val,b,:,_,;,Destructor,(,),{,Return,;,},Var,$_,,,ap,,,Z2_,,,o,:,Array,[,Array,[,Array,[,Array,[,String,,,51,],,,0b11,],,,0X12,],,,0B1,],;,},Class,_,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_484(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:b{N(P:Int ;_7,Q:kf_;l_:Array [Array [Float ,0x5_7],0X8_6]){}Val __,$_:Array [Array [Array [Float ,0b110],0B1000111],6_2_72];}Class Z87u_:_{}''',
                '''Class,__,:,b,{,N,(,P,:,Int,;,_7,,,Q,:,kf_,;,l_,:,Array,[,Array,[,Float,,,0x57,],,,0X86,],),{,},Val,__,,,$_,:,Array,[,Array,[,Array,[,Float,,,0b110,],,,0B1000111,],,,6272,],;,},Class,Z87u_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_485(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _9_6:LqCY_{Constructor (){}Var $5,$9,$_:Array [Float ,0133];Val i_,$8,$q18,$_,$_k_:Array [Boolean ,04];Val I,$b__9,$2,M,_,$z_:Array [Float ,02];Constructor (Z,__,_,d1,ts,_W,__:n){} }Class q:K_{}''',
                '''Class,_,{,},Class,_9_6,:,LqCY_,{,Constructor,(,),{,},Var,$5,,,$9,,,$_,:,Array,[,Float,,,0133,],;,Val,i_,,,$8,,,$q18,,,$_,,,$_k_,:,Array,[,Boolean,,,04,],;,Val,I,,,$b__9,,,$2,,,M,,,_,,,$z_,:,Array,[,Float,,,02,],;,Constructor,(,Z,,,__,,,_,,,d1,,,ts,,,_W,,,__,:,n,),{,},},Class,q,:,K_,{,},<EOF>''',
                101
            )
        )

    def test_486(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:r5j{Constructor (){Break ;}Constructor (_:String ;_:Array [Array [Array [Array [Float ,02],07],1_6],9];c0,V,L9,a_,_:Float ;f_8,b_:_){ {Continue ;} }}''',
                '''Class,_,:,r5j,{,Constructor,(,),{,Break,;,},Constructor,(,_,:,String,;,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,02,],,,07,],,,16,],,,9,],;,c0,,,V,,,L9,,,a_,,,_,:,Float,;,f_8,,,b_,:,_,),{,{,Continue,;,},},},<EOF>''',
                101
            )
        )

    def test_487(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k:_3{$__4(e__,bqq_,J1,C,__,_mo:_;n_:_f;_,_5_:j8K;XD3,_t:Float ;_,_:_){Return ;}Destructor (){}Destructor (){} }''',
                '''Class,k,:,_3,{,$__4,(,e__,,,bqq_,,,J1,,,C,,,__,,,_mo,:,_,;,n_,:,_f,;,_,,,_5_,:,j8K,;,XD3,,,_t,:,Float,;,_,,,_,:,_,),{,Return,;,},Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_488(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P{}Class _{Var J,_:_;}Class A6{}Class _{j(_4,E,C:Array [Array [Int ,050],050]){}Var $H8:Array [String ,3];Constructor (){} }''',
                '''Class,P,{,},Class,_,{,Var,J,,,_,:,_,;,},Class,A6,{,},Class,_,{,j,(,_4,,,E,,,C,:,Array,[,Array,[,Int,,,050,],,,050,],),{,},Var,$H8,:,Array,[,String,,,3,],;,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_489(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:i{Val $__:rdx3;$8(){}Constructor (){}Constructor (_:Array [Boolean ,02];_1,_b_:Array [String ,0x55]){} }''',
                '''Class,_,:,i,{,Val,$__,:,rdx3,;,$8,(,),{,},Constructor,(,),{,},Constructor,(,_,:,Array,[,Boolean,,,02,],;,_1,,,_b_,:,Array,[,String,,,0x55,],),{,},},<EOF>''',
                101
            )
        )

    def test_490(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k{}Class Y:_RL{Constructor (_,_5x,OZ_:Array [Array [String ,0121],4]){}Destructor (){}Val Z7,$l_,F4,$0,$QY2:Array [Array [String ,4],0B1_10];}''',
                '''Class,k,{,},Class,Y,:,_RL,{,Constructor,(,_,,,_5x,,,OZ_,:,Array,[,Array,[,String,,,0121,],,,4,],),{,},Destructor,(,),{,},Val,Z7,,,$l_,,,F4,,,$0,,,$QY2,:,Array,[,Array,[,String,,,4,],,,0B110,],;,},<EOF>''',
                101
            )
        )

    def test_491(self):
        self.assertTrue(
            TestLexer.test(
                '''Class r_8R4_{}Class v{Val _c5:String ;_(mqsRP_,___,p__5:Array [Array [Array [Float ,86],54],0x9]){Break ;}Constructor (v,q,g3F,B,g,k3:B_E;Z11,_j,O:g){}Destructor (){} }''',
                '''Class,r_8R4_,{,},Class,v,{,Val,_c5,:,String,;,_,(,mqsRP_,,,___,,,p__5,:,Array,[,Array,[,Array,[,Float,,,86,],,,54,],,,0x9,],),{,Break,;,},Constructor,(,v,,,q,,,g3F,,,B,,,g,,,k3,:,B_E,;,Z11,,,_j,,,O,:,g,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_492(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2_:s{Constructor (_,_:String ;_G:_;n0:b){Continue ;}$pi_(B,_9:String ;__T5e,m_,V,M,_G,b:W;__4,_,_rU:_){} }''',
                '''Class,_2_,:,s,{,Constructor,(,_,,,_,:,String,;,_G,:,_,;,n0,:,b,),{,Continue,;,},$pi_,(,B,,,_9,:,String,;,__T5e,,,m_,,,V,,,M,,,_G,,,b,:,W,;,__4,,,_,,,_rU,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_493(self):
        self.assertTrue(
            TestLexer.test(
                '''Class EB{}Class W{Destructor (){} }Class _{Constructor (V1,__2W_uLJ,_o:Array [Array [Array [Array [Array [Boolean ,0X52],0xB],0b1100010],62],0X52];_f1:_7;C:Int ){} }''',
                '''Class,EB,{,},Class,W,{,Destructor,(,),{,},},Class,_,{,Constructor,(,V1,,,__2W_uLJ,,,_o,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X52,],,,0xB,],,,0b1100010,],,,62,],,,0X52,],;,_f1,:,_7,;,C,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_494(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A{}Class e:___5{Var _:Array [Array [Array [Int ,0X2],06],0XC];}Class l6p7_:L_{Constructor (){} }Class _3Z_{}Class _:c_{$_f(v:Int ){}Val _I,v_O,o5:Array [Int ,010];Var _6,_,$9t_M:Int ;}''',
                '''Class,A,{,},Class,e,:,___5,{,Var,_,:,Array,[,Array,[,Array,[,Int,,,0X2,],,,06,],,,0XC,],;,},Class,l6p7_,:,L_,{,Constructor,(,),{,},},Class,_3Z_,{,},Class,_,:,c_,{,$_f,(,v,:,Int,),{,},Val,_I,,,v_O,,,o5,:,Array,[,Int,,,010,],;,Var,_6,,,_,,,$9t_M,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_495(self):
        self.assertTrue(
            TestLexer.test(
                '''Class BjlR1:J{Destructor (){}Var _,$d_m:Array [String ,0121];__V(M2dx,_Z,K2T2:_Z){Continue ;{Continue ;Break ;Break ;} }}''',
                '''Class,BjlR1,:,J,{,Destructor,(,),{,},Var,_,,,$d_m,:,Array,[,String,,,0121,],;,__V,(,M2dx,,,_Z,,,K2T2,:,_Z,),{,Continue,;,{,Continue,;,Break,;,Break,;,},},},<EOF>''',
                101
            )
        )

    def test_496(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X:L{}Class _I7:_{Destructor (){}Val k:Array [Array [Array [Array [Array [Array [Int ,0X2B],6_7],90],04],0X2B],0xF];}''',
                '''Class,X,:,L,{,},Class,_I7,:,_,{,Destructor,(,),{,},Val,k,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0X2B,],,,67,],,,90,],,,04,],,,0X2B,],,,0xF,],;,},<EOF>''',
                101
            )
        )

    def test_497(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _n:_{}Class _:_{Nc4(y,Y,T__:Array [String ,0b1_001];_,A5:String ;_6_E,_V,kp7I,h_,v:Array [Array [Array [Array [Boolean ,5],04_4_17],0B10110],0b1100011];_b218,B,_:Array [Array [Array [Array [Array [Float ,6_2],65],0143],0B1],0xB]){} }''',
                '''Class,_n,:,_,{,},Class,_,:,_,{,Nc4,(,y,,,Y,,,T__,:,Array,[,String,,,0b1001,],;,_,,,A5,:,String,;,_6_E,,,_V,,,kp7I,,,h_,,,v,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,5,],,,04417,],,,0B10110,],,,0b1100011,],;,_b218,,,B,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,62,],,,65,],,,0143,],,,0B1,],,,0xB,],),{,},},<EOF>''',
                101
            )
        )

    def test_498(self):
        self.assertTrue(
            TestLexer.test(
                '''Class U{Val ____rv,$42VQU,__,$_8:Array [Array [Array [Array [Array [Array [Array [Float ,1],0104],0b1],0X8],0B1],57],0B1_1_1_1_1];_(){} }''',
                '''Class,U,{,Val,____rv,,,$42VQU,,,__,,,$_8,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,1,],,,0104,],,,0b1,],,,0X8,],,,0B1,],,,57,],,,0B11111,],;,_,(,),{,},},<EOF>''',
                101
            )
        )

    def test_499(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:u6K{}Class _:u{$9n3(N,__4:String ;_,x:___;_f:_;_:Float ){GV4::$4();} }Class _:U{Var _,$_7:Array [Array [Boolean ,02_2_52_11_35],017];}''',
                '''Class,_,:,u6K,{,},Class,_,:,u,{,$9n3,(,N,,,__4,:,String,;,_,,,x,:,___,;,_f,:,_,;,_,:,Float,),{,GV4,::,$4,(,),;,},},Class,_,:,U,{,Var,_,,,$_7,:,Array,[,Array,[,Boolean,,,022521135,],,,017,],;,},<EOF>''',
                101
            )
        )
