import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_0(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___{}Class __n_{Destructor (){}Constructor (_9,u:__;_,u:_;_:v_2;_37_c,p:Array [Array [Array [Array [Array [String ,044],06],0B1010010],3],0x1]){}Val LI,_L7L:Boolean ;}''',
                '''Class,___,{,},Class,__n_,{,Destructor,(,),{,},Constructor,(,_9,,,u,:,__,;,_,,,u,:,_,;,_,:,v_2,;,_37_c,,,p,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,044,],,,06,],,,0B1010010,],,,3,],,,0x1,],),{,},Val,LI,,,_L7L,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_1(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var __,_9:_;$_(_,R,_,_z_0_k:_;_8:Int ;S_7:Array [Array [Array [Boolean ,03_4],03_10],05];P0,_7,h,_:Array [String ,063];___O_,_:_;j:Boolean ){} }Class T{}''',
                '''Class,_,{,Var,__,,,_9,:,_,;,$_,(,_,,,R,,,_,,,_z_0_k,:,_,;,_8,:,Int,;,S_7,:,Array,[,Array,[,Array,[,Boolean,,,034,],,,0310,],,,05,],;,P0,,,_7,,,h,,,_,:,Array,[,String,,,063,],;,___O_,,,_,:,_,;,j,:,Boolean,),{,},},Class,T,{,},<EOF>''',
                101
            )
        )

    def test_2(self):
        self.assertTrue(
            TestLexer.test(
                '''Class p:_{Destructor (){}$Q(_1,_2_:Int ;_:Array [Array [Boolean ,0X4C],02_6];r,r,G_:Array [Array [Array [Array [Float ,0XB_90_E_2_D1],0b110110],89],89];_:Int ){} }''',
                '''Class,p,:,_,{,Destructor,(,),{,},$Q,(,_1,,,_2_,:,Int,;,_,:,Array,[,Array,[,Boolean,,,0X4C,],,,026,],;,r,,,r,,,G_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0XB90E2D1,],,,0b110110,],,,89,],,,89,],;,_,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_3(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:r37p{u0(o,f,I_X:Array [Boolean ,95];___,La,_:Float ){Break ;} }Class _q4X6:n7{Val $20Q,En,_,B_S:Float ;Destructor (){}Destructor (){ {} }}''',
                '''Class,_,:,r37p,{,u0,(,o,,,f,,,I_X,:,Array,[,Boolean,,,95,],;,___,,,La,,,_,:,Float,),{,Break,;,},},Class,_q4X6,:,n7,{,Val,$20Q,,,En,,,_,,,B_S,:,Float,;,Destructor,(,),{,},Destructor,(,),{,{,},},},<EOF>''',
                101
            )
        )

    def test_4(self):
        self.assertTrue(
            TestLexer.test(
                '''Class f50:_2_c_{_2(){Continue ;}$_0(_:q){Break ;}Constructor (){} }Class h:C2z{$z(___:Int ){ {} }}Class rl__{Constructor (_,_6:Array [Array [Array [Array [Array [Float ,020],0b100101],7],9],0b100101]){} }Class m:e_{Val $v:Int ;Val $9:Array [Boolean ,0B1101];}''',
                '''Class,f50,:,_2_c_,{,_2,(,),{,Continue,;,},$_0,(,_,:,q,),{,Break,;,},Constructor,(,),{,},},Class,h,:,C2z,{,$z,(,___,:,Int,),{,{,},},},Class,rl__,{,Constructor,(,_,,,_6,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,020,],,,0b100101,],,,7,],,,9,],,,0b100101,],),{,},},Class,m,:,e_,{,Val,$v,:,Int,;,Val,$9,:,Array,[,Boolean,,,0B1101,],;,},<EOF>''',
                101
            )
        )

    def test_5(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q_:Ps{}Class _7{_(N,E_,_,_,R:Array [Array [String ,0144],0xE];g,F,b,T9,_:Array [Float ,8];f:_;_,_:Boolean ){}Constructor (){} }Class _8:_qa{}''',
                '''Class,q_,:,Ps,{,},Class,_7,{,_,(,N,,,E_,,,_,,,_,,,R,:,Array,[,Array,[,String,,,0144,],,,0xE,],;,g,,,F,,,b,,,T9,,,_,:,Array,[,Float,,,8,],;,f,:,_,;,_,,,_,:,Boolean,),{,},Constructor,(,),{,},},Class,_8,:,_qa,{,},<EOF>''',
                101
            )
        )

    def test_6(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_3{$9_(_F,z,p:__){}Constructor (H8:_4_;c83___,_:Boolean ;m_,_,_:Float ;__,_,__J_,_,D,___:Array [String ,0x7_8];a80AG,S,_,_:Array [Array [Array [String ,5_5_2],93],93]){}Destructor (){} }''',
                '''Class,_,:,_3,{,$9_,(,_F,,,z,,,p,:,__,),{,},Constructor,(,H8,:,_4_,;,c83___,,,_,:,Boolean,;,m_,,,_,,,_,:,Float,;,__,,,_,,,__J_,,,_,,,D,,,___,:,Array,[,String,,,0x78,],;,a80AG,,,S,,,_,,,_,:,Array,[,Array,[,Array,[,String,,,552,],,,93,],,,93,],),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_7(self):
        self.assertTrue(
            TestLexer.test(
                '''Class O{Constructor (Nz_,d,_:_l){Var Ii59,_,_1_:Boolean ;Break ;}M(){}Var tx:Array [Int ,0x6_8];Constructor (){}Destructor (){} }Class _l{}''',
                '''Class,O,{,Constructor,(,Nz_,,,d,,,_,:,_l,),{,Var,Ii59,,,_,,,_1_,:,Boolean,;,Break,;,},M,(,),{,},Var,tx,:,Array,[,Int,,,0x68,],;,Constructor,(,),{,},Destructor,(,),{,},},Class,_l,{,},<EOF>''',
                101
            )
        )

    def test_8(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ____{Var _6:Array [Array [Array [String ,56],56],85];$7(_D5:Array [Float ,0X18];t:Array [Array [Array [Array [Int ,0B1001111],56],0X98_D_3_4],0X18];_,EY,mK,_,_4v0:Array [Array [Array [Int ,0X18],33],56];_,S2_3__,_,L:s3;_Z4Z43_:Boolean ){} }''',
                '''Class,____,{,Var,_6,:,Array,[,Array,[,Array,[,String,,,56,],,,56,],,,85,],;,$7,(,_D5,:,Array,[,Float,,,0X18,],;,t,:,Array,[,Array,[,Array,[,Array,[,Int,,,0B1001111,],,,56,],,,0X98D34,],,,0X18,],;,_,,,EY,,,mK,,,_,,,_4v0,:,Array,[,Array,[,Array,[,Int,,,0X18,],,,33,],,,56,],;,_,,,S2_3__,,,_,,,L,:,s3,;,_Z4Z43_,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_9(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y{}Class S75h_7_v6{Constructor (__:Boolean ){Var _6,O,_1__,__:Array [Array [Array [Float ,0b1],0b1001001],0B1111];} }''',
                '''Class,y,{,},Class,S75h_7_v6,{,Constructor,(,__,:,Boolean,),{,Var,_6,,,O,,,_1__,,,__,:,Array,[,Array,[,Array,[,Float,,,0b1,],,,0b1001001,],,,0B1111,],;,},},<EOF>''',
                101
            )
        )

    def test_10(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:O{m_(xh:Array [String ,20];_2:Array [Array [Boolean ,0XC],0B101111]){ {} }$_(_,_,U,i0_:Array [Array [String ,05],03];w__v_,_,I,GW,T_,_i:Array [Array [Array [Array [Int ,0x2],66],735],06]){} }Class _1{}''',
                '''Class,__,:,O,{,m_,(,xh,:,Array,[,String,,,20,],;,_2,:,Array,[,Array,[,Boolean,,,0XC,],,,0B101111,],),{,{,},},$_,(,_,,,_,,,U,,,i0_,:,Array,[,Array,[,String,,,05,],,,03,],;,w__v_,,,_,,,I,,,GW,,,T_,,,_i,:,Array,[,Array,[,Array,[,Array,[,Int,,,0x2,],,,66,],,,735,],,,06,],),{,},},Class,_1,{,},<EOF>''',
                101
            )
        )

    def test_11(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:___{Constructor (){}Var $_:Int ;}Class Q{Destructor (){}Constructor (){Return ;} }Class Q{}Class _{}Class _R{}Class _:__{}Class ___{}Class __:_{}''',
                '''Class,_,:,___,{,Constructor,(,),{,},Var,$_,:,Int,;,},Class,Q,{,Destructor,(,),{,},Constructor,(,),{,Return,;,},},Class,Q,{,},Class,_,{,},Class,_R,{,},Class,_,:,__,{,},Class,___,{,},Class,__,:,_,{,},<EOF>''',
                101
            )
        )

    def test_12(self):
        self.assertTrue(
            TestLexer.test(
                '''Class R_I6:_{Destructor (){}Var _:p;}Class _{$D81m(_,_,h:Array [Array [Boolean ,023],0514]){ {{} }}Var __0R:Int ;}''',
                '''Class,R_I6,:,_,{,Destructor,(,),{,},Var,_,:,p,;,},Class,_,{,$D81m,(,_,,,_,,,h,:,Array,[,Array,[,Boolean,,,023,],,,0514,],),{,{,{,},},},Var,__0R,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_13(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _P{$4(_wO1v,dw,xi__,_,dF:_I;_,_:Array [Array [String ,0b100],071]){} }Class r:_{$_(yy_51:String ;_5,__,_3:Array [Int ,03]){} }''',
                '''Class,_P,{,$4,(,_wO1v,,,dw,,,xi__,,,_,,,dF,:,_I,;,_,,,_,:,Array,[,Array,[,String,,,0b100,],,,071,],),{,},},Class,r,:,_,{,$_,(,yy_51,:,String,;,_5,,,__,,,_3,:,Array,[,Int,,,03,],),{,},},<EOF>''',
                101
            )
        )

    def test_14(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Z6_{_9T7f(__,_x1,W:Array [Array [Boolean ,0b10001],02];d,_:Float ;l_:Float ;R,g_CF,_qz:Array [Array [Array [Array [Float ,0b1],0b1],0b10001],071]){} }''',
                '''Class,Z6_,{,_9T7f,(,__,,,_x1,,,W,:,Array,[,Array,[,Boolean,,,0b10001,],,,02,],;,d,,,_,:,Float,;,l_,:,Float,;,R,,,g_CF,,,_qz,:,Array,[,Array,[,Array,[,Array,[,Float,,,0b1,],,,0b1,],,,0b10001,],,,071,],),{,},},<EOF>''',
                101
            )
        )

    def test_15(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _PI:_{$4(w_y5,z__,I_,_s:g;_,y,_5_r,l_1r,__7,_:_){}$_(_:D;C_:Array [String ,46]){}Var $__:Array [Array [Int ,0b1011],0X1D];}''',
                '''Class,_PI,:,_,{,$4,(,w_y5,,,z__,,,I_,,,_s,:,g,;,_,,,y,,,_5_r,,,l_1r,,,__7,,,_,:,_,),{,},$_,(,_,:,D,;,C_,:,Array,[,String,,,46,],),{,},Var,$__,:,Array,[,Array,[,Int,,,0b1011,],,,0X1D,],;,},<EOF>''',
                101
            )
        )

    def test_16(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Pg_EUI:_{Destructor (){}Constructor (){} }Class _{}Class n0_{Constructor (_,J,c,_9:Boolean ){Var _,__:Float ;}Destructor (){} }''',
                '''Class,Pg_EUI,:,_,{,Destructor,(,),{,},Constructor,(,),{,},},Class,_,{,},Class,n0_,{,Constructor,(,_,,,J,,,c,,,_9,:,Boolean,),{,Var,_,,,__,:,Float,;,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_17(self):
        self.assertTrue(
            TestLexer.test(
                '''Class z:ij{Constructor (){Break ;}Val $NXue_,$_k,p_,$M1:Array [Array [Array [Int ,0b1010100],97],8];Var $_8:Array [Float ,0x5];_(vb_:L___){} }Class _:m{}''',
                '''Class,z,:,ij,{,Constructor,(,),{,Break,;,},Val,$NXue_,,,$_k,,,p_,,,$M1,:,Array,[,Array,[,Array,[,Int,,,0b1010100,],,,97,],,,8,],;,Var,$_8,:,Array,[,Float,,,0x5,],;,_,(,vb_,:,L___,),{,},},Class,_,:,m,{,},<EOF>''',
                101
            )
        )

    def test_18(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $3,$j_:Array [Array [Array [Array [Array [String ,0b1_0],0xB_77B],0b111011],0b111011],0x3];}Class _4Z{$_(e3_0,_2,__:Float ;_,le,W2E,__:G){} }''',
                '''Class,_,{,Val,$3,,,$j_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b10,],,,0xB77B,],,,0b111011,],,,0b111011,],,,0x3,],;,},Class,_4Z,{,$_,(,e3_0,,,_2,,,__,:,Float,;,_,,,le,,,W2E,,,__,:,G,),{,},},<EOF>''',
                101
            )
        )

    def test_19(self):
        self.assertTrue(
            TestLexer.test(
                '''Class dH10_B:_{$y(A9:Array [Array [Array [Array [Array [Int ,07],6_1_5],5_6_58],0X1],07];qz,_K3,_:Array [String ,0B111100]){} }''',
                '''Class,dH10_B,:,_,{,$y,(,A9,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,07,],,,615,],,,5658,],,,0X1,],,,07,],;,qz,,,_K3,,,_,:,Array,[,String,,,0B111100,],),{,},},<EOF>''',
                101
            )
        )

    def test_20(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _4{Constructor (_,_3r,Yq__,m6:N;_:Float ;g7:String ;I,_K:Array [Float ,7]){Val __:Array [Array [Array [String ,0XDE_3_66],01],02];Return ;} }''',
                '''Class,_4,{,Constructor,(,_,,,_3r,,,Yq__,,,m6,:,N,;,_,:,Float,;,g7,:,String,;,I,,,_K,:,Array,[,Float,,,7,],),{,Val,__,:,Array,[,Array,[,Array,[,String,,,0XDE366,],,,01,],,,02,],;,Return,;,},},<EOF>''',
                101
            )
        )

    def test_21(self):
        self.assertTrue(
            TestLexer.test(
                '''Class p:_Q8_F{}Class Q:_j_{Constructor (_:Array [Int ,0XF_5];_91:_){}Destructor (){Qk6::$___();}Constructor (){} }Class _LNe{}Class v{Var $_,T:Array [Int ,0104];_(N:M79T2K_){} }Class _:_{}Class _UL:V2{}Class t{}Class _85:_H5DW{}''',
                '''Class,p,:,_Q8_F,{,},Class,Q,:,_j_,{,Constructor,(,_,:,Array,[,Int,,,0XF5,],;,_91,:,_,),{,},Destructor,(,),{,Qk6,::,$___,(,),;,},Constructor,(,),{,},},Class,_LNe,{,},Class,v,{,Var,$_,,,T,:,Array,[,Int,,,0104,],;,_,(,N,:,M79T2K_,),{,},},Class,_,:,_,{,},Class,_UL,:,V2,{,},Class,t,{,},Class,_85,:,_H5DW,{,},<EOF>''',
                101
            )
        )

    def test_22(self):
        self.assertTrue(
            TestLexer.test(
                '''Class u3:_{chns(_S:Array [Boolean ,0X3B]){} }Class F{Var $1r4r:Array [Array [Boolean ,0X3B],5];}Class Lv{}Class x6{}''',
                '''Class,u3,:,_,{,chns,(,_S,:,Array,[,Boolean,,,0X3B,],),{,},},Class,F,{,Var,$1r4r,:,Array,[,Array,[,Boolean,,,0X3B,],,,5,],;,},Class,Lv,{,},Class,x6,{,},<EOF>''',
                101
            )
        )

    def test_23(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var $_,$_,$__:Int ;Constructor (){}__(p:Array [Int ,5]){} }Class W97:F{Destructor (){}Var _j_:Array [Array [Float ,0XD],42];}Class kj{Destructor (){} }''',
                '''Class,_,{,Var,$_,,,$_,,,$__,:,Int,;,Constructor,(,),{,},__,(,p,:,Array,[,Int,,,5,],),{,},},Class,W97,:,F,{,Destructor,(,),{,},Var,_j_,:,Array,[,Array,[,Float,,,0XD,],,,42,],;,},Class,kj,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_24(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{$c(I:Array [Array [String ,0B1_1_0],0B1];_,_6:Boolean ){ {}Var _:x_;} }Class _26:T{Constructor (grE:Float ){} }Class _{Var $_:Cz6q0_;}''',
                '''Class,_,{,$c,(,I,:,Array,[,Array,[,String,,,0B110,],,,0B1,],;,_,,,_6,:,Boolean,),{,{,},Var,_,:,x_,;,},},Class,_26,:,T,{,Constructor,(,grE,:,Float,),{,},},Class,_,{,Var,$_,:,Cz6q0_,;,},<EOF>''',
                101
            )
        )

    def test_25(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _Hf_B:tW_{Var $_4,___t:_EV_;_(f,_:x_09;l_g_g,q:Float ;y_d_m:Array [Float ,0x24];_z,t,j,d,n:Int ){}Val $_,$O5,l:String ;Var $_,_Bi,$V0:Float ;}''',
                '''Class,_Hf_B,:,tW_,{,Var,$_4,,,___t,:,_EV_,;,_,(,f,,,_,:,x_09,;,l_g_g,,,q,:,Float,;,y_d_m,:,Array,[,Float,,,0x24,],;,_z,,,t,,,j,,,d,,,n,:,Int,),{,},Val,$_,,,$O5,,,l,:,String,;,Var,$_,,,_Bi,,,$V0,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_26(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g{}Class _{}Class _:O{}Class r_B{_(_:_s;_,V:Array [Array [String ,0x9],0b1_1];F5__,Q9Z6,___:Array [Array [Array [Float ,07],01],0B1000010];_,q,Z:Array [Float ,03]){}Var $0B_:T4;}''',
                '''Class,g,{,},Class,_,{,},Class,_,:,O,{,},Class,r_B,{,_,(,_,:,_s,;,_,,,V,:,Array,[,Array,[,String,,,0x9,],,,0b11,],;,F5__,,,Q9Z6,,,___,:,Array,[,Array,[,Array,[,Float,,,07,],,,01,],,,0B1000010,],;,_,,,q,,,Z,:,Array,[,Float,,,03,],),{,},Var,$0B_,:,T4,;,},<EOF>''',
                101
            )
        )

    def test_27(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T2:_{$__(Lw,a__,_,g:Float ;I,p,j,_,_X_:_T_9_;___,_ds:Float ){t::$D.r();{}Break ;}Constructor (__:Float ){} }''',
                '''Class,T2,:,_,{,$__,(,Lw,,,a__,,,_,,,g,:,Float,;,I,,,p,,,j,,,_,,,_X_,:,_T_9_,;,___,,,_ds,:,Float,),{,t,::,$D,.,r,(,),;,{,},Break,;,},Constructor,(,__,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_28(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _6{Val P:_B_;Destructor (){}Var R_819,_UY,$_9,$__:Int ;}Class eH0{}Class __{}Class x1_J5:_{Destructor (){} }Class X:__{}''',
                '''Class,_6,{,Val,P,:,_B_,;,Destructor,(,),{,},Var,R_819,,,_UY,,,$_9,,,$__,:,Int,;,},Class,eH0,{,},Class,__,{,},Class,x1_J5,:,_,{,Destructor,(,),{,},},Class,X,:,__,{,},<EOF>''',
                101
            )
        )

    def test_29(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _4:L{}Class _c:_1{Constructor (S,_d_,I,_:Float ;_,_,_:__){}Var _,$7,$68_,S,l_9v,a5,_jO,__:Array [Boolean ,015];}''',
                '''Class,_4,:,L,{,},Class,_c,:,_1,{,Constructor,(,S,,,_d_,,,I,,,_,:,Float,;,_,,,_,,,_,:,__,),{,},Var,_,,,$7,,,$68_,,,S,,,l_9v,,,a5,,,_jO,,,__,:,Array,[,Boolean,,,015,],;,},<EOF>''',
                101
            )
        )

    def test_30(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __c:I3I{Val _31,_,$30c,$3E,$4D9,$u0_,$Vjb_1,$5:Boolean ;__(q:Array [Array [Array [Array [Boolean ,0b1100000],4],5],5];__,Zj:e){Break ;j__::$W();Return ;}Constructor (_:__8;_2,A_,_:Int ){} }Class H_:___{}''',
                '''Class,__c,:,I3I,{,Val,_31,,,_,,,$30c,,,$3E,,,$4D9,,,$u0_,,,$Vjb_1,,,$5,:,Boolean,;,__,(,q,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1100000,],,,4,],,,5,],,,5,],;,__,,,Zj,:,e,),{,Break,;,j__,::,$W,(,),;,Return,;,},Constructor,(,_,:,__8,;,_2,,,A_,,,_,:,Int,),{,},},Class,H_,:,___,{,},<EOF>''',
                101
            )
        )

    def test_31(self):
        self.assertTrue(
            TestLexer.test(
                '''Class jN:__A_{Constructor (Q7_R_,_:Array [Array [Array [Int ,9_912_9],0X8],0B1];__,e,_,_,_6,_,e2,_,n:Float ){Var o__,_p_s_H6,d,V:Array [Boolean ,0b1];} }Class _{}''',
                '''Class,jN,:,__A_,{,Constructor,(,Q7_R_,,,_,:,Array,[,Array,[,Array,[,Int,,,99129,],,,0X8,],,,0B1,],;,__,,,e,,,_,,,_,,,_6,,,_,,,e2,,,_,,,n,:,Float,),{,Var,o__,,,_p_s_H6,,,d,,,V,:,Array,[,Boolean,,,0b1,],;,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_32(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _5:A49c{}Class LT8mcG4_{_(_:Int ;_,v:Int ;E,_,K:_;i6_df:C_;vLr:Array [Int ,0x6_0_8_8]){Var _:Array [Int ,0X9];}Constructor (_:Float ){} }''',
                '''Class,_5,:,A49c,{,},Class,LT8mcG4_,{,_,(,_,:,Int,;,_,,,v,:,Int,;,E,,,_,,,K,:,_,;,i6_df,:,C_,;,vLr,:,Array,[,Int,,,0x6088,],),{,Var,_,:,Array,[,Int,,,0X9,],;,},Constructor,(,_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_33(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2_{$E_1(__2_U6:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,0B111100],7_2_66],017],0B11],0x5],14],67],1],0B111100],9_1],0111],0B111100],9],0b110100],67]){}$3(WS:Array [String ,0111];mP_N:Array [Array [Array [String ,0x1C],69_7],0b110100]){Return ;} }Class th:bh{Destructor (){}_(){} }''',
                '''Class,_2_,{,$E_1,(,__2_U6,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B111100,],,,7266,],,,017,],,,0B11,],,,0x5,],,,14,],,,67,],,,1,],,,0B111100,],,,91,],,,0111,],,,0B111100,],,,9,],,,0b110100,],,,67,],),{,},$3,(,WS,:,Array,[,String,,,0111,],;,mP_N,:,Array,[,Array,[,Array,[,String,,,0x1C,],,,697,],,,0b110100,],),{,Return,;,},},Class,th,:,bh,{,Destructor,(,),{,},_,(,),{,},},<EOF>''',
                101
            )
        )

    def test_34(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n:_{Val Fzu_:_;RU(__:Array [Float ,650_5]){Return ;} }Class c1:_{Val N__3_8,$t:Array [Array [Int ,0b1_0],0B1001100];}''',
                '''Class,n,:,_,{,Val,Fzu_,:,_,;,RU,(,__,:,Array,[,Float,,,6505,],),{,Return,;,},},Class,c1,:,_,{,Val,N__3_8,,,$t,:,Array,[,Array,[,Int,,,0b10,],,,0B1001100,],;,},<EOF>''',
                101
            )
        )

    def test_35(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C:__p{Val $4,$_2:Int ;Var $G,__v:Array [Array [Float ,0X64],0XE_2];Val z57V,$O:Array [Array [Array [Float ,0XB_B_7],5],5];Val $4R,$_S_,k__2R:Array [Boolean ,7_6_6];}''',
                '''Class,C,:,__p,{,Val,$4,,,$_2,:,Int,;,Var,$G,,,__v,:,Array,[,Array,[,Float,,,0X64,],,,0XE2,],;,Val,z57V,,,$O,:,Array,[,Array,[,Array,[,Float,,,0XBB7,],,,5,],,,5,],;,Val,$4R,,,$_S_,,,k__2R,:,Array,[,Boolean,,,766,],;,},<EOF>''',
                101
            )
        )

    def test_36(self):
        self.assertTrue(
            TestLexer.test(
                '''Class G{Destructor (){}Var _,__,J,$B__76,_6,$4,$j:_;}Class _2d_4{Var $u:String ;}Class __{Var __0:Array [String ,73_5];Val $0_mLA:Array [Int ,1_8_94];}Class _{Destructor (){} }''',
                '''Class,G,{,Destructor,(,),{,},Var,_,,,__,,,J,,,$B__76,,,_6,,,$4,,,$j,:,_,;,},Class,_2d_4,{,Var,$u,:,String,;,},Class,__,{,Var,__0,:,Array,[,String,,,735,],;,Val,$0_mLA,:,Array,[,Int,,,1894,],;,},Class,_,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_37(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:E{}Class I{Constructor (){ {} }}Class F{}Class _AD{Val $6:Array [Boolean ,50];}Class rSr:f_Q{}Class Y{Var _p69_7,_,U:Boolean ;}''',
                '''Class,_,:,E,{,},Class,I,{,Constructor,(,),{,{,},},},Class,F,{,},Class,_AD,{,Val,$6,:,Array,[,Boolean,,,50,],;,},Class,rSr,:,f_Q,{,},Class,Y,{,Var,_p69_7,,,_,,,U,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_38(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $7:Float ;$0(_:Float ;__G:Array [Int ,02];a,G:Int ;_:Array [Array [Array [Array [String ,8],03],0x3D],66_73_4]){} }''',
                '''Class,_,{,Val,$7,:,Float,;,$0,(,_,:,Float,;,__G,:,Array,[,Int,,,02,],;,a,,,G,:,Int,;,_,:,Array,[,Array,[,Array,[,Array,[,String,,,8,],,,03,],,,0x3D,],,,66734,],),{,},},<EOF>''',
                101
            )
        )

    def test_39(self):
        self.assertTrue(
            TestLexer.test(
                '''Class s_:h8_{m6(_:Array [Array [Array [Float ,0B10_01_1_1],037],26];__,X_8,I64_2_5Ga_:Array [Boolean ,037]){} }Class _{}''',
                '''Class,s_,:,h8_,{,m6,(,_,:,Array,[,Array,[,Array,[,Float,,,0B100111,],,,037,],,,26,],;,__,,,X_8,,,I64_2_5Ga_,:,Array,[,Boolean,,,037,],),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_40(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___{}Class _2W4___2{}Class Fm{Constructor (bm51:Array [Array [Int ,1],05_7]){} }Class y4:_9{_(Y:H;__,yd,_,_T,_:k;qOF,_L5,_4:_11){}Val $___6t_,_:Array [Boolean ,0B1];Val __:D;$1_(){} }Class Br{_V(f_,_,_,_:Sk_4){}Constructor (C,L:Array [Boolean ,0b110101]){} }''',
                '''Class,___,{,},Class,_2W4___2,{,},Class,Fm,{,Constructor,(,bm51,:,Array,[,Array,[,Int,,,1,],,,057,],),{,},},Class,y4,:,_9,{,_,(,Y,:,H,;,__,,,yd,,,_,,,_T,,,_,:,k,;,qOF,,,_L5,,,_4,:,_11,),{,},Val,$___6t_,,,_,:,Array,[,Boolean,,,0B1,],;,Val,__,:,D,;,$1_,(,),{,},},Class,Br,{,_V,(,f_,,,_,,,_,,,_,:,Sk_4,),{,},Constructor,(,C,,,L,:,Array,[,Boolean,,,0b110101,],),{,},},<EOF>''',
                101
            )
        )

    def test_41(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E_:_{}Class _:_{_L_n75_I8S_(U7R_Q:Array [Array [String ,0X4C],0X9];i:Array [Array [Boolean ,0X9],0623]){_m::$_();} }''',
                '''Class,E_,:,_,{,},Class,_,:,_,{,_L_n75_I8S_,(,U7R_Q,:,Array,[,Array,[,String,,,0X4C,],,,0X9,],;,i,:,Array,[,Array,[,Boolean,,,0X9,],,,0623,],),{,_m,::,$_,(,),;,},},<EOF>''',
                101
            )
        )

    def test_42(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Constructor (M_n5:Array [Array [Int ,0x20],86]){Break ;Break ;}Val O,H_9,$S:Array [Boolean ,07];Constructor (F:String ;X:Array [String ,0131];t,p:Int ;Q:_){}Var $5144,$4,_:Float ;}''',
                '''Class,_,:,_,{,Constructor,(,M_n5,:,Array,[,Array,[,Int,,,0x20,],,,86,],),{,Break,;,Break,;,},Val,O,,,H_9,,,$S,:,Array,[,Boolean,,,07,],;,Constructor,(,F,:,String,;,X,:,Array,[,String,,,0131,],;,t,,,p,:,Int,;,Q,:,_,),{,},Var,$5144,,,$4,,,_,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_43(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T{$715(){Return ;} }Class p_:_{Val $__,$l2_5:Array [Boolean ,0b1];Destructor (){} }Class F79:_{}Class C:oV{}''',
                '''Class,T,{,$715,(,),{,Return,;,},},Class,p_,:,_,{,Val,$__,,,$l2_5,:,Array,[,Boolean,,,0b1,],;,Destructor,(,),{,},},Class,F79,:,_,{,},Class,C,:,oV,{,},<EOF>''',
                101
            )
        )

    def test_44(self):
        self.assertTrue(
            TestLexer.test(
                '''Class i1_y3:v{Var $5X_G95:Boolean ;}Class _8:m{Var _4,$_k:V_;$4(_M__8_,_,_Ir8_:_){Continue ;}Val $a,$__3__82,H_K3N:Int ;}Class b{Var $9W,_:String ;e(){} }''',
                '''Class,i1_y3,:,v,{,Var,$5X_G95,:,Boolean,;,},Class,_8,:,m,{,Var,_4,,,$_k,:,V_,;,$4,(,_M__8_,,,_,,,_Ir8_,:,_,),{,Continue,;,},Val,$a,,,$__3__82,,,H_K3N,:,Int,;,},Class,b,{,Var,$9W,,,_,:,String,;,e,(,),{,},},<EOF>''',
                101
            )
        )

    def test_45(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _K:_{Constructor (_,P_,w7e9_:String ;_:Float ){} }Class uPh:M{$__(){Break ;Continue ;{}s_::$__4();Val Wp,_1:Array [Array [Array [Float ,031],0X7_D],0B10101];} }Class x:G__{Constructor (__T,I___,G,c__,__v,l_7,_,_,_:Boolean ;GL_,e_:__5){} }''',
                '''Class,_K,:,_,{,Constructor,(,_,,,P_,,,w7e9_,:,String,;,_,:,Float,),{,},},Class,uPh,:,M,{,$__,(,),{,Break,;,Continue,;,{,},s_,::,$__4,(,),;,Val,Wp,,,_1,:,Array,[,Array,[,Array,[,Float,,,031,],,,0X7D,],,,0B10101,],;,},},Class,x,:,G__,{,Constructor,(,__T,,,I___,,,G,,,c__,,,__v,,,l_7,,,_,,,_,,,_,:,Boolean,;,GL_,,,e_,:,__5,),{,},},<EOF>''',
                101
            )
        )

    def test_46(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g9:_97_{}Class _a{Var _xT,$_:Array [Boolean ,0B1];Var $Z,$5,$__:Boolean ;}Class __T{Constructor (){Continue ;} }Class QVj:T1_{}''',
                '''Class,g9,:,_97_,{,},Class,_a,{,Var,_xT,,,$_,:,Array,[,Boolean,,,0B1,],;,Var,$Z,,,$5,,,$__,:,Boolean,;,},Class,__T,{,Constructor,(,),{,Continue,;,},},Class,QVj,:,T1_,{,},<EOF>''',
                101
            )
        )

    def test_47(self):
        self.assertTrue(
            TestLexer.test(
                '''Class S:_{Var _25_:String ;$I(__:Array [Int ,0b1]){}Constructor (){}Var $8,$P,___:Array [Int ,0b1_1_1];Val $0:String ;Var K,$u,$ZA7:Array [Array [Int ,0B1100010],0X1_E];}Class _2:_6{}''',
                '''Class,S,:,_,{,Var,_25_,:,String,;,$I,(,__,:,Array,[,Int,,,0b1,],),{,},Constructor,(,),{,},Var,$8,,,$P,,,___,:,Array,[,Int,,,0b111,],;,Val,$0,:,String,;,Var,K,,,$u,,,$ZA7,:,Array,[,Array,[,Int,,,0B1100010,],,,0X1E,],;,},Class,_2,:,_6,{,},<EOF>''',
                101
            )
        )

    def test_48(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Bngw4c:_{}Class _X_M{Val $4:Array [Array [Float ,0XE_A],392];}Class _{}Class _:g{Val $L,$5_6,$0,_QX9_,t:Array [Array [Array [Boolean ,02],0b1_1],0B101101];}''',
                '''Class,Bngw4c,:,_,{,},Class,_X_M,{,Val,$4,:,Array,[,Array,[,Float,,,0XEA,],,,392,],;,},Class,_,{,},Class,_,:,g,{,Val,$L,,,$5_6,,,$0,,,_QX9_,,,t,:,Array,[,Array,[,Array,[,Boolean,,,02,],,,0b11,],,,0B101101,],;,},<EOF>''',
                101
            )
        )

    def test_49(self):
        self.assertTrue(
            TestLexer.test(
                '''Class yG_62V:s0o{Constructor (_,k,_:_;Y3:CO;_:f60f){Val __6B:Int ;}Constructor (){}Var _:Array [Boolean ,0X48];Constructor (_ZK9:Int ;s:Array [Array [Int ,07],05_0_5]){} }Class _:__U0{}Class Zr_gJ6{}Class VG3{}Class C:f{Destructor (){}Constructor (o,h:Array [Array [Float ,0B11111],20];_,C,_s3g_,_,_,a,a:L){}Var X,$84s:L5P;Var h_,$_,$5U8_v,mNk,s:__W;}''',
                '''Class,yG_62V,:,s0o,{,Constructor,(,_,,,k,,,_,:,_,;,Y3,:,CO,;,_,:,f60f,),{,Val,__6B,:,Int,;,},Constructor,(,),{,},Var,_,:,Array,[,Boolean,,,0X48,],;,Constructor,(,_ZK9,:,Int,;,s,:,Array,[,Array,[,Int,,,07,],,,0505,],),{,},},Class,_,:,__U0,{,},Class,Zr_gJ6,{,},Class,VG3,{,},Class,C,:,f,{,Destructor,(,),{,},Constructor,(,o,,,h,:,Array,[,Array,[,Float,,,0B11111,],,,20,],;,_,,,C,,,_s3g_,,,_,,,_,,,a,,,a,:,L,),{,},Var,X,,,$84s,:,L5P,;,Var,h_,,,$_,,,$5U8_v,,,mNk,,,s,:,__W,;,},<EOF>''',
                101
            )
        )

    def test_50(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___{$M5S(g,_,pS,_2,_5,_0:Array [Array [Int ,04_6],6_4_1]){Val _,_qd_,_9ck,_8:Array [Array [Float ,58],0X7];} }''',
                '''Class,___,{,$M5S,(,g,,,_,,,pS,,,_2,,,_5,,,_0,:,Array,[,Array,[,Int,,,046,],,,641,],),{,Val,_,,,_qd_,,,_9ck,,,_8,:,Array,[,Array,[,Float,,,58,],,,0X7,],;,},},<EOF>''',
                101
            )
        )

    def test_51(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:Y{}Class _:VO_BTF7{Var __6:Array [Int ,0b1000010];__(G,___,Y:d4;_:_;_:Array [Array [Array [Int ,4],02],0b1000010];hC,_,m:Boolean ){} }''',
                '''Class,_,:,Y,{,},Class,_,:,VO_BTF7,{,Var,__6,:,Array,[,Int,,,0b1000010,],;,__,(,G,,,___,,,Y,:,d4,;,_,:,_,;,_,:,Array,[,Array,[,Array,[,Int,,,4,],,,02,],,,0b1000010,],;,hC,,,_,,,m,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_52(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8{}Class _d__6d:__660i{}Class _m:_{Var _,X6wPe:Array [Boolean ,0x49];Var t_7,__:Array [Array [Boolean ,0107],0B1];Val $C1,$T7:Float ;}''',
                '''Class,_8,{,},Class,_d__6d,:,__660i,{,},Class,_m,:,_,{,Var,_,,,X6wPe,:,Array,[,Boolean,,,0x49,],;,Var,t_7,,,__,:,Array,[,Array,[,Boolean,,,0107,],,,0B1,],;,Val,$C1,,,$T7,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_53(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _796:S_N9B9__2{Destructor (){Continue ;Break ;}Var _:Boolean ;Val $z,$M2:Array [Array [Array [Array [Float ,07],0B1001],0x4A],07];Var _C_:Float ;}''',
                '''Class,_796,:,S_N9B9__2,{,Destructor,(,),{,Continue,;,Break,;,},Var,_,:,Boolean,;,Val,$z,,,$M2,:,Array,[,Array,[,Array,[,Array,[,Float,,,07,],,,0B1001,],,,0x4A,],,,07,],;,Var,_C_,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_54(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n{_(__,j_,__5C,H_C_,__56:String ;z:String ;__:_;_40_:String ){}Var $l_u54H:Array [Array [Array [Array [Float ,66],0131],0b110000],0131];}''',
                '''Class,n,{,_,(,__,,,j_,,,__5C,,,H_C_,,,__56,:,String,;,z,:,String,;,__,:,_,;,_40_,:,String,),{,},Var,$l_u54H,:,Array,[,Array,[,Array,[,Array,[,Float,,,66,],,,0131,],,,0b110000,],,,0131,],;,},<EOF>''',
                101
            )
        )

    def test_55(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class e8:__7{}Class N0_1q{Constructor (x,f2c,i5:Int ;_,_,km4,y_:_y_){}Destructor (){} }Class __{}Class _j{}''',
                '''Class,__,{,},Class,e8,:,__7,{,},Class,N0_1q,{,Constructor,(,x,,,f2c,,,i5,:,Int,;,_,,,_,,,km4,,,y_,:,_y_,),{,},Destructor,(,),{,},},Class,__,{,},Class,_j,{,},<EOF>''',
                101
            )
        )

    def test_56(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{E_(_g0:Array [Array [Float ,0XC_D],5]){}_(U6,_,O,c0mVU,o:String ;_,_XQ:Array [String ,02_6];U:Array [Array [Int ,0100],0xFB_7_B_9_A_BC];_:Array [String ,0100];_4:Array [String ,5];c,S_5,_,_:Array [Array [Boolean ,1123],0B1]){ {} }}''',
                '''Class,_,{,E_,(,_g0,:,Array,[,Array,[,Float,,,0XCD,],,,5,],),{,},_,(,U6,,,_,,,O,,,c0mVU,,,o,:,String,;,_,,,_XQ,:,Array,[,String,,,026,],;,U,:,Array,[,Array,[,Int,,,0100,],,,0xFB7B9ABC,],;,_,:,Array,[,String,,,0100,],;,_4,:,Array,[,String,,,5,],;,c,,,S_5,,,_,,,_,:,Array,[,Array,[,Boolean,,,1123,],,,0B1,],),{,{,},},},<EOF>''',
                101
            )
        )

    def test_57(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class __30o_U2{Constructor (_:Float ;A:Array [Boolean ,0b1010100];_,_,_:Float ;B_1:Boolean ){}Destructor (){Continue ;}Destructor (){}Var $3:__S5;Val $_D,$l:Array [Array [Array [Array [Float ,057],0B1],5],0x29];}''',
                '''Class,_,{,},Class,__30o_U2,{,Constructor,(,_,:,Float,;,A,:,Array,[,Boolean,,,0b1010100,],;,_,,,_,,,_,:,Float,;,B_1,:,Boolean,),{,},Destructor,(,),{,Continue,;,},Destructor,(,),{,},Var,$3,:,__S5,;,Val,$_D,,,$l,:,Array,[,Array,[,Array,[,Array,[,Float,,,057,],,,0B1,],,,5,],,,0x29,],;,},<EOF>''',
                101
            )
        )

    def test_58(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _Kl:_{}Class _5{_(){} }Class X_4{Constructor (){}Var ge:Array [Array [Array [Array [Array [Int ,0b1],065],0b11110],72],06];}Class _{}''',
                '''Class,_Kl,:,_,{,},Class,_5,{,_,(,),{,},},Class,X_4,{,Constructor,(,),{,},Var,ge,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0b1,],,,065,],,,0b11110,],,,72,],,,06,],;,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_59(self):
        self.assertTrue(
            TestLexer.test(
                '''Class f{$_42(_:Boolean ;__,b,I_,a_,_,R,f,L6w_9,hn:z;_9,_,__,_:Array [Array [Array [Float ,0X2E],0x13],05]){} }Class o_6{}''',
                '''Class,f,{,$_42,(,_,:,Boolean,;,__,,,b,,,I_,,,a_,,,_,,,R,,,f,,,L6w_9,,,hn,:,z,;,_9,,,_,,,__,,,_,:,Array,[,Array,[,Array,[,Float,,,0X2E,],,,0x13,],,,05,],),{,},},Class,o_6,{,},<EOF>''',
                101
            )
        )

    def test_60(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class _:z8{Val $_____6,_2,A,$m:Array [Int ,75];Var c:Array [Array [Float ,0b101001],0x8_8_5CF12];Constructor (_,F,__:Array [Array [Boolean ,75],043];j,_5:hJ){} }Class _LWQc{}''',
                '''Class,__,{,},Class,_,:,z8,{,Val,$_____6,,,_2,,,A,,,$m,:,Array,[,Int,,,75,],;,Var,c,:,Array,[,Array,[,Float,,,0b101001,],,,0x885CF12,],;,Constructor,(,_,,,F,,,__,:,Array,[,Array,[,Boolean,,,75,],,,043,],;,j,,,_5,:,hJ,),{,},},Class,_LWQc,{,},<EOF>''',
                101
            )
        )

    def test_61(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J0_G:_{$b(){Continue ;}Constructor (){}Constructor (){}Destructor (){}Val $_5,$___8:Array [Array [Int ,0121],0121];}''',
                '''Class,J0_G,:,_,{,$b,(,),{,Continue,;,},Constructor,(,),{,},Constructor,(,),{,},Destructor,(,),{,},Val,$_5,,,$___8,:,Array,[,Array,[,Int,,,0121,],,,0121,],;,},<EOF>''',
                101
            )
        )

    def test_62(self):
        self.assertTrue(
            TestLexer.test(
                '''Class I:_{Destructor (){}Var P:Array [Boolean ,0X2_2];Constructor (_:String ;_h_4,_8:Array [Array [Array [Float ,95],0x9_30_1],0b111110]){} }''',
                '''Class,I,:,_,{,Destructor,(,),{,},Var,P,:,Array,[,Boolean,,,0X22,],;,Constructor,(,_,:,String,;,_h_4,,,_8,:,Array,[,Array,[,Array,[,Float,,,95,],,,0x9301,],,,0b111110,],),{,},},<EOF>''',
                101
            )
        )

    def test_63(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _L_{}Class _:_{Constructor (t6Z:Int ;n:Array [Int ,0b110110];_:Float ;ST_R:Float ;_,uj:Array [String ,047];B_5_FIX,_,__,S,L,z,_S3,x_:Int ;__,_0:Array [Float ,0B10_00_01_1_0]){Return !!-"".v._-New Z()._()._()._;} }Class I:_{}''',
                '''Class,_L_,{,},Class,_,:,_,{,Constructor,(,t6Z,:,Int,;,n,:,Array,[,Int,,,0b110110,],;,_,:,Float,;,ST_R,:,Float,;,_,,,uj,:,Array,[,String,,,047,],;,B_5_FIX,,,_,,,__,,,S,,,L,,,z,,,_S3,,,x_,:,Int,;,__,,,_0,:,Array,[,Float,,,0B10000110,],),{,Return,!,!,-,,.,v,.,_,-,New,Z,(,),.,_,(,),.,_,(,),.,_,;,},},Class,I,:,_,{,},<EOF>''',
                101
            )
        )

    def test_64(self):
        self.assertTrue(
            TestLexer.test(
                '''Class O_{Val u,j,$0___5,$K_,I:String ;A_(){}Constructor (_2,_C_,C,_:Array [String ,0x5D]){} }Class _:_{Val $_,$_N:Array [String ,5];}''',
                '''Class,O_,{,Val,u,,,j,,,$0___5,,,$K_,,,I,:,String,;,A_,(,),{,},Constructor,(,_2,,,_C_,,,C,,,_,:,Array,[,String,,,0x5D,],),{,},},Class,_,:,_,{,Val,$_,,,$_N,:,Array,[,String,,,5,],;,},<EOF>''',
                101
            )
        )

    def test_65(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J_{Val $33,$Z:z;Constructor (_X:Z;O_2:Boolean ){Var Q8:_;}Var J:d5;Val _:Array [Array [Array [Array [Array [String ,0B110101],5],0X9_7],015],015];}Class _2_{}''',
                '''Class,J_,{,Val,$33,,,$Z,:,z,;,Constructor,(,_X,:,Z,;,O_2,:,Boolean,),{,Var,Q8,:,_,;,},Var,J,:,d5,;,Val,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B110101,],,,5,],,,0X97,],,,015,],,,015,],;,},Class,_2_,{,},<EOF>''',
                101
            )
        )

    def test_66(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _p:_{}Class _{}Class g{}Class _:S{}Class m_{Var _:Int ;Var $F,_,bnhB10:String ;Destructor (){}Var $d,$r:Array [Array [Boolean ,9],0X53];}''',
                '''Class,_p,:,_,{,},Class,_,{,},Class,g,{,},Class,_,:,S,{,},Class,m_,{,Var,_,:,Int,;,Var,$F,,,_,,,bnhB10,:,String,;,Destructor,(,),{,},Var,$d,,,$r,:,Array,[,Array,[,Boolean,,,9,],,,0X53,],;,},<EOF>''',
                101
            )
        )

    def test_67(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V{qu__(c5:Uj9;l12:Array [Array [Array [Boolean ,071],0x3_7],0b1];d_0:Float ){Continue ;} }Class _:Y2c1M{}''',
                '''Class,V,{,qu__,(,c5,:,Uj9,;,l12,:,Array,[,Array,[,Array,[,Boolean,,,071,],,,0x37,],,,0b1,],;,d_0,:,Float,),{,Continue,;,},},Class,_,:,Y2c1M,{,},<EOF>''',
                101
            )
        )

    def test_68(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g_5:G{_(_,m:Array [Array [Array [Array [Int ,06],0X31],03_0],0X31];O49,W_2_1,_:Array [Array [Array [Float ,06],020],047];_:Array [String ,3]){} }''',
                '''Class,g_5,:,G,{,_,(,_,,,m,:,Array,[,Array,[,Array,[,Array,[,Int,,,06,],,,0X31,],,,030,],,,0X31,],;,O49,,,W_2_1,,,_,:,Array,[,Array,[,Array,[,Float,,,06,],,,020,],,,047,],;,_,:,Array,[,String,,,3,],),{,},},<EOF>''',
                101
            )
        )

    def test_69(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T6:__SB4_{Val $R,$y_:Boolean ;Destructor (){Var _,___:Int ;}Destructor (){}Destructor (){}Val $F,_,_:_;Var $_,__,__,_:Array [Array [Array [Boolean ,0B111100],033],033];}Class _47_4OHZ___{}''',
                '''Class,T6,:,__SB4_,{,Val,$R,,,$y_,:,Boolean,;,Destructor,(,),{,Var,_,,,___,:,Int,;,},Destructor,(,),{,},Destructor,(,),{,},Val,$F,,,_,,,_,:,_,;,Var,$_,,,__,,,__,,,_,:,Array,[,Array,[,Array,[,Boolean,,,0B111100,],,,033,],,,033,],;,},Class,_47_4OHZ___,{,},<EOF>''',
                101
            )
        )

    def test_70(self):
        self.assertTrue(
            TestLexer.test(
                '''Class D_{Var $_,U,$6:Float ;Destructor (){Val r9,_:Array [Array [Array [Array [Float ,05_353_2],65],0b11_0],0xC];Break ;} }''',
                '''Class,D_,{,Var,$_,,,U,,,$6,:,Float,;,Destructor,(,),{,Val,r9,,,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,053532,],,,65,],,,0b110,],,,0xC,],;,Break,;,},},<EOF>''',
                101
            )
        )

    def test_71(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o:y93N_h{}Class K{Constructor (___u_,w,s_:Array [Array [Array [Array [Array [String ,03],057],0x1],0xF1_1_CBE],28];J,nYO,__21o:Int ;g2:Int ;_:X){} }''',
                '''Class,o,:,y93N_h,{,},Class,K,{,Constructor,(,___u_,,,w,,,s_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,03,],,,057,],,,0x1,],,,0xF11CBE,],,,28,],;,J,,,nYO,,,__21o,:,Int,;,g2,:,Int,;,_,:,X,),{,},},<EOF>''',
                101
            )
        )

    def test_72(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __8:_36E{Constructor (tV,_:n_dB8K__w;yt,U_,_,Y,_,R:Array [String ,05]){Continue ;} }Class g:Yr{}Class N_{}Class _{}''',
                '''Class,__8,:,_36E,{,Constructor,(,tV,,,_,:,n_dB8K__w,;,yt,,,U_,,,_,,,Y,,,_,,,R,:,Array,[,String,,,05,],),{,Continue,;,},},Class,g,:,Yr,{,},Class,N_,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_73(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (Xk96,UQ:_;_t:Array [Array [Array [Float ,0b110100],0B1_0],0B1_1_000100_1];_:Array [Array [Float ,03],03]){}Val I_,_,$_3,$__,$2a27,W5,G_t,$P,cR2,Y,_k:Array [Int ,11];}''',
                '''Class,_,{,Constructor,(,Xk96,,,UQ,:,_,;,_t,:,Array,[,Array,[,Array,[,Float,,,0b110100,],,,0B10,],,,0B110001001,],;,_,:,Array,[,Array,[,Float,,,03,],,,03,],),{,},Val,I_,,,_,,,$_3,,,$__,,,$2a27,,,W5,,,G_t,,,$P,,,cR2,,,Y,,,_k,:,Array,[,Int,,,11,],;,},<EOF>''',
                101
            )
        )

    def test_74(self):
        self.assertTrue(
            TestLexer.test(
                '''Class z73{}Class _{Destructor (){} }Class __{Var $_,_:Array [Array [Array [Array [Boolean ,0xB0],014],0b1],04_6_3_5];}Class Q{Constructor (L,g:Array [Int ,0x1F_0];p,_6_:S1;_:Array [Array [Array [Boolean ,0b1_1011_11_1101_0],0B1_10],37];_:Float ){Val B:Int ;} }''',
                '''Class,z73,{,},Class,_,{,Destructor,(,),{,},},Class,__,{,Var,$_,,,_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0xB0,],,,014,],,,0b1,],,,04635,],;,},Class,Q,{,Constructor,(,L,,,g,:,Array,[,Int,,,0x1F0,],;,p,,,_6_,:,S1,;,_,:,Array,[,Array,[,Array,[,Boolean,,,0b110111111010,],,,0B110,],,,37,],;,_,:,Float,),{,Val,B,:,Int,;,},},<EOF>''',
                101
            )
        )

    def test_75(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _244_:_{Constructor (R_:Array [Array [Array [Float ,07_2_2],0136],03];Xa:Float ;_,_91,__:Array [Float ,1]){} }''',
                '''Class,_244_,:,_,{,Constructor,(,R_,:,Array,[,Array,[,Array,[,Float,,,0722,],,,0136,],,,03,],;,Xa,:,Float,;,_,,,_91,,,__,:,Array,[,Float,,,1,],),{,},},<EOF>''',
                101
            )
        )

    def test_76(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b_:P_55G{Var $0,$_:Int ;Destructor (){} }Class _:H{Destructor (){} }Class _w76A{}Class n:_1o_{Val _1U,$__A,$n_8_,_,___:Ny;}''',
                '''Class,b_,:,P_55G,{,Var,$0,,,$_,:,Int,;,Destructor,(,),{,},},Class,_,:,H,{,Destructor,(,),{,},},Class,_w76A,{,},Class,n,:,_1o_,{,Val,_1U,,,$__A,,,$n_8_,,,_,,,___,:,Ny,;,},<EOF>''',
                101
            )
        )

    def test_77(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q_{Constructor (){Continue ;Continue ;}Val $5,$9,ns,z_,$k:String ;}Class _:_{Destructor (){Continue ;}Val _6n_,_,$_,$5,_ZD,$J,$lS_,$4y:Array [Array [Array [Float ,0110],0B101],0B101];Var $s_:__I;}''',
                '''Class,q_,{,Constructor,(,),{,Continue,;,Continue,;,},Val,$5,,,$9,,,ns,,,z_,,,$k,:,String,;,},Class,_,:,_,{,Destructor,(,),{,Continue,;,},Val,_6n_,,,_,,,$_,,,$5,,,_ZD,,,$J,,,$lS_,,,$4y,:,Array,[,Array,[,Array,[,Float,,,0110,],,,0B101,],,,0B101,],;,Var,$s_,:,__I,;,},<EOF>''',
                101
            )
        )

    def test_78(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _1_M{Var _,_,$_k8sV7,$_:Array [Int ,74_0];Constructor (){} }Class B:_{Val $8:Float ;Constructor (_,_1,_Y5,__,_819,__,I1:_1_4){}Destructor (){Var a:D__;Break ;} }''',
                '''Class,_1_M,{,Var,_,,,_,,,$_k8sV7,,,$_,:,Array,[,Int,,,740,],;,Constructor,(,),{,},},Class,B,:,_,{,Val,$8,:,Float,;,Constructor,(,_,,,_1,,,_Y5,,,__,,,_819,,,__,,,I1,:,_1_4,),{,},Destructor,(,),{,Var,a,:,D__,;,Break,;,},},<EOF>''',
                101
            )
        )

    def test_79(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Var Z,$B:US_;Var $L3:Float ;}Class e{D(_6:String ){} }Class _SCX6{X(){} }Class b{Val $_Ip,__7,_1:Boolean ;}''',
                '''Class,_,:,_,{,Var,Z,,,$B,:,US_,;,Var,$L3,:,Float,;,},Class,e,{,D,(,_6,:,String,),{,},},Class,_SCX6,{,X,(,),{,},},Class,b,{,Val,$_Ip,,,__7,,,_1,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_80(self):
        self.assertTrue(
            TestLexer.test(
                '''Class a8:OR{}Class _:_c_{}Class k6:__{_(Z5lCRQ:Array [Array [Array [Array [Array [Array [String ,0x36],67],0X56],21],0x8],0X56]){}D__1(_:F;O_27:Boolean ;__f,__:Int ){} }Class _:_{Constructor (){} }''',
                '''Class,a8,:,OR,{,},Class,_,:,_c_,{,},Class,k6,:,__,{,_,(,Z5lCRQ,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0x36,],,,67,],,,0X56,],,,21,],,,0x8,],,,0X56,],),{,},D__1,(,_,:,F,;,O_27,:,Boolean,;,__f,,,__,:,Int,),{,},},Class,_,:,_,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_81(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:_Y{}Class oP{Constructor (q,_,__:Array [Boolean ,0X59];P7E,_n1_6,r,_:L;_,_Y:String ){} }Class Q_y7:_{Var $__:Boolean ;}Class __{Val z00_,_v6m:_;Var _,_,sZ,SH7W,$l:Array [Array [Array [Boolean ,0x9_1],0X1],0X59];}''',
                '''Class,__,:,_Y,{,},Class,oP,{,Constructor,(,q,,,_,,,__,:,Array,[,Boolean,,,0X59,],;,P7E,,,_n1_6,,,r,,,_,:,L,;,_,,,_Y,:,String,),{,},},Class,Q_y7,:,_,{,Var,$__,:,Boolean,;,},Class,__,{,Val,z00_,,,_v6m,:,_,;,Var,_,,,_,,,sZ,,,SH7W,,,$l,:,Array,[,Array,[,Array,[,Boolean,,,0x91,],,,0X1,],,,0X59,],;,},<EOF>''',
                101
            )
        )

    def test_82(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o_:__{}Class _:h{Constructor (R2,BA:Float ;qZ:Array [Array [Array [Array [Array [Float ,0b11001],0b1],02_0],067],027];_9___:Boolean ){} }Class N_8{Val __K9:Int ;}Class Z:_y1{Constructor (_j_,__0_:_9;_,Y,LQ,__:Array [Array [Array [Array [Int ,0B11_1],6],8],0xDB_C_B]){} }''',
                '''Class,o_,:,__,{,},Class,_,:,h,{,Constructor,(,R2,,,BA,:,Float,;,qZ,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b11001,],,,0b1,],,,020,],,,067,],,,027,],;,_9___,:,Boolean,),{,},},Class,N_8,{,Val,__K9,:,Int,;,},Class,Z,:,_y1,{,Constructor,(,_j_,,,__0_,:,_9,;,_,,,Y,,,LQ,,,__,:,Array,[,Array,[,Array,[,Array,[,Int,,,0B111,],,,6,],,,8,],,,0xDBCB,],),{,},},<EOF>''',
                101
            )
        )

    def test_83(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _Z:_{Val $I:Array [Array [Int ,0140],07];}Class _:c{_(){Q6::$_7();{} }Destructor (){Break ;}Constructor (){}Var r_,_:B;}''',
                '''Class,_Z,:,_,{,Val,$I,:,Array,[,Array,[,Int,,,0140,],,,07,],;,},Class,_,:,c,{,_,(,),{,Q6,::,$_7,(,),;,{,},},Destructor,(,),{,Break,;,},Constructor,(,),{,},Var,r_,,,_,:,B,;,},<EOF>''',
                101
            )
        )

    def test_84(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (){}Val _5_:W;}Class s{Var _Hs,$4n:j;}Class _L:t08{Var v_:String ;Constructor (J,_,z,_:Int ){} }Class g{}''',
                '''Class,_,{,Constructor,(,),{,},Val,_5_,:,W,;,},Class,s,{,Var,_Hs,,,$4n,:,j,;,},Class,_L,:,t08,{,Var,v_,:,String,;,Constructor,(,J,,,_,,,z,,,_,:,Int,),{,},},Class,g,{,},<EOF>''',
                101
            )
        )

    def test_85(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k:v__Lo{Constructor (_1:Array [Array [Array [Array [Int ,04_6_0_24_5_55],0X32],0B1],0XD]){Var _M_:String ;} }''',
                '''Class,k,:,v__Lo,{,Constructor,(,_1,:,Array,[,Array,[,Array,[,Array,[,Int,,,046024555,],,,0X32,],,,0B1,],,,0XD,],),{,Var,_M_,:,String,;,},},<EOF>''',
                101
            )
        )

    def test_86(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _54I{c(_,__b:Array [Array [Int ,0121],063];_,rK:Array [Int ,55];_T:Array [Array [Float ,38],0121];_2m_Y,__,_,r_R13,_:j;a,_83:Int ;gr:Int ){} }''',
                '''Class,_54I,{,c,(,_,,,__b,:,Array,[,Array,[,Int,,,0121,],,,063,],;,_,,,rK,:,Array,[,Int,,,55,],;,_T,:,Array,[,Array,[,Float,,,38,],,,0121,],;,_2m_Y,,,__,,,_,,,r_R13,,,_,:,j,;,a,,,_83,:,Int,;,gr,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_87(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_ly{__La(_H_,_:Boolean ){Continue ;} }Class Dp8:_0_6{$H(U3,_s___98:Array [Array [Float ,0X42],90]){ {{} }}Var $Qc2,_,o_u:Array [Array [Float ,02],90];}''',
                '''Class,_,:,_ly,{,__La,(,_H_,,,_,:,Boolean,),{,Continue,;,},},Class,Dp8,:,_0_6,{,$H,(,U3,,,_s___98,:,Array,[,Array,[,Float,,,0X42,],,,90,],),{,{,{,},},},Var,$Qc2,,,_,,,o_u,:,Array,[,Array,[,Float,,,02,],,,90,],;,},<EOF>''',
                101
            )
        )

    def test_88(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class __Q:_{L1(w:_;_Hg_a,wA:String ;X_:Float ){} }Class _9697:S_{_(b:Float ){}Var $3q:Array [Array [Float ,014],0B1];}Class __:m8{}''',
                '''Class,_,{,},Class,__Q,:,_,{,L1,(,w,:,_,;,_Hg_a,,,wA,:,String,;,X_,:,Float,),{,},},Class,_9697,:,S_,{,_,(,b,:,Float,),{,},Var,$3q,:,Array,[,Array,[,Float,,,014,],,,0B1,],;,},Class,__,:,m8,{,},<EOF>''',
                101
            )
        )

    def test_89(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:h3{$P6(_x:Array [Array [Array [Array [Array [String ,0B11],0X42],0XF],04_7],32];__,x_4H5,P:Array [String ,0b1010010];E:L;_1,____:Boolean ;_:_){}Destructor (){Continue ;} }''',
                '''Class,_,:,h3,{,$P6,(,_x,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B11,],,,0X42,],,,0XF,],,,047,],,,32,],;,__,,,x_4H5,,,P,:,Array,[,String,,,0b1010010,],;,E,:,L,;,_1,,,____,:,Boolean,;,_,:,_,),{,},Destructor,(,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_90(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o:a{}Class C{}Class C_{Var _:Boolean ;$R(){ {Continue ;} }Constructor (__93:Array [Boolean ,0B100]){}$_Bx_(__,__:_){Break ;} }''',
                '''Class,o,:,a,{,},Class,C,{,},Class,C_,{,Var,_,:,Boolean,;,$R,(,),{,{,Continue,;,},},Constructor,(,__93,:,Array,[,Boolean,,,0B100,],),{,},$_Bx_,(,__,,,__,:,_,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_91(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _G{$4(_,X,z,o__,_0:Float ){} }Class __463z42__:L1X{}Class NR0{Constructor (_5F:V;_,_Ef,l_:_B7;_0:String ){} }''',
                '''Class,_G,{,$4,(,_,,,X,,,z,,,o__,,,_0,:,Float,),{,},},Class,__463z42__,:,L1X,{,},Class,NR0,{,Constructor,(,_5F,:,V,;,_,,,_Ef,,,l_,:,_B7,;,_0,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_92(self):
        self.assertTrue(
            TestLexer.test(
                '''Class R_:n__1k{$_2__(_,t,r,_Tg,d,JlK,Z1:s;E,_:Array [Array [Array [Boolean ,0B1010100],0b1_1_1],0b1_1];MyR,__17_w:_;I2q1,_:Array [Array [Float ,3],0133]){ {} }}''',
                '''Class,R_,:,n__1k,{,$_2__,(,_,,,t,,,r,,,_Tg,,,d,,,JlK,,,Z1,:,s,;,E,,,_,:,Array,[,Array,[,Array,[,Boolean,,,0B1010100,],,,0b111,],,,0b11,],;,MyR,,,__17_w,:,_,;,I2q1,,,_,:,Array,[,Array,[,Float,,,3,],,,0133,],),{,{,},},},<EOF>''',
                101
            )
        )

    def test_93(self):
        self.assertTrue(
            TestLexer.test(
                '''Class sj89{Destructor (){} }Class iy_:_9_{Val s,$s,_QP6_83_1,q,$2,$_:String ;}Class k{Destructor (){Return ;} }''',
                '''Class,sj89,{,Destructor,(,),{,},},Class,iy_,:,_9_,{,Val,s,,,$s,,,_QP6_83_1,,,q,,,$2,,,$_,:,String,;,},Class,k,{,Destructor,(,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_94(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Destructor (){}Var $8_,$275,__:_;}Class c:h6irf3_{}Class sR:z9_{Var _:String ;}Class ov3h:y9{Var _,$_,___5:g;}Class _:r{Var $__,$_,Do_x:S;_2_(){} }''',
                '''Class,_,{,Destructor,(,),{,},Var,$8_,,,$275,,,__,:,_,;,},Class,c,:,h6irf3_,{,},Class,sR,:,z9_,{,Var,_,:,String,;,},Class,ov3h,:,y9,{,Var,_,,,$_,,,___5,:,g,;,},Class,_,:,r,{,Var,$__,,,$_,,,Do_x,:,S,;,_2_,(,),{,},},<EOF>''',
                101
            )
        )

    def test_95(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8{}Class K:_{Var $1:Boolean ;Constructor (){__FMNg::$7().O().__()._j().K7()._.__7_();}Val __,W_z:String ;Var $zt1_,_QMiQ_4,$a:Array [Array [Int ,0b10101],3_3_1];}Class _{}''',
                '''Class,_8,{,},Class,K,:,_,{,Var,$1,:,Boolean,;,Constructor,(,),{,__FMNg,::,$7,(,),.,O,(,),.,__,(,),.,_j,(,),.,K7,(,),.,_,.,__7_,(,),;,},Val,__,,,W_z,:,String,;,Var,$zt1_,,,_QMiQ_4,,,$a,:,Array,[,Array,[,Int,,,0b10101,],,,331,],;,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_96(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A9g_wK_:_{Val $c,$4_Mo:Array [Array [Array [Array [Int ,5_65],0B1],0b1],0x6];Var _,$0,$1xh_54:Boolean ;}''',
                '''Class,A9g_wK_,:,_,{,Val,$c,,,$4_Mo,:,Array,[,Array,[,Array,[,Array,[,Int,,,565,],,,0B1,],,,0b1,],,,0x6,],;,Var,_,,,$0,,,$1xh_54,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_97(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var $_,$D,M3dW_15:____;__(h9,t,q,_,_4Vz_:Boolean ;u:GE9;__,__2:_;v:____8_6F){} }Class DL{}Class t:R4{Constructor (_,G:_1O4_;O:Array [Array [Array [Array [Float ,022],022],0b1011],0b1011]){} }''',
                '''Class,_,{,Var,$_,,,$D,,,M3dW_15,:,____,;,__,(,h9,,,t,,,q,,,_,,,_4Vz_,:,Boolean,;,u,:,GE9,;,__,,,__2,:,_,;,v,:,____8_6F,),{,},},Class,DL,{,},Class,t,:,R4,{,Constructor,(,_,,,G,:,_1O4_,;,O,:,Array,[,Array,[,Array,[,Array,[,Float,,,022,],,,022,],,,0b1011,],,,0b1011,],),{,},},<EOF>''',
                101
            )
        )

    def test_98(self):
        self.assertTrue(
            TestLexer.test(
                '''Class i:jH_{Constructor (){_::$8();} }Class _:_{}Class Ya__{}Class E_V:j_{Val $2,$_7_,Ll:Array [Array [Array [Array [Boolean ,07],0x26],040],040];}Class o64{}''',
                '''Class,i,:,jH_,{,Constructor,(,),{,_,::,$8,(,),;,},},Class,_,:,_,{,},Class,Ya__,{,},Class,E_V,:,j_,{,Val,$2,,,$_7_,,,Ll,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,07,],,,0x26,],,,040,],,,040,],;,},Class,o64,{,},<EOF>''',
                101
            )
        )

    def test_99(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w:l_{Var $63,_,$n,$9:T;}Class t_Iz:q6{X(y9,d2:Array [Float ,0xD]){Break ;} }Class BM{Constructor (Jc8,OC,L_3:_0;_,k,c4:E){Return ;Var _7_7j:Dw;} }Class Ah1:_405{}Class s{}Class b7_:_V{}Class f_{}Class C{Var pI,$630,_:Float ;}Class _{}Class m:_{}Class P_9_2:s{Var $5:String ;}''',
                '''Class,w,:,l_,{,Var,$63,,,_,,,$n,,,$9,:,T,;,},Class,t_Iz,:,q6,{,X,(,y9,,,d2,:,Array,[,Float,,,0xD,],),{,Break,;,},},Class,BM,{,Constructor,(,Jc8,,,OC,,,L_3,:,_0,;,_,,,k,,,c4,:,E,),{,Return,;,Var,_7_7j,:,Dw,;,},},Class,Ah1,:,_405,{,},Class,s,{,},Class,b7_,:,_V,{,},Class,f_,{,},Class,C,{,Var,pI,,,$630,,,_,:,Float,;,},Class,_,{,},Class,m,:,_,{,},Class,P_9_2,:,s,{,Var,$5,:,String,;,},<EOF>''',
                101
            )
        )

    def test_100(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Jo{Constructor (v_90:Array [Array [Array [Array [String ,0b1_0],0B1001000],8],0X1C];__,_:Float ;V:_99;G:String ;_:Array [Int ,0X1C]){} }Class U:Y{}''',
                '''Class,Jo,{,Constructor,(,v_90,:,Array,[,Array,[,Array,[,Array,[,String,,,0b10,],,,0B1001000,],,,8,],,,0X1C,],;,__,,,_,:,Float,;,V,:,_99,;,G,:,String,;,_,:,Array,[,Int,,,0X1C,],),{,},},Class,U,:,Y,{,},<EOF>''',
                101
            )
        )

    def test_101(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w{Destructor (){ {Continue ;}Val Y,_:Float ;}Constructor (O:Float ;_N:Array [Array [Int ,48],0X5]){Break ;}Val $8,W23S82vl:Array [Array [Int ,0b10_0_0_1_0],48];}''',
                '''Class,w,{,Destructor,(,),{,{,Continue,;,},Val,Y,,,_,:,Float,;,},Constructor,(,O,:,Float,;,_N,:,Array,[,Array,[,Int,,,48,],,,0X5,],),{,Break,;,},Val,$8,,,W23S82vl,:,Array,[,Array,[,Int,,,0b100010,],,,48,],;,},<EOF>''',
                101
            )
        )

    def test_102(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P2s0:W{Constructor (p:_){}Constructor (U,I:Float ;L:Float ;__,_,_w,_:_1M){} }Class K8{Constructor (){Break ;}Destructor (){} }Class c0:xB_{Destructor (){} }Class i{}Class _3:_{}''',
                '''Class,P2s0,:,W,{,Constructor,(,p,:,_,),{,},Constructor,(,U,,,I,:,Float,;,L,:,Float,;,__,,,_,,,_w,,,_,:,_1M,),{,},},Class,K8,{,Constructor,(,),{,Break,;,},Destructor,(,),{,},},Class,c0,:,xB_,{,Destructor,(,),{,},},Class,i,{,},Class,_3,:,_,{,},<EOF>''',
                101
            )
        )

    def test_103(self):
        self.assertTrue(
            TestLexer.test(
                '''Class u:f41{Var $6,__4_92g,_77,$3EF0,$u,n:Float ;Constructor (__O,cg,k902___9,ox,_,_,f_,C:Array [Array [Int ,0x3F],4];_Np,_nu:V;_,l:Boolean ;__X:_){}Val $9:Array [Boolean ,0b1_1];}''',
                '''Class,u,:,f41,{,Var,$6,,,__4_92g,,,_77,,,$3EF0,,,$u,,,n,:,Float,;,Constructor,(,__O,,,cg,,,k902___9,,,ox,,,_,,,_,,,f_,,,C,:,Array,[,Array,[,Int,,,0x3F,],,,4,],;,_Np,,,_nu,:,V,;,_,,,l,:,Boolean,;,__X,:,_,),{,},Val,$9,:,Array,[,Boolean,,,0b11,],;,},<EOF>''',
                101
            )
        )

    def test_104(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:u{Val q_R_ow8,$5,$_,$_e,$EbGU_:Array [Array [Array [Array [Array [Array [Array [Array [Int ,0x2_A_1A],036],0B1],06],036],0X5C],036],0xF];Destructor (){}Val _1,$_7,t:_;}Class _5:E{}''',
                '''Class,__,:,u,{,Val,q_R_ow8,,,$5,,,$_,,,$_e,,,$EbGU_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x2A1A,],,,036,],,,0B1,],,,06,],,,036,],,,0X5C,],,,036,],,,0xF,],;,Destructor,(,),{,},Val,_1,,,$_7,,,t,:,_,;,},Class,_5,:,E,{,},<EOF>''',
                101
            )
        )

    def test_105(self):
        self.assertTrue(
            TestLexer.test(
                '''Class e___:f{}Class z:_UP{}Class _{Constructor (){} }Class _f:_{$_(){} }Class _:_{$5__(){}$3_9_(M_,pf,_5:__6;_:K1){} }''',
                '''Class,e___,:,f,{,},Class,z,:,_UP,{,},Class,_,{,Constructor,(,),{,},},Class,_f,:,_,{,$_,(,),{,},},Class,_,:,_,{,$5__,(,),{,},$3_9_,(,M_,,,pf,,,_5,:,__6,;,_,:,K1,),{,},},<EOF>''',
                101
            )
        )

    def test_106(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9:_6{$_3641J8__(qq85c,_w311_:_;_,_,M,iT:V_){}Constructor (){}Var $2_OS:Array [Array [Array [Array [String ,0B111011],0B111011],0B1],05];}''',
                '''Class,_9,:,_6,{,$_3641J8__,(,qq85c,,,_w311_,:,_,;,_,,,_,,,M,,,iT,:,V_,),{,},Constructor,(,),{,},Var,$2_OS,:,Array,[,Array,[,Array,[,Array,[,String,,,0B111011,],,,0B111011,],,,0B1,],,,05,],;,},<EOF>''',
                101
            )
        )

    def test_107(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Constructor (l_:Array [Array [Float ,0b1],7_65]){}Val $_,$P37:j_N;G8_I628(v:_;___h_5,_,k_,__,_nN:Array [Array [Int ,0b110101],45]){Continue ;} }''',
                '''Class,_,:,_,{,Constructor,(,l_,:,Array,[,Array,[,Float,,,0b1,],,,765,],),{,},Val,$_,,,$P37,:,j_N,;,G8_I628,(,v,:,_,;,___h_5,,,_,,,k_,,,__,,,_nN,:,Array,[,Array,[,Int,,,0b110101,],,,45,],),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_108(self):
        self.assertTrue(
            TestLexer.test(
                '''Class cyU___:x87__{}Class x{}Class __:G_{Val $_,$4__,$A_J,i7__,$_,_,_:Array [Array [Array [Array [Int ,0X53],0x643F],0X53],0114];Destructor (){} }Class M_0p6q{}''',
                '''Class,cyU___,:,x87__,{,},Class,x,{,},Class,__,:,G_,{,Val,$_,,,$4__,,,$A_J,,,i7__,,,$_,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0X53,],,,0x643F,],,,0X53,],,,0114,],;,Destructor,(,),{,},},Class,M_0p6q,{,},<EOF>''',
                101
            )
        )

    def test_109(self):
        self.assertTrue(
            TestLexer.test(
                '''Class d:V3{Constructor (k3,P__,iQ_1z,L,U,_6,__:Float ;_:Array [Array [Array [Array [Float ,0x43],100],07_05_30],04_6_01_34_2];_J85:Array [Array [Float ,02_0],04];__:_){}Constructor (_V,_:R_){}$z(_:Array [Array [Array [Float ,0134],0B1100011],06]){} }''',
                '''Class,d,:,V3,{,Constructor,(,k3,,,P__,,,iQ_1z,,,L,,,U,,,_6,,,__,:,Float,;,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0x43,],,,100,],,,070530,],,,04601342,],;,_J85,:,Array,[,Array,[,Float,,,020,],,,04,],;,__,:,_,),{,},Constructor,(,_V,,,_,:,R_,),{,},$z,(,_,:,Array,[,Array,[,Array,[,Float,,,0134,],,,0B1100011,],,,06,],),{,},},<EOF>''',
                101
            )
        )

    def test_110(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:h{}Class _{}Class _d4:_{Constructor (q,T:Int ;G:k;P:Boolean ;B_,_6,__,_s_:__;_U,_N3,oP9C,H:h){Continue ;} }''',
                '''Class,_,:,h,{,},Class,_,{,},Class,_d4,:,_,{,Constructor,(,q,,,T,:,Int,;,G,:,k,;,P,:,Boolean,;,B_,,,_6,,,__,,,_s_,:,__,;,_U,,,_N3,,,oP9C,,,H,:,h,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_111(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q:_{_(R:Array [Boolean ,067_4_571]){}Var D_s,_,$B,Ym,$__:Boolean ;Constructor (){}Val $_:Array [Array [Boolean ,0b101110],0b101110];}Class _7:_{}''',
                '''Class,q,:,_,{,_,(,R,:,Array,[,Boolean,,,0674571,],),{,},Var,D_s,,,_,,,$B,,,Ym,,,$__,:,Boolean,;,Constructor,(,),{,},Val,$_,:,Array,[,Array,[,Boolean,,,0b101110,],,,0b101110,],;,},Class,_7,:,_,{,},<EOF>''',
                101
            )
        )

    def test_112(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:___{B(ae,_,_V:Array [Int ,0X47]){}Constructor (_:Float ){ {}Break ;}Constructor (_:Boolean ){Var ObT:Array [Array [String ,0x3C],6];} }''',
                '''Class,_,:,___,{,B,(,ae,,,_,,,_V,:,Array,[,Int,,,0X47,],),{,},Constructor,(,_,:,Float,),{,{,},Break,;,},Constructor,(,_,:,Boolean,),{,Var,ObT,:,Array,[,Array,[,String,,,0x3C,],,,6,],;,},},<EOF>''',
                101
            )
        )

    def test_113(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:hA_{Constructor (z_,Y_V_:_;V:Int ;_,_:_;J_:Float ;n4:_1x8E_;_,R_w_:Int ;_18P_,l06_,w:A;_KQ,_,_,_:Array [Array [Float ,0137],4_6_2]){} }''',
                '''Class,_,:,hA_,{,Constructor,(,z_,,,Y_V_,:,_,;,V,:,Int,;,_,,,_,:,_,;,J_,:,Float,;,n4,:,_1x8E_,;,_,,,R_w_,:,Int,;,_18P_,,,l06_,,,w,:,A,;,_KQ,,,_,,,_,,,_,:,Array,[,Array,[,Float,,,0137,],,,462,],),{,},},<EOF>''',
                101
            )
        )

    def test_114(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _G{Val B_X,$__0:Array [Array [Array [Boolean ,4],0b1_01],0116];Val $r_:String ;Var l:e3;}Class J_:W_1{$5(_f:R_D;WK:Array [Boolean ,0b110100]){} }''',
                '''Class,_G,{,Val,B_X,,,$__0,:,Array,[,Array,[,Array,[,Boolean,,,4,],,,0b101,],,,0116,],;,Val,$r_,:,String,;,Var,l,:,e3,;,},Class,J_,:,W_1,{,$5,(,_f,:,R_D,;,WK,:,Array,[,Boolean,,,0b110100,],),{,},},<EOF>''',
                101
            )
        )

    def test_115(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:V{_(_,_,D5__:Boolean ;P,_M8u_:Array [Array [Array [Array [Array [Array [Boolean ,92_7],9],0B1000000],0b111101],0b111101],0B1000000];F:Array [Float ,0xD]){} }Class _C:_{}''',
                '''Class,_,:,V,{,_,(,_,,,_,,,D5__,:,Boolean,;,P,,,_M8u_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,927,],,,9,],,,0B1000000,],,,0b111101,],,,0b111101,],,,0B1000000,],;,F,:,Array,[,Float,,,0xD,],),{,},},Class,_C,:,_,{,},<EOF>''',
                101
            )
        )

    def test_116(self):
        self.assertTrue(
            TestLexer.test(
                '''Class S:_{Val _9:Array [Int ,0B1010100];Val d,$__:Array [Int ,301_1_65];Destructor (){}Destructor (){Var _2B2,__1,_H2,_:Array [Array [Array [Array [Array [Array [Array [Int ,30],8_44],061],7_1],0124],30],0124];} }''',
                '''Class,S,:,_,{,Val,_9,:,Array,[,Int,,,0B1010100,],;,Val,d,,,$__,:,Array,[,Int,,,301165,],;,Destructor,(,),{,},Destructor,(,),{,Var,_2B2,,,__1,,,_H2,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,30,],,,844,],,,061,],,,71,],,,0124,],,,30,],,,0124,],;,},},<EOF>''',
                101
            )
        )

    def test_117(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:i{Constructor (B,E:Array [Array [String ,0133],01_0_30_77]){Break ;}$gR4(_:Array [Float ,0b1_0]){}$5(_53_N,Y,R5_3v,_X:Int ;C:_04p){ {}Continue ;Continue ;}Constructor (_:__p;q_:Float ){} }''',
                '''Class,__,:,i,{,Constructor,(,B,,,E,:,Array,[,Array,[,String,,,0133,],,,0103077,],),{,Break,;,},$gR4,(,_,:,Array,[,Float,,,0b10,],),{,},$5,(,_53_N,,,Y,,,R5_3v,,,_X,:,Int,;,C,:,_04p,),{,{,},Continue,;,Continue,;,},Constructor,(,_,:,__p,;,q_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_118(self):
        self.assertTrue(
            TestLexer.test(
                '''Class a_20:_{}Class i4D_t_:K_3{Val L:Array [Array [Array [Array [Array [Array [Array [Float ,0B1],0b1_0_1],3],10_06],02],043],0B1_0];}''',
                '''Class,a_20,:,_,{,},Class,i4D_t_,:,K_3,{,Val,L,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B1,],,,0b101,],,,3,],,,1006,],,,02,],,,043,],,,0B10,],;,},<EOF>''',
                101
            )
        )

    def test_119(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:__5{Var $__1V,_:Array [Array [Int ,07],9_20_9];Val _Q,$c,_:Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,031],07],0B10],0B101101],0x19],05_6],0b1],71],0b1];}''',
                '''Class,_,:,__5,{,Var,$__1V,,,_,:,Array,[,Array,[,Int,,,07,],,,9209,],;,Val,_Q,,,$c,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,031,],,,07,],,,0B10,],,,0B101101,],,,0x19,],,,056,],,,0b1,],,,71,],,,0b1,],;,},<EOF>''',
                101
            )
        )

    def test_120(self):
        self.assertTrue(
            TestLexer.test(
                '''Class W_:u{$E8_(__:Array [String ,0b10011];_:Array [Array [Array [Array [Array [String ,0b1],5],0xC],0b1],04]){Continue ;} }Class _:Z{}Class _:__{}''',
                '''Class,W_,:,u,{,$E8_,(,__,:,Array,[,String,,,0b10011,],;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b1,],,,5,],,,0xC,],,,0b1,],,,04,],),{,Continue,;,},},Class,_,:,Z,{,},Class,_,:,__,{,},<EOF>''',
                101
            )
        )

    def test_121(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __1:_m{Destructor (){} }Class uJu:_9_{Var _,Vf_s,g1,l:Array [Array [Boolean ,0x8],0X12];Destructor (){Break ;} }Class _:_{}''',
                '''Class,__1,:,_m,{,Destructor,(,),{,},},Class,uJu,:,_9_,{,Var,_,,,Vf_s,,,g1,,,l,:,Array,[,Array,[,Boolean,,,0x8,],,,0X12,],;,Destructor,(,),{,Break,;,},},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_122(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_5{p3(){Val _,C:G;}Val _,$9F,$I,_:Array [Array [Array [Array [Array [Array [String ,043],4],0b10100],0x32],043],0B1];}Class _PED8h___{Val _5O__:Float ;Val $x_:YsC_;}Class u{Constructor (){} }Class b:x{}Class __q{Destructor (){} }Class _{}''',
                '''Class,_,:,_5,{,p3,(,),{,Val,_,,,C,:,G,;,},Val,_,,,$9F,,,$I,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,043,],,,4,],,,0b10100,],,,0x32,],,,043,],,,0B1,],;,},Class,_PED8h___,{,Val,_5O__,:,Float,;,Val,$x_,:,YsC_,;,},Class,u,{,Constructor,(,),{,},},Class,b,:,x,{,},Class,__q,{,Destructor,(,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_123(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (){}Constructor (_,_P,_,j5,__,_,y_8_,___:Array [Array [Array [Array [Array [Int ,0x20],020],0b11],0b11],020]){ {} }}Class _5y{Destructor (){}Destructor (){} }Class _:V_0__Nl740_4{}Class __3:_{Val __,$5K:Array [Array [Array [Array [String ,14],0b10],0b10],0x20];}Class _{}''',
                '''Class,_,{,Constructor,(,),{,},Constructor,(,_,,,_P,,,_,,,j5,,,__,,,_,,,y_8_,,,___,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x20,],,,020,],,,0b11,],,,0b11,],,,020,],),{,{,},},},Class,_5y,{,Destructor,(,),{,},Destructor,(,),{,},},Class,_,:,V_0__Nl740_4,{,},Class,__3,:,_,{,Val,__,,,$5K,:,Array,[,Array,[,Array,[,Array,[,String,,,14,],,,0b10,],,,0b10,],,,0x20,],;,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_124(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:_68e_X{Var $_1,$7,y:Array [Float ,32];_t(_,I:_;_:Int ;c:Tb2;B_u:String ;_1,b_97,f:Float ){}Var yh,w,_WFD,$2,$_,$42_,$_,$tP,_,_,Q:_8;}''',
                '''Class,__,:,_68e_X,{,Var,$_1,,,$7,,,y,:,Array,[,Float,,,32,],;,_t,(,_,,,I,:,_,;,_,:,Int,;,c,:,Tb2,;,B_u,:,String,;,_1,,,b_97,,,f,:,Float,),{,},Var,yh,,,w,,,_WFD,,,$2,,,$_,,,$42_,,,$_,,,$tP,,,_,,,_,,,Q,:,_8,;,},<EOF>''',
                101
            )
        )

    def test_125(self):
        self.assertTrue(
            TestLexer.test(
                '''Class x{Val $3:String ;}Class _7:j{Val $__9ll3_7:Array [Boolean ,34];}Class _6_{Val $_,$Uc,$d:Array [Array [Boolean ,3],34];Destructor (){Continue ;} }''',
                '''Class,x,{,Val,$3,:,String,;,},Class,_7,:,j,{,Val,$__9ll3_7,:,Array,[,Boolean,,,34,],;,},Class,_6_,{,Val,$_,,,$Uc,,,$d,:,Array,[,Array,[,Boolean,,,3,],,,34,],;,Destructor,(,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_126(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_5{Val $L:Int ;Constructor (){Continue ;Var _,d,_7_,B_,_v:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0B111110],0X2A],0134],0B111110],0X4_48D],0B1_1],0B111110],0134];} }Class _{Var o:Array [Array [Float ,0B111110],0X6];}''',
                '''Class,_,:,_5,{,Val,$L,:,Int,;,Constructor,(,),{,Continue,;,Var,_,,,d,,,_7_,,,B_,,,_v,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B111110,],,,0X2A,],,,0134,],,,0B111110,],,,0X448D,],,,0B11,],,,0B111110,],,,0134,],;,},},Class,_,{,Var,o,:,Array,[,Array,[,Float,,,0B111110,],,,0X6,],;,},<EOF>''',
                101
            )
        )

    def test_127(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t{Constructor (){}Var $8:Array [Int ,0b1101];Constructor (){}Constructor (){Break ;Break ;} }Class _:t{}Class _{}''',
                '''Class,t,{,Constructor,(,),{,},Var,$8,:,Array,[,Int,,,0b1101,],;,Constructor,(,),{,},Constructor,(,),{,Break,;,Break,;,},},Class,_,:,t,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_128(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C31_u8rGl{}Class j2m:__{Constructor (){Continue ;Break ;} }Class _{Destructor (){Return ;Break ;} }Class pU{}''',
                '''Class,C31_u8rGl,{,},Class,j2m,:,__,{,Constructor,(,),{,Continue,;,Break,;,},},Class,_,{,Destructor,(,),{,Return,;,Break,;,},},Class,pU,{,},<EOF>''',
                101
            )
        )

    def test_129(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{$_i(W,_,ci,U,r,__:String ;_:Oa){}Var $H:Float ;$ou05m(q,_,_,_2:Array [Float ,0B1]){}w_r9(_,b__n:String ;E__,H5:h;Nj:__;_,_:H){} }Class u_G0_{}''',
                '''Class,_,{,$_i,(,W,,,_,,,ci,,,U,,,r,,,__,:,String,;,_,:,Oa,),{,},Var,$H,:,Float,;,$ou05m,(,q,,,_,,,_,,,_2,:,Array,[,Float,,,0B1,],),{,},w_r9,(,_,,,b__n,:,String,;,E__,,,H5,:,h,;,Nj,:,__,;,_,,,_,:,H,),{,},},Class,u_G0_,{,},<EOF>''',
                101
            )
        )

    def test_130(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0:X{Constructor (_0,__7,q,_w,_,_:Int ;x5q,bTY,_,u:_;Q6:Boolean ){}Z(___kpU:Array [Array [Boolean ,7],0111];_:_){} }''',
                '''Class,_0,:,X,{,Constructor,(,_0,,,__7,,,q,,,_w,,,_,,,_,:,Int,;,x5q,,,bTY,,,_,,,u,:,_,;,Q6,:,Boolean,),{,},Z,(,___kpU,:,Array,[,Array,[,Boolean,,,7,],,,0111,],;,_,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_131(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $_,A,$G,B,$I:Array [Array [Array [Array [Boolean ,0124],0124],0124],71];}Class n:T__{}Class J_7:X{$2_(P,L,__,_7_:Array [Boolean ,0XE];Av__:Array [Array [Array [String ,71],0124],0xB]){} }''',
                '''Class,_,{,Val,$_,,,A,,,$G,,,B,,,$I,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0124,],,,0124,],,,0124,],,,71,],;,},Class,n,:,T__,{,},Class,J_7,:,X,{,$2_,(,P,,,L,,,__,,,_7_,:,Array,[,Boolean,,,0XE,],;,Av__,:,Array,[,Array,[,Array,[,String,,,71,],,,0124,],,,0xB,],),{,},},<EOF>''',
                101
            )
        )

    def test_132(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _3{Constructor (){Continue ;}Var _:Array [Array [Array [Float ,0115],0x28],0115];_82H(_66:Float ){Break ;}Var _:Array [Array [Array [String ,0B110],0115],0xB_D_31];}Class __{}''',
                '''Class,_,{,},Class,_3,{,Constructor,(,),{,Continue,;,},Var,_,:,Array,[,Array,[,Array,[,Float,,,0115,],,,0x28,],,,0115,],;,_82H,(,_66,:,Float,),{,Break,;,},Var,_,:,Array,[,Array,[,Array,[,String,,,0B110,],,,0115,],,,0xBD31,],;,},Class,__,{,},<EOF>''',
                101
            )
        )

    def test_133(self):
        self.assertTrue(
            TestLexer.test(
                '''Class HJ:lm4_0{c_h(_K,_k_W:_;_,_b_:Array [Array [Array [Array [Array [Boolean ,7],0344],0xFE],076],6_0]){Break ;} }''',
                '''Class,HJ,:,lm4_0,{,c_h,(,_K,,,_k_W,:,_,;,_,,,_b_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,7,],,,0344,],,,0xFE,],,,076,],,,60,],),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_134(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (){} }Class z:_{Val q,rd,__:Array [Array [Array [String ,0XC],0X2F],0X2F];Var $u_:Float ;}Class _PV:L{}''',
                '''Class,_,{,Constructor,(,),{,},},Class,z,:,_,{,Val,q,,,rd,,,__,:,Array,[,Array,[,Array,[,String,,,0XC,],,,0X2F,],,,0X2F,],;,Var,$u_,:,Float,;,},Class,_PV,:,L,{,},<EOF>''',
                101
            )
        )

    def test_135(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __m:_{Constructor (_J,_rl7_8,_:Float ){}Var Ri:Array [Int ,0b1_10];Constructor (_:Array [String ,052];a,_,_v_8:_h58e;_c:Array [Int ,052];m4,_,G_:Mm_b;S:Float ;_:___){} }''',
                '''Class,__m,:,_,{,Constructor,(,_J,,,_rl7_8,,,_,:,Float,),{,},Var,Ri,:,Array,[,Int,,,0b110,],;,Constructor,(,_,:,Array,[,String,,,052,],;,a,,,_,,,_v_8,:,_h58e,;,_c,:,Array,[,Int,,,052,],;,m4,,,_,,,G_,:,Mm_b,;,S,:,Float,;,_,:,___,),{,},},<EOF>''',
                101
            )
        )

    def test_136(self):
        self.assertTrue(
            TestLexer.test(
                '''Class h_s_{Var _,_:E3;Destructor (){} }Class _F_{Var r__,_,cj,_,q_:Array [Array [Int ,0x7],0xC_4];Constructor (__:__){Val _1_z:Array [Array [Boolean ,0b110101],0B1];} }Class d{Constructor (_J:String ){}Var E:_;}''',
                '''Class,h_s_,{,Var,_,,,_,:,E3,;,Destructor,(,),{,},},Class,_F_,{,Var,r__,,,_,,,cj,,,_,,,q_,:,Array,[,Array,[,Int,,,0x7,],,,0xC4,],;,Constructor,(,__,:,__,),{,Val,_1_z,:,Array,[,Array,[,Boolean,,,0b110101,],,,0B1,],;,},},Class,d,{,Constructor,(,_J,:,String,),{,},Var,E,:,_,;,},<EOF>''',
                101
            )
        )

    def test_137(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _PN1:G{}Class O:_ZVV{Var j3:Array [Array [Array [Array [Boolean ,057],0x5],34],0xD_1_BA];}Class _p_:B0{}Class K7:D{___(_:n_){} }''',
                '''Class,_PN1,:,G,{,},Class,O,:,_ZVV,{,Var,j3,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,057,],,,0x5,],,,34,],,,0xD1BA,],;,},Class,_p_,:,B0,{,},Class,K7,:,D,{,___,(,_,:,n_,),{,},},<EOF>''',
                101
            )
        )

    def test_138(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class oh:p{}Class Q{Var $6O:Int ;}Class _0_:_6{Constructor (cV:_;_:Array [Array [String ,91],7];_md,_2,D,T_:_){Continue ;}Val U:Array [Array [Array [Array [Float ,02],0132],0B1000000],0655];Val y,$V,z9:_;}''',
                '''Class,_,{,},Class,oh,:,p,{,},Class,Q,{,Var,$6O,:,Int,;,},Class,_0_,:,_6,{,Constructor,(,cV,:,_,;,_,:,Array,[,Array,[,String,,,91,],,,7,],;,_md,,,_2,,,D,,,T_,:,_,),{,Continue,;,},Val,U,:,Array,[,Array,[,Array,[,Array,[,Float,,,02,],,,0132,],,,0B1000000,],,,0655,],;,Val,y,,,$V,,,z9,:,_,;,},<EOF>''',
                101
            )
        )

    def test_139(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X{}Class __Q_{}Class _mE{_(_,u1,W,z__,__:Array [Array [Array [Array [String ,69],027],0B1],0B10111]){}Val $Y:Array [Array [Float ,0b1_1],69];Var $q,q,I_,$6B,_:Array [Array [Array [Array [Int ,0b101101],03_2_7],0X46],0X2D];}''',
                '''Class,X,{,},Class,__Q_,{,},Class,_mE,{,_,(,_,,,u1,,,W,,,z__,,,__,:,Array,[,Array,[,Array,[,Array,[,String,,,69,],,,027,],,,0B1,],,,0B10111,],),{,},Val,$Y,:,Array,[,Array,[,Float,,,0b11,],,,69,],;,Var,$q,,,q,,,I_,,,$6B,,,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b101101,],,,0327,],,,0X46,],,,0X2D,],;,},<EOF>''',
                101
            )
        )

    def test_140(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (n,v_,_,_:Float ;IzoV,i_:Array [Array [Boolean ,04_2],0B111_0];i:Int ;_h,H97GR3rN8Nu_:t__;__:Float ;_8,_:H;_3_s:Array [Array [Float ,0X4C],070]){} }''',
                '''Class,_,{,Constructor,(,n,,,v_,,,_,,,_,:,Float,;,IzoV,,,i_,:,Array,[,Array,[,Boolean,,,042,],,,0B1110,],;,i,:,Int,;,_h,,,H97GR3rN8Nu_,:,t__,;,__,:,Float,;,_8,,,_,:,H,;,_3_s,:,Array,[,Array,[,Float,,,0X4C,],,,070,],),{,},},<EOF>''',
                101
            )
        )

    def test_141(self):
        self.assertTrue(
            TestLexer.test(
                '''Class e_:T{}Class _{_(){} }Class m:t{Val $3_:Float ;Constructor (){}Val ___1,$_,i0:_;Var _:_;Constructor (_39:_;j62k,K_:Array [Array [Array [Boolean ,0B11],0B1],56];L_,_:String ){} }''',
                '''Class,e_,:,T,{,},Class,_,{,_,(,),{,},},Class,m,:,t,{,Val,$3_,:,Float,;,Constructor,(,),{,},Val,___1,,,$_,,,i0,:,_,;,Var,_,:,_,;,Constructor,(,_39,:,_,;,j62k,,,K_,:,Array,[,Array,[,Array,[,Boolean,,,0B11,],,,0B1,],,,56,],;,L_,,,_,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_142(self):
        self.assertTrue(
            TestLexer.test(
                '''Class L_51_{W(){}Constructor (_4u:Array [Array [Int ,0B1000011],0B11]){}$_(){} }Class _:_8{Val _4,k,Z3_9_,$x56YP:Array [Float ,07];Constructor (){2.N();}Destructor (){Return ;} }Class _{}Class I{}''',
                '''Class,L_51_,{,W,(,),{,},Constructor,(,_4u,:,Array,[,Array,[,Int,,,0B1000011,],,,0B11,],),{,},$_,(,),{,},},Class,_,:,_8,{,Val,_4,,,k,,,Z3_9_,,,$x56YP,:,Array,[,Float,,,07,],;,Constructor,(,),{,2.,N,(,),;,},Destructor,(,),{,Return,;,},},Class,_,{,},Class,I,{,},<EOF>''',
                101
            )
        )

    def test_143(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:t30{}Class U:_{}Class _:N{Var x,$N,_,__9,$_:Array [Float ,0xD];}Class ZLW0:_Xa_{}Class Q:K{Val E9:String ;}''',
                '''Class,__,:,t30,{,},Class,U,:,_,{,},Class,_,:,N,{,Var,x,,,$N,,,_,,,__9,,,$_,:,Array,[,Float,,,0xD,],;,},Class,ZLW0,:,_Xa_,{,},Class,Q,:,K,{,Val,E9,:,String,;,},<EOF>''',
                101
            )
        )

    def test_144(self):
        self.assertTrue(
            TestLexer.test(
                '''Class kN5C319{}Class _____:_{}Class U:_{Constructor (_,_,z,Ae:Boolean ;FM:Array [Int ,03]){} }Class r{$0_(){}Var _:Int ;}''',
                '''Class,kN5C319,{,},Class,_____,:,_,{,},Class,U,:,_,{,Constructor,(,_,,,_,,,z,,,Ae,:,Boolean,;,FM,:,Array,[,Int,,,03,],),{,},},Class,r,{,$0_,(,),{,},Var,_,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_145(self):
        self.assertTrue(
            TestLexer.test(
                '''Class h{Constructor (_13:Array [Boolean ,072]){____::$0l();u_::$Y();} }Class _8:u{Var _:Array [Array [Array [Int ,42],0X7],01];}Class Yh73{}''',
                '''Class,h,{,Constructor,(,_13,:,Array,[,Boolean,,,072,],),{,____,::,$0l,(,),;,u_,::,$Y,(,),;,},},Class,_8,:,u,{,Var,_,:,Array,[,Array,[,Array,[,Int,,,42,],,,0X7,],,,01,],;,},Class,Yh73,{,},<EOF>''',
                101
            )
        )

    def test_146(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ta:_{$_Ycx(_2:Float ){}Var $ZA__:Array [Array [Array [Array [Array [Array [Array [Int ,0X18],0x12],0x12],01],0B10100],8],0b1_10_1];}''',
                '''Class,ta,:,_,{,$_Ycx,(,_2,:,Float,),{,},Var,$ZA__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0X18,],,,0x12,],,,0x12,],,,01,],,,0B10100,],,,8,],,,0b1101,],;,},<EOF>''',
                101
            )
        )

    def test_147(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _d{Constructor (_R,_,W_:__0N8;__,_4:Float ;U:String ;M_,L__os___S,__,N__,_1:_;q_,B:_;_,T:b){Break ;}$4_(__,_:Array [Array [Int ,0137],94];L,e:Array [Boolean ,0x5];f,u,d_:String ){} }''',
                '''Class,_d,{,Constructor,(,_R,,,_,,,W_,:,__0N8,;,__,,,_4,:,Float,;,U,:,String,;,M_,,,L__os___S,,,__,,,N__,,,_1,:,_,;,q_,,,B,:,_,;,_,,,T,:,b,),{,Break,;,},$4_,(,__,,,_,:,Array,[,Array,[,Int,,,0137,],,,94,],;,L,,,e,:,Array,[,Boolean,,,0x5,],;,f,,,u,,,d_,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_148(self):
        self.assertTrue(
            TestLexer.test(
                '''Class j_{$5(_8XN:Float ;_86o:Array [Array [Array [String ,35],0b1],0X5]){}Constructor (){} }Class _8{Var $s,__,$3:__0;}Class th:__E{}Class F{}Class _:_U{Destructor (){Break ;}$_d3(){Continue ;} }Class _:p{}Class __{}''',
                '''Class,j_,{,$5,(,_8XN,:,Float,;,_86o,:,Array,[,Array,[,Array,[,String,,,35,],,,0b1,],,,0X5,],),{,},Constructor,(,),{,},},Class,_8,{,Var,$s,,,__,,,$3,:,__0,;,},Class,th,:,__E,{,},Class,F,{,},Class,_,:,_U,{,Destructor,(,),{,Break,;,},$_d3,(,),{,Continue,;,},},Class,_,:,p,{,},Class,__,{,},<EOF>''',
                101
            )
        )

    def test_149(self):
        self.assertTrue(
            TestLexer.test(
                '''Class R4_:a_{Constructor (F41_:_7q;_8:_;_4,_,_:Array [Array [Array [Float ,02],0XF],0x8_4_03];h_:ni_;X:E;_g_:Array [Boolean ,0b1_0];_p2c:_){} }''',
                '''Class,R4_,:,a_,{,Constructor,(,F41_,:,_7q,;,_8,:,_,;,_4,,,_,,,_,:,Array,[,Array,[,Array,[,Float,,,02,],,,0XF,],,,0x8403,],;,h_,:,ni_,;,X,:,E,;,_g_,:,Array,[,Boolean,,,0b10,],;,_p2c,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_150(self):
        self.assertTrue(
            TestLexer.test(
                '''Class s{}Class _:_{Constructor (p_,_,t,_:Array [Int ,0B101101];__,GW,_,_:Array [Array [String ,0B101101],1]){} }Class g__Z:l{}''',
                '''Class,s,{,},Class,_,:,_,{,Constructor,(,p_,,,_,,,t,,,_,:,Array,[,Int,,,0B101101,],;,__,,,GW,,,_,,,_,:,Array,[,Array,[,String,,,0B101101,],,,1,],),{,},},Class,g__Z,:,l,{,},<EOF>''',
                101
            )
        )

    def test_151(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o_{$7(_:K_;H3,_:Array [Int ,5_1];_:Array [Float ,0B1]){Break ;{ {} }} }Class _{Val $d,qp_h,$_4:_;}Class _{}Class _T{}''',
                '''Class,o_,{,$7,(,_,:,K_,;,H3,,,_,:,Array,[,Int,,,51,],;,_,:,Array,[,Float,,,0B1,],),{,Break,;,{,{,},},},},Class,_,{,Val,$d,,,qp_h,,,$_4,:,_,;,},Class,_,{,},Class,_T,{,},<EOF>''',
                101
            )
        )

    def test_152(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Destructor (){}Val J,g:Float ;$_s(_5Mj,kw,_,Z_,p:Array [Array [Array [Array [Array [String ,0B101001],03],0B101001],0x6],0b1]){ {}{} }}''',
                '''Class,_,{,Destructor,(,),{,},Val,J,,,g,:,Float,;,$_s,(,_5Mj,,,kw,,,_,,,Z_,,,p,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B101001,],,,03,],,,0B101001,],,,0x6,],,,0b1,],),{,{,},{,},},},<EOF>''',
                101
            )
        )

    def test_153(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __n{}Class _26{}Class _9{}Class Wi{Val $1V:Array [Array [String ,01],0B11];Constructor (_:_){Break ;Return ;} }Class _E2{}Class _l_{}''',
                '''Class,__n,{,},Class,_26,{,},Class,_9,{,},Class,Wi,{,Val,$1V,:,Array,[,Array,[,String,,,01,],,,0B11,],;,Constructor,(,_,:,_,),{,Break,;,Return,;,},},Class,_E2,{,},Class,_l_,{,},<EOF>''',
                101
            )
        )

    def test_154(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class x_{Var _,_90I_p:String ;$_3(){}$_(_,__:Boolean ;__,_,_:Array [Array [String ,0b111110],0xA];_q:_X9){} }''',
                '''Class,_,{,},Class,x_,{,Var,_,,,_90I_p,:,String,;,$_3,(,),{,},$_,(,_,,,__,:,Boolean,;,__,,,_,,,_,:,Array,[,Array,[,String,,,0b111110,],,,0xA,],;,_q,:,_X9,),{,},},<EOF>''',
                101
            )
        )

    def test_155(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:__6{Val _,b:Array [Array [Array [Array [String ,0X29],248],0x5],24];Constructor (dV_:Array [String ,24];_:Array [Int ,0XAA];__,T:Array [Float ,0b110110];h,bC:_;_:_;_:Boolean ){}Destructor (){} }''',
                '''Class,_,:,__6,{,Val,_,,,b,:,Array,[,Array,[,Array,[,Array,[,String,,,0X29,],,,248,],,,0x5,],,,24,],;,Constructor,(,dV_,:,Array,[,String,,,24,],;,_,:,Array,[,Int,,,0XAA,],;,__,,,T,:,Array,[,Float,,,0b110110,],;,h,,,bC,:,_,;,_,:,_,;,_,:,Boolean,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_156(self):
        self.assertTrue(
            TestLexer.test(
                '''Class f:_DG_{_(kr,im_P_:Array [Array [Array [Array [Array [String ,0xC_AD],0X5],2],8],3]){Continue ;} }Class _{}''',
                '''Class,f,:,_DG_,{,_,(,kr,,,im_P_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0xCAD,],,,0X5,],,,2,],,,8,],,,3,],),{,Continue,;,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_157(self):
        self.assertTrue(
            TestLexer.test(
                '''Class O_{Destructor (){Break ;} }Class _Wj:D_k{Var $_:Array [Array [Array [Array [Array [Array [Array [String ,0X12],0X7],0x3],0132],0X5_B],071_3],0132];}Class _3{_(_,h:_8){} }''',
                '''Class,O_,{,Destructor,(,),{,Break,;,},},Class,_Wj,:,D_k,{,Var,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X12,],,,0X7,],,,0x3,],,,0132,],,,0X5B,],,,0713,],,,0132,],;,},Class,_3,{,_,(,_,,,h,:,_8,),{,},},<EOF>''',
                101
            )
        )

    def test_158(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m5Gd:_{Var $_6,$_,_X:__7;Var $_,_:Array [Array [Array [Array [Float ,65],05],06_7_26],65];}Class _{Var $g6:_;}''',
                '''Class,m5Gd,:,_,{,Var,$_6,,,$_,,,_X,:,__7,;,Var,$_,,,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,65,],,,05,],,,06726,],,,65,],;,},Class,_,{,Var,$g6,:,_,;,},<EOF>''',
                101
            )
        )

    def test_159(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $__,_4,$K:Array [Array [Int ,6_536_8_0_70_95_5],0X5D];Destructor (){}Destructor (){Return ;{}Break ;Return ;{Val _U,_1:Boolean ;} }Destructor (){Continue ;} }Class _P:V__{}''',
                '''Class,_,{,Val,$__,,,_4,,,$K,:,Array,[,Array,[,Int,,,65368070955,],,,0X5D,],;,Destructor,(,),{,},Destructor,(,),{,Return,;,{,},Break,;,Return,;,{,Val,_U,,,_1,:,Boolean,;,},},Destructor,(,),{,Continue,;,},},Class,_P,:,V__,{,},<EOF>''',
                101
            )
        )

    def test_160(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:T__0{}Class _r59:O{}Class j9{}Class f{}Class L8:_{Constructor (){}Destructor (){Val _:Array [Int ,0b1];Continue ;} }Class V:k{}Class N5kc2{Constructor (){}_3n2(__,Z,__4_i,_,_F,__:b76;_09,_,_,_n__D,G,_8_77:Array [Array [Boolean ,041],2_25_12]){} }''',
                '''Class,_,:,T__0,{,},Class,_r59,:,O,{,},Class,j9,{,},Class,f,{,},Class,L8,:,_,{,Constructor,(,),{,},Destructor,(,),{,Val,_,:,Array,[,Int,,,0b1,],;,Continue,;,},},Class,V,:,k,{,},Class,N5kc2,{,Constructor,(,),{,},_3n2,(,__,,,Z,,,__4_i,,,_,,,_F,,,__,:,b76,;,_09,,,_,,,_,,,_n__D,,,G,,,_8_77,:,Array,[,Array,[,Boolean,,,041,],,,22512,],),{,},},<EOF>''',
                101
            )
        )

    def test_161(self):
        self.assertTrue(
            TestLexer.test(
                '''Class D{}Class _H:___{}Class _{Constructor (){}Constructor (__i_1,_1KE,__u4B_:Array [Boolean ,0217];_U:Float ;I:_6;_x,l_:qU){} }Class _:j{}''',
                '''Class,D,{,},Class,_H,:,___,{,},Class,_,{,Constructor,(,),{,},Constructor,(,__i_1,,,_1KE,,,__u4B_,:,Array,[,Boolean,,,0217,],;,_U,:,Float,;,I,:,_6,;,_x,,,l_,:,qU,),{,},},Class,_,:,j,{,},<EOF>''',
                101
            )
        )

    def test_162(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_,Eh:Array [Float ,0b1]){}Var r,$_,Z:Boolean ;X_8(_3:Int ;ccNVKr0,_f3jz,_:Q;iBq978,I:String ){Continue ;} }Class __:_{Constructor (_L_:Array [Array [Array [String ,0xA],03],0143]){} }''',
                '''Class,_,{,Constructor,(,_,,,Eh,:,Array,[,Float,,,0b1,],),{,},Var,r,,,$_,,,Z,:,Boolean,;,X_8,(,_3,:,Int,;,ccNVKr0,,,_f3jz,,,_,:,Q,;,iBq978,,,I,:,String,),{,Continue,;,},},Class,__,:,_,{,Constructor,(,_L_,:,Array,[,Array,[,Array,[,String,,,0xA,],,,03,],,,0143,],),{,},},<EOF>''',
                101
            )
        )

    def test_163(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _P_U0_:_2_8m2_S{$U8(S,_:Array [Array [Array [String ,04],0111],0X7_7_A]){} }Class g46G:_7_{Destructor (){} }''',
                '''Class,_P_U0_,:,_2_8m2_S,{,$U8,(,S,,,_,:,Array,[,Array,[,Array,[,String,,,04,],,,0111,],,,0X77A,],),{,},},Class,g46G,:,_7_,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_164(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class _{Constructor (F,_:__0_J;V:Boolean ;_,_6v:Int ;__bM,b:Array [Float ,0X1C]){Var q_:Float ;}Val _:Int ;}''',
                '''Class,_,:,_,{,},Class,_,{,Constructor,(,F,,,_,:,__0_J,;,V,:,Boolean,;,_,,,_6v,:,Int,;,__bM,,,b,:,Array,[,Float,,,0X1C,],),{,Var,q_,:,Float,;,},Val,_,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_165(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q_Q0_:Z{}Class c:S2{Constructor (D2:Array [Boolean ,0B1];_:String ;R,_:__;_,_,K,C,_mk,E,_,e,_:Array [Array [Array [Array [Boolean ,1],0B1000000],0X1D],0b1011000];_:Array [Float ,0b1011000];_v,j5_,c47,j:Boolean ;_J8,_2,_:Boolean ){} }Class _94{Constructor (){} }Class __k{Var y:O;}''',
                '''Class,q_Q0_,:,Z,{,},Class,c,:,S2,{,Constructor,(,D2,:,Array,[,Boolean,,,0B1,],;,_,:,String,;,R,,,_,:,__,;,_,,,_,,,K,,,C,,,_mk,,,E,,,_,,,e,,,_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,1,],,,0B1000000,],,,0X1D,],,,0b1011000,],;,_,:,Array,[,Float,,,0b1011000,],;,_v,,,j5_,,,c47,,,j,:,Boolean,;,_J8,,,_2,,,_,:,Boolean,),{,},},Class,_94,{,Constructor,(,),{,},},Class,__k,{,Var,y,:,O,;,},<EOF>''',
                101
            )
        )

    def test_166(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var $7,$7R,$_,$_,_,$_,__,$_,_,a:Array [Array [Array [Array [Array [Float ,0b1],0B1],0375_50],0b101101],0x10];}Class utcX{Val _1,I5F0,$2:Array [Array [Array [Array [Float ,02_253],032],0b101101],0X7];}''',
                '''Class,_,{,Var,$7,,,$7R,,,$_,,,$_,,,_,,,$_,,,__,,,$_,,,_,,,a,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1,],,,0B1,],,,037550,],,,0b101101,],,,0x10,],;,},Class,utcX,{,Val,_1,,,I5F0,,,$2,:,Array,[,Array,[,Array,[,Array,[,Float,,,02253,],,,032,],,,0b101101,],,,0X7,],;,},<EOF>''',
                101
            )
        )

    def test_167(self):
        self.assertTrue(
            TestLexer.test(
                '''Class j_c:_Of{Constructor (){}Destructor (){}Destructor (){} }Class L:J1gJ{Constructor (W,__,RN:Array [Float ,2];p4s2,_:_){}Val _h,$P:Array [Float ,0X4A];}Class CC57{}''',
                '''Class,j_c,:,_Of,{,Constructor,(,),{,},Destructor,(,),{,},Destructor,(,),{,},},Class,L,:,J1gJ,{,Constructor,(,W,,,__,,,RN,:,Array,[,Float,,,2,],;,p4s2,,,_,:,_,),{,},Val,_h,,,$P,:,Array,[,Float,,,0X4A,],;,},Class,CC57,{,},<EOF>''',
                101
            )
        )

    def test_168(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class __{Destructor (){} }Class _{Constructor (d,_:Array [Array [Array [Array [Array [Array [String ,04],06],041],0B1],0x6_E5],06];jD_680C,C,O:W_){}Val __,e,_,_:Array [Int ,0X60];Var M,$_,_:Array [Array [String ,0B1],0B1];}''',
                '''Class,_,{,},Class,__,{,Destructor,(,),{,},},Class,_,{,Constructor,(,d,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,04,],,,06,],,,041,],,,0B1,],,,0x6E5,],,,06,],;,jD_680C,,,C,,,O,:,W_,),{,},Val,__,,,e,,,_,,,_,:,Array,[,Int,,,0X60,],;,Var,M,,,$_,,,_,:,Array,[,Array,[,String,,,0B1,],,,0B1,],;,},<EOF>''',
                101
            )
        )

    def test_169(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _N8{}Class s{Constructor (_:Array [Array [Int ,0b1],0B1110];_S,_nj_,_,e,_12_,_:Array [Array [Array [Int ,74],0b1111],0x80];r,UG96:Float ){Return ;} }Class _7_{}''',
                '''Class,_N8,{,},Class,s,{,Constructor,(,_,:,Array,[,Array,[,Int,,,0b1,],,,0B1110,],;,_S,,,_nj_,,,_,,,e,,,_12_,,,_,:,Array,[,Array,[,Array,[,Int,,,74,],,,0b1111,],,,0x80,],;,r,,,UG96,:,Float,),{,Return,;,},},Class,_7_,{,},<EOF>''',
                101
            )
        )

    def test_170(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_il,_,_:Boolean ;d_8_1,I,_:Array [Array [Array [Array [Array [Int ,0122],03],1],04_6_2_3],0xB];_:Boolean ){} }Class ____{}''',
                '''Class,_,{,Constructor,(,_il,,,_,,,_,:,Boolean,;,d_8_1,,,I,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0122,],,,03,],,,1,],,,04623,],,,0xB,],;,_,:,Boolean,),{,},},Class,____,{,},<EOF>''',
                101
            )
        )

    def test_171(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{Var $n99,__n,$74__,$_9:w;Var $1,G:Float ;}Class YK3{Val V_:Float ;}Class r:___u{Destructor (){} }Class v{}''',
                '''Class,__,{,Var,$n99,,,__n,,,$74__,,,$_9,:,w,;,Var,$1,,,G,:,Float,;,},Class,YK3,{,Val,V_,:,Float,;,},Class,r,:,___u,{,Destructor,(,),{,},},Class,v,{,},<EOF>''',
                101
            )
        )

    def test_172(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V:_{vM(f8:Int ){}Constructor (_p5:D;Y730kO,__n,M:Int ){Break ;}Destructor (){}Constructor (){}Var OcFyUe:Int ;Val _,$_:H_;Constructor (){} }''',
                '''Class,V,:,_,{,vM,(,f8,:,Int,),{,},Constructor,(,_p5,:,D,;,Y730kO,,,__n,,,M,:,Int,),{,Break,;,},Destructor,(,),{,},Constructor,(,),{,},Var,OcFyUe,:,Int,;,Val,_,,,$_,:,H_,;,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_173(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _p{}Class _{Constructor (u,_v,e:_5g;It__,u:_C;M,I_X:String ;_,_:S_8;p,_,a,fz,i,_,_,T_:Array [Int ,9];E1:String ;_7,_:J_){}Destructor (){} }Class eM:J{}''',
                '''Class,_p,{,},Class,_,{,Constructor,(,u,,,_v,,,e,:,_5g,;,It__,,,u,:,_C,;,M,,,I_X,:,String,;,_,,,_,:,S_8,;,p,,,_,,,a,,,fz,,,i,,,_,,,_,,,T_,:,Array,[,Int,,,9,],;,E1,:,String,;,_7,,,_,:,J_,),{,},Destructor,(,),{,},},Class,eM,:,J,{,},<EOF>''',
                101
            )
        )

    def test_174(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Z:Fp{$5_(_,_i_,f,_8i6:Array [Array [Int ,0143],15];_n:Boolean ){Return ;{} }}Class r9:__{Val t:Array [Array [Array [Boolean ,15],0B100111],0X6];}''',
                '''Class,Z,:,Fp,{,$5_,(,_,,,_i_,,,f,,,_8i6,:,Array,[,Array,[,Int,,,0143,],,,15,],;,_n,:,Boolean,),{,Return,;,{,},},},Class,r9,:,__,{,Val,t,:,Array,[,Array,[,Array,[,Boolean,,,15,],,,0B100111,],,,0X6,],;,},<EOF>''',
                101
            )
        )

    def test_175(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y:_{Destructor (){}Var _a:Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,69],0b1_1],0x5],066],0B1010101],0XBA],04],0xE],69];}''',
                '''Class,y,:,_,{,Destructor,(,),{,},Var,_a,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,69,],,,0b11,],,,0x5,],,,066,],,,0B1010101,],,,0XBA,],,,04,],,,0xE,],,,69,],;,},<EOF>''',
                101
            )
        )

    def test_176(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n_:q_{Constructor (_m5f4:O7_U;NR_d:_6S__4_){}Destructor (){}Var $5:Int ;Constructor (){}Var $V00e_:Array [Boolean ,0B1010];Constructor (){__::$i4_().Y();Continue ;} }''',
                '''Class,n_,:,q_,{,Constructor,(,_m5f4,:,O7_U,;,NR_d,:,_6S__4_,),{,},Destructor,(,),{,},Var,$5,:,Int,;,Constructor,(,),{,},Var,$V00e_,:,Array,[,Boolean,,,0B1010,],;,Constructor,(,),{,__,::,$i4_,(,),.,Y,(,),;,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_177(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _1{Constructor (){}Destructor (){} }Class _2_ci{}Class w6:c{Val $1I:fW2_;Constructor (___70_4_:Float ;TL_R_,_w:_B;V0,L:Boolean ;_:String ;__,_:_7_){}Var _:Array [Array [Array [Int ,0X1_0],051],55];}Class _fH:_Ba{Var $V,___l6,_,$37:c3;}Class _{}''',
                '''Class,_1,{,Constructor,(,),{,},Destructor,(,),{,},},Class,_2_ci,{,},Class,w6,:,c,{,Val,$1I,:,fW2_,;,Constructor,(,___70_4_,:,Float,;,TL_R_,,,_w,:,_B,;,V0,,,L,:,Boolean,;,_,:,String,;,__,,,_,:,_7_,),{,},Var,_,:,Array,[,Array,[,Array,[,Int,,,0X10,],,,051,],,,55,],;,},Class,_fH,:,_Ba,{,Var,$V,,,___l6,,,_,,,$37,:,c3,;,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_178(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _34D{}Class k0{}Class _3{}Class g_39{Constructor (V:Array [Array [Int ,0B10110],02]){Break ;}Val w:String ;}Class _7_{_(){} }''',
                '''Class,_34D,{,},Class,k0,{,},Class,_3,{,},Class,g_39,{,Constructor,(,V,:,Array,[,Array,[,Int,,,0B10110,],,,02,],),{,Break,;,},Val,w,:,String,;,},Class,_7_,{,_,(,),{,},},<EOF>''',
                101
            )
        )

    def test_179(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class ho0:r{Constructor (y,__:H9h;_z,_10,_,_:Boolean ){}Constructor (_:String ){f2::$_();} }Class _:Y3{}''',
                '''Class,_,{,},Class,ho0,:,r,{,Constructor,(,y,,,__,:,H9h,;,_z,,,_10,,,_,,,_,:,Boolean,),{,},Constructor,(,_,:,String,),{,f2,::,$_,(,),;,},},Class,_,:,Y3,{,},<EOF>''',
                101
            )
        )

    def test_180(self):
        self.assertTrue(
            TestLexer.test(
                '''Class O_oc:_{_(h,___p0,k7_,_4,I,_,__,_3_:Array [Int ,0xA]){Continue ;}Val $46_,$I6,$16_,x_1:Array [Array [Int ,075],06];}''',
                '''Class,O_oc,:,_,{,_,(,h,,,___p0,,,k7_,,,_4,,,I,,,_,,,__,,,_3_,:,Array,[,Int,,,0xA,],),{,Continue,;,},Val,$46_,,,$I6,,,$16_,,,x_1,:,Array,[,Array,[,Int,,,075,],,,06,],;,},<EOF>''',
                101
            )
        )

    def test_181(self):
        self.assertTrue(
            TestLexer.test(
                '''Class hF{Constructor (){}Constructor (_d3,D27:Boolean ){Var _,j1,__,x,__Wz,f:ad;Continue ;}$__(l26:Float ){} }''',
                '''Class,hF,{,Constructor,(,),{,},Constructor,(,_d3,,,D27,:,Boolean,),{,Var,_,,,j1,,,__,,,x,,,__Wz,,,f,:,ad,;,Continue,;,},$__,(,l26,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_182(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:r6{}Class _:_s_{$J(){} }Class __{}Class P{Constructor (_5:_;_:_e){} }Class N:U{}Class _U242:l{Val $1,_,$81,$N0,$p:Float ;}Class i{Destructor (){Break ;{} }Y(F:b;_8:Array [Float ,71];m,_,__,_:Array [Int ,0b10];f:Int ){Break ;}Val $xX,T__QN,$_,L__,$_____,$us,$2:_;$5(Z,_:Array [String ,7]){} }''',
                '''Class,_,:,r6,{,},Class,_,:,_s_,{,$J,(,),{,},},Class,__,{,},Class,P,{,Constructor,(,_5,:,_,;,_,:,_e,),{,},},Class,N,:,U,{,},Class,_U242,:,l,{,Val,$1,,,_,,,$81,,,$N0,,,$p,:,Float,;,},Class,i,{,Destructor,(,),{,Break,;,{,},},Y,(,F,:,b,;,_8,:,Array,[,Float,,,71,],;,m,,,_,,,__,,,_,:,Array,[,Int,,,0b10,],;,f,:,Int,),{,Break,;,},Val,$xX,,,T__QN,,,$_,,,L__,,,$_____,,,$us,,,$2,:,_,;,$5,(,Z,,,_,:,Array,[,String,,,7,],),{,},},<EOF>''',
                101
            )
        )

    def test_183(self):
        self.assertTrue(
            TestLexer.test(
                '''Class G_:_0{Constructor (p2,v,_:Array [Array [Array [String ,0b1_0],0X26],0X5];_,X,_,__,_H__:Array [Boolean ,1]){}Val $5:String ;}''',
                '''Class,G_,:,_0,{,Constructor,(,p2,,,v,,,_,:,Array,[,Array,[,Array,[,String,,,0b10,],,,0X26,],,,0X5,],;,_,,,X,,,_,,,__,,,_H__,:,Array,[,Boolean,,,1,],),{,},Val,$5,:,String,;,},<EOF>''',
                101
            )
        )

    def test_184(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8{}Class _6_{Destructor (){ {} }Val $_H:__;Var m6,__E,K_:Array [Array [Array [Array [Array [Boolean ,3],0b1000011],5],5],5];Var $T_:Int ;Var _,a,_:String ;}''',
                '''Class,_8,{,},Class,_6_,{,Destructor,(,),{,{,},},Val,$_H,:,__,;,Var,m6,,,__E,,,K_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,3,],,,0b1000011,],,,5,],,,5,],,,5,],;,Var,$T_,:,Int,;,Var,_,,,a,,,_,:,String,;,},<EOF>''',
                101
            )
        )

    def test_185(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2{n(){} }Class rv{Var G_,$_:String ;Constructor (){} }Class __:_{Val K:String ;Destructor (){}Destructor (){}eq(C3_,S_:p){}__8(){} }''',
                '''Class,_2,{,n,(,),{,},},Class,rv,{,Var,G_,,,$_,:,String,;,Constructor,(,),{,},},Class,__,:,_,{,Val,K,:,String,;,Destructor,(,),{,},Destructor,(,),{,},eq,(,C3_,,,S_,:,p,),{,},__8,(,),{,},},<EOF>''',
                101
            )
        )

    def test_186(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k{}Class _{Constructor (__5:Array [Array [Int ,4],013];e,bP,_W,_:jT;_,_,r,b,__3U,M0U:Boolean ){Continue ;}Var _,_:String ;}Class bQ{}Class o_0:v{}''',
                '''Class,k,{,},Class,_,{,Constructor,(,__5,:,Array,[,Array,[,Int,,,4,],,,013,],;,e,,,bP,,,_W,,,_,:,jT,;,_,,,_,,,r,,,b,,,__3U,,,M0U,:,Boolean,),{,Continue,;,},Var,_,,,_,:,String,;,},Class,bQ,{,},Class,o_0,:,v,{,},<EOF>''',
                101
            )
        )

    def test_187(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g5_{}Class _E0{}Class _{}Class rx_{}Class WZd_{}Class _{}Class Y:N{$6(v,_sK73,_8_46,_1:Int ;_2B:Array [Array [String ,0X56],0x9];S:Int ;_A_,_9:l){} }Class __{}''',
                '''Class,g5_,{,},Class,_E0,{,},Class,_,{,},Class,rx_,{,},Class,WZd_,{,},Class,_,{,},Class,Y,:,N,{,$6,(,v,,,_sK73,,,_8_46,,,_1,:,Int,;,_2B,:,Array,[,Array,[,String,,,0X56,],,,0x9,],;,S,:,Int,;,_A_,,,_9,:,l,),{,},},Class,__,{,},<EOF>''',
                101
            )
        )

    def test_188(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A:_{Destructor (){}Destructor (){} }Class _k9x12{Constructor (_32:_){Var L99__:Array [Array [Array [Array [Float ,7_38],86],86],0B1];} }''',
                '''Class,A,:,_,{,Destructor,(,),{,},Destructor,(,),{,},},Class,_k9x12,{,Constructor,(,_32,:,_,),{,Var,L99__,:,Array,[,Array,[,Array,[,Array,[,Float,,,738,],,,86,],,,86,],,,0B1,],;,},},<EOF>''',
                101
            )
        )

    def test_189(self):
        self.assertTrue(
            TestLexer.test(
                '''Class h_p{r2n(){ {Val zM5H,_,v_3:String ;} }SB(R:Array [Float ,0XF];m_,E,S,_MW:Array [Array [Array [Int ,0b11],07],0b110011];K,__,J:Array [Array [String ,5998],0X8];_,__:Array [Float ,0B11100]){e61::$7V().____();Continue ;} }''',
                '''Class,h_p,{,r2n,(,),{,{,Val,zM5H,,,_,,,v_3,:,String,;,},},SB,(,R,:,Array,[,Float,,,0XF,],;,m_,,,E,,,S,,,_MW,:,Array,[,Array,[,Array,[,Int,,,0b11,],,,07,],,,0b110011,],;,K,,,__,,,J,:,Array,[,Array,[,String,,,5998,],,,0X8,],;,_,,,__,:,Array,[,Float,,,0B11100,],),{,e61,::,$7V,(,),.,____,(,),;,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_190(self):
        self.assertTrue(
            TestLexer.test(
                '''Class LK{}Class L:_{}Class z{Constructor (_C_55:Array [Float ,0B1]){}$3l(_7__00q_:Boolean ;__,J,_:String ;_:f;_,_:Array [Array [Boolean ,0x3],0120];X6,l,R,_E,_u:Int ;_:S;h_46_6_:Array [Float ,0B1000101];_,oQ:m4){} }''',
                '''Class,LK,{,},Class,L,:,_,{,},Class,z,{,Constructor,(,_C_55,:,Array,[,Float,,,0B1,],),{,},$3l,(,_7__00q_,:,Boolean,;,__,,,J,,,_,:,String,;,_,:,f,;,_,,,_,:,Array,[,Array,[,Boolean,,,0x3,],,,0120,],;,X6,,,l,,,R,,,_E,,,_u,:,Int,;,_,:,S,;,h_46_6_,:,Array,[,Float,,,0B1000101,],;,_,,,oQ,:,m4,),{,},},<EOF>''',
                101
            )
        )

    def test_191(self):
        self.assertTrue(
            TestLexer.test(
                '''Class e:_{Destructor (){}Var _8,$_6_,y_n_4_E,_,$6,L,t,_,$_:_6_;Val X,$_,$T6,$_:G;}Class u{Constructor (j_:Int ;_5gJ,_,_,_,a:Boolean ){} }''',
                '''Class,e,:,_,{,Destructor,(,),{,},Var,_8,,,$_6_,,,y_n_4_E,,,_,,,$6,,,L,,,t,,,_,,,$_,:,_6_,;,Val,X,,,$_,,,$T6,,,$_,:,G,;,},Class,u,{,Constructor,(,j_,:,Int,;,_5gJ,,,_,,,_,,,_,,,a,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_192(self):
        self.assertTrue(
            TestLexer.test(
                '''Class a___:e_Tc{}Class U:K{Var _,$Y_57___,$lr:_;}Class __{}Class _{}Class _:a{$6_(_2_:Array [Int ,0B1010100];K:Float ){_R::$G.O_();L::$26__.__();} }Class C3:l_545_1{}Class _I{}Class _S:_{Val $Zgl:B;Var $__,g,$_,$_:Array [Boolean ,0XF2];}Class c05:R{}''',
                '''Class,a___,:,e_Tc,{,},Class,U,:,K,{,Var,_,,,$Y_57___,,,$lr,:,_,;,},Class,__,{,},Class,_,{,},Class,_,:,a,{,$6_,(,_2_,:,Array,[,Int,,,0B1010100,],;,K,:,Float,),{,_R,::,$G,.,O_,(,),;,L,::,$26__,.,__,(,),;,},},Class,C3,:,l_545_1,{,},Class,_I,{,},Class,_S,:,_,{,Val,$Zgl,:,B,;,Var,$__,,,g,,,$_,,,$_,:,Array,[,Boolean,,,0XF2,],;,},Class,c05,:,R,{,},<EOF>''',
                101
            )
        )

    def test_193(self):
        self.assertTrue(
            TestLexer.test(
                '''Class G:A_6{$3(){}Val $q_L__:g;Destructor (){}$1H(d,P,N__,s_,b,B,L,q,_:Array [Boolean ,0B101];_,_2:Array [Int ,0B101]){} }''',
                '''Class,G,:,A_6,{,$3,(,),{,},Val,$q_L__,:,g,;,Destructor,(,),{,},$1H,(,d,,,P,,,N__,,,s_,,,b,,,B,,,L,,,q,,,_,:,Array,[,Boolean,,,0B101,],;,_,,,_2,:,Array,[,Int,,,0B101,],),{,},},<EOF>''',
                101
            )
        )

    def test_194(self):
        self.assertTrue(
            TestLexer.test(
                '''Class f{Constructor (kA,f6_y:Boolean ;o:String ;V_8R_,_:M_;__:_){} }Class _1{}Class c:_Y_{}Class _:_{}Class _{}''',
                '''Class,f,{,Constructor,(,kA,,,f6_y,:,Boolean,;,o,:,String,;,V_8R_,,,_,:,M_,;,__,:,_,),{,},},Class,_1,{,},Class,c,:,_Y_,{,},Class,_,:,_,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_195(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_M{Constructor (){}Constructor (_:String ;Fsm:Array [String ,0XC_D9]){Continue ;}Constructor (_0_,L:o9){Break ;} }''',
                '''Class,_,:,_M,{,Constructor,(,),{,},Constructor,(,_,:,String,;,Fsm,:,Array,[,String,,,0XCD9,],),{,Continue,;,},Constructor,(,_0_,,,L,:,o9,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_196(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m_F{Val _:Array [Int ,85];}Class _R{Val s4_W,_m:Array [Array [Array [Array [Array [Float ,0106],0B11101],0X7],077_01_3],0106];Destructor (){} }''',
                '''Class,m_F,{,Val,_,:,Array,[,Int,,,85,],;,},Class,_R,{,Val,s4_W,,,_m,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0106,],,,0B11101,],,,0X7,],,,077013,],,,0106,],;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_197(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ____5:_{Constructor (_,K,oj:Array [Array [Array [Array [Float ,051],07_0],03],03];o_,Xe6U,_9,c:Array [Array [Int ,01],0XB]){} }''',
                '''Class,____5,:,_,{,Constructor,(,_,,,K,,,oj,:,Array,[,Array,[,Array,[,Array,[,Float,,,051,],,,070,],,,03,],,,03,],;,o_,,,Xe6U,,,_9,,,c,:,Array,[,Array,[,Int,,,01,],,,0XB,],),{,},},<EOF>''',
                101
            )
        )

    def test_198(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y_7j:w7O_{Constructor (){} }Class B4:rd2{Destructor (){}Destructor (){Val _,_,_9__,v33:Array [Array [Array [String ,28],0XB],0110];} }Class t{}Class _:i{}''',
                '''Class,y_7j,:,w7O_,{,Constructor,(,),{,},},Class,B4,:,rd2,{,Destructor,(,),{,},Destructor,(,),{,Val,_,,,_,,,_9__,,,v33,:,Array,[,Array,[,Array,[,String,,,28,],,,0XB,],,,0110,],;,},},Class,t,{,},Class,_,:,i,{,},<EOF>''',
                101
            )
        )

    def test_199(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _y09{}Class C:_075{Val $_L5:Array [Array [Array [Array [Array [Array [Int ,32],06],0x5F],014],0X5_42],5];}Class m{}''',
                '''Class,_y09,{,},Class,C,:,_075,{,Val,$_L5,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,32,],,,06,],,,0x5F,],,,014,],,,0X542,],,,5,],;,},Class,m,{,},<EOF>''',
                101
            )
        )

    def test_200(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class __1{Val $_,_l__q7:Array [Array [Array [Array [Array [Array [Array [Int ,88],053_1],0X5],0b1_0],03],75492],0x7_AD94_1EB_8_71];}Class _1_{}''',
                '''Class,_,{,},Class,__1,{,Val,$_,,,_l__q7,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,88,],,,0531,],,,0X5,],,,0b10,],,,03,],,,75492,],,,0x7AD941EB871,],;,},Class,_1_,{,},<EOF>''',
                101
            )
        )

    def test_201(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _g:R_{}Class k:S{Val $_43_,o,_t,$R,$7_,t:Array [Float ,0b101011];_(_5_:Float ;GH8__:Int ){} }Class _:z__{}Class _{Constructor (){Break ;} }Class _{}''',
                '''Class,_g,:,R_,{,},Class,k,:,S,{,Val,$_43_,,,o,,,_t,,,$R,,,$7_,,,t,:,Array,[,Float,,,0b101011,],;,_,(,_5_,:,Float,;,GH8__,:,Int,),{,},},Class,_,:,z__,{,},Class,_,{,Constructor,(,),{,Break,;,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_202(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class g_{$tT_(_11:Array [Array [Array [Array [Array [Array [Boolean ,0x13],01],0X9F_5_7],0B111000],0x13],03]){Var __3:Array [Float ,49];} }Class _{}''',
                '''Class,_,{,},Class,g_,{,$tT_,(,_11,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x13,],,,01,],,,0X9F57,],,,0B111000,],,,0x13,],,,03,],),{,Var,__3,:,Array,[,Float,,,49,],;,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_203(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y6{Val _:Array [Array [Array [Array [Int ,0xC],0X51],0b1000000],0X51];}Class _E{}Class A:H8{}Class H:i{}Class _:_U{Var _,$_,_:String ;}''',
                '''Class,y6,{,Val,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0xC,],,,0X51,],,,0b1000000,],,,0X51,],;,},Class,_E,{,},Class,A,:,H8,{,},Class,H,:,i,{,},Class,_,:,_U,{,Var,_,,,$_,,,_,:,String,;,},<EOF>''',
                101
            )
        )

    def test_204(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w813:c{A(_Pb4,_p,A,_5q,__,Y,B___78_,_:Float ;z:String ;_,_:Array [Boolean ,2];n_3,x3O_7_:Array [Array [Array [Array [String ,5],0B101001],0X1E],0x45];K:_74;_,_9,B:Array [String ,0X34]){} }''',
                '''Class,w813,:,c,{,A,(,_Pb4,,,_p,,,A,,,_5q,,,__,,,Y,,,B___78_,,,_,:,Float,;,z,:,String,;,_,,,_,:,Array,[,Boolean,,,2,],;,n_3,,,x3O_7_,:,Array,[,Array,[,Array,[,Array,[,String,,,5,],,,0B101001,],,,0X1E,],,,0x45,],;,K,:,_74,;,_,,,_9,,,B,:,Array,[,String,,,0X34,],),{,},},<EOF>''',
                101
            )
        )

    def test_205(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Destructor (){} }Class _2{$x_(D:C2){}Var _6_1,l_Z_1_:Array [Array [Array [Array [Array [Int ,7],0B111111],7],0xC_27],0b10];}''',
                '''Class,_,{,Destructor,(,),{,},},Class,_2,{,$x_,(,D,:,C2,),{,},Var,_6_1,,,l_Z_1_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,7,],,,0B111111,],,,7,],,,0xC27,],,,0b10,],;,},<EOF>''',
                101
            )
        )

    def test_206(self):
        self.assertTrue(
            TestLexer.test(
                '''Class N9{Val z:Boolean ;Destructor (){ {Break ;}{Var _s8,_s,u,__y,R:Float ;Continue ;Val __,_I:Array [Int ,077];Return ;}{} }}''',
                '''Class,N9,{,Val,z,:,Boolean,;,Destructor,(,),{,{,Break,;,},{,Var,_s8,,,_s,,,u,,,__y,,,R,:,Float,;,Continue,;,Val,__,,,_I,:,Array,[,Int,,,077,],;,Return,;,},{,},},},<EOF>''',
                101
            )
        )

    def test_207(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __48:Zi1{}Class _M9K6{}Class z:A{c4(){} }Class _13{Val $m,W,$0:Array [Boolean ,024];Val q7S,$8,_72,$__,$1:e;}Class _{Destructor (){}Val _,$V:l;Val _,_,$f:Boolean ;}Class _{}''',
                '''Class,__48,:,Zi1,{,},Class,_M9K6,{,},Class,z,:,A,{,c4,(,),{,},},Class,_13,{,Val,$m,,,W,,,$0,:,Array,[,Boolean,,,024,],;,Val,q7S,,,$8,,,_72,,,$__,,,$1,:,e,;,},Class,_,{,Destructor,(,),{,},Val,_,,,$V,:,l,;,Val,_,,,_,,,$f,:,Boolean,;,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_208(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8:ZIX{}Class Qr{}Class _{Var _,P,_,K,$b0v,x:Boolean ;Destructor (){Return ;}j(){} }Class _6_4:D{$g3(){} }Class D4:_{Val G1_v:String ;}Class m{}''',
                '''Class,_8,:,ZIX,{,},Class,Qr,{,},Class,_,{,Var,_,,,P,,,_,,,K,,,$b0v,,,x,:,Boolean,;,Destructor,(,),{,Return,;,},j,(,),{,},},Class,_6_4,:,D,{,$g3,(,),{,},},Class,D4,:,_,{,Val,G1_v,:,String,;,},Class,m,{,},<EOF>''',
                101
            )
        )

    def test_209(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (w:Array [Array [Int ,0b1],0x5]){ {{Continue ;}{}Val d:Array [Float ,1];Break ;} }}Class _G:_{Val $J:_;}Class ka{}''',
                '''Class,_,{,Constructor,(,w,:,Array,[,Array,[,Int,,,0b1,],,,0x5,],),{,{,{,Continue,;,},{,},Val,d,:,Array,[,Float,,,1,],;,Break,;,},},},Class,_G,:,_,{,Val,$J,:,_,;,},Class,ka,{,},<EOF>''',
                101
            )
        )

    def test_210(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var $h,_:_d_;Var $8,$_k:Array [Int ,0B1];Var _:Array [Array [Array [String ,0X55],076],0X8];$_y_(){}$oA_0(_9_:Boolean ;H:Array [Array [Float ,0XC0],80]){} }Class _:u{Constructor (_3jgy,G:Array [Array [String ,0b10010],80];G:Int ){} }''',
                '''Class,_,{,Var,$h,,,_,:,_d_,;,Var,$8,,,$_k,:,Array,[,Int,,,0B1,],;,Var,_,:,Array,[,Array,[,Array,[,String,,,0X55,],,,076,],,,0X8,],;,$_y_,(,),{,},$oA_0,(,_9_,:,Boolean,;,H,:,Array,[,Array,[,Float,,,0XC0,],,,80,],),{,},},Class,_,:,u,{,Constructor,(,_3jgy,,,G,:,Array,[,Array,[,String,,,0b10010,],,,80,],;,G,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_211(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Poa__:_{Constructor (__:Array [Int ,2];_:Array [Array [Array [Array [Float ,0B1],0xD2_0],0x7],0XF]){g::$2();}Destructor (){} }Class T{Var __:Array [Array [Array [Boolean ,0XE7],7],060];}''',
                '''Class,Poa__,:,_,{,Constructor,(,__,:,Array,[,Int,,,2,],;,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B1,],,,0xD20,],,,0x7,],,,0XF,],),{,g,::,$2,(,),;,},Destructor,(,),{,},},Class,T,{,Var,__,:,Array,[,Array,[,Array,[,Boolean,,,0XE7,],,,7,],,,060,],;,},<EOF>''',
                101
            )
        )

    def test_212(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _80e:i4{US8(){}Var F,$62:Array [Array [Array [Array [Array [Array [Boolean ,0B1_0],0X43],0121],0B1],0B1],0x1C];Constructor (){} }Class B:_{}Class Y{R4_(){ {Break ;} }}''',
                '''Class,_80e,:,i4,{,US8,(,),{,},Var,F,,,$62,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B10,],,,0X43,],,,0121,],,,0B1,],,,0B1,],,,0x1C,],;,Constructor,(,),{,},},Class,B,:,_,{,},Class,Y,{,R4_,(,),{,{,Break,;,},},},<EOF>''',
                101
            )
        )

    def test_213(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7_{Constructor (_,Xd:Int ;_8:Array [Float ,0B1011010];_3:Array [Array [Array [Array [Array [Boolean ,046],0x8],04_7],0B11],0xB]){}Destructor (){Wy_::$0();} }''',
                '''Class,_7_,{,Constructor,(,_,,,Xd,:,Int,;,_8,:,Array,[,Float,,,0B1011010,],;,_3,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,046,],,,0x8,],,,047,],,,0B11,],,,0xB,],),{,},Destructor,(,),{,Wy_,::,$0,(,),;,},},<EOF>''',
                101
            )
        )

    def test_214(self):
        self.assertTrue(
            TestLexer.test(
                '''Class xL:D{Var $8:p;Constructor (D8:Array [Array [Int ,6],48];_4,_q8,p:Array [Array [Array [Array [Array [Array [Array [Array [String ,0X34],0X34],0x6_2_0_E],0X34],79_7_6],01],0102],0b1]){} }Class f:d{}''',
                '''Class,xL,:,D,{,Var,$8,:,p,;,Constructor,(,D8,:,Array,[,Array,[,Int,,,6,],,,48,],;,_4,,,_q8,,,p,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X34,],,,0X34,],,,0x620E,],,,0X34,],,,7976,],,,01,],,,0102,],,,0b1,],),{,},},Class,f,:,d,{,},<EOF>''',
                101
            )
        )

    def test_215(self):
        self.assertTrue(
            TestLexer.test(
                '''Class I{}Class x_:___8_{Constructor (g6,C_,S5D:Array [Array [Boolean ,0x1],72]){Return ;} }Class _5:_{Var $b:D;}Class u{}Class h:_i{}''',
                '''Class,I,{,},Class,x_,:,___8_,{,Constructor,(,g6,,,C_,,,S5D,:,Array,[,Array,[,Boolean,,,0x1,],,,72,],),{,Return,;,},},Class,_5,:,_,{,Var,$b,:,D,;,},Class,u,{,},Class,h,:,_i,{,},<EOF>''',
                101
            )
        )

    def test_216(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _1{Constructor (___,h,z,__:_;M,_,C:Array [Float ,0B1_0];_:Array [String ,8];k,V2Fy_Ot,NA,_K0qS,Z__,k:Int ;_,dS:Float ){} }''',
                '''Class,_1,{,Constructor,(,___,,,h,,,z,,,__,:,_,;,M,,,_,,,C,:,Array,[,Float,,,0B10,],;,_,:,Array,[,String,,,8,],;,k,,,V2Fy_Ot,,,NA,,,_K0qS,,,Z__,,,k,:,Int,;,_,,,dS,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_217(self):
        self.assertTrue(
            TestLexer.test(
                '''Class qr:E{}Class _{}Class d:__q{}Class _8iya:Z_{Val _:b;}Class w_:A{Constructor (_04_4:Array [String ,0b1100];_8_,n_J77_:_;C:Array [Array [Array [Boolean ,0b1_0],0xC],0xC];a5,__:__){} }Class N{}Class G:_{}''',
                '''Class,qr,:,E,{,},Class,_,{,},Class,d,:,__q,{,},Class,_8iya,:,Z_,{,Val,_,:,b,;,},Class,w_,:,A,{,Constructor,(,_04_4,:,Array,[,String,,,0b1100,],;,_8_,,,n_J77_,:,_,;,C,:,Array,[,Array,[,Array,[,Boolean,,,0b10,],,,0xC,],,,0xC,],;,a5,,,__,:,__,),{,},},Class,N,{,},Class,G,:,_,{,},<EOF>''',
                101
            )
        )

    def test_218(self):
        self.assertTrue(
            TestLexer.test(
                '''Class d{$_(_dj6z,_9:L5;_:Float ){ {Var __:Boolean ;Continue ;}{Continue ;} }$_b(_:Int ;_,_:Int ){} }Class _Y{}Class __B_:F{}Class n9_4{}''',
                '''Class,d,{,$_,(,_dj6z,,,_9,:,L5,;,_,:,Float,),{,{,Var,__,:,Boolean,;,Continue,;,},{,Continue,;,},},$_b,(,_,:,Int,;,_,,,_,:,Int,),{,},},Class,_Y,{,},Class,__B_,:,F,{,},Class,n9_4,{,},<EOF>''',
                101
            )
        )

    def test_219(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _Yr{}Class _{Constructor (){Continue ;Return ;}Var _,$E4,R,J,$m__:L9j;____0r(T,_,_8,_Qe1_:Boolean ;rCZ9u,__,_Q3:s;q_:Array [Boolean ,0B100010]){Break ;} }Class _:U{Destructor (){} }''',
                '''Class,_Yr,{,},Class,_,{,Constructor,(,),{,Continue,;,Return,;,},Var,_,,,$E4,,,R,,,J,,,$m__,:,L9j,;,____0r,(,T,,,_,,,_8,,,_Qe1_,:,Boolean,;,rCZ9u,,,__,,,_Q3,:,s,;,q_,:,Array,[,Boolean,,,0B100010,],),{,Break,;,},},Class,_,:,U,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_220(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Y8_:_{__(){}_0_(_:Array [Boolean ,0B11_0];__,_:Array [Float ,0x20]){}Constructor (d_:Array [Float ,84];l,__f_,e2:Array [Float ,6];_:Array [String ,0107]){} }''',
                '''Class,Y8_,:,_,{,__,(,),{,},_0_,(,_,:,Array,[,Boolean,,,0B110,],;,__,,,_,:,Array,[,Float,,,0x20,],),{,},Constructor,(,d_,:,Array,[,Float,,,84,],;,l,,,__f_,,,e2,:,Array,[,Float,,,6,],;,_,:,Array,[,String,,,0107,],),{,},},<EOF>''',
                101
            )
        )

    def test_221(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m0{Val __I,$2:_;}Class _81_{V(){}Var _:String ;Destructor (){} }Class i_lfl9:_{}Class _w____u05{Var _,$x5,$L_H_:Array [Array [Array [Array [Array [Int ,0X5F],0X5F],0b1],9_1],0X6];Var $2a46e:_z57_;}''',
                '''Class,m0,{,Val,__I,,,$2,:,_,;,},Class,_81_,{,V,(,),{,},Var,_,:,String,;,Destructor,(,),{,},},Class,i_lfl9,:,_,{,},Class,_w____u05,{,Var,_,,,$x5,,,$L_H_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0X5F,],,,0X5F,],,,0b1,],,,91,],,,0X6,],;,Var,$2a46e,:,_z57_,;,},<EOF>''',
                101
            )
        )

    def test_222(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (v,B,Q:Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0B1],6],0x3A],49],0B1011010],0XC],0b110011],0X1C_3D2],01_2]){}$1O(p_67_,Y,__m,M:Array [Array [Boolean ,0xA_6],0x3A];b,J6,E,B9,_:Array [Float ,49];Sk_70:LC;_8_,M,_,_07:Boolean ;_v,B8,__,_,_:_3;__E3,_7,_:String ;D:String ;C,w,k3:Float ;__4T,p6,_,g_l:q4_){}Constructor (_:_N0;j,wk:M_;MS:Array [Int ,0b101_0];_L:Array [Int ,7_2]){} }''',
                '''Class,_,{,Constructor,(,v,,,B,,,Q,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1,],,,6,],,,0x3A,],,,49,],,,0B1011010,],,,0XC,],,,0b110011,],,,0X1C3D2,],,,012,],),{,},$1O,(,p_67_,,,Y,,,__m,,,M,:,Array,[,Array,[,Boolean,,,0xA6,],,,0x3A,],;,b,,,J6,,,E,,,B9,,,_,:,Array,[,Float,,,49,],;,Sk_70,:,LC,;,_8_,,,M,,,_,,,_07,:,Boolean,;,_v,,,B8,,,__,,,_,,,_,:,_3,;,__E3,,,_7,,,_,:,String,;,D,:,String,;,C,,,w,,,k3,:,Float,;,__4T,,,p6,,,_,,,g_l,:,q4_,),{,},Constructor,(,_,:,_N0,;,j,,,wk,:,M_,;,MS,:,Array,[,Int,,,0b1010,],;,_L,:,Array,[,Int,,,72,],),{,},},<EOF>''',
                101
            )
        )

    def test_223(self):
        self.assertTrue(
            TestLexer.test(
                '''Class H{Var k,$4,_:_L8;Constructor (){Return ;} }Class X:h9{Var __,Q,_:Array [Array [Array [Array [Array [Array [Boolean ,35],0B1_1_0],035],35],02],030];}''',
                '''Class,H,{,Var,k,,,$4,,,_,:,_L8,;,Constructor,(,),{,Return,;,},},Class,X,:,h9,{,Var,__,,,Q,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,35,],,,0B110,],,,035,],,,35,],,,02,],,,030,],;,},<EOF>''',
                101
            )
        )

    def test_224(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Q_{$3__(P,O7C,p,A:_5;WQ_,g:Array [Array [Boolean ,99],013]){q::$GY.g116_W06y();Break ;}Constructor (){} }''',
                '''Class,Q_,{,$3__,(,P,,,O7C,,,p,,,A,:,_5,;,WQ_,,,g,:,Array,[,Array,[,Boolean,,,99,],,,013,],),{,q,::,$GY,.,g116_W06y,(,),;,Break,;,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_225(self):
        self.assertTrue(
            TestLexer.test(
                '''Class c:M{Destructor (){}Val $tZ6:D0;}Class ___u{}Class __Z_:_{}Class _{Destructor (){} }Class e7{}Class lT:_{}''',
                '''Class,c,:,M,{,Destructor,(,),{,},Val,$tZ6,:,D0,;,},Class,___u,{,},Class,__Z_,:,_,{,},Class,_,{,Destructor,(,),{,},},Class,e7,{,},Class,lT,:,_,{,},<EOF>''',
                101
            )
        )

    def test_226(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Soo:__y{}Class i:h8{}Class Z:Yl{Constructor (){}Constructor (l_,b,b:Array [Boolean ,03652];f:_28X;_N9:Array [Int ,22];_9:__2;_Re,__,_:n;_:Array [Int ,0b101010];___6p:_Z;h2,_D:S99){Break ;Break ;Return ;} }''',
                '''Class,Soo,:,__y,{,},Class,i,:,h8,{,},Class,Z,:,Yl,{,Constructor,(,),{,},Constructor,(,l_,,,b,,,b,:,Array,[,Boolean,,,03652,],;,f,:,_28X,;,_N9,:,Array,[,Int,,,22,],;,_9,:,__2,;,_Re,,,__,,,_,:,n,;,_,:,Array,[,Int,,,0b101010,],;,___6p,:,_Z,;,h2,,,_D,:,S99,),{,Break,;,Break,;,Return,;,},},<EOF>''',
                101
            )
        )

    def test_227(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class __{Constructor (_6r8,_8_RIS_,__4,B,__8,_:Array [Array [Float ,014],0X2A];Y:Float ;V,u_:Boolean ;iE:__5;F,__:p){Continue ;} }Class K4{}Class __C5:H_2{Var _:Int ;}''',
                '''Class,_,{,},Class,__,{,Constructor,(,_6r8,,,_8_RIS_,,,__4,,,B,,,__8,,,_,:,Array,[,Array,[,Float,,,014,],,,0X2A,],;,Y,:,Float,;,V,,,u_,:,Boolean,;,iE,:,__5,;,F,,,__,:,p,),{,Continue,;,},},Class,K4,{,},Class,__C5,:,H_2,{,Var,_,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_228(self):
        self.assertTrue(
            TestLexer.test(
                '''Class p_0z{}Class C:M5{B_(__3998A,Q_:Float ;X:Array [Array [Array [Int ,0x14],86],0xF]){}Var $_I:_15;Var $l_:Boolean ;}Class _55:B_{}''',
                '''Class,p_0z,{,},Class,C,:,M5,{,B_,(,__3998A,,,Q_,:,Float,;,X,:,Array,[,Array,[,Array,[,Int,,,0x14,],,,86,],,,0xF,],),{,},Var,$_I,:,_15,;,Var,$l_,:,Boolean,;,},Class,_55,:,B_,{,},<EOF>''',
                101
            )
        )

    def test_229(self):
        self.assertTrue(
            TestLexer.test(
                '''Class x{}Class _E:_42_62{Destructor (){}Val B,$_:_7_Nz;Var ___,$1,P:Array [Array [Array [Float ,0xD],0B1_0],021];Val $__6,vq:Int ;}''',
                '''Class,x,{,},Class,_E,:,_42_62,{,Destructor,(,),{,},Val,B,,,$_,:,_7_Nz,;,Var,___,,,$1,,,P,:,Array,[,Array,[,Array,[,Float,,,0xD,],,,0B10,],,,021,],;,Val,$__6,,,vq,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_230(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class A9_:wti7{Constructor (){} }Class R_{Destructor (){} }Class ___58X:_d{Constructor (){Continue ;}Destructor (){} }Class _v{}''',
                '''Class,_,{,},Class,A9_,:,wti7,{,Constructor,(,),{,},},Class,R_,{,Destructor,(,),{,},},Class,___58X,:,_d,{,Constructor,(,),{,Continue,;,},Destructor,(,),{,},},Class,_v,{,},<EOF>''',
                101
            )
        )

    def test_231(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A{Val $R__:Array [Array [Array [Array [Boolean ,0B1001001],0B111],0X28],21];Constructor (b6:Array [String ,0x1];_1Q,w_:String ){_::$_();Break ;} }Class _1{}''',
                '''Class,A,{,Val,$R__,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1001001,],,,0B111,],,,0X28,],,,21,],;,Constructor,(,b6,:,Array,[,String,,,0x1,],;,_1Q,,,w_,:,String,),{,_,::,$_,(,),;,Break,;,},},Class,_1,{,},<EOF>''',
                101
            )
        )

    def test_232(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Q:__3{}Class _0:L{Destructor (){}Val _,$J_:Float ;}Class SSm:_{Val P,$_,$K:Array [Array [Float ,041],041];$4(R,I:Array [Float ,0xDB_F_C_AD2]){}_(_:Array [Array [Array [Array [Float ,6],3],03],0b100101];__7,f:Int ;S1_,_:ZCQ){} }''',
                '''Class,Q,:,__3,{,},Class,_0,:,L,{,Destructor,(,),{,},Val,_,,,$J_,:,Float,;,},Class,SSm,:,_,{,Val,P,,,$_,,,$K,:,Array,[,Array,[,Float,,,041,],,,041,],;,$4,(,R,,,I,:,Array,[,Float,,,0xDBFCAD2,],),{,},_,(,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,6,],,,3,],,,03,],,,0b100101,],;,__7,,,f,:,Int,;,S1_,,,_,:,ZCQ,),{,},},<EOF>''',
                101
            )
        )

    def test_233(self):
        self.assertTrue(
            TestLexer.test(
                '''Class O5:_{Constructor (_qt:f_;T_,_,__1:H){}Destructor (){}_Ii(_O6:Int ;o6,_3,UM:Array [Float ,0B1011110];wP7:Array [Boolean ,0X6]){}Val _:Array [Array [Array [Array [Float ,0B1011110],0101],0b101111],0x7];}''',
                '''Class,O5,:,_,{,Constructor,(,_qt,:,f_,;,T_,,,_,,,__1,:,H,),{,},Destructor,(,),{,},_Ii,(,_O6,:,Int,;,o6,,,_3,,,UM,:,Array,[,Float,,,0B1011110,],;,wP7,:,Array,[,Boolean,,,0X6,],),{,},Val,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B1011110,],,,0101,],,,0b101111,],,,0x7,],;,},<EOF>''',
                101
            )
        )

    def test_234(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:f{j_4(_5,_m,zj3u,d_v4,_,_,_w,h,_,PB_:Float ;G_:Float ;t,_,C,_6:Int ;_:Float ;N,h:Array [Array [String ,0X3B],0x7]){}Val E,$_,_,$_:_;Val $vK45:Int ;}''',
                '''Class,_,:,f,{,j_4,(,_5,,,_m,,,zj3u,,,d_v4,,,_,,,_,,,_w,,,h,,,_,,,PB_,:,Float,;,G_,:,Float,;,t,,,_,,,C,,,_6,:,Int,;,_,:,Float,;,N,,,h,:,Array,[,Array,[,String,,,0X3B,],,,0x7,],),{,},Val,E,,,$_,,,_,,,$_,:,_,;,Val,$vK45,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_235(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_v{Constructor (e_:Array [Array [Array [Float ,03_7_10],04],0xDEB_9];_1:Int ;b14T,_5l_:String ){ {} }I(Efy:Z){} }Class m:_{}''',
                '''Class,_,:,_v,{,Constructor,(,e_,:,Array,[,Array,[,Array,[,Float,,,03710,],,,04,],,,0xDEB9,],;,_1,:,Int,;,b14T,,,_5l_,:,String,),{,{,},},I,(,Efy,:,Z,),{,},},Class,m,:,_,{,},<EOF>''',
                101
            )
        )

    def test_236(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (s5_:Array [Array [Array [Array [Array [Array [Array [Boolean ,0b1],0X2D],0106],59],7],0106],0B1];N:D7){ {} }}''',
                '''Class,_,{,Constructor,(,s5_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1,],,,0X2D,],,,0106,],,,59,],,,7,],,,0106,],,,0B1,],;,N,:,D7,),{,{,},},},<EOF>''',
                101
            )
        )

    def test_237(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _:_6{}Class _{}Class Sp{}Class _{_D5U4(__67:Array [Array [String ,0XB],02];_74K,C:Array [Boolean ,0123];S:Boolean ;_:h){}$_6z1(N_d,o,_,d36w3,t:Array [Array [String ,0xE],0XF]){Return ;Break ;Break ;} }''',
                '''Class,_,{,},Class,_,:,_6,{,},Class,_,{,},Class,Sp,{,},Class,_,{,_D5U4,(,__67,:,Array,[,Array,[,String,,,0XB,],,,02,],;,_74K,,,C,:,Array,[,Boolean,,,0123,],;,S,:,Boolean,;,_,:,h,),{,},$_6z1,(,N_d,,,o,,,_,,,d36w3,,,t,:,Array,[,Array,[,String,,,0xE,],,,0XF,],),{,Return,;,Break,;,Break,;,},},<EOF>''',
                101
            )
        )

    def test_238(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _6_:_N28{}Class SB0_:M__T_p5W54_r290_{Val $_:__;}Class _T:_{}Class Z5:_{$4y6(){Break ;} }Class Th{}Class _Z{$7(D:Int ){} }Class _{}''',
                '''Class,_6_,:,_N28,{,},Class,SB0_,:,M__T_p5W54_r290_,{,Val,$_,:,__,;,},Class,_T,:,_,{,},Class,Z5,:,_,{,$4y6,(,),{,Break,;,},},Class,Th,{,},Class,_Z,{,$7,(,D,:,Int,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_239(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __Lw6g_:wf__7_{Destructor (){} }Class D:dH{Constructor (_ye_,N:Array [String ,0B100011];_7_:Array [Array [Array [Array [Array [Boolean ,0X4A],0b1001101],34],34],0b11];J,d00:J_){Continue ;} }Class CD_{}Class _:___7{}''',
                '''Class,__Lw6g_,:,wf__7_,{,Destructor,(,),{,},},Class,D,:,dH,{,Constructor,(,_ye_,,,N,:,Array,[,String,,,0B100011,],;,_7_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X4A,],,,0b1001101,],,,34,],,,34,],,,0b11,],;,J,,,d00,:,J_,),{,Continue,;,},},Class,CD_,{,},Class,_,:,___7,{,},<EOF>''',
                101
            )
        )

    def test_240(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{Constructor (){Break ;}Val _43T2,LV9Y9_,Gc___:Boolean ;Constructor (){}Destructor (){}Constructor (){} }''',
                '''Class,__,{,Constructor,(,),{,Break,;,},Val,_43T2,,,LV9Y9_,,,Gc___,:,Boolean,;,Constructor,(,),{,},Destructor,(,),{,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_241(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _t_{Val R,$7_,$k_,$v6__,B_,l:a_81z;PV(__rz1i__,iv___,o:Boolean ;____,l:Boolean ;_,o78___:Array [Array [Array [Boolean ,0XA],0B1],90]){}Constructor (_:Array [String ,0B1_0]){} }''',
                '''Class,_t_,{,Val,R,,,$7_,,,$k_,,,$v6__,,,B_,,,l,:,a_81z,;,PV,(,__rz1i__,,,iv___,,,o,:,Boolean,;,____,,,l,:,Boolean,;,_,,,o78___,:,Array,[,Array,[,Array,[,Boolean,,,0XA,],,,0B1,],,,90,],),{,},Constructor,(,_,:,Array,[,String,,,0B10,],),{,},},<EOF>''',
                101
            )
        )

    def test_242(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2D_:_{Val $D:String ;Var _,_,Y,A,$5_m2_8B,$___,$9__P_,A:EN;}Class ___:_94{Destructor (){}Val $_552,$z,_,__s,$_:Array [Int ,5];Destructor (){} }''',
                '''Class,_2D_,:,_,{,Val,$D,:,String,;,Var,_,,,_,,,Y,,,A,,,$5_m2_8B,,,$___,,,$9__P_,,,A,:,EN,;,},Class,___,:,_94,{,Destructor,(,),{,},Val,$_552,,,$z,,,_,,,__s,,,$_,:,Array,[,Int,,,5,],;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_243(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (l__:Array [Array [Array [Boolean ,05_20],0B1_1100_0],0B1];rc:Boolean ;_I63O,s__lV:Array [Int ,040]){} }''',
                '''Class,_,{,Constructor,(,l__,:,Array,[,Array,[,Array,[,Boolean,,,0520,],,,0B111000,],,,0B1,],;,rc,:,Boolean,;,_I63O,,,s__lV,:,Array,[,Int,,,040,],),{,},},<EOF>''',
                101
            )
        )

    def test_244(self):
        self.assertTrue(
            TestLexer.test(
                '''Class d:_{}Class _:M_{Var $3:String ;Val $x,_,_2,$_,_:Array [Array [Array [Boolean ,0B1_1],0b10],0X2E];}Class G2:_U{}Class H6{}''',
                '''Class,d,:,_,{,},Class,_,:,M_,{,Var,$3,:,String,;,Val,$x,,,_,,,_2,,,$_,,,_,:,Array,[,Array,[,Array,[,Boolean,,,0B11,],,,0b10,],,,0X2E,],;,},Class,G2,:,_U,{,},Class,H6,{,},<EOF>''',
                101
            )
        )

    def test_245(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_,R_:Array [Array [Array [Int ,0b100101],21],03];j,_e:Float ;i_l3,_u:_){} }Class _{}Class TK_{}Class F36{}''',
                '''Class,_,{,Constructor,(,_,,,R_,:,Array,[,Array,[,Array,[,Int,,,0b100101,],,,21,],,,03,],;,j,,,_e,:,Float,;,i_l3,,,_u,:,_,),{,},},Class,_,{,},Class,TK_,{,},Class,F36,{,},<EOF>''',
                101
            )
        )

    def test_246(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _w_{}Class _:E{Destructor (){} }Class _{Val Z9:Array [Array [Int ,0B11100],04];Var IN,_,_,$3_:String ;Destructor (){} }''',
                '''Class,_w_,{,},Class,_,:,E,{,Destructor,(,),{,},},Class,_,{,Val,Z9,:,Array,[,Array,[,Int,,,0B11100,],,,04,],;,Var,IN,,,_,,,_,,,$3_,:,String,;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_247(self):
        self.assertTrue(
            TestLexer.test(
                '''Class d__:lK_{}Class __d{Destructor (){}Var _754:Array [Array [Boolean ,0X14],0B1010011];}Class _:r{Val $q,_L,$W:o6;}Class _{}''',
                '''Class,d__,:,lK_,{,},Class,__d,{,Destructor,(,),{,},Var,_754,:,Array,[,Array,[,Boolean,,,0X14,],,,0B1010011,],;,},Class,_,:,r,{,Val,$q,,,_L,,,$W,:,o6,;,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_248(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{$62(U,iN,M_:o){}I(___:Array [Boolean ,072];_:String ;z3:_){}Var _:Array [Int ,5_5];}Class __:T__{_(_0:_){} }''',
                '''Class,_,{,$62,(,U,,,iN,,,M_,:,o,),{,},I,(,___,:,Array,[,Boolean,,,072,],;,_,:,String,;,z3,:,_,),{,},Var,_,:,Array,[,Int,,,55,],;,},Class,__,:,T__,{,_,(,_0,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_249(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (n,q:Boolean ;_,M:Boolean ;A,T:Array [Array [Boolean ,0X3A02_C62],0x9]){} }Class _r:a{}Class L_{j__(){} }Class GFCQ6_{}''',
                '''Class,_,{,Constructor,(,n,,,q,:,Boolean,;,_,,,M,:,Boolean,;,A,,,T,:,Array,[,Array,[,Boolean,,,0X3A02C62,],,,0x9,],),{,},},Class,_r,:,a,{,},Class,L_,{,j__,(,),{,},},Class,GFCQ6_,{,},<EOF>''',
                101
            )
        )

    def test_250(self):
        self.assertTrue(
            TestLexer.test(
                '''Class NS:_{Val y,$_,_:Array [Array [Int ,0x1],02_50];Var $_0_6_s__,$_:Array [Array [Array [Array [Boolean ,0B1_11],0x32],0b1100000],0125];}''',
                '''Class,NS,:,_,{,Val,y,,,$_,,,_,:,Array,[,Array,[,Int,,,0x1,],,,0250,],;,Var,$_0_6_s__,,,$_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B111,],,,0x32,],,,0b1100000,],,,0125,],;,},<EOF>''',
                101
            )
        )

    def test_251(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V:_{Destructor (){}$_(){}Val $h_HO__V_,$Y,$Z:Array [Array [String ,01_10],0B1];Val F,__,_8Xg2,_:Int ;}Class _6:w_{}''',
                '''Class,V,:,_,{,Destructor,(,),{,},$_,(,),{,},Val,$h_HO__V_,,,$Y,,,$Z,:,Array,[,Array,[,String,,,0110,],,,0B1,],;,Val,F,,,__,,,_8Xg2,,,_,:,Int,;,},Class,_6,:,w_,{,},<EOF>''',
                101
            )
        )

    def test_252(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class s:_S_{Val e:Array [Float ,56];Destructor (){}$96_b_(){} }Class _T7Y18_r3:bsA7G{}Class Q{Constructor (E:Array [Int ,031]){} }Class R_:_2{}''',
                '''Class,_,{,},Class,s,:,_S_,{,Val,e,:,Array,[,Float,,,56,],;,Destructor,(,),{,},$96_b_,(,),{,},},Class,_T7Y18_r3,:,bsA7G,{,},Class,Q,{,Constructor,(,E,:,Array,[,Int,,,031,],),{,},},Class,R_,:,_2,{,},<EOF>''',
                101
            )
        )

    def test_253(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{B_1(WGJ,__9,R:Z;a,_6__:Array [Array [Array [Array [Float ,073],05],1],1];_m:Array [String ,1]){} }Class r{}''',
                '''Class,__,{,B_1,(,WGJ,,,__9,,,R,:,Z,;,a,,,_6__,:,Array,[,Array,[,Array,[,Array,[,Float,,,073,],,,05,],,,1,],,,1,],;,_m,:,Array,[,String,,,1,],),{,},},Class,r,{,},<EOF>''',
                101
            )
        )

    def test_254(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{_K(){} }Class K{Y_A3(_7:Array [Int ,0b1001100];d_:u;_a,_L:String ;_6H1:_){}$1_(a:_){Break ;Break ;}Var qkD:_5;}Class _{}''',
                '''Class,_,{,_K,(,),{,},},Class,K,{,Y_A3,(,_7,:,Array,[,Int,,,0b1001100,],;,d_,:,u,;,_a,,,_L,:,String,;,_6H1,:,_,),{,},$1_,(,a,:,_,),{,Break,;,Break,;,},Var,qkD,:,_5,;,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_255(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l__{}Class a{}Class __5S{Var $0_,$k,__:G2_;Var $U9:Boolean ;Constructor (){ {} }}Class _:x{}Class _9:W6__{$9(){} }''',
                '''Class,l__,{,},Class,a,{,},Class,__5S,{,Var,$0_,,,$k,,,__,:,G2_,;,Var,$U9,:,Boolean,;,Constructor,(,),{,{,},},},Class,_,:,x,{,},Class,_9,:,W6__,{,$9,(,),{,},},<EOF>''',
                101
            )
        )

    def test_256(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:V{}Class _6g{Val $_,_:Array [String ,3_7_2];Var x7,$_991,$8:Array [Array [Array [Array [Int ,06],85],06],0135];Var M:Array [String ,0b1];}''',
                '''Class,_,:,V,{,},Class,_6g,{,Val,$_,,,_,:,Array,[,String,,,372,],;,Var,x7,,,$_991,,,$8,:,Array,[,Array,[,Array,[,Array,[,Int,,,06,],,,85,],,,06,],,,0135,],;,Var,M,:,Array,[,String,,,0b1,],;,},<EOF>''',
                101
            )
        )

    def test_257(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Kp{Constructor (_,T_:Boolean ){}Destructor (){} }Class L{Val S___61gCH:Array [Array [Boolean ,020],63];}Class _:S{}Class R{}''',
                '''Class,Kp,{,Constructor,(,_,,,T_,:,Boolean,),{,},Destructor,(,),{,},},Class,L,{,Val,S___61gCH,:,Array,[,Array,[,Boolean,,,020,],,,63,],;,},Class,_,:,S,{,},Class,R,{,},<EOF>''',
                101
            )
        )

    def test_258(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{s_(jm,_,__:String ;r56_:Float ;M_6o:_i__N){_2::$i9();} }Class K1z4_{Constructor (_8_:Int ;k0:Array [String ,0B1001100]){}Var $3,$k0:h;}''',
                '''Class,_,{,s_,(,jm,,,_,,,__,:,String,;,r56_,:,Float,;,M_6o,:,_i__N,),{,_2,::,$i9,(,),;,},},Class,K1z4_,{,Constructor,(,_8_,:,Int,;,k0,:,Array,[,String,,,0B1001100,],),{,},Var,$3,,,$k0,:,h,;,},<EOF>''',
                101
            )
        )

    def test_259(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _:dZ{$a(T:Boolean ){}Var $7,$_,V,$O,i0,$_:Array [Array [Array [Int ,0XAC],03],015];}Class _0:x{}''',
                '''Class,_,{,},Class,_,:,dZ,{,$a,(,T,:,Boolean,),{,},Var,$7,,,$_,,,V,,,$O,,,i0,,,$_,:,Array,[,Array,[,Array,[,Int,,,0XAC,],,,03,],,,015,],;,},Class,_0,:,x,{,},<EOF>''',
                101
            )
        )

    def test_260(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:O{}Class _X{$_0e2k(ox:x;W__,i579b83:_;_2MZ,c,_:Array [Array [Array [Int ,07],0x7],0X4B]){Continue ;}Val $_:Array [Array [Float ,0b1000010],3];}Class _:_{}''',
                '''Class,_,:,O,{,},Class,_X,{,$_0e2k,(,ox,:,x,;,W__,,,i579b83,:,_,;,_2MZ,,,c,,,_,:,Array,[,Array,[,Array,[,Int,,,07,],,,0x7,],,,0X4B,],),{,Continue,;,},Val,$_,:,Array,[,Array,[,Float,,,0b1000010,],,,3,],;,},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_261(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:P_8xZ{Destructor (){Continue ;}Val $g53:Array [Array [Array [Array [String ,0b111000],0x7C],62],1];}Class S:xK{__(){Val _,h:Array [Int ,0B1];} }Class _32_Z:U{Val $__:_W;}''',
                '''Class,_,:,P_8xZ,{,Destructor,(,),{,Continue,;,},Val,$g53,:,Array,[,Array,[,Array,[,Array,[,String,,,0b111000,],,,0x7C,],,,62,],,,1,],;,},Class,S,:,xK,{,__,(,),{,Val,_,,,h,:,Array,[,Int,,,0B1,],;,},},Class,_32_Z,:,U,{,Val,$__,:,_W,;,},<EOF>''',
                101
            )
        )

    def test_262(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _y_62_:KB{}Class _3_k:_{$M(S1:Array [Float ,0x16];E,_,o,_:Array [Boolean ,0B1];_rU:Array [Int ,024];K,T:Array [Float ,36]){} }''',
                '''Class,_y_62_,:,KB,{,},Class,_3_k,:,_,{,$M,(,S1,:,Array,[,Float,,,0x16,],;,E,,,_,,,o,,,_,:,Array,[,Boolean,,,0B1,],;,_rU,:,Array,[,Int,,,024,],;,K,,,T,:,Array,[,Float,,,36,],),{,},},<EOF>''',
                101
            )
        )

    def test_263(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _5{$4(){}Var $d,$_99,$__,b,$1:Array [Int ,0b1];}Class H{Constructor (){__::$_();Break ;Var _:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,0X27],05_504_2],071],410],8],0X27],0X27],01],071],0X27],0b11011];}Val x:__j_;}''',
                '''Class,_5,{,$4,(,),{,},Var,$d,,,$_99,,,$__,,,b,,,$1,:,Array,[,Int,,,0b1,],;,},Class,H,{,Constructor,(,),{,__,::,$_,(,),;,Break,;,Var,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X27,],,,055042,],,,071,],,,410,],,,8,],,,0X27,],,,0X27,],,,01,],,,071,],,,0X27,],,,0b11011,],;,},Val,x,:,__j_,;,},<EOF>''',
                101
            )
        )

    def test_264(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t6_:n_65q7{$_(yX,__GK_:Boolean ;_O:Array [Array [Array [Array [Array [Boolean ,0XB],0b1_1],0107],0B101001],0107]){} }''',
                '''Class,t6_,:,n_65q7,{,$_,(,yX,,,__GK_,:,Boolean,;,_O,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0XB,],,,0b11,],,,0107,],,,0B101001,],,,0107,],),{,},},<EOF>''',
                101
            )
        )

    def test_265(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class fu_:_{Val _Y7:E;Constructor (V:Array [Array [Array [Array [Boolean ,0B111_1_0],55],0b110110],05_52_07];_r_7,_Z,_2,_:Boolean ;G,B0_:Float ;D,G2:Array [String ,55];_:Float ;_V,_9R_c:Array [String ,02346_6]){} }''',
                '''Class,__,{,},Class,fu_,:,_,{,Val,_Y7,:,E,;,Constructor,(,V,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B11110,],,,55,],,,0b110110,],,,055207,],;,_r_7,,,_Z,,,_2,,,_,:,Boolean,;,G,,,B0_,:,Float,;,D,,,G2,:,Array,[,String,,,55,],;,_,:,Float,;,_V,,,_9R_c,:,Array,[,String,,,023466,],),{,},},<EOF>''',
                101
            )
        )

    def test_266(self):
        self.assertTrue(
            TestLexer.test(
                '''Class oXk{}Class _{}Class ___G78:c6{}Class _{}Class _w{}Class _K_:_{}Class z:L6R{}Class _{Constructor (P,o__29,I19_6:Float ;ba:Float ;_Z_:Float ;_,X_:__){}Destructor (){} }''',
                '''Class,oXk,{,},Class,_,{,},Class,___G78,:,c6,{,},Class,_,{,},Class,_w,{,},Class,_K_,:,_,{,},Class,z,:,L6R,{,},Class,_,{,Constructor,(,P,,,o__29,,,I19_6,:,Float,;,ba,:,Float,;,_Z_,:,Float,;,_,,,X_,:,__,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_267(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C:_{}Class h{Constructor (){}Destructor (){}Var B:String ;}Class V:w{}Class xH2__o:t_1u{}Class _:_Z_6__6{}''',
                '''Class,C,:,_,{,},Class,h,{,Constructor,(,),{,},Destructor,(,),{,},Var,B,:,String,;,},Class,V,:,w,{,},Class,xH2__o,:,t_1u,{,},Class,_,:,_Z_6__6,{,},<EOF>''',
                101
            )
        )

    def test_268(self):
        self.assertTrue(
            TestLexer.test(
                '''Class f3:yoD_{}Class _:r{Var $_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,0x1],071],72],04],0xA],0b10],3],0X68B],071],0X40],0X40];}Class __{Destructor (){}Val _F_:_;Var h9,GO:Array [Array [String ,0b1_1],0b100000];}Class _:_3{}''',
                '''Class,f3,:,yoD_,{,},Class,_,:,r,{,Var,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x1,],,,071,],,,72,],,,04,],,,0xA,],,,0b10,],,,3,],,,0X68B,],,,071,],,,0X40,],,,0X40,],;,},Class,__,{,Destructor,(,),{,},Val,_F_,:,_,;,Var,h9,,,GO,:,Array,[,Array,[,String,,,0b11,],,,0b100000,],;,},Class,_,:,_3,{,},<EOF>''',
                101
            )
        )

    def test_269(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _1{Constructor (G4_:Array [Array [Array [Array [Array [Array [Float ,2],846_8_4],0X54],0104],0b1],0X54]){} }Class _:c_{Constructor (p:Boolean ){} }Class V{Val j:_=!!_I::$_r;}''',
                '''Class,_1,{,Constructor,(,G4_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,2,],,,84684,],,,0X54,],,,0104,],,,0b1,],,,0X54,],),{,},},Class,_,:,c_,{,Constructor,(,p,:,Boolean,),{,},},Class,V,{,Val,j,:,_,=,!,!,_I,::,$_r,;,},<EOF>''',
                101
            )
        )

    def test_270(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _1vJ_1{__7(_Y:Array [Array [Array [Array [Boolean ,07_5],9_4],0b1],03];_7,O:a){}Val _:Array [Boolean ,0x33];}''',
                '''Class,_,{,},Class,_1vJ_1,{,__7,(,_Y,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,075,],,,94,],,,0b1,],,,03,],;,_7,,,O,:,a,),{,},Val,_,:,Array,[,Boolean,,,0x33,],;,},<EOF>''',
                101
            )
        )

    def test_271(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P{Destructor (){} }Class p_:em_J2{}Class __:_9{Var $_J,_:Array [Boolean ,0b1];}Class _:Y{_M(){} }Class L{$9(){} }Class _:_{}''',
                '''Class,P,{,Destructor,(,),{,},},Class,p_,:,em_J2,{,},Class,__,:,_9,{,Var,$_J,,,_,:,Array,[,Boolean,,,0b1,],;,},Class,_,:,Y,{,_M,(,),{,},},Class,L,{,$9,(,),{,},},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_272(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_82{Constructor (){}Val $_3_UQ__7,$e_4_,W:M;}Class G:I{}Class _ka{}Class E__C_0{$_(){Return ;}$2jb_L2wm(){}Destructor (){} }Class Y{Destructor (){} }''',
                '''Class,_,:,_82,{,Constructor,(,),{,},Val,$_3_UQ__7,,,$e_4_,,,W,:,M,;,},Class,G,:,I,{,},Class,_ka,{,},Class,E__C_0,{,$_,(,),{,Return,;,},$2jb_L2wm,(,),{,},Destructor,(,),{,},},Class,Y,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_273(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _l{I___(x_:String ;j_:_50P;N_x_,_,B:Array [Array [Array [Array [Boolean ,0B1000_0_10],0XE],06],0B110110]){} }''',
                '''Class,_l,{,I___,(,x_,:,String,;,j_,:,_50P,;,N_x_,,,_,,,B,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1000010,],,,0XE,],,,06,],,,0B110110,],),{,},},<EOF>''',
                101
            )
        )

    def test_274(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J6:_{Destructor (){} }Class N4_{Constructor (f_I:m__0_;_:Array [Array [Array [Array [Array [String ,0133_5],0b1101],043],043],0X9]){Return ;{} }Constructor (_7s:_c){} }Class G{}Class _:Si0{}''',
                '''Class,J6,:,_,{,Destructor,(,),{,},},Class,N4_,{,Constructor,(,f_I,:,m__0_,;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,01335,],,,0b1101,],,,043,],,,043,],,,0X9,],),{,Return,;,{,},},Constructor,(,_7s,:,_c,),{,},},Class,G,{,},Class,_,:,Si0,{,},<EOF>''',
                101
            )
        )

    def test_275(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g:C{Constructor (S,_0i_6,W7_:Array [Array [Array [Array [Array [Array [Array [Int ,0x1],0b11],04],7],0b1],0b1],0B10]){ {} }}''',
                '''Class,g,:,C,{,Constructor,(,S,,,_0i_6,,,W7_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x1,],,,0b11,],,,04,],,,7,],,,0b1,],,,0b1,],,,0B10,],),{,{,},},},<EOF>''',
                101
            )
        )

    def test_276(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class __rW__:_90o{Val Cq:Array [Array [String ,06],0B110100];Constructor (_,_I,__4767_5:Float ;_5:Array [Float ,05];_,_,T6J1_,b1G:Array [Array [Array [Array [Array [Int ,54],04],0b1_0],0XA],0b1110];K,_,c:Array [Int ,0X12]){_::$0R.ri.__f.b();} }''',
                '''Class,_,:,_,{,},Class,__rW__,:,_90o,{,Val,Cq,:,Array,[,Array,[,String,,,06,],,,0B110100,],;,Constructor,(,_,,,_I,,,__4767_5,:,Float,;,_5,:,Array,[,Float,,,05,],;,_,,,_,,,T6J1_,,,b1G,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,54,],,,04,],,,0b10,],,,0XA,],,,0b1110,],;,K,,,_,,,c,:,Array,[,Int,,,0X12,],),{,_,::,$0R,.,ri,.,__f,.,b,(,),;,},},<EOF>''',
                101
            )
        )

    def test_277(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b{Constructor (_,_:u_9Z_;J,U_:__M;_j8,j,v,_:Array [Array [Boolean ,0140],0X34];r:_;_1_N_c90:String ){}Constructor (V0:Array [String ,03]){} }''',
                '''Class,b,{,Constructor,(,_,,,_,:,u_9Z_,;,J,,,U_,:,__M,;,_j8,,,j,,,v,,,_,:,Array,[,Array,[,Boolean,,,0140,],,,0X34,],;,r,:,_,;,_1_N_c90,:,String,),{,},Constructor,(,V0,:,Array,[,String,,,03,],),{,},},<EOF>''',
                101
            )
        )

    def test_278(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l_:_{Val $_:Array [Array [Array [Float ,067],06],0X9];}Class _{Val p___,$_:p;Destructor (){}Var r9b:K;}Class j8__:x{Val _:Array [Array [Array [String ,067],52],067];}''',
                '''Class,l_,:,_,{,Val,$_,:,Array,[,Array,[,Array,[,Float,,,067,],,,06,],,,0X9,],;,},Class,_,{,Val,p___,,,$_,:,p,;,Destructor,(,),{,},Var,r9b,:,K,;,},Class,j8__,:,x,{,Val,_,:,Array,[,Array,[,Array,[,String,,,067,],,,52,],,,067,],;,},<EOF>''',
                101
            )
        )

    def test_279(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0D:_{Y(){}Val $Aa,$P8,$3:Array [Array [Array [Array [Array [Array [Array [String ,0B10_0],0X2E],9],0x29],0x29],04],023];}Class b_:_R{}Class _4:K{}Class sq1{Constructor (_:Array [Array [Int ,0b10_1],0535_270];_:C_5qun_;j:Array [String ,29];_,m:Int ){} }''',
                '''Class,_0D,:,_,{,Y,(,),{,},Val,$Aa,,,$P8,,,$3,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B100,],,,0X2E,],,,9,],,,0x29,],,,0x29,],,,04,],,,023,],;,},Class,b_,:,_R,{,},Class,_4,:,K,{,},Class,sq1,{,Constructor,(,_,:,Array,[,Array,[,Int,,,0b101,],,,0535270,],;,_,:,C_5qun_,;,j,:,Array,[,String,,,29,],;,_,,,m,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_280(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $_,_,$e,t:String ;}Class _:_{_(_9:Array [Array [Boolean ,0XD],0x9_3_B]){Val a,y:String ;Continue ;} }''',
                '''Class,_,{,Val,$_,,,_,,,$e,,,t,:,String,;,},Class,_,:,_,{,_,(,_9,:,Array,[,Array,[,Boolean,,,0XD,],,,0x93B,],),{,Val,a,,,y,:,String,;,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_281(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:b__{Constructor (Z:Array [Array [Array [Array [Array [Array [Array [String ,0X35],0X4],0X35],24],0110],0X4_B_4],03]){}Constructor (){} }''',
                '''Class,_,:,b__,{,Constructor,(,Z,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X35,],,,0X4,],,,0X35,],,,24,],,,0110,],,,0X4B4,],,,03,],),{,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_282(self):
        self.assertTrue(
            TestLexer.test(
                '''Class S:x_{}Class _{}Class S{}Class _7f:_{}Class _{Var $d__r,_,$e9__y:Array [Array [Int ,0XAA],0X9];}Class _5:f90{}''',
                '''Class,S,:,x_,{,},Class,_,{,},Class,S,{,},Class,_7f,:,_,{,},Class,_,{,Var,$d__r,,,_,,,$e9__y,:,Array,[,Array,[,Int,,,0XAA,],,,0X9,],;,},Class,_5,:,f90,{,},<EOF>''',
                101
            )
        )

    def test_283(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t{}Class __a:_M5{}Class _{__W(){} }Class __{Val _0:Array [String ,7_31];}Class R{Val _5:Float ;Constructor (_:Array [Array [Boolean ,6_1],0b1_01_110]){}Var $Z1,X,$_gx_,_:Int ;Val Y9,v,__x48:Int ;Destructor (){} }Class k{}Class da{Constructor (B,V:_ZX){Break ;} }''',
                '''Class,t,{,},Class,__a,:,_M5,{,},Class,_,{,__W,(,),{,},},Class,__,{,Val,_0,:,Array,[,String,,,731,],;,},Class,R,{,Val,_5,:,Float,;,Constructor,(,_,:,Array,[,Array,[,Boolean,,,61,],,,0b101110,],),{,},Var,$Z1,,,X,,,$_gx_,,,_,:,Int,;,Val,Y9,,,v,,,__x48,:,Int,;,Destructor,(,),{,},},Class,k,{,},Class,da,{,Constructor,(,B,,,V,:,_ZX,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_284(self):
        self.assertTrue(
            TestLexer.test(
                '''Class j{}Class _2f:q{}Class q_:t{}Class ED{}Class _{Val YOp,$j8:_;Var $__,Q:String ;}Class _:T9g{Val _,$l,$_,_,_71,$0:Array [Array [Float ,79],0X57];_8(){} }''',
                '''Class,j,{,},Class,_2f,:,q,{,},Class,q_,:,t,{,},Class,ED,{,},Class,_,{,Val,YOp,,,$j8,:,_,;,Var,$__,,,Q,:,String,;,},Class,_,:,T9g,{,Val,_,,,$l,,,$_,,,_,,,_71,,,$0,:,Array,[,Array,[,Float,,,79,],,,0X57,],;,_8,(,),{,},},<EOF>''',
                101
            )
        )

    def test_285(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:k{Destructor (){}Var $5,$_,$x:_6;Destructor (){}Val $_b1:Int =!!!z1i::$V_C._I/!!!I::$__().m__;Destructor (){} }Class F{}Class F{Constructor (O8:Array [Boolean ,59]){} }Class J:_{}Class _1_{}''',
                '''Class,_,:,k,{,Destructor,(,),{,},Var,$5,,,$_,,,$x,:,_6,;,Destructor,(,),{,},Val,$_b1,:,Int,=,!,!,!,z1i,::,$V_C,.,_I,/,!,!,!,I,::,$__,(,),.,m__,;,Destructor,(,),{,},},Class,F,{,},Class,F,{,Constructor,(,O8,:,Array,[,Boolean,,,59,],),{,},},Class,J,:,_,{,},Class,_1_,{,},<EOF>''',
                101
            )
        )

    def test_286(self):
        self.assertTrue(
            TestLexer.test(
                '''Class I_{Var l,$4,kl,$6:String ;x9(){Continue ;Var _:r;Var m:_;}$e(W_0:String ;_8:C3){Var A:U;} }Class PF{Val $V_,$___:_;}Class c:_{Constructor (){_f2::$3_();_::$j9();} }''',
                '''Class,I_,{,Var,l,,,$4,,,kl,,,$6,:,String,;,x9,(,),{,Continue,;,Var,_,:,r,;,Var,m,:,_,;,},$e,(,W_0,:,String,;,_8,:,C3,),{,Var,A,:,U,;,},},Class,PF,{,Val,$V_,,,$___,:,_,;,},Class,c,:,_,{,Constructor,(,),{,_f2,::,$3_,(,),;,_,::,$j9,(,),;,},},<EOF>''',
                101
            )
        )

    def test_287(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _L:_{Val $58_p:Array [Boolean ,0b1_1_1_0];Val p__1,F_r,__W,$wx18,$___,_4,s_,_21:Array [Array [Array [Boolean ,0B1],0b1001],100];_c(){}_(_:Int ;H:J4_939_){} }Class k:w7{}Class _:F{}Class E9y:_6{}Class __{}''',
                '''Class,_L,:,_,{,Val,$58_p,:,Array,[,Boolean,,,0b1110,],;,Val,p__1,,,F_r,,,__W,,,$wx18,,,$___,,,_4,,,s_,,,_21,:,Array,[,Array,[,Array,[,Boolean,,,0B1,],,,0b1001,],,,100,],;,_c,(,),{,},_,(,_,:,Int,;,H,:,J4_939_,),{,},},Class,k,:,w7,{,},Class,_,:,F,{,},Class,E9y,:,_6,{,},Class,__,{,},<EOF>''',
                101
            )
        )

    def test_288(self):
        self.assertTrue(
            TestLexer.test(
                '''Class VS___:z_{Var $c:Array [Boolean ,0B10100];$_Y(){ {Break ;Continue ;} }}Class _{Constructor (f,_E,k,G_:Int ;_g,_,_IG,__:_;_:_){} }''',
                '''Class,VS___,:,z_,{,Var,$c,:,Array,[,Boolean,,,0B10100,],;,$_Y,(,),{,{,Break,;,Continue,;,},},},Class,_,{,Constructor,(,f,,,_E,,,k,,,G_,:,Int,;,_g,,,_,,,_IG,,,__,:,_,;,_,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_289(self):
        self.assertTrue(
            TestLexer.test(
                '''Class O_:__Cm{Var $Y3r0W,_,x__59,___:Array [Array [Float ,37],0B1111];Var $6:Array [Boolean ,0XF]=-_D2i5::$Q.yJ9x;Var $___A,JD:D_;}''',
                '''Class,O_,:,__Cm,{,Var,$Y3r0W,,,_,,,x__59,,,___,:,Array,[,Array,[,Float,,,37,],,,0B1111,],;,Var,$6,:,Array,[,Boolean,,,0XF,],=,-,_D2i5,::,$Q,.,yJ9x,;,Var,$___A,,,JD,:,D_,;,},<EOF>''',
                101
            )
        )

    def test_290(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val s_:String ;}Class L:j__{_(c:Boolean ;_:Array [Array [Array [Array [Boolean ,76],507_3],0B100010],71]){}Var $_,Q_:Float ;}''',
                '''Class,_,{,Val,s_,:,String,;,},Class,L,:,j__,{,_,(,c,:,Boolean,;,_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,76,],,,5073,],,,0B100010,],,,71,],),{,},Var,$_,,,Q_,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_291(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V:_146{$n(_t4,x,M,o8_:Array [Array [Array [Array [Array [Int ,0B11],07],3],0b1010011],4];_B:Array [Array [Float ,8_4_9_1],3];xMHg,K8__,_,_7,E_6:_h;_:Boolean ;J:K;__r:Float ;IZ_,__,_:Qx1v__){} }''',
                '''Class,V,:,_146,{,$n,(,_t4,,,x,,,M,,,o8_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B11,],,,07,],,,3,],,,0b1010011,],,,4,],;,_B,:,Array,[,Array,[,Float,,,8491,],,,3,],;,xMHg,,,K8__,,,_,,,_7,,,E_6,:,_h,;,_,:,Boolean,;,J,:,K,;,__r,:,Float,;,IZ_,,,__,,,_,:,Qx1v__,),{,},},<EOF>''',
                101
            )
        )

    def test_292(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l:___{Constructor (a___:W___m;__:Y;g,_,t,_3:Array [Array [Int ,8],055]){ {_q::$_7_._()._.O_xqw.k();Break ;} }}''',
                '''Class,l,:,___,{,Constructor,(,a___,:,W___m,;,__,:,Y,;,g,,,_,,,t,,,_3,:,Array,[,Array,[,Int,,,8,],,,055,],),{,{,_q,::,$_7_,.,_,(,),.,_,.,O_xqw,.,k,(,),;,Break,;,},},},<EOF>''',
                101
            )
        )

    def test_293(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:__{Var $__:_S;Constructor (){}$D3DV(){}Var $_M,_F:Array [Array [Array [Int ,050],49],050];}Class _65{I(){Continue ;} }Class N{}Class X:_{}''',
                '''Class,_,:,__,{,Var,$__,:,_S,;,Constructor,(,),{,},$D3DV,(,),{,},Var,$_M,,,_F,:,Array,[,Array,[,Array,[,Int,,,050,],,,49,],,,050,],;,},Class,_65,{,I,(,),{,Continue,;,},},Class,N,{,},Class,X,:,_,{,},<EOF>''',
                101
            )
        )

    def test_294(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _I{$_(U:Array [Array [Array [String ,2_11_3_53],0xD],05_16_0];_:Array [Array [Array [Array [Array [Array [Int ,0B1],16],05_2],03],0X12],30_1]){} }Class _6o:B{Destructor (){Continue ;} }''',
                '''Class,_I,{,$_,(,U,:,Array,[,Array,[,Array,[,String,,,211353,],,,0xD,],,,05160,],;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B1,],,,16,],,,052,],,,03,],,,0X12,],,,301,],),{,},},Class,_6o,:,B,{,Destructor,(,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_295(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:A{}Class M_r{Constructor (){}Var _:Boolean ;Destructor (){Var _v3,dc_,D,A_L:String ;}Destructor (){} }''',
                '''Class,__,:,A,{,},Class,M_r,{,Constructor,(,),{,},Var,_,:,Boolean,;,Destructor,(,),{,Var,_v3,,,dc_,,,D,,,A_L,:,String,;,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_296(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class U{}Class F_G{Destructor (){} }Class R_:K{Constructor (_:K){}Constructor (_,_0,H,_C,m_P,_:String ){Break ;} }''',
                '''Class,_,{,},Class,U,{,},Class,F_G,{,Destructor,(,),{,},},Class,R_,:,K,{,Constructor,(,_,:,K,),{,},Constructor,(,_,,,_0,,,H,,,_C,,,m_P,,,_,:,String,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_297(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Th__{Val $23l7_:M;}Class _:__{Var _,$3,_,_:Array [Int ,0b11_11_11];Constructor (C:t;GZ8,G_3_q,k_Qq:String ){} }''',
                '''Class,Th__,{,Val,$23l7_,:,M,;,},Class,_,:,__,{,Var,_,,,$3,,,_,,,_,:,Array,[,Int,,,0b111111,],;,Constructor,(,C,:,t,;,GZ8,,,G_3_q,,,k_Qq,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_298(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Destructor (){}$2_(_,u:String ;_hy_:Array [Array [String ,0b1_1100_1],056]){_::$_().F();}Destructor (){} }Class N{Destructor (){}Val E_,$r,$I,$_:r___RwL2_;}''',
                '''Class,_,{,Destructor,(,),{,},$2_,(,_,,,u,:,String,;,_hy_,:,Array,[,Array,[,String,,,0b111001,],,,056,],),{,_,::,$_,(,),.,F,(,),;,},Destructor,(,),{,},},Class,N,{,Destructor,(,),{,},Val,E_,,,$r,,,$I,,,$_,:,r___RwL2_,;,},<EOF>''',
                101
            )
        )

    def test_299(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class D:q_{Var $40K:J;}Class v3{Constructor (_,MK,Y:String ){}Constructor (){}Var $_,v_h,_,$_gx,o:String ;}''',
                '''Class,_,{,},Class,D,:,q_,{,Var,$40K,:,J,;,},Class,v3,{,Constructor,(,_,,,MK,,,Y,:,String,),{,},Constructor,(,),{,},Var,$_,,,v_h,,,_,,,$_gx,,,o,:,String,;,},<EOF>''',
                101
            )
        )

    def test_300(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l:_{Var $_,$_,H5,_,$__:Float ;}Class h_:T9{Var $5,$49:Boolean ;Constructor (){Continue ;}Val _,a:__;Val $3,x,I,j__:l;}''',
                '''Class,l,:,_,{,Var,$_,,,$_,,,H5,,,_,,,$__,:,Float,;,},Class,h_,:,T9,{,Var,$5,,,$49,:,Boolean,;,Constructor,(,),{,Continue,;,},Val,_,,,a,:,__,;,Val,$3,,,x,,,I,,,j__,:,l,;,},<EOF>''',
                101
            )
        )

    def test_301(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_N{Val L:Array [Array [Array [Array [Array [Array [String ,48],0b100001],7],0B1_1],0x41],48];}Class sK0Q1{}Class __{Val $d:Float ;}Class _{Var N_,_:_R;}Class R{Constructor (){} }''',
                '''Class,_,:,_N,{,Val,L,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,48,],,,0b100001,],,,7,],,,0B11,],,,0x41,],,,48,],;,},Class,sK0Q1,{,},Class,__,{,Val,$d,:,Float,;,},Class,_,{,Var,N_,,,_,:,_R,;,},Class,R,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_302(self):
        self.assertTrue(
            TestLexer.test(
                '''Class h1:_I{Constructor (_d,Z,_4:Float ){Return ;} }Class B{}Class K{Val tX:String ;Constructor (_:Array [String ,071];_,_:Array [Array [Boolean ,0x40],0x963_D];_Q,__:Array [Int ,062];y,_2O__:Array [String ,062];Kbi,_:Array [Array [Array [Float ,0X14],0X14],0b111010]){} }''',
                '''Class,h1,:,_I,{,Constructor,(,_d,,,Z,,,_4,:,Float,),{,Return,;,},},Class,B,{,},Class,K,{,Val,tX,:,String,;,Constructor,(,_,:,Array,[,String,,,071,],;,_,,,_,:,Array,[,Array,[,Boolean,,,0x40,],,,0x963D,],;,_Q,,,__,:,Array,[,Int,,,062,],;,y,,,_2O__,:,Array,[,String,,,062,],;,Kbi,,,_,:,Array,[,Array,[,Array,[,Float,,,0X14,],,,0X14,],,,0b111010,],),{,},},<EOF>''',
                101
            )
        )

    def test_303(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _S22o_:_{Constructor (){}Constructor (___:Array [Array [Array [Array [Array [Array [Array [Int ,024],0XD],2],020],597],0X30],67];_,x,_79:String ;_:Int ){} }Class _8q_d9__A{}''',
                '''Class,_S22o_,:,_,{,Constructor,(,),{,},Constructor,(,___,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,024,],,,0XD,],,,2,],,,020,],,,597,],,,0X30,],,,67,],;,_,,,x,,,_79,:,String,;,_,:,Int,),{,},},Class,_8q_d9__A,{,},<EOF>''',
                101
            )
        )

    def test_304(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _{}Class H_N2_:z{_(_2,F,_,t2,_4_:Array [Array [Array [Boolean ,0113],8_84],46];_0:Float ;L:Float ;_,_I5,c02r,_a,_,n:Array [String ,0b1_1];u_,p:Int ){} }Class S{Val x0,_,$_:String ;}''',
                '''Class,_,{,},Class,_,{,},Class,H_N2_,:,z,{,_,(,_2,,,F,,,_,,,t2,,,_4_,:,Array,[,Array,[,Array,[,Boolean,,,0113,],,,884,],,,46,],;,_0,:,Float,;,L,:,Float,;,_,,,_I5,,,c02r,,,_a,,,_,,,n,:,Array,[,String,,,0b11,],;,u_,,,p,:,Int,),{,},},Class,S,{,Val,x0,,,_,,,$_,:,String,;,},<EOF>''',
                101
            )
        )

    def test_305(self):
        self.assertTrue(
            TestLexer.test(
                '''Class I{Val _9:Array [Array [Array [Int ,0B1100001],4],7];Destructor (){}Val $K_:h5;Var u,$4:_;}Class _{}Class o_00{$J(){} }Class v{}Class Ii{}''',
                '''Class,I,{,Val,_9,:,Array,[,Array,[,Array,[,Int,,,0B1100001,],,,4,],,,7,],;,Destructor,(,),{,},Val,$K_,:,h5,;,Var,u,,,$4,:,_,;,},Class,_,{,},Class,o_00,{,$J,(,),{,},},Class,v,{,},Class,Ii,{,},<EOF>''',
                101
            )
        )

    def test_306(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7y_2{Constructor (){}Val _,$B:Array [Array [Array [Array [Boolean ,6],0X6],0B1],0X3E];}Class _:_{Destructor (){}Val $FE_f,$u1,R:Array [Array [Float ,7],38];}''',
                '''Class,_7y_2,{,Constructor,(,),{,},Val,_,,,$B,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,6,],,,0X6,],,,0B1,],,,0X3E,],;,},Class,_,:,_,{,Destructor,(,),{,},Val,$FE_f,,,$u1,,,R,:,Array,[,Array,[,Float,,,7,],,,38,],;,},<EOF>''',
                101
            )
        )

    def test_307(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _00{Destructor (){Continue ;}n__(){Continue ;}Val i_:UZ;Constructor (){} }Class __:_{$SY___8(_1,VTf____3:Array [Float ,0b10]){}Var $0cAzSE:Array [Boolean ,0xB];Val $__8,$Q,K:Array [Array [String ,6],0B1011110];}Class m_M9:_{}''',
                '''Class,_00,{,Destructor,(,),{,Continue,;,},n__,(,),{,Continue,;,},Val,i_,:,UZ,;,Constructor,(,),{,},},Class,__,:,_,{,$SY___8,(,_1,,,VTf____3,:,Array,[,Float,,,0b10,],),{,},Var,$0cAzSE,:,Array,[,Boolean,,,0xB,],;,Val,$__8,,,$Q,,,K,:,Array,[,Array,[,String,,,6,],,,0B1011110,],;,},Class,m_M9,:,_,{,},<EOF>''',
                101
            )
        )

    def test_308(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Ay0_:_{Constructor (_g:z0){}Val $6x:Array [Array [Array [Array [Array [Array [Float ,0B1_11_1_000_0],3_5],3],021],021],3];Constructor (p:Float ){}_5hm(__vl38,_2_,_q:Float ;__O:_02){Break ;{Return ;Break ;} }}Class FpfQ:_{Val L_C:e;}Class _{}Class _:_{}''',
                '''Class,Ay0_,:,_,{,Constructor,(,_g,:,z0,),{,},Val,$6x,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B11110000,],,,35,],,,3,],,,021,],,,021,],,,3,],;,Constructor,(,p,:,Float,),{,},_5hm,(,__vl38,,,_2_,,,_q,:,Float,;,__O,:,_02,),{,Break,;,{,Return,;,Break,;,},},},Class,FpfQ,:,_,{,Val,L_C,:,e,;,},Class,_,{,},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_309(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:k{}Class d{Val $KnZ_34,_:Array [Array [String ,0b1_0],0x6];Val p_c_M4_,I:Array [String ,0X8A_F];}Class _Ns{$7e(_,b:Float ){} }Class _:X{Destructor (){} }''',
                '''Class,_,:,k,{,},Class,d,{,Val,$KnZ_34,,,_,:,Array,[,Array,[,String,,,0b10,],,,0x6,],;,Val,p_c_M4_,,,I,:,Array,[,String,,,0X8AF,],;,},Class,_Ns,{,$7e,(,_,,,b,:,Float,),{,},},Class,_,:,X,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_310(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val xm8_x0_:Array [Array [Array [Array [Array [Array [Array [Array [Float ,05_5_33],0x51],0X7A],0x9E],0B10],8],0x8],8];}''',
                '''Class,_,{,Val,xm8_x0_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,05533,],,,0x51,],,,0X7A,],,,0x9E,],,,0B10,],,,8,],,,0x8,],,,8,],;,},<EOF>''',
                101
            )
        )

    def test_311(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _y:W4V{}Class p:X{Constructor (){Continue ;} }Class _{}Class _88:_{kB(){Return ;Val N4,t,_:Float ;Val __,__0Fe_:Array [Boolean ,03];} }''',
                '''Class,_y,:,W4V,{,},Class,p,:,X,{,Constructor,(,),{,Continue,;,},},Class,_,{,},Class,_88,:,_,{,kB,(,),{,Return,;,Val,N4,,,t,,,_,:,Float,;,Val,__,,,__0Fe_,:,Array,[,Boolean,,,03,],;,},},<EOF>''',
                101
            )
        )

    def test_312(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n{_6(_,_,__3__:a;_:Array [Array [Array [Array [Array [Int ,0X22],77],0B1],0xD],42];_1:X9ww;X_Y:Boolean ;_3_9,__:Boolean ){} }''',
                '''Class,n,{,_6,(,_,,,_,,,__3__,:,a,;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0X22,],,,77,],,,0B1,],,,0xD,],,,42,],;,_1,:,X9ww,;,X_Y,:,Boolean,;,_3_9,,,__,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_313(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P{_(E:Array [String ,83];__f:Array [Array [Array [Array [String ,0107],0107],04_5_06],7];_0,_,J,U51,n,_,o7,_,YM,d,_:Array [Array [Array [Array [Array [Array [Float ,0x26],0b1_11],83],0b110],0X41],4]){Return ;} }''',
                '''Class,P,{,_,(,E,:,Array,[,String,,,83,],;,__f,:,Array,[,Array,[,Array,[,Array,[,String,,,0107,],,,0107,],,,04506,],,,7,],;,_0,,,_,,,J,,,U51,,,n,,,_,,,o7,,,_,,,YM,,,d,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x26,],,,0b111,],,,83,],,,0b110,],,,0X41,],,,4,],),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_314(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_L{Destructor (){} }Class h:q{$3_(_0FB7:_;_9t,_,_,_,Z:String ;_:Array [Float ,062];E,_:Array [Int ,0B11_1]){} }''',
                '''Class,_,:,_L,{,Destructor,(,),{,},},Class,h,:,q,{,$3_,(,_0FB7,:,_,;,_9t,,,_,,,_,,,_,,,Z,:,String,;,_,:,Array,[,Float,,,062,],;,E,,,_,:,Array,[,Int,,,0B111,],),{,},},<EOF>''',
                101
            )
        )

    def test_315(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:ATto6{Constructor (){}Val a_:r7;Constructor (_r,_7:_;_:A){}Val S3:Array [Array [String ,17],0b1_1_0_1001];Var $0l,_,$6lvW_7,_:_;}''',
                '''Class,_,:,ATto6,{,Constructor,(,),{,},Val,a_,:,r7,;,Constructor,(,_r,,,_7,:,_,;,_,:,A,),{,},Val,S3,:,Array,[,Array,[,String,,,17,],,,0b1101001,],;,Var,$0l,,,_,,,$6lvW_7,,,_,:,_,;,},<EOF>''',
                101
            )
        )

    def test_316(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _d{Var _4:V;$__3(d5a_,l0,U_2__,r,_,l_:Boolean ){}Destructor (){} }Class _x__{}Class Jq_1_X7{Constructor (){} }''',
                '''Class,_d,{,Var,_4,:,V,;,$__3,(,d5a_,,,l0,,,U_2__,,,r,,,_,,,l_,:,Boolean,),{,},Destructor,(,),{,},},Class,_x__,{,},Class,Jq_1_X7,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_317(self):
        self.assertTrue(
            TestLexer.test(
                '''Class W:_{Destructor (){Break ;} }Class g_9{_(b:Array [Array [Array [Float ,1_8],0636],97];YA8:__4;_,_,_,_8:B){} }Class _{}''',
                '''Class,W,:,_,{,Destructor,(,),{,Break,;,},},Class,g_9,{,_,(,b,:,Array,[,Array,[,Array,[,Float,,,18,],,,0636,],,,97,],;,YA8,:,__4,;,_,,,_,,,_,,,_8,:,B,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_318(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Val $4_M:Int ;Val _:Boolean ;Var _C5:Array [Array [Array [Array [Array [Boolean ,071],0XB_9],071],0X2],071];}''',
                '''Class,_,:,_,{,Val,$4_M,:,Int,;,Val,_,:,Boolean,;,Var,_C5,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,071,],,,0XB9,],,,071,],,,0X2,],,,071,],;,},<EOF>''',
                101
            )
        )

    def test_319(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_:_;_m_:Int ;_f:Array [Array [Float ,04],02]){}Destructor (){} }Class nf{}Class _:S{Constructor (){} }Class __2_{}''',
                '''Class,_,{,Constructor,(,_,:,_,;,_m_,:,Int,;,_f,:,Array,[,Array,[,Float,,,04,],,,02,],),{,},Destructor,(,),{,},},Class,nf,{,},Class,_,:,S,{,Constructor,(,),{,},},Class,__2_,{,},<EOF>''',
                101
            )
        )

    def test_320(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _4_{}Class _:p7g{}Class _z:n{Constructor (_,_:Array [Float ,72];_R:Array [Boolean ,070];n:Int ;dU,c6,__,u:Array [Boolean ,0B11]){} }''',
                '''Class,_4_,{,},Class,_,:,p7g,{,},Class,_z,:,n,{,Constructor,(,_,,,_,:,Array,[,Float,,,72,],;,_R,:,Array,[,Boolean,,,070,],;,n,:,Int,;,dU,,,c6,,,__,,,u,:,Array,[,Boolean,,,0B11,],),{,},},<EOF>''',
                101
            )
        )

    def test_321(self):
        self.assertTrue(
            TestLexer.test(
                '''Class dWH_a{}Class __{$_8(_,_,_,K:Boolean ;I:Array [Array [Array [Int ,020],0B1011100],0x55];_:Int ){} }Class __:MP{_(_,r:H_){} }''',
                '''Class,dWH_a,{,},Class,__,{,$_8,(,_,,,_,,,_,,,K,:,Boolean,;,I,:,Array,[,Array,[,Array,[,Int,,,020,],,,0B1011100,],,,0x55,],;,_,:,Int,),{,},},Class,__,:,MP,{,_,(,_,,,r,:,H_,),{,},},<EOF>''',
                101
            )
        )

    def test_322(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:__917{Constructor (_wN_,_,W3:Array [Float ,0b1100000];_,ES,__s,_:Array [Int ,5];s_6__,_E,_:_V;G7_,_9___,_6v,O,_,XE:Array [Array [Array [Int ,0x25],062],5]){} }''',
                '''Class,_,:,__917,{,Constructor,(,_wN_,,,_,,,W3,:,Array,[,Float,,,0b1100000,],;,_,,,ES,,,__s,,,_,:,Array,[,Int,,,5,],;,s_6__,,,_E,,,_,:,_V,;,G7_,,,_9___,,,_6v,,,O,,,_,,,XE,:,Array,[,Array,[,Array,[,Int,,,0x25,],,,062,],,,5,],),{,},},<EOF>''',
                101
            )
        )

    def test_323(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __69HF:P54{Val _,_1,$w:Array [Array [Array [String ,2],5],06];Destructor (){} }Class _{}Class _:_8X{}Class _{}''',
                '''Class,__69HF,:,P54,{,Val,_,,,_1,,,$w,:,Array,[,Array,[,Array,[,String,,,2,],,,5,],,,06,],;,Destructor,(,),{,},},Class,_,{,},Class,_,:,_8X,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_324(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var $_9_,CP6,rt__,_W,g961,$_,_,$__,$1,_,_:Boolean ;Destructor (){}Destructor (){}ov(I_,_V,_M917,m:Array [Int ,0X35]){}Val e,_,V_,__:Float ;IA(_,__H_,_,k_,_o:String ){} }''',
                '''Class,_,{,Var,$_9_,,,CP6,,,rt__,,,_W,,,g961,,,$_,,,_,,,$__,,,$1,,,_,,,_,:,Boolean,;,Destructor,(,),{,},Destructor,(,),{,},ov,(,I_,,,_V,,,_M917,,,m,:,Array,[,Int,,,0X35,],),{,},Val,e,,,_,,,V_,,,__,:,Float,;,IA,(,_,,,__H_,,,_,,,k_,,,_o,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_325(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:r{Constructor (_,N:Boolean ;g:Float ;M:Array [Array [Boolean ,02],65];A,e:Array [Array [Boolean ,0120],0B1000100]){} }''',
                '''Class,_,:,r,{,Constructor,(,_,,,N,:,Boolean,;,g,:,Float,;,M,:,Array,[,Array,[,Boolean,,,02,],,,65,],;,A,,,e,:,Array,[,Array,[,Boolean,,,0120,],,,0B1000100,],),{,},},<EOF>''',
                101
            )
        )

    def test_326(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _Uj{}Class N:_3R_5{}Class q5H{_9(_7,_:Array [Float ,0B101010];W,___:Array [Array [Int ,063],0b111110]){G::$a2_Z4_().__.w();}Destructor (){}Val r9:Array [Array [Array [Boolean ,0X2_6_5E],81],0X39];}''',
                '''Class,_Uj,{,},Class,N,:,_3R_5,{,},Class,q5H,{,_9,(,_7,,,_,:,Array,[,Float,,,0B101010,],;,W,,,___,:,Array,[,Array,[,Int,,,063,],,,0b111110,],),{,G,::,$a2_Z4_,(,),.,__,.,w,(,),;,},Destructor,(,),{,},Val,r9,:,Array,[,Array,[,Array,[,Boolean,,,0X265E,],,,81,],,,0X39,],;,},<EOF>''',
                101
            )
        )

    def test_327(self):
        self.assertTrue(
            TestLexer.test(
                '''Class W{Constructor (_,_:Array [Array [Boolean ,016_4],51]){Continue ;Var _,m,_,d:Array [Array [Array [Boolean ,51],035],51];Continue ;Continue ;} }Class U:_{}''',
                '''Class,W,{,Constructor,(,_,,,_,:,Array,[,Array,[,Boolean,,,0164,],,,51,],),{,Continue,;,Var,_,,,m,,,_,,,d,:,Array,[,Array,[,Array,[,Boolean,,,51,],,,035,],,,51,],;,Continue,;,Continue,;,},},Class,U,:,_,{,},<EOF>''',
                101
            )
        )

    def test_328(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _zIK2U:_{}Class _:_{_6_(N:Array [Int ,0B1];A730:Array [Array [Float ,8],056]){} }Class h:_{Val _,$9:Array [Boolean ,056];m_(___,_,_4_:_){} }''',
                '''Class,_zIK2U,:,_,{,},Class,_,:,_,{,_6_,(,N,:,Array,[,Int,,,0B1,],;,A730,:,Array,[,Array,[,Float,,,8,],,,056,],),{,},},Class,h,:,_,{,Val,_,,,$9,:,Array,[,Boolean,,,056,],;,m_,(,___,,,_,,,_4_,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_329(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Ux:Y{Destructor (){}Val ie__,$9,$_,__6,_2__Y,CG:d;Var n_:Array [Array [Array [Array [Boolean ,0x52],07],0B11111],0B1];$di0_(A:o5_;_:Float ){} }Class ___7:_{}Class _2k:Z{}''',
                '''Class,Ux,:,Y,{,Destructor,(,),{,},Val,ie__,,,$9,,,$_,,,__6,,,_2__Y,,,CG,:,d,;,Var,n_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x52,],,,07,],,,0B11111,],,,0B1,],;,$di0_,(,A,:,o5_,;,_,:,Float,),{,},},Class,___7,:,_,{,},Class,_2k,:,Z,{,},<EOF>''',
                101
            )
        )

    def test_330(self):
        self.assertTrue(
            TestLexer.test(
                '''Class z{Destructor (){} }Class _:_{Destructor (){Break ;Return ;} }Class _5ma:w8{_(){}Val e__:__46_1;}Class b:_{}''',
                '''Class,z,{,Destructor,(,),{,},},Class,_,:,_,{,Destructor,(,),{,Break,;,Return,;,},},Class,_5ma,:,w8,{,_,(,),{,},Val,e__,:,__46_1,;,},Class,b,:,_,{,},<EOF>''',
                101
            )
        )

    def test_331(self):
        self.assertTrue(
            TestLexer.test(
                '''Class I__{Var $t,$7,b,$u:Array [Int ,0X41];}Class _{Destructor (){}Val n:Array [Boolean ,027];Destructor (){} }Class V:_{Destructor (){} }Class _5:mM{}''',
                '''Class,I__,{,Var,$t,,,$7,,,b,,,$u,:,Array,[,Int,,,0X41,],;,},Class,_,{,Destructor,(,),{,},Val,n,:,Array,[,Boolean,,,027,],;,Destructor,(,),{,},},Class,V,:,_,{,Destructor,(,),{,},},Class,_5,:,mM,{,},<EOF>''',
                101
            )
        )

    def test_332(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var _2_N,$_,M0,$2_4:Array [Array [Array [Array [Array [Array [Array [Float ,0b1000],7],037],0b1000],0x61],0b1000],91];}Class i:J{}Class __e7y{}Class _1__1_:_N{}''',
                '''Class,_,{,Var,_2_N,,,$_,,,M0,,,$2_4,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1000,],,,7,],,,037,],,,0b1000,],,,0x61,],,,0b1000,],,,91,],;,},Class,i,:,J,{,},Class,__e7y,{,},Class,_1__1_,:,_N,{,},<EOF>''',
                101
            )
        )

    def test_333(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q6:_TuWc61{}Class _:_{Constructor (t__,_,T,_vW,c_:R){}Destructor (){Var H,g,__:N_d4__QIy9U_;} }Class a:Z5{}''',
                '''Class,q6,:,_TuWc61,{,},Class,_,:,_,{,Constructor,(,t__,,,_,,,T,,,_vW,,,c_,:,R,),{,},Destructor,(,),{,Var,H,,,g,,,__,:,N_d4__QIy9U_,;,},},Class,a,:,Z5,{,},<EOF>''',
                101
            )
        )

    def test_334(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V{Var V4813,__:Array [String ,5];Constructor (_:F;d:String ;k_,W_,_,___:Boolean ;_:Boolean ;_1S:Float ;y33,E6,U,_:t_){} }''',
                '''Class,V,{,Var,V4813,,,__,:,Array,[,String,,,5,],;,Constructor,(,_,:,F,;,d,:,String,;,k_,,,W_,,,_,,,___,:,Boolean,;,_,:,Boolean,;,_1S,:,Float,;,y33,,,E6,,,U,,,_,:,t_,),{,},},<EOF>''',
                101
            )
        )

    def test_335(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w6{Constructor (_,__,i57_,_08:_6__;_,f__:Array [Array [Array [Array [Float ,50],0x69],0x1],0X5]){}Val __:_;}''',
                '''Class,w6,{,Constructor,(,_,,,__,,,i57_,,,_08,:,_6__,;,_,,,f__,:,Array,[,Array,[,Array,[,Array,[,Float,,,50,],,,0x69,],,,0x1,],,,0X5,],),{,},Val,__,:,_,;,},<EOF>''',
                101
            )
        )

    def test_336(self):
        self.assertTrue(
            TestLexer.test(
                '''Class I_M_:c__7_e0{Constructor (oEe723,IG__:r;Yz,k,_Q:Array [String ,3];v1,J__,__,j__4:Boolean ;B__h,s_qmT:Array [String ,0142]){} }Class M_c__:_{}''',
                '''Class,I_M_,:,c__7_e0,{,Constructor,(,oEe723,,,IG__,:,r,;,Yz,,,k,,,_Q,:,Array,[,String,,,3,],;,v1,,,J__,,,__,,,j__4,:,Boolean,;,B__h,,,s_qmT,:,Array,[,String,,,0142,],),{,},},Class,M_c__,:,_,{,},<EOF>''',
                101
            )
        )

    def test_337(self):
        self.assertTrue(
            TestLexer.test(
                '''Class f_:_{r_7(){}$8(){} }Class _:s_J{}Class pB{$__Ai(_R__W_o_:Array [Float ,0B1011];__x:Array [Boolean ,0X5]){} }''',
                '''Class,f_,:,_,{,r_7,(,),{,},$8,(,),{,},},Class,_,:,s_J,{,},Class,pB,{,$__Ai,(,_R__W_o_,:,Array,[,Float,,,0B1011,],;,__x,:,Array,[,Boolean,,,0X5,],),{,},},<EOF>''',
                101
            )
        )

    def test_338(self):
        self.assertTrue(
            TestLexer.test(
                '''Class H{Constructor (){Break ;}Var _,O,_545_,$UE:Array [String ,4];}Class _B_{}Class _T_{_227_m(){}Var $2:_;}Class Z:_1_{__t_(){Return ;} }''',
                '''Class,H,{,Constructor,(,),{,Break,;,},Var,_,,,O,,,_545_,,,$UE,:,Array,[,String,,,4,],;,},Class,_B_,{,},Class,_T_,{,_227_m,(,),{,},Var,$2,:,_,;,},Class,Z,:,_1_,{,__t_,(,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_339(self):
        self.assertTrue(
            TestLexer.test(
                '''Class U:l{}Class x{Destructor (){} }Class _{Constructor (J_:Float ;_,_:Array [Array [Boolean ,016],0x8_6];j2_A:Int ;w_:Int ;_:_;_,_:_){} }''',
                '''Class,U,:,l,{,},Class,x,{,Destructor,(,),{,},},Class,_,{,Constructor,(,J_,:,Float,;,_,,,_,:,Array,[,Array,[,Boolean,,,016,],,,0x86,],;,j2_A,:,Int,;,w_,:,Int,;,_,:,_,;,_,,,_,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_340(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b{}Class F{}Class x:_{Destructor (){}Val g,$n:Boolean ;$_K(q4_:Boolean ;_Y_:String ;S:Array [Array [Int ,0X4E_F4F],0B111010]){Val _:_;}Constructor (){} }''',
                '''Class,b,{,},Class,F,{,},Class,x,:,_,{,Destructor,(,),{,},Val,g,,,$n,:,Boolean,;,$_K,(,q4_,:,Boolean,;,_Y_,:,String,;,S,:,Array,[,Array,[,Int,,,0X4EF4F,],,,0B111010,],),{,Val,_,:,_,;,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_341(self):
        self.assertTrue(
            TestLexer.test(
                '''Class N{}Class _o{Var $_,$2:Int ;_(){}__(__Y,_,_,s5_c:Array [Array [Array [Float ,0XA],0B110011],8]){}Var _K:Array [Array [Array [Array [Int ,0B110011],0X7F_2],0B1],0B110011];Destructor (){Return ;}_(S8:Array [Array [Array [Int ,0B1],8],063_004_67_0];T_:y){Break ;} }Class _{}Class e{Destructor (){}Val $1,$K_,$Z:String ;}Class _:_4{Var $29,B,$_,$_9:Array [Float ,075];}''',
                '''Class,N,{,},Class,_o,{,Var,$_,,,$2,:,Int,;,_,(,),{,},__,(,__Y,,,_,,,_,,,s5_c,:,Array,[,Array,[,Array,[,Float,,,0XA,],,,0B110011,],,,8,],),{,},Var,_K,:,Array,[,Array,[,Array,[,Array,[,Int,,,0B110011,],,,0X7F2,],,,0B1,],,,0B110011,],;,Destructor,(,),{,Return,;,},_,(,S8,:,Array,[,Array,[,Array,[,Int,,,0B1,],,,8,],,,063004670,],;,T_,:,y,),{,Break,;,},},Class,_,{,},Class,e,{,Destructor,(,),{,},Val,$1,,,$K_,,,$Z,:,String,;,},Class,_,:,_4,{,Var,$29,,,B,,,$_,,,$_9,:,Array,[,Float,,,075,],;,},<EOF>''',
                101
            )
        )

    def test_342(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class _:JD{Destructor (){} }Class ___1:_370{}Class _{_Yq4(_,__,_,___WF:Array [String ,0B101101];d_:Array [Float ,0b1];d_6__,_,_,H:Float ;v4,___47:Array [Int ,0B101101];M,N,_:P_){}Var $0:String ;Val $_1_B,M,$Jl__:Array [Float ,0101];}Class u:h{}Class A{}''',
                '''Class,_,:,_,{,},Class,_,:,JD,{,Destructor,(,),{,},},Class,___1,:,_370,{,},Class,_,{,_Yq4,(,_,,,__,,,_,,,___WF,:,Array,[,String,,,0B101101,],;,d_,:,Array,[,Float,,,0b1,],;,d_6__,,,_,,,_,,,H,:,Float,;,v4,,,___47,:,Array,[,Int,,,0B101101,],;,M,,,N,,,_,:,P_,),{,},Var,$0,:,String,;,Val,$_1_B,,,M,,,$Jl__,:,Array,[,Float,,,0101,],;,},Class,u,:,h,{,},Class,A,{,},<EOF>''',
                101
            )
        )

    def test_343(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _z{Constructor (_:Float ;E:String ;_,_:Array [Array [Boolean ,1],0B1];_:Array [Array [Int ,12],0b1_00];_,_J,p,h:String ;x,D,_r:Boolean ;O,__,_1:Array [Array [Array [Boolean ,0335],0xB],70];i,p_7,i1,h6z:t3;_d_43:__){}Var _69:Array [Boolean ,2];__(){Break ;} }Class _{}Class e:_{}Class __3{}''',
                '''Class,_z,{,Constructor,(,_,:,Float,;,E,:,String,;,_,,,_,:,Array,[,Array,[,Boolean,,,1,],,,0B1,],;,_,:,Array,[,Array,[,Int,,,12,],,,0b100,],;,_,,,_J,,,p,,,h,:,String,;,x,,,D,,,_r,:,Boolean,;,O,,,__,,,_1,:,Array,[,Array,[,Array,[,Boolean,,,0335,],,,0xB,],,,70,],;,i,,,p_7,,,i1,,,h6z,:,t3,;,_d_43,:,__,),{,},Var,_69,:,Array,[,Boolean,,,2,],;,__,(,),{,Break,;,},},Class,_,{,},Class,e,:,_,{,},Class,__3,{,},<EOF>''',
                101
            )
        )

    def test_344(self):
        self.assertTrue(
            TestLexer.test(
                '''Class p{}Class V___h{}Class _{Var $3u0,$_n,$L6__5,$81,s_,$7_1_I,s:Array [Int ,0B1];}Class _:_j{}Class _l:P{O(X:E4){} }''',
                '''Class,p,{,},Class,V___h,{,},Class,_,{,Var,$3u0,,,$_n,,,$L6__5,,,$81,,,s_,,,$7_1_I,,,s,:,Array,[,Int,,,0B1,],;,},Class,_,:,_j,{,},Class,_l,:,P,{,O,(,X,:,E4,),{,},},<EOF>''',
                101
            )
        )

    def test_345(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Constructor (){Return ;Break ;}Val $4QM,_y:Array [Array [Array [Boolean ,64],0X3A],0xF5];Destructor (){}Destructor (){Continue ;} }''',
                '''Class,_,:,_,{,Constructor,(,),{,Return,;,Break,;,},Val,$4QM,,,_y,:,Array,[,Array,[,Array,[,Boolean,,,64,],,,0X3A,],,,0xF5,],;,Destructor,(,),{,},Destructor,(,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_346(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9d:D4__{_Sn6(__n,_1_:Int ){Return ;}Constructor (i_26:Array [Array [Array [Array [Array [Array [String ,85],0X69],075],0B111],0x11],0X45]){} }''',
                '''Class,_9d,:,D4__,{,_Sn6,(,__n,,,_1_,:,Int,),{,Return,;,},Constructor,(,i_26,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,85,],,,0X69,],,,075,],,,0B111,],,,0x11,],,,0X45,],),{,},},<EOF>''',
                101
            )
        )

    def test_347(self):
        self.assertTrue(
            TestLexer.test(
                '''Class L{Val $_,$5__,$V,__K:Array [Int ,0b10000];B_(_K:Array [Boolean ,0x47];_t_:Int ;_,h:Array [Float ,77];t_31_p,t:Array [Array [Array [Array [Boolean ,04_7],9],0xE],0X6_19];k,bi16,r,r2:Array [Array [Array [String ,0b1],0b10000],0x4_C]){} }''',
                '''Class,L,{,Val,$_,,,$5__,,,$V,,,__K,:,Array,[,Int,,,0b10000,],;,B_,(,_K,:,Array,[,Boolean,,,0x47,],;,_t_,:,Int,;,_,,,h,:,Array,[,Float,,,77,],;,t_31_p,,,t,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,047,],,,9,],,,0xE,],,,0X619,],;,k,,,bi16,,,r,,,r2,:,Array,[,Array,[,Array,[,String,,,0b1,],,,0b10000,],,,0x4C,],),{,},},<EOF>''',
                101
            )
        )

    def test_348(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:W4{Val __5,___bRf_0:Int ;Var D_,_W_,$0kB,$k_5:Array [Array [Int ,0121],5];Constructor (U:_5X__){Return ;}Destructor (){Var _:_;} }''',
                '''Class,_,:,W4,{,Val,__5,,,___bRf_0,:,Int,;,Var,D_,,,_W_,,,$0kB,,,$k_5,:,Array,[,Array,[,Int,,,0121,],,,5,],;,Constructor,(,U,:,_5X__,),{,Return,;,},Destructor,(,),{,Var,_,:,_,;,},},<EOF>''',
                101
            )
        )

    def test_349(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o{Constructor (y,_:__M;__t3:Array [Array [Array [Array [Boolean ,772],02_4_75456],03],03];_,___:Array [Array [Array [Array [Boolean ,0b1100011],027],063],0B1]){} }''',
                '''Class,o,{,Constructor,(,y,,,_,:,__M,;,__t3,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,772,],,,02475456,],,,03,],,,03,],;,_,,,___,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1100011,],,,027,],,,063,],,,0B1,],),{,},},<EOF>''',
                101
            )
        )

    def test_350(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:F{_(_:V_;d:__){}Constructor (_:Array [Array [Array [Array [Array [Array [String ,59],59],0b10000],051],1],59];_Z:Array [Int ,0B11110]){} }''',
                '''Class,_,:,F,{,_,(,_,:,V_,;,d,:,__,),{,},Constructor,(,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,59,],,,59,],,,0b10000,],,,051,],,,1,],,,59,],;,_Z,:,Array,[,Int,,,0B11110,],),{,},},<EOF>''',
                101
            )
        )

    def test_351(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class _Ve:_0_4_{}Class U:h{_(o8,d8D1__4:Array [Array [Array [Boolean ,04663],0B110001],73]){Var _,tWK6:L5_;} }Class ___5:_{$oFB(c:Float ){} }''',
                '''Class,_,:,_,{,},Class,_Ve,:,_0_4_,{,},Class,U,:,h,{,_,(,o8,,,d8D1__4,:,Array,[,Array,[,Array,[,Boolean,,,04663,],,,0B110001,],,,73,],),{,Var,_,,,tWK6,:,L5_,;,},},Class,___5,:,_,{,$oFB,(,c,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_352(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (a7,_R:Array [Array [Boolean ,9],0B1011110];_,_3,_Yz:Array [Array [String ,3_19],0x29_43_7];_,GO:Int ;M6:mw__){Return ;Continue ;} }Class LH:i_{}''',
                '''Class,_,{,Constructor,(,a7,,,_R,:,Array,[,Array,[,Boolean,,,9,],,,0B1011110,],;,_,,,_3,,,_Yz,:,Array,[,Array,[,String,,,319,],,,0x29437,],;,_,,,GO,:,Int,;,M6,:,mw__,),{,Return,;,Continue,;,},},Class,LH,:,i_,{,},<EOF>''',
                101
            )
        )

    def test_353(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q7{Val _5_,$__,$1:__2;Val $m,T1,$8:Array [Array [String ,07],0x2F];Var $9p1S3:Boolean ;Var $_:Int ;Var V,m,$__9L:Array [Array [Float ,0X52],0X52];}''',
                '''Class,q7,{,Val,_5_,,,$__,,,$1,:,__2,;,Val,$m,,,T1,,,$8,:,Array,[,Array,[,String,,,07,],,,0x2F,],;,Var,$9p1S3,:,Boolean,;,Var,$_,:,Int,;,Var,V,,,m,,,$__9L,:,Array,[,Array,[,Float,,,0X52,],,,0X52,],;,},<EOF>''',
                101
            )
        )

    def test_354(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{G_(){} }Class B{}Class A0:_{$2(P_2C7,H_P78,_,_,_,X_1,__,_:Array [String ,03];w,f:_b__d){}Var n0:Float ;}''',
                '''Class,_,{,G_,(,),{,},},Class,B,{,},Class,A0,:,_,{,$2,(,P_2C7,,,H_P78,,,_,,,_,,,_,,,X_1,,,__,,,_,:,Array,[,String,,,03,],;,w,,,f,:,_b__d,),{,},Var,n0,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_355(self):
        self.assertTrue(
            TestLexer.test(
                '''Class xY:_E{Var $Y_,$P_:Array [String ,0b1_10_1_1_0_1_0_1];}Class T{Val $_Q:Array [Float ,1_9];Var _,$0,$X,$W,_:Array [Array [String ,0X3_C],066];}''',
                '''Class,xY,:,_E,{,Var,$Y_,,,$P_,:,Array,[,String,,,0b110110101,],;,},Class,T,{,Val,$_Q,:,Array,[,Float,,,19,],;,Var,_,,,$0,,,$X,,,$W,,,_,:,Array,[,Array,[,String,,,0X3C,],,,066,],;,},<EOF>''',
                101
            )
        )

    def test_356(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t:_{}Class L9_:Q_j{Val G,$_,$9,w,$c0,v_754,_,_,_,$6__mB_:Array [Array [String ,0b1_1_00],0x27];}Class lY_{Destructor (){} }Class _c{}Class _{}Class iKy:__{}Class e:_{}Class Z:mr_o{Val $7_j,Q__c:M_t;}''',
                '''Class,t,:,_,{,},Class,L9_,:,Q_j,{,Val,G,,,$_,,,$9,,,w,,,$c0,,,v_754,,,_,,,_,,,_,,,$6__mB_,:,Array,[,Array,[,String,,,0b1100,],,,0x27,],;,},Class,lY_,{,Destructor,(,),{,},},Class,_c,{,},Class,_,{,},Class,iKy,:,__,{,},Class,e,:,_,{,},Class,Z,:,mr_o,{,Val,$7_j,,,Q__c,:,M_t,;,},<EOF>''',
                101
            )
        )

    def test_357(self):
        self.assertTrue(
            TestLexer.test(
                '''Class lV:H{Val $_,$4__Q_,B,_L___z,zc:Boolean ;Var $2_9_5,V,_42,_Q3,E:Array [Array [Array [Int ,0xC19_9],0x52],0B101101];}Class _p0__:l{}''',
                '''Class,lV,:,H,{,Val,$_,,,$4__Q_,,,B,,,_L___z,,,zc,:,Boolean,;,Var,$2_9_5,,,V,,,_42,,,_Q3,,,E,:,Array,[,Array,[,Array,[,Int,,,0xC199,],,,0x52,],,,0B101101,],;,},Class,_p0__,:,l,{,},<EOF>''',
                101
            )
        )

    def test_358(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class h_3:VV{}Class W:N{}Class Q_d:Z1{}Class _{Val $r,z:Array [Int ,0x22];Val D:Array [Float ,0X6];}Class X{Constructor (_i:Int ;_,O,_:_;D,f,L,_,s40_1,nk,__,_:Int ;rH2,aI:Array [Array [Array [Float ,0B1100011],0B1],85]){Break ;Continue ;} }''',
                '''Class,_,:,_,{,},Class,h_3,:,VV,{,},Class,W,:,N,{,},Class,Q_d,:,Z1,{,},Class,_,{,Val,$r,,,z,:,Array,[,Int,,,0x22,],;,Val,D,:,Array,[,Float,,,0X6,],;,},Class,X,{,Constructor,(,_i,:,Int,;,_,,,O,,,_,:,_,;,D,,,f,,,L,,,_,,,s40_1,,,nk,,,__,,,_,:,Int,;,rH2,,,aI,:,Array,[,Array,[,Array,[,Float,,,0B1100011,],,,0B1,],,,85,],),{,Break,;,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_359(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Destructor (){}Val _,$2F,$n,_,$0BB__c:Array [Array [String ,0X9],030];}Class _{Destructor (){} }Class x{}''',
                '''Class,_,{,Destructor,(,),{,},Val,_,,,$2F,,,$n,,,_,,,$0BB__c,:,Array,[,Array,[,String,,,0X9,],,,030,],;,},Class,_,{,Destructor,(,),{,},},Class,x,{,},<EOF>''',
                101
            )
        )

    def test_360(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ZD8:B_{_(__75o,_SB0:Array [Boolean ,0B100101]){}Var $6Ob,$__:j;}Class _f1{}Class _:C{Destructor (){}Var $_:_;}Class _54_T1_{}Class _:_{}''',
                '''Class,ZD8,:,B_,{,_,(,__75o,,,_SB0,:,Array,[,Boolean,,,0B100101,],),{,},Var,$6Ob,,,$__,:,j,;,},Class,_f1,{,},Class,_,:,C,{,Destructor,(,),{,},Var,$_,:,_,;,},Class,_54_T1_,{,},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_361(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class _:___{Var $_:Array [Array [Array [Int ,0x45],6],0B1011001];}Class X{Var $1___,_,$2fc:Boolean ;Val __,$_:Float ;$_(_,_,_,g1:Boolean ;_:Float ){}$9LuO(){} }Class L:z{Var E:Float ;Val $8:Boolean ;}''',
                '''Class,_,:,_,{,},Class,_,:,___,{,Var,$_,:,Array,[,Array,[,Array,[,Int,,,0x45,],,,6,],,,0B1011001,],;,},Class,X,{,Var,$1___,,,_,,,$2fc,:,Boolean,;,Val,__,,,$_,:,Float,;,$_,(,_,,,_,,,_,,,g1,:,Boolean,;,_,:,Float,),{,},$9LuO,(,),{,},},Class,L,:,z,{,Var,E,:,Float,;,Val,$8,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_362(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _L{}Class _2J_{Constructor (_:String ;_,_4:Array [Float ,0b1]){Var d,sk4:__;}Constructor (__,_,_N:_;_,_16:Array [Array [Float ,02],0x6];__O0xf:Array [Array [Array [String ,06],1],6_8];_:d;nB__:i_l;_,_:_){} }Class _{}''',
                '''Class,_L,{,},Class,_2J_,{,Constructor,(,_,:,String,;,_,,,_4,:,Array,[,Float,,,0b1,],),{,Var,d,,,sk4,:,__,;,},Constructor,(,__,,,_,,,_N,:,_,;,_,,,_16,:,Array,[,Array,[,Float,,,02,],,,0x6,],;,__O0xf,:,Array,[,Array,[,Array,[,String,,,06,],,,1,],,,68,],;,_,:,d,;,nB__,:,i_l,;,_,,,_,:,_,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_363(self):
        self.assertTrue(
            TestLexer.test(
                '''Class v{Constructor (){H_::$5.B();}Val k,$___AP:l;Var E_:z5;Val __d__,_:Array [Array [Array [Array [Int ,1],023],0x4D],0XF];}''',
                '''Class,v,{,Constructor,(,),{,H_,::,$5,.,B,(,),;,},Val,k,,,$___AP,:,l,;,Var,E_,:,z5,;,Val,__d__,,,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,1,],,,023,],,,0x4D,],,,0XF,],;,},<EOF>''',
                101
            )
        )

    def test_364(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:U_{$6O(_:Array [Float ,05];_,__:Array [Array [Int ,0b1_0_0_0_1],39];n:__5){}Destructor (){ {} }}Class _:_{}''',
                '''Class,_,:,U_,{,$6O,(,_,:,Array,[,Float,,,05,],;,_,,,__,:,Array,[,Array,[,Int,,,0b10001,],,,39,],;,n,:,__5,),{,},Destructor,(,),{,{,},},},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_365(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class ___:_{}Class gLf4__6:w_{}Class _f{Val V_9_6:Array [Array [Int ,3204_56],0b1_0_1_01];i(_v,z:Array [String ,0XF];J7:_;_wM2,O:_9q;__:Int ;__24ijO,_s,_I__:S;Xu_,_,_,__h:Boolean ){}Destructor (){} }''',
                '''Class,_,{,},Class,___,:,_,{,},Class,gLf4__6,:,w_,{,},Class,_f,{,Val,V_9_6,:,Array,[,Array,[,Int,,,320456,],,,0b10101,],;,i,(,_v,,,z,:,Array,[,String,,,0XF,],;,J7,:,_,;,_wM2,,,O,:,_9q,;,__,:,Int,;,__24ijO,,,_s,,,_I__,:,S,;,Xu_,,,_,,,_,,,__h,:,Boolean,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_366(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _iT5:x1{Var $H:Int ;}Class n9s_{}Class __:T{Constructor (B12:Float ){}Val w,_:Array [Array [Array [Array [Array [String ,45],0b11_1],044],0X9_58],044];}Class _0{}''',
                '''Class,_iT5,:,x1,{,Var,$H,:,Int,;,},Class,n9s_,{,},Class,__,:,T,{,Constructor,(,B12,:,Float,),{,},Val,w,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,45,],,,0b111,],,,044,],,,0X958,],,,044,],;,},Class,_0,{,},<EOF>''',
                101
            )
        )

    def test_367(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Val $d4,n,$8K,$8,_,_:Array [Array [Array [Array [Float ,4],0B1001011],8_95_2],89];}Class ik:_{$1(I:Array [Float ,89];P,E:D;rr_:Array [Array [Float ,0x48],0102];D_4,a____:Int ;D:Array [Array [Float ,0B101],89]){} }''',
                '''Class,_,:,_,{,Val,$d4,,,n,,,$8K,,,$8,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,4,],,,0B1001011,],,,8952,],,,89,],;,},Class,ik,:,_,{,$1,(,I,:,Array,[,Float,,,89,],;,P,,,E,:,D,;,rr_,:,Array,[,Array,[,Float,,,0x48,],,,0102,],;,D_4,,,a____,:,Int,;,D,:,Array,[,Array,[,Float,,,0B101,],,,89,],),{,},},<EOF>''',
                101
            )
        )

    def test_368(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _40X{}Class _:_61{Constructor (_,s_,OD:W2;_z:_9;Rq,__x2:Array [Array [String ,01],0133];Ug_27_i76:R;__,i,_xYP9:String ){}Val $g_,_:_;}Class __Ux{}Class O4G:_O{}Class _{}Class i{}''',
                '''Class,_40X,{,},Class,_,:,_61,{,Constructor,(,_,,,s_,,,OD,:,W2,;,_z,:,_9,;,Rq,,,__x2,:,Array,[,Array,[,String,,,01,],,,0133,],;,Ug_27_i76,:,R,;,__,,,i,,,_xYP9,:,String,),{,},Val,$g_,,,_,:,_,;,},Class,__Ux,{,},Class,O4G,:,_O,{,},Class,_,{,},Class,i,{,},<EOF>''',
                101
            )
        )

    def test_369(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_31O_:Array [Boolean ,8]){} }Class C__u_3:_{Val $_:Float ;Val _:Array [Array [Float ,07],0x7];}Class __:_u_2QH{}''',
                '''Class,_,{,Constructor,(,_31O_,:,Array,[,Boolean,,,8,],),{,},},Class,C__u_3,:,_,{,Val,$_,:,Float,;,Val,_,:,Array,[,Array,[,Float,,,07,],,,0x7,],;,},Class,__,:,_u_2QH,{,},<EOF>''',
                101
            )
        )

    def test_370(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class n:_{Destructor (){} }Class _:_{Var $yF_2,$7_:Fs;Val $_,_e_8:Array [Int ,0X1B];Destructor (){Break ;} }''',
                '''Class,_,{,},Class,n,:,_,{,Destructor,(,),{,},},Class,_,:,_,{,Var,$yF_2,,,$7_,:,Fs,;,Val,$_,,,_e_8,:,Array,[,Int,,,0X1B,],;,Destructor,(,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_371(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P:m{Var _,$1_:_;}Class a:Fl7B_4G{Var $M,H__U:Array [Array [String ,0XD3],0B1000110];}Class quV:D{Var $M9,$f_do:Int ;$1__(UO9_,F:_;__:Array [Array [Float ,04_74],04_7];tM__92,A__:_9;K:Int ){Break ;Continue ;} }''',
                '''Class,P,:,m,{,Var,_,,,$1_,:,_,;,},Class,a,:,Fl7B_4G,{,Var,$M,,,H__U,:,Array,[,Array,[,String,,,0XD3,],,,0B1000110,],;,},Class,quV,:,D,{,Var,$M9,,,$f_do,:,Int,;,$1__,(,UO9_,,,F,:,_,;,__,:,Array,[,Array,[,Float,,,0474,],,,047,],;,tM__92,,,A__,:,_9,;,K,:,Int,),{,Break,;,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_372(self):
        self.assertTrue(
            TestLexer.test(
                '''Class f{Destructor (){} }Class _N:Hy2{Var $f_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,0B10001],0b11100],030],03],030],5],0x6],030],030],88],8_6],0X8D];}''',
                '''Class,f,{,Destructor,(,),{,},},Class,_N,:,Hy2,{,Var,$f_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B10001,],,,0b11100,],,,030,],,,03,],,,030,],,,5,],,,0x6,],,,030,],,,030,],,,88,],,,86,],,,0X8D,],;,},<EOF>''',
                101
            )
        )

    def test_373(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _S{}Class V:___B{Constructor (){}Constructor (){} }Class f:g{Val $_,k5n7,A,___,$_K:Array [Array [Int ,0b1],0x5D];}Class ______:WG{Destructor (){} }''',
                '''Class,_S,{,},Class,V,:,___B,{,Constructor,(,),{,},Constructor,(,),{,},},Class,f,:,g,{,Val,$_,,,k5n7,,,A,,,___,,,$_K,:,Array,[,Array,[,Int,,,0b1,],,,0x5D,],;,},Class,______,:,WG,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_374(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g__{}Class y__{n(z,wi2_,r,_,b1_,_7_,_u:_OJ_p05;__,y8__9P:Array [Float ,65];_:Array [String ,0136_50_1_07]){Break ;} }Class _:_{}''',
                '''Class,g__,{,},Class,y__,{,n,(,z,,,wi2_,,,r,,,_,,,b1_,,,_7_,,,_u,:,_OJ_p05,;,__,,,y8__9P,:,Array,[,Float,,,65,],;,_,:,Array,[,String,,,013650107,],),{,Break,;,},},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_375(self):
        self.assertTrue(
            TestLexer.test(
                '''Class D_{Constructor (r_11p,IX:Float ;T_z,w,___,_Vj5,e:Array [Array [Array [Int ,0B1100000],0X4E],057];e3,_,__:String ){Break ;}hJf(){Continue ;Break ;} }Class _l:J{}''',
                '''Class,D_,{,Constructor,(,r_11p,,,IX,:,Float,;,T_z,,,w,,,___,,,_Vj5,,,e,:,Array,[,Array,[,Array,[,Int,,,0B1100000,],,,0X4E,],,,057,],;,e3,,,_,,,__,:,String,),{,Break,;,},hJf,(,),{,Continue,;,Break,;,},},Class,_l,:,J,{,},<EOF>''',
                101
            )
        )

    def test_376(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___x9:rv{Val $1:Array [Array [Array [Array [Array [Array [String ,0134],0B1],065],0X47],0xF_9],0b10101];$T(_:Float ){} }''',
                '''Class,___x9,:,rv,{,Val,$1,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0134,],,,0B1,],,,065,],,,0X47,],,,0xF9,],,,0b10101,],;,$T,(,_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_377(self):
        self.assertTrue(
            TestLexer.test(
                '''Class S8{}Class _:_683k{}Class z:__{}Class _O4_S_swpz:_4{Val _,zP,UO:Array [Int ,03];Val $d:Float ;_(k_R1,N,_,_:_;J,_____29_:Int ;_o,_,_:Float ){} }''',
                '''Class,S8,{,},Class,_,:,_683k,{,},Class,z,:,__,{,},Class,_O4_S_swpz,:,_4,{,Val,_,,,zP,,,UO,:,Array,[,Int,,,03,],;,Val,$d,:,Float,;,_,(,k_R1,,,N,,,_,,,_,:,_,;,J,,,_____29_,:,Int,;,_o,,,_,,,_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_378(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:__{Val s,$5:Array [Array [Array [Array [Array [Array [Array [Int ,0X5D],056],0B11_0_0_11],0b1],3],06_6_0],33];}Class _J8w88w:_3{}''',
                '''Class,_,:,__,{,Val,s,,,$5,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0X5D,],,,056,],,,0B110011,],,,0b1,],,,3,],,,0660,],,,33,],;,},Class,_J8w88w,:,_3,{,},<EOF>''',
                101
            )
        )

    def test_379(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P2:k{Val J:_;$5fR_(D5:String ;h:Array [Array [Boolean ,0b111100],0xF];_5_Z,_,_1:y;_1:_;_Y_,_,_b:s){}$4(){} }''',
                '''Class,P2,:,k,{,Val,J,:,_,;,$5fR_,(,D5,:,String,;,h,:,Array,[,Array,[,Boolean,,,0b111100,],,,0xF,],;,_5_Z,,,_,,,_1,:,y,;,_1,:,_,;,_Y_,,,_,,,_b,:,s,),{,},$4,(,),{,},},<EOF>''',
                101
            )
        )

    def test_380(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_4_{Constructor (){Return ;_::$_();}Destructor (){} }Class Af__:C{Destructor (){}Destructor (){ {Continue ;} }}''',
                '''Class,_,:,_4_,{,Constructor,(,),{,Return,;,_,::,$_,(,),;,},Destructor,(,),{,},},Class,Af__,:,C,{,Destructor,(,),{,},Destructor,(,),{,{,Continue,;,},},},<EOF>''',
                101
            )
        )

    def test_381(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w_{Var Q0,N,Q,_,qQ:Boolean ;}Class c:B{}Class Z_qHp_{Var $_:Array [Array [Array [String ,0x8_E],060],0740176662];}''',
                '''Class,w_,{,Var,Q0,,,N,,,Q,,,_,,,qQ,:,Boolean,;,},Class,c,:,B,{,},Class,Z_qHp_,{,Var,$_,:,Array,[,Array,[,Array,[,String,,,0x8E,],,,060,],,,0740176662,],;,},<EOF>''',
                101
            )
        )

    def test_382(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{_(_C_,X:Array [Array [String ,8],065];_,_,P:_;K5:Float ;_5,z:Array [Array [Array [Array [Array [Boolean ,0b1100],0b1100],0X1F_4],0b1_1],0B1010010];C:f){Var w10_o3:Int ;Return ;} }''',
                '''Class,_,{,_,(,_C_,,,X,:,Array,[,Array,[,String,,,8,],,,065,],;,_,,,_,,,P,:,_,;,K5,:,Float,;,_5,,,z,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1100,],,,0b1100,],,,0X1F4,],,,0b11,],,,0B1010010,],;,C,:,f,),{,Var,w10_o3,:,Int,;,Return,;,},},<EOF>''',
                101
            )
        )

    def test_383(self):
        self.assertTrue(
            TestLexer.test(
                '''Class D{}Class B6:_X{Destructor (){}Var M8:Array [Int ,5];Var $__:Array [Array [Array [Array [Float ,15],02],15],3_7_3_4];Var X9L_7Q,$_:_8;}Class _9_{}Class __:_y{}''',
                '''Class,D,{,},Class,B6,:,_X,{,Destructor,(,),{,},Var,M8,:,Array,[,Int,,,5,],;,Var,$__,:,Array,[,Array,[,Array,[,Array,[,Float,,,15,],,,02,],,,15,],,,3734,],;,Var,X9L_7Q,,,$_,:,_8,;,},Class,_9_,{,},Class,__,:,_y,{,},<EOF>''',
                101
            )
        )

    def test_384(self):
        self.assertTrue(
            TestLexer.test(
                '''Class u:_Gt{}Class _pg7{}Class sv{}Class _{}Class _{Destructor (){}Var _,$6:Array [Array [Array [Boolean ,0B1001011],071],0B1];}''',
                '''Class,u,:,_Gt,{,},Class,_pg7,{,},Class,sv,{,},Class,_,{,},Class,_,{,Destructor,(,),{,},Var,_,,,$6,:,Array,[,Array,[,Array,[,Boolean,,,0B1001011,],,,071,],,,0B1,],;,},<EOF>''',
                101
            )
        )

    def test_385(self):
        self.assertTrue(
            TestLexer.test(
                '''Class M{}Class A:_{Constructor (){}Val FH:Array [Float ,58];Destructor (){} }Class o{_(P,h:u){}$2(){}Destructor (){} }Class L:_Lu8{}''',
                '''Class,M,{,},Class,A,:,_,{,Constructor,(,),{,},Val,FH,:,Array,[,Float,,,58,],;,Destructor,(,),{,},},Class,o,{,_,(,P,,,h,:,u,),{,},$2,(,),{,},Destructor,(,),{,},},Class,L,:,_Lu8,{,},<EOF>''',
                101
            )
        )

    def test_386(self):
        self.assertTrue(
            TestLexer.test(
                '''Class K___:__{Val $__i_,_L0,P_,$_:String ;}Class f{$5(X,A_c,_86_7m9:_;_:Array [Array [Array [Int ,0X27],74],06];_,_F2_:Int ;_2,_YR_:Float ;_0:Array [String ,0b1_0]){Z_::$g();} }''',
                '''Class,K___,:,__,{,Val,$__i_,,,_L0,,,P_,,,$_,:,String,;,},Class,f,{,$5,(,X,,,A_c,,,_86_7m9,:,_,;,_,:,Array,[,Array,[,Array,[,Int,,,0X27,],,,74,],,,06,],;,_,,,_F2_,:,Int,;,_2,,,_YR_,:,Float,;,_0,:,Array,[,String,,,0b10,],),{,Z_,::,$g,(,),;,},},<EOF>''',
                101
            )
        )

    def test_387(self):
        self.assertTrue(
            TestLexer.test(
                '''Class S_:_u8z{}Class e{Constructor (cZ__,P79,H,E_,_,h_9:Array [Float ,0x3]){} }Class koAS1:_{}Class J5{}Class D:__s{}''',
                '''Class,S_,:,_u8z,{,},Class,e,{,Constructor,(,cZ__,,,P79,,,H,,,E_,,,_,,,h_9,:,Array,[,Float,,,0x3,],),{,},},Class,koAS1,:,_,{,},Class,J5,{,},Class,D,:,__s,{,},<EOF>''',
                101
            )
        )

    def test_388(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q:_{Val B,$5,Q9:a;}Class l:Sg{}Class T_:j{}Class _HA7:_{Val __:Array [Array [Float ,034],0B11_1];}Class _26:_8{}''',
                '''Class,q,:,_,{,Val,B,,,$5,,,Q9,:,a,;,},Class,l,:,Sg,{,},Class,T_,:,j,{,},Class,_HA7,:,_,{,Val,__,:,Array,[,Array,[,Float,,,034,],,,0B111,],;,},Class,_26,:,_8,{,},<EOF>''',
                101
            )
        )

    def test_389(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:F{}Class t_{Destructor (){ {Var ___:Array [Array [Float ,8],0X2];} }Destructor (){}Destructor (){} }Class _7nA{}''',
                '''Class,_,:,F,{,},Class,t_,{,Destructor,(,),{,{,Var,___,:,Array,[,Array,[,Float,,,8,],,,0X2,],;,},},Destructor,(,),{,},Destructor,(,),{,},},Class,_7nA,{,},<EOF>''',
                101
            )
        )

    def test_390(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Cw_(){} }Class _:_{m(__,_,_,_:Array [Array [Array [Array [String ,0x9],148_39],0b1_1],43_5];_,_8,x,tdL,_:Array [Array [String ,6],0x62]){Break ;} }''',
                '''Class,_,{,Cw_,(,),{,},},Class,_,:,_,{,m,(,__,,,_,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,String,,,0x9,],,,14839,],,,0b11,],,,435,],;,_,,,_8,,,x,,,tdL,,,_,:,Array,[,Array,[,String,,,6,],,,0x62,],),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_391(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (o,_2:Array [String ,6]){Val A_Z,j6,vH:Array [Array [Float ,0x4B],28];}_(I,_6,H,__,mX,G_o,z7,I,_,r_:__u3_){} }''',
                '''Class,_,{,Constructor,(,o,,,_2,:,Array,[,String,,,6,],),{,Val,A_Z,,,j6,,,vH,:,Array,[,Array,[,Float,,,0x4B,],,,28,],;,},_,(,I,,,_6,,,H,,,__,,,mX,,,G_o,,,z7,,,I,,,_,,,r_,:,__u3_,),{,},},<EOF>''',
                101
            )
        )

    def test_392(self):
        self.assertTrue(
            TestLexer.test(
                '''Class D5{Constructor (){}Constructor (_,_,r_:Array [Array [Int ,0B100110],0X6];_2_R3,M,____:Array [String ,0B1]){} }''',
                '''Class,D5,{,Constructor,(,),{,},Constructor,(,_,,,_,,,r_,:,Array,[,Array,[,Int,,,0B100110,],,,0X6,],;,_2_R3,,,M,,,____,:,Array,[,String,,,0B1,],),{,},},<EOF>''',
                101
            )
        )

    def test_393(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t:k_j{Var _e,$7:Array [Array [Array [Array [String ,06],0x8E34],0X8],86];Var $eS_I,$TM:Array [Array [Array [Array [Array [Boolean ,0b1001011],067],7],0B1110],0b1001011];_(){} }Class _:f3{Destructor (){} }''',
                '''Class,t,:,k_j,{,Var,_e,,,$7,:,Array,[,Array,[,Array,[,Array,[,String,,,06,],,,0x8E34,],,,0X8,],,,86,],;,Var,$eS_I,,,$TM,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1001011,],,,067,],,,7,],,,0B1110,],,,0b1001011,],;,_,(,),{,},},Class,_,:,f3,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_394(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_,_,_:Array [Int ,0B111111];_0,_,_,_,b:Boolean ){Break ;}$_F(){}Constructor (h,h:q){} }Class _53{Val $T,U,$_:Float ;Val $4xV,L1:Int ;Var __:V_;}''',
                '''Class,_,{,Constructor,(,_,,,_,,,_,:,Array,[,Int,,,0B111111,],;,_0,,,_,,,_,,,_,,,b,:,Boolean,),{,Break,;,},$_F,(,),{,},Constructor,(,h,,,h,:,q,),{,},},Class,_53,{,Val,$T,,,U,,,$_,:,Float,;,Val,$4xV,,,L1,:,Int,;,Var,__,:,V_,;,},<EOF>''',
                101
            )
        )

    def test_395(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y2:S2_{A_(I:_;_,y15qp:n){Break ;}D(_ce3__,_,_,WM7_9,z,_:Array [Array [Array [Float ,0x20],77],0b1000011]){} }Class _Od_:S{}''',
                '''Class,y2,:,S2_,{,A_,(,I,:,_,;,_,,,y15qp,:,n,),{,Break,;,},D,(,_ce3__,,,_,,,_,,,WM7_9,,,z,,,_,:,Array,[,Array,[,Array,[,Float,,,0x20,],,,77,],,,0b1000011,],),{,},},Class,_Od_,:,S,{,},<EOF>''',
                101
            )
        )

    def test_396(self):
        self.assertTrue(
            TestLexer.test(
                '''Class S2{}Class _:_{$F(_,_2,l:pe;W:Array [Array [Array [Boolean ,0X31],06],0x8];_q,B_:o;s_F:Float ;_,w:String ){} }''',
                '''Class,S2,{,},Class,_,:,_,{,$F,(,_,,,_2,,,l,:,pe,;,W,:,Array,[,Array,[,Array,[,Boolean,,,0X31,],,,06,],,,0x8,],;,_q,,,B_,:,o,;,s_F,:,Float,;,_,,,w,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_397(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8_{Var $s:Array [Boolean ,02];Val S,_:Array [Array [Array [Array [Array [Boolean ,0b111100],0x57],0X79],0B10],0134];Var $_,$J,_,_,_,_:Array [String ,0134];}''',
                '''Class,_8_,{,Var,$s,:,Array,[,Boolean,,,02,],;,Val,S,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b111100,],,,0x57,],,,0X79,],,,0B10,],,,0134,],;,Var,$_,,,$J,,,_,,,_,,,_,,,_,:,Array,[,String,,,0134,],;,},<EOF>''',
                101
            )
        )

    def test_398(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T_0{Constructor (SF:m_2;k:_;N0__,Y_h19,G,f,w:Array [Array [String ,0B1],070];_,f,R:String ){Break ;Return ;Val r,__,_0q_,o,W:Array [Float ,0B1];}Val $_:Array [Array [Int ,0XEC_0],95];}''',
                '''Class,T_0,{,Constructor,(,SF,:,m_2,;,k,:,_,;,N0__,,,Y_h19,,,G,,,f,,,w,:,Array,[,Array,[,String,,,0B1,],,,070,],;,_,,,f,,,R,:,String,),{,Break,;,Return,;,Val,r,,,__,,,_0q_,,,o,,,W,:,Array,[,Float,,,0B1,],;,},Val,$_,:,Array,[,Array,[,Int,,,0XEC0,],,,95,],;,},<EOF>''',
                101
            )
        )

    def test_399(self):
        self.assertTrue(
            TestLexer.test(
                '''Class v:m{}Class t{}Class _:_53{}Class v__Q_3:_{}Class g{Var p__7__:Float ;}Class a:_l__l{}Class w:Q{Var $6_:Array [Float ,7];}''',
                '''Class,v,:,m,{,},Class,t,{,},Class,_,:,_53,{,},Class,v__Q_3,:,_,{,},Class,g,{,Var,p__7__,:,Float,;,},Class,a,:,_l__l,{,},Class,w,:,Q,{,Var,$6_,:,Array,[,Float,,,7,],;,},<EOF>''',
                101
            )
        )

    def test_400(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o_{Destructor (){}Val $_:Array [Array [Array [Array [Array [Float ,0B11101],02],95],050_2],07];}Class _:ff{}Class _6:_J{}Class _:U{}Class L_1_{}''',
                '''Class,o_,{,Destructor,(,),{,},Val,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B11101,],,,02,],,,95,],,,0502,],,,07,],;,},Class,_,:,ff,{,},Class,_6,:,_J,{,},Class,_,:,U,{,},Class,L_1_,{,},<EOF>''',
                101
            )
        )

    def test_401(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{$_(D1:_;vz_,D,___:Array [Array [Array [Array [Array [Float ,25_9],050],0X42],99],99];M,_,_,t:Array [Array [Boolean ,0X2D],0X61];__201,_:Array [Array [Array [Float ,0b10],99],03_1]){}_8(){} }''',
                '''Class,_,{,$_,(,D1,:,_,;,vz_,,,D,,,___,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,259,],,,050,],,,0X42,],,,99,],,,99,],;,M,,,_,,,_,,,t,:,Array,[,Array,[,Boolean,,,0X2D,],,,0X61,],;,__201,,,_,:,Array,[,Array,[,Array,[,Float,,,0b10,],,,99,],,,031,],),{,},_8,(,),{,},},<EOF>''',
                101
            )
        )

    def test_402(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w7:q{Constructor (u,_U5:Array [Array [Array [Array [Array [Array [String ,95],06],95],2_41_46],03],0X30];_:Float ){} }''',
                '''Class,w7,:,q,{,Constructor,(,u,,,_U5,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,95,],,,06,],,,95,],,,24146,],,,03,],,,0X30,],;,_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_403(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t:__H8{Val $_:Array [Array [Int ,0b1100000],0B1];$___(_9f__6:Array [Array [Array [Array [Float ,0B1001010],67],0x41],67];H_,_,_,C,a,k_:Array [Float ,0x41];b:Float ;o8,_,_,W:String ){} }''',
                '''Class,t,:,__H8,{,Val,$_,:,Array,[,Array,[,Int,,,0b1100000,],,,0B1,],;,$___,(,_9f__6,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B1001010,],,,67,],,,0x41,],,,67,],;,H_,,,_,,,_,,,C,,,a,,,k_,:,Array,[,Float,,,0x41,],;,b,:,Float,;,o8,,,_,,,_,,,W,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_404(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:O{$_30(I:Array [Array [Array [Array [Array [Int ,030],0b1],03],0b1001110],030]){} }Class l:F2sd_K{Val L_0:_T7;}''',
                '''Class,_,:,O,{,$_30,(,I,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,030,],,,0b1,],,,03,],,,0b1001110,],,,030,],),{,},},Class,l,:,F2sd_K,{,Val,L_0,:,_T7,;,},<EOF>''',
                101
            )
        )

    def test_405(self):
        self.assertTrue(
            TestLexer.test(
                '''Class M7:E_{Constructor (g:__;V8:Array [Array [Array [Array [String ,67],3],04_6],0b1001010];_s31:Array [Array [Boolean ,0X6_9_F_7],0x21]){}$w(e3,_:_;lw:_;_,_,VJ,__:Array [Boolean ,0x21];__:Float ;a_:Array [Array [Array [Boolean ,67],0b1001010],0B1];_,yR1G,_,_C_,_,_4k,s,u_9,R:_){Continue ;}Val $g_,$H:Array [Float ,0X1C];}''',
                '''Class,M7,:,E_,{,Constructor,(,g,:,__,;,V8,:,Array,[,Array,[,Array,[,Array,[,String,,,67,],,,3,],,,046,],,,0b1001010,],;,_s31,:,Array,[,Array,[,Boolean,,,0X69F7,],,,0x21,],),{,},$w,(,e3,,,_,:,_,;,lw,:,_,;,_,,,_,,,VJ,,,__,:,Array,[,Boolean,,,0x21,],;,__,:,Float,;,a_,:,Array,[,Array,[,Array,[,Boolean,,,67,],,,0b1001010,],,,0B1,],;,_,,,yR1G,,,_,,,_C_,,,_,,,_4k,,,s,,,u_9,,,R,:,_,),{,Continue,;,},Val,$g_,,,$H,:,Array,[,Float,,,0X1C,],;,},<EOF>''',
                101
            )
        )

    def test_406(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:__{Destructor (){}$2v0H(){} }Class M{Destructor (){Return ;}Val cH:Float ;}Class h{}Class w:_{}Class _Y{}Class _2t_{}Class R{}''',
                '''Class,_,:,__,{,Destructor,(,),{,},$2v0H,(,),{,},},Class,M,{,Destructor,(,),{,Return,;,},Val,cH,:,Float,;,},Class,h,{,},Class,w,:,_,{,},Class,_Y,{,},Class,_2t_,{,},Class,R,{,},<EOF>''',
                101
            )
        )

    def test_407(self):
        self.assertTrue(
            TestLexer.test(
                '''Class HjKW:__{Var $t,$8:Array [Array [String ,0b10],0xA];}Class L_{Constructor (I,K:r_;V,_:Float ;r,g_,___53,_b4j,v,_:Array [Boolean ,0b1010011]){} }''',
                '''Class,HjKW,:,__,{,Var,$t,,,$8,:,Array,[,Array,[,String,,,0b10,],,,0xA,],;,},Class,L_,{,Constructor,(,I,,,K,:,r_,;,V,,,_,:,Float,;,r,,,g_,,,___53,,,_b4j,,,v,,,_,:,Array,[,Boolean,,,0b1010011,],),{,},},<EOF>''',
                101
            )
        )

    def test_408(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g_89m:_{Val $_:Array [Array [Array [Array [Int ,0b10110],0B11],72],0X7];Destructor (){New _()._();}Var e:Int ;}''',
                '''Class,g_89m,:,_,{,Val,$_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b10110,],,,0B11,],,,72,],,,0X7,],;,Destructor,(,),{,New,_,(,),.,_,(,),;,},Var,e,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_409(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _z0x:F_3{}Class _U_:_Z{Constructor (_,_:Array [String ,01_2];__:Array [Boolean ,0X17];_8T_,_,_:_X;_:R){} }''',
                '''Class,_z0x,:,F_3,{,},Class,_U_,:,_Z,{,Constructor,(,_,,,_,:,Array,[,String,,,012,],;,__,:,Array,[,Boolean,,,0X17,],;,_8T_,,,_,,,_,:,_X,;,_,:,R,),{,},},<EOF>''',
                101
            )
        )

    def test_410(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _G:S{Constructor (Q_3OiQ7:String ){}Constructor (y_,_:_){Break ;If (!-___::$_17){Val q,_R:String ;}Else {}Val _:Int ;Var vj:Float ;} }''',
                '''Class,_G,:,S,{,Constructor,(,Q_3OiQ7,:,String,),{,},Constructor,(,y_,,,_,:,_,),{,Break,;,If,(,!,-,___,::,$_17,),{,Val,q,,,_R,:,String,;,},Else,{,},Val,_,:,Int,;,Var,vj,:,Float,;,},},<EOF>''',
                101
            )
        )

    def test_411(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P_:_n__{Var N:Array [Array [Array [Array [Array [Array [Array [Int ,8_9_2],0B10000],07],03],0X61],0X61],0x50D_9_1_B_9_D_A_7_A];}''',
                '''Class,P_,:,_n__,{,Var,N,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,892,],,,0B10000,],,,07,],,,03,],,,0X61,],,,0X61,],,,0x50D91B9DA7A,],;,},<EOF>''',
                101
            )
        )

    def test_412(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V4:__{w(__,_:Float ;_r:Boolean ;O,k_,pPp1y_,_,F,__,_,M_q_f:_Z){} }Class X{Destructor (){ {}Break ;} }Class E:_{}''',
                '''Class,V4,:,__,{,w,(,__,,,_,:,Float,;,_r,:,Boolean,;,O,,,k_,,,pPp1y_,,,_,,,F,,,__,,,_,,,M_q_f,:,_Z,),{,},},Class,X,{,Destructor,(,),{,{,},Break,;,},},Class,E,:,_,{,},<EOF>''',
                101
            )
        )

    def test_413(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var _b:___6;Val _,__ED_n16,D1:Float ;}Class R{Constructor (j_j:Array [Float ,077];__o,v,P,__,_2:Float ){} }Class xcwp{}Class N:D{}''',
                '''Class,_,{,Var,_b,:,___6,;,Val,_,,,__ED_n16,,,D1,:,Float,;,},Class,R,{,Constructor,(,j_j,:,Array,[,Float,,,077,],;,__o,,,v,,,P,,,__,,,_2,:,Float,),{,},},Class,xcwp,{,},Class,N,:,D,{,},<EOF>''',
                101
            )
        )

    def test_414(self):
        self.assertTrue(
            TestLexer.test(
                '''Class er8{}Class _:_{Constructor (_7_:Int ){}_(_Q:_;SY,F,G,tK_90D:_N;h__,_L_,L0,G:Int ;Y,m_T___:Array [Boolean ,0B1];__N4:Array [Array [Float ,18_16],0XF]){Continue ;}Constructor (_o,__,_91,A7,_34_8:Int ){} }Class _:m{}''',
                '''Class,er8,{,},Class,_,:,_,{,Constructor,(,_7_,:,Int,),{,},_,(,_Q,:,_,;,SY,,,F,,,G,,,tK_90D,:,_N,;,h__,,,_L_,,,L0,,,G,:,Int,;,Y,,,m_T___,:,Array,[,Boolean,,,0B1,],;,__N4,:,Array,[,Array,[,Float,,,1816,],,,0XF,],),{,Continue,;,},Constructor,(,_o,,,__,,,_91,,,A7,,,_34_8,:,Int,),{,},},Class,_,:,m,{,},<EOF>''',
                101
            )
        )

    def test_415(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class _8:B{}Class U7{}Class mD{$j7_K_(_,_331,g:Array [Array [String ,0XF5],0x36];__:Array [Boolean ,6]){} }''',
                '''Class,__,{,},Class,_8,:,B,{,},Class,U7,{,},Class,mD,{,$j7_K_,(,_,,,_331,,,g,:,Array,[,Array,[,String,,,0XF5,],,,0x36,],;,__,:,Array,[,Boolean,,,6,],),{,},},<EOF>''',
                101
            )
        )

    def test_416(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _f{Var $Q:Array [Array [Array [Int ,0b1],0X5_1_2],48_75_70];Var _D,$97_,$0,$3,$l:_;C(_W,_3:Array [Int ,225_245]){Continue ;} }Class Pb{}Class _6{}''',
                '''Class,_f,{,Var,$Q,:,Array,[,Array,[,Array,[,Int,,,0b1,],,,0X512,],,,487570,],;,Var,_D,,,$97_,,,$0,,,$3,,,$l,:,_,;,C,(,_W,,,_3,:,Array,[,Int,,,225245,],),{,Continue,;,},},Class,Pb,{,},Class,_6,{,},<EOF>''',
                101
            )
        )

    def test_417(self):
        self.assertTrue(
            TestLexer.test(
                '''Class h{Destructor (){}Var $X0,_,m__:Array [String ,0x6_D_3];}Class R1_:R5{}Class D{}Class _lC6___1{Val $f:String ;}''',
                '''Class,h,{,Destructor,(,),{,},Var,$X0,,,_,,,m__,:,Array,[,String,,,0x6D3,],;,},Class,R1_,:,R5,{,},Class,D,{,},Class,_lC6___1,{,Val,$f,:,String,;,},<EOF>''',
                101
            )
        )

    def test_418(self):
        self.assertTrue(
            TestLexer.test(
                '''Class h:_{Destructor (){}Constructor (){}$_(__,K:t;j,__2wb,_:Array [Float ,047];L,_:Float ;_:Float ;k_,_6_19:String ){} }''',
                '''Class,h,:,_,{,Destructor,(,),{,},Constructor,(,),{,},$_,(,__,,,K,:,t,;,j,,,__2wb,,,_,:,Array,[,Float,,,047,],;,L,,,_,:,Float,;,_,:,Float,;,k_,,,_6_19,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_419(self):
        self.assertTrue(
            TestLexer.test(
                '''Class zd3L:_2{$F(){}Val X,R:Array [Array [Array [Array [Array [Array [Int ,81],01],0B1011110],0b1],0b1_110_0],0B1011110];_(__4,_,_r0P_3,kk:Array [Array [Array [Int ,81],22],81];E_:Int ;e,_,Oh:_5_;___7:String ){} }''',
                '''Class,zd3L,:,_2,{,$F,(,),{,},Val,X,,,R,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,81,],,,01,],,,0B1011110,],,,0b1,],,,0b11100,],,,0B1011110,],;,_,(,__4,,,_,,,_r0P_3,,,kk,:,Array,[,Array,[,Array,[,Int,,,81,],,,22,],,,81,],;,E_,:,Int,;,e,,,_,,,Oh,:,_5_,;,___7,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_420(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n_:Fb7{Constructor (x,g,_0_1:Array [String ,6];_,V9,_F_v__1,pZ,z,__0u:Array [String ,0b1]){Continue ;}Destructor (){}Val $M7,$4,$1,__:h;}Class __:Fs{}''',
                '''Class,n_,:,Fb7,{,Constructor,(,x,,,g,,,_0_1,:,Array,[,String,,,6,],;,_,,,V9,,,_F_v__1,,,pZ,,,z,,,__0u,:,Array,[,String,,,0b1,],),{,Continue,;,},Destructor,(,),{,},Val,$M7,,,$4,,,$1,,,__,:,h,;,},Class,__,:,Fs,{,},<EOF>''',
                101
            )
        )

    def test_421(self):
        self.assertTrue(
            TestLexer.test(
                '''Class F_{$__13(_:_;_8__:Boolean ;n:s;q,c:Array [String ,0b1010100];_,i__,B__,b:Boolean ){}Constructor (s:Array [Int ,05];__u:Array [Int ,43];_n:Boolean ;g_G1:A;R4:Array [Array [Array [Boolean ,32],0xA],8]){} }''',
                '''Class,F_,{,$__13,(,_,:,_,;,_8__,:,Boolean,;,n,:,s,;,q,,,c,:,Array,[,String,,,0b1010100,],;,_,,,i__,,,B__,,,b,:,Boolean,),{,},Constructor,(,s,:,Array,[,Int,,,05,],;,__u,:,Array,[,Int,,,43,],;,_n,:,Boolean,;,g_G1,:,A,;,R4,:,Array,[,Array,[,Array,[,Boolean,,,32,],,,0xA,],,,8,],),{,},},<EOF>''',
                101
            )
        )

    def test_422(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _20_s:p2{_l0tqZ_(_:Float ;G_:Array [String ,0b1_1];c9,h:Int ;a1_:Array [Int ,0b1_0_10]){}Var _,$_,$_t:_;}Class p:H{}''',
                '''Class,_20_s,:,p2,{,_l0tqZ_,(,_,:,Float,;,G_,:,Array,[,String,,,0b11,],;,c9,,,h,:,Int,;,a1_,:,Array,[,Int,,,0b1010,],),{,},Var,_,,,$_,,,$_t,:,_,;,},Class,p,:,H,{,},<EOF>''',
                101
            )
        )

    def test_423(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o{}Class _EA_6{}Class S:_{Constructor (__0zo1__,J_:Int ;N22Y_4,l2,N:Array [Array [String ,0XD],0x38]){} }''',
                '''Class,o,{,},Class,_EA_6,{,},Class,S,:,_,{,Constructor,(,__0zo1__,,,J_,:,Int,;,N22Y_4,,,l2,,,N,:,Array,[,Array,[,String,,,0XD,],,,0x38,],),{,},},<EOF>''',
                101
            )
        )

    def test_424(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J_17_{Var $__,y5_,_o_,j,$7,$_,vI:Array [Array [Array [Array [Array [Boolean ,7_4],0X37],5_2_2],9],0X37];}Class y:_{}''',
                '''Class,J_17_,{,Var,$__,,,y5_,,,_o_,,,j,,,$7,,,$_,,,vI,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,74,],,,0X37,],,,522,],,,9,],,,0X37,],;,},Class,y,:,_,{,},<EOF>''',
                101
            )
        )

    def test_425(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g_F{$__Q(_J:Array [Array [Int ,045],0x4C]){} }Class t_a_G2{_(_:Array [Array [Float ,0x7_9],070_2]){_J9::$_t();} }Class p{}Class _:_{}Class K{Destructor (){}_(_,y:Array [Array [Array [Array [Boolean ,0x4C],045],045],5_3_8]){}Val $0,$a1_:Array [Array [Array [Float ,04],0X4_4],0B1000110];Var _,$_,_:String ;}''',
                '''Class,g_F,{,$__Q,(,_J,:,Array,[,Array,[,Int,,,045,],,,0x4C,],),{,},},Class,t_a_G2,{,_,(,_,:,Array,[,Array,[,Float,,,0x79,],,,0702,],),{,_J9,::,$_t,(,),;,},},Class,p,{,},Class,_,:,_,{,},Class,K,{,Destructor,(,),{,},_,(,_,,,y,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x4C,],,,045,],,,045,],,,538,],),{,},Val,$0,,,$a1_,:,Array,[,Array,[,Array,[,Float,,,04,],,,0X44,],,,0B1000110,],;,Var,_,,,$_,,,_,:,String,;,},<EOF>''',
                101
            )
        )

    def test_426(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Bm{d__(){Continue ;} }Class H{}Class c_i_:____{Var _:String ;Constructor (l,sL:Array [Array [Float ,0b1],0X5B]){Break ;Break ;} }Class __mv_0{}''',
                '''Class,Bm,{,d__,(,),{,Continue,;,},},Class,H,{,},Class,c_i_,:,____,{,Var,_,:,String,;,Constructor,(,l,,,sL,:,Array,[,Array,[,Float,,,0b1,],,,0X5B,],),{,Break,;,Break,;,},},Class,__mv_0,{,},<EOF>''',
                101
            )
        )

    def test_427(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:d{Var $3:Int ;}Class __{}Class _3:_{Destructor (){JyU::$_();_::$A();} }Class _C1{Destructor (){}Constructor (_,_S,__k:Int ;_:_;_:Array [String ,0B11]){} }''',
                '''Class,_,:,d,{,Var,$3,:,Int,;,},Class,__,{,},Class,_3,:,_,{,Destructor,(,),{,JyU,::,$_,(,),;,_,::,$A,(,),;,},},Class,_C1,{,Destructor,(,),{,},Constructor,(,_,,,_S,,,__k,:,Int,;,_,:,_,;,_,:,Array,[,String,,,0B11,],),{,},},<EOF>''',
                101
            )
        )

    def test_428(self):
        self.assertTrue(
            TestLexer.test(
                '''Class d:B{}Class p:P89l55{}Class _:a{Constructor (i:Array [Array [String ,26],26];_,_2Y,B:Array [Float ,0X3D];_,_Ec:Array [Array [Array [Boolean ,0x8],073646],0b11100]){} }Class I6:jX8{Constructor (_J,z_,_,_s,___Q_,_9_:n_){} }''',
                '''Class,d,:,B,{,},Class,p,:,P89l55,{,},Class,_,:,a,{,Constructor,(,i,:,Array,[,Array,[,String,,,26,],,,26,],;,_,,,_2Y,,,B,:,Array,[,Float,,,0X3D,],;,_,,,_Ec,:,Array,[,Array,[,Array,[,Boolean,,,0x8,],,,073646,],,,0b11100,],),{,},},Class,I6,:,jX8,{,Constructor,(,_J,,,z_,,,_,,,_s,,,___Q_,,,_9_,:,n_,),{,},},<EOF>''',
                101
            )
        )

    def test_429(self):
        self.assertTrue(
            TestLexer.test(
                '''Class F{}Class _7v08{$0(){Val _w,_,_6_,n5yz9:Array [Array [Array [String ,87],87],21];{} }Val t_:Array [Array [Array [Array [String ,0b1_0_001],047],0b1],0117];}''',
                '''Class,F,{,},Class,_7v08,{,$0,(,),{,Val,_w,,,_,,,_6_,,,n5yz9,:,Array,[,Array,[,Array,[,String,,,87,],,,87,],,,21,],;,{,},},Val,t_,:,Array,[,Array,[,Array,[,Array,[,String,,,0b10001,],,,047,],,,0b1,],,,0117,],;,},<EOF>''',
                101
            )
        )

    def test_430(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_2{Constructor (q:Array [Array [Boolean ,0B1_0],0x4];V,_,__:X_){}Constructor (y,_:_6_;b_,_y_:I;_:Array [Int ,195];_:Array [Array [Array [String ,0B11_11_1_1],02],0B1_1_00_1_1_1_0_1];t:Array [String ,60];_s,_:Array [Array [Int ,0b1],60]){}Destructor (){} }''',
                '''Class,_,:,_2,{,Constructor,(,q,:,Array,[,Array,[,Boolean,,,0B10,],,,0x4,],;,V,,,_,,,__,:,X_,),{,},Constructor,(,y,,,_,:,_6_,;,b_,,,_y_,:,I,;,_,:,Array,[,Int,,,195,],;,_,:,Array,[,Array,[,Array,[,String,,,0B111111,],,,02,],,,0B110011101,],;,t,:,Array,[,String,,,60,],;,_s,,,_,:,Array,[,Array,[,Int,,,0b1,],,,60,],),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_431(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l{Constructor (_88_0_:_2){}$X(s:_;R,_2,j_v:Int ;f:String ;_H:String ;_7,_,_2,__:_;P:Boolean ){Return ;} }''',
                '''Class,l,{,Constructor,(,_88_0_,:,_2,),{,},$X,(,s,:,_,;,R,,,_2,,,j_v,:,Int,;,f,:,String,;,_H,:,String,;,_7,,,_,,,_2,,,__,:,_,;,P,:,Boolean,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_432(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:b_{Val Z:Array [Float ,0x38];}Class M:_{}Class _e9{Constructor (){} }Class _83:____{Destructor (){Break ;{} }}''',
                '''Class,__,:,b_,{,Val,Z,:,Array,[,Float,,,0x38,],;,},Class,M,:,_,{,},Class,_e9,{,Constructor,(,),{,},},Class,_83,:,____,{,Destructor,(,),{,Break,;,{,},},},<EOF>''',
                101
            )
        )

    def test_433(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:_E_{}Class _f{Y(_,_0:_47;K:__){p::$99v_();}Destructor (){}Constructor (_,_a,_:_5;_,V,J,n,_7:Array [Int ,0XA_4_7]){} }''',
                '''Class,__,:,_E_,{,},Class,_f,{,Y,(,_,,,_0,:,_47,;,K,:,__,),{,p,::,$99v_,(,),;,},Destructor,(,),{,},Constructor,(,_,,,_a,,,_,:,_5,;,_,,,V,,,J,,,n,,,_7,:,Array,[,Int,,,0XA47,],),{,},},<EOF>''',
                101
            )
        )

    def test_434(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E{Destructor (){}Var $u_:Array [String ,4];_(H:_;N6:Array [Array [Float ,02],051];B,d5p:_;WCzg_J,h5_:Array [Boolean ,0570_4];f:U;y7:_09;T2m:Int ){} }Class a1:_{Val l:_;Val $5:Array [Int ,0b100110];}''',
                '''Class,E,{,Destructor,(,),{,},Var,$u_,:,Array,[,String,,,4,],;,_,(,H,:,_,;,N6,:,Array,[,Array,[,Float,,,02,],,,051,],;,B,,,d5p,:,_,;,WCzg_J,,,h5_,:,Array,[,Boolean,,,05704,],;,f,:,U,;,y7,:,_09,;,T2m,:,Int,),{,},},Class,a1,:,_,{,Val,l,:,_,;,Val,$5,:,Array,[,Int,,,0b100110,],;,},<EOF>''',
                101
            )
        )

    def test_435(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _m{}Class _:F{CX(N_V,_:Array [String ,0x6_3];C,__Zy_0p,f,aV,E2,_,_5,__,e,_s8Kl,_8,_,_:Array [Array [Array [Array [Float ,0b1011],6],0X2],0B1001]){Break ;} }''',
                '''Class,_m,{,},Class,_,:,F,{,CX,(,N_V,,,_,:,Array,[,String,,,0x63,],;,C,,,__Zy_0p,,,f,,,aV,,,E2,,,_,,,_5,,,__,,,e,,,_s8Kl,,,_8,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0b1011,],,,6,],,,0X2,],,,0B1001,],),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_436(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _y9F8_c:d{Val __,Tp8:Array [Int ,06_7_4_23];Val $_:Float ;}Class __:_{Val _:Float ;$6n_(_89:_;r5T:EKK;_,__:X;_:Array [Array [Float ,6],0X8]){ {} }Destructor (){Break ;}Destructor (){}Val G_:Array [Array [Int ,02],04];}''',
                '''Class,_y9F8_c,:,d,{,Val,__,,,Tp8,:,Array,[,Int,,,067423,],;,Val,$_,:,Float,;,},Class,__,:,_,{,Val,_,:,Float,;,$6n_,(,_89,:,_,;,r5T,:,EKK,;,_,,,__,:,X,;,_,:,Array,[,Array,[,Float,,,6,],,,0X8,],),{,{,},},Destructor,(,),{,Break,;,},Destructor,(,),{,},Val,G_,:,Array,[,Array,[,Int,,,02,],,,04,],;,},<EOF>''',
                101
            )
        )

    def test_437(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:__{_8I(A,h,R:Boolean ;s_89M:Int ){Return ;} }Class _K4_X4:u5{$_(_:Float ;kay2mV:Float ){} }Class d{}Class _2_:t_{}''',
                '''Class,_,:,__,{,_8I,(,A,,,h,,,R,:,Boolean,;,s_89M,:,Int,),{,Return,;,},},Class,_K4_X4,:,u5,{,$_,(,_,:,Float,;,kay2mV,:,Float,),{,},},Class,d,{,},Class,_2_,:,t_,{,},<EOF>''',
                101
            )
        )

    def test_438(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V1:_2{}Class Ke_{Val $_0_E,_CS____,$__:Array [Int ,01_4_45_13];$vyH(d_,h,y,Jd,_,S,__B:Int ;___QO:Boolean ){Return ;} }''',
                '''Class,V1,:,_2,{,},Class,Ke_,{,Val,$_0_E,,,_CS____,,,$__,:,Array,[,Int,,,0144513,],;,$vyH,(,d_,,,h,,,y,,,Jd,,,_,,,S,,,__B,:,Int,;,___QO,:,Boolean,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_439(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_5T{$T__Zy(i,_DF:Array [Array [Array [Float ,0B1],04],0b1_0001_1];q:Float ;_3__0:String ){} }Class _:_7{}''',
                '''Class,_,:,_5T,{,$T__Zy,(,i,,,_DF,:,Array,[,Array,[,Array,[,Float,,,0B1,],,,04,],,,0b100011,],;,q,:,Float,;,_3__0,:,String,),{,},},Class,_,:,_7,{,},<EOF>''',
                101
            )
        )

    def test_440(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _UV__:u6{}Class _:_{}Class e71:_{}Class o{Var BAR_D5,$_,$n,K_,$1,O:String ;Constructor (_O4k,a7,_6,H5Ke_96_:r9){} }''',
                '''Class,_UV__,:,u6,{,},Class,_,:,_,{,},Class,e71,:,_,{,},Class,o,{,Var,BAR_D5,,,$_,,,$n,,,K_,,,$1,,,O,:,String,;,Constructor,(,_O4k,,,a7,,,_6,,,H5Ke_96_,:,r9,),{,},},<EOF>''',
                101
            )
        )

    def test_441(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Var __,$7,$__:Array [Array [String ,0b1],51];Destructor (){} }Class _p_:Q{Val l,__m_,$z7o:_;}Class L_763{Var _H,l_:Array [Array [Array [String ,012],0b10],0X4]=_0::$_r_().W4,!!-Null ;Var _:Array [Array [Array [Array [String ,04],07],012],012];Var _s__W6__,__15:d;}Class pF{X(){}Destructor (){} }''',
                '''Class,_,:,_,{,Var,__,,,$7,,,$__,:,Array,[,Array,[,String,,,0b1,],,,51,],;,Destructor,(,),{,},},Class,_p_,:,Q,{,Val,l,,,__m_,,,$z7o,:,_,;,},Class,L_763,{,Var,_H,,,l_,:,Array,[,Array,[,Array,[,String,,,012,],,,0b10,],,,0X4,],=,_0,::,$_r_,(,),.,W4,,,!,!,-,Null,;,Var,_,:,Array,[,Array,[,Array,[,Array,[,String,,,04,],,,07,],,,012,],,,012,],;,Var,_s__W6__,,,__15,:,d,;,},Class,pF,{,X,(,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_442(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Destructor (){}Constructor (_:_){Return ;}Var $Lu:Array [Array [Array [Boolean ,0X2_7],0b1000_0_1],0X17];Destructor (){} }''',
                '''Class,_,:,_,{,Destructor,(,),{,},Constructor,(,_,:,_,),{,Return,;,},Var,$Lu,:,Array,[,Array,[,Array,[,Boolean,,,0X27,],,,0b100001,],,,0X17,],;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_443(self):
        self.assertTrue(
            TestLexer.test(
                '''Class e8{$M9(_:_;__,W,_:Array [Array [String ,0X1],0XDD_8];n,jLF1:_){} }Class _E_3_M{N4(zQ2w38:Boolean ){}Val _:Array [Float ,06];}''',
                '''Class,e8,{,$M9,(,_,:,_,;,__,,,W,,,_,:,Array,[,Array,[,String,,,0X1,],,,0XDD8,],;,n,,,jLF1,:,_,),{,},},Class,_E_3_M,{,N4,(,zQ2w38,:,Boolean,),{,},Val,_,:,Array,[,Float,,,06,],;,},<EOF>''',
                101
            )
        )

    def test_444(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E:R_6{Constructor (){ {}Return ;} }Class Z{_(w_,_G,_8,__,_,__:Array [Boolean ,043];Bm_t9_0pb13o,_Bj:Boolean ;q3J:D){}Destructor (){} }Class NB{Destructor (){} }Class _:__{$_(p,G6,q:String ){}Constructor (){} }Class _{}''',
                '''Class,E,:,R_6,{,Constructor,(,),{,{,},Return,;,},},Class,Z,{,_,(,w_,,,_G,,,_8,,,__,,,_,,,__,:,Array,[,Boolean,,,043,],;,Bm_t9_0pb13o,,,_Bj,:,Boolean,;,q3J,:,D,),{,},Destructor,(,),{,},},Class,NB,{,Destructor,(,),{,},},Class,_,:,__,{,$_,(,p,,,G6,,,q,:,String,),{,},Constructor,(,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_445(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _g6:j{Constructor (f:Array [Int ,4_8];f,_1:Array [String ,0B1011]){Continue ;}$_(d,__,__,_5,M,_4_m_:Float ;_6:Boolean ){} }''',
                '''Class,_g6,:,j,{,Constructor,(,f,:,Array,[,Int,,,48,],;,f,,,_1,:,Array,[,String,,,0B1011,],),{,Continue,;,},$_,(,d,,,__,,,__,,,_5,,,M,,,_4_m_,:,Float,;,_6,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_446(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:L{}Class _{}Class _:_{}Class _:j_{Var $3,$_,$__:Array [Boolean ,0XF];Constructor (o,H2,X,__7:Boolean ;r8,_,_,_,_S,___,T:Array [String ,050]){} }''',
                '''Class,__,:,L,{,},Class,_,{,},Class,_,:,_,{,},Class,_,:,j_,{,Var,$3,,,$_,,,$__,:,Array,[,Boolean,,,0XF,],;,Constructor,(,o,,,H2,,,X,,,__7,:,Boolean,;,r8,,,_,,,_,,,_,,,_S,,,___,,,T,:,Array,[,String,,,050,],),{,},},<EOF>''',
                101
            )
        )

    def test_447(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_a{}Class _4:a{Var $_,T:Array [Array [Array [Array [Array [Array [Array [Float ,0B11],0B111010],0B1_0],0B111010],8],032],0x4];}''',
                '''Class,_,:,_a,{,},Class,_4,:,a,{,Var,$_,,,T,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B11,],,,0B111010,],,,0B10,],,,0B111010,],,,8,],,,032,],,,0x4,],;,},<EOF>''',
                101
            )
        )

    def test_448(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9{Constructor (){}Var $_,$y4,_,_:_;Var Q,_61_,_,S_o,i,$1,VX30Fbt,_:__;Val D_8,r,CF:w;}Class b___:IwT{}''',
                '''Class,_9,{,Constructor,(,),{,},Var,$_,,,$y4,,,_,,,_,:,_,;,Var,Q,,,_61_,,,_,,,S_o,,,i,,,$1,,,VX30Fbt,,,_,:,__,;,Val,D_8,,,r,,,CF,:,w,;,},Class,b___,:,IwT,{,},<EOF>''',
                101
            )
        )

    def test_449(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _3A_f:_v7{Val d,_C_q,_:Float ;}Class _{}Class _B{}Class _:t_{}Class s{Constructor (){} }Class V_{$___(j:Array [Array [Array [Boolean ,0b11],0B1],0b1];j3:w_;U:R2){} }''',
                '''Class,_3A_f,:,_v7,{,Val,d,,,_C_q,,,_,:,Float,;,},Class,_,{,},Class,_B,{,},Class,_,:,t_,{,},Class,s,{,Constructor,(,),{,},},Class,V_,{,$___,(,j,:,Array,[,Array,[,Array,[,Boolean,,,0b11,],,,0B1,],,,0b1,],;,j3,:,w_,;,U,:,R2,),{,},},<EOF>''',
                101
            )
        )

    def test_450(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:_h{_(_,_o:Array [Array [Array [Float ,0B1],0B1_01_1],51]){}Destructor (){}Val $W:Array [Boolean ,0x8_B];Var $C:Boolean ;}''',
                '''Class,__,:,_h,{,_,(,_,,,_o,:,Array,[,Array,[,Array,[,Float,,,0B1,],,,0B1011,],,,51,],),{,},Destructor,(,),{,},Val,$W,:,Array,[,Boolean,,,0x8B,],;,Var,$C,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_451(self):
        self.assertTrue(
            TestLexer.test(
                '''Class H:H_X1{Constructor (){} }Class j{}Class __{Constructor (PZ9:Boolean ;_3:Array [Int ,13];b_:_){ {} }}Class q:_{Destructor (){} }''',
                '''Class,H,:,H_X1,{,Constructor,(,),{,},},Class,j,{,},Class,__,{,Constructor,(,PZ9,:,Boolean,;,_3,:,Array,[,Int,,,13,],;,b_,:,_,),{,{,},},},Class,q,:,_,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_452(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _a5:D_{$DK(x:Array [Array [Array [Array [Array [Float ,3],0100],9],71],03_4_41];_l7:String ;__:Boolean ){}$Y9(){} }''',
                '''Class,_a5,:,D_,{,$DK,(,x,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,3,],,,0100,],,,9,],,,71,],,,03441,],;,_l7,:,String,;,__,:,Boolean,),{,},$Y9,(,),{,},},<EOF>''',
                101
            )
        )

    def test_453(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _n:_O{Var $2:Boolean ;Constructor (_:Array [Array [Array [Array [Array [String ,0b100000],4_76_5],03_7_6],24],0114];_B:Array [Int ,0b1_1_1]){} }Class W:H{}''',
                '''Class,_n,:,_O,{,Var,$2,:,Boolean,;,Constructor,(,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b100000,],,,4765,],,,0376,],,,24,],,,0114,],;,_B,:,Array,[,Int,,,0b111,],),{,},},Class,W,:,H,{,},<EOF>''',
                101
            )
        )

    def test_454(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _3:_K{ab(__3_:Array [String ,0b10_1_0];B:Array [Boolean ,0b1000110];b,_,L:String ;_5P:_;g7,_3,_6:Array [Boolean ,0b1_1101_0];o,_:C__;gn1,Q:String ;k__,_,_7_:g;_:Array [Boolean ,0xB]){Break ;} }''',
                '''Class,_3,:,_K,{,ab,(,__3_,:,Array,[,String,,,0b1010,],;,B,:,Array,[,Boolean,,,0b1000110,],;,b,,,_,,,L,:,String,;,_5P,:,_,;,g7,,,_3,,,_6,:,Array,[,Boolean,,,0b111010,],;,o,,,_,:,C__,;,gn1,,,Q,:,String,;,k__,,,_,,,_7_,:,g,;,_,:,Array,[,Boolean,,,0xB,],),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_455(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __5CP2_T1:_7{_(M9w__81:Array [Array [Boolean ,06],0B1100100];M0e_,_,m,v,_Y,_,_A,L6,_:_j;f_K:_G__R7__){} }Class y{}''',
                '''Class,__5CP2_T1,:,_7,{,_,(,M9w__81,:,Array,[,Array,[,Boolean,,,06,],,,0B1100100,],;,M0e_,,,_,,,m,,,v,,,_Y,,,_,,,_A,,,L6,,,_,:,_j,;,f_K,:,_G__R7__,),{,},},Class,y,{,},<EOF>''',
                101
            )
        )

    def test_456(self):
        self.assertTrue(
            TestLexer.test(
                '''Class d{Var $s:Int ;}Class _0{Var $___8_J_6:String ;}Class _2:D{Constructor (_o:Float ;b,_:Array [Array [Array [Array [Int ,70],0x39],0B1001101],0xA]){New qS__().____().h8();} }Class s_:d{}''',
                '''Class,d,{,Var,$s,:,Int,;,},Class,_0,{,Var,$___8_J_6,:,String,;,},Class,_2,:,D,{,Constructor,(,_o,:,Float,;,b,,,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,70,],,,0x39,],,,0B1001101,],,,0xA,],),{,New,qS__,(,),.,____,(,),.,h8,(,),;,},},Class,s_,:,d,{,},<EOF>''',
                101
            )
        )

    def test_457(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:i{}Class A0_:C4_O{Val Z:Array [Array [String ,8],06_3_6_4_5];Var $6F___5,$W5,$5:Array [String ,0x8_9];Val Qo:Int ;$c(){} }''',
                '''Class,_,:,i,{,},Class,A0_,:,C4_O,{,Val,Z,:,Array,[,Array,[,String,,,8,],,,063645,],;,Var,$6F___5,,,$W5,,,$5,:,Array,[,String,,,0x89,],;,Val,Qo,:,Int,;,$c,(,),{,},},<EOF>''',
                101
            )
        )

    def test_458(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:p{}Class __:_{}Class R:Z{Val $p_W1:uSFv;}Class M:k{Destructor (){}Constructor (){Break ;}Constructor (){} }''',
                '''Class,_,:,p,{,},Class,__,:,_,{,},Class,R,:,Z,{,Val,$p_W1,:,uSFv,;,},Class,M,:,k,{,Destructor,(,),{,},Constructor,(,),{,Break,;,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_459(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b_{Destructor (){}Var $_bz:Array [Array [Array [Array [Int ,0xC33],0X4E],3],06];}Class __:d{Var $_,$_,z4:L;Var __,$2:_p;}''',
                '''Class,b_,{,Destructor,(,),{,},Var,$_bz,:,Array,[,Array,[,Array,[,Array,[,Int,,,0xC33,],,,0X4E,],,,3,],,,06,],;,},Class,__,:,d,{,Var,$_,,,$_,,,z4,:,L,;,Var,__,,,$2,:,_p,;,},<EOF>''',
                101
            )
        )

    def test_460(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{Destructor (){}Constructor (_M_,B4_g,S,_,T_,_,h:Array [Array [Boolean ,0104],3]){} }Class G{}Class _:N{}''',
                '''Class,__,{,Destructor,(,),{,},Constructor,(,_M_,,,B4_g,,,S,,,_,,,T_,,,_,,,h,:,Array,[,Array,[,Boolean,,,0104,],,,3,],),{,},},Class,G,{,},Class,_,:,N,{,},<EOF>''',
                101
            )
        )

    def test_461(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:e8{Destructor (){} }Class I35_:P_I48{Val _18_,$4:String ;}Class Q{Var $t_:_1;Val g:Boolean ;Val r,E:k_;Val _70pqY:Array [String ,7];Val _Q,$e3:f;}''',
                '''Class,_,:,e8,{,Destructor,(,),{,},},Class,I35_,:,P_I48,{,Val,_18_,,,$4,:,String,;,},Class,Q,{,Var,$t_,:,_1,;,Val,g,:,Boolean,;,Val,r,,,E,:,k_,;,Val,_70pqY,:,Array,[,String,,,7,],;,Val,_Q,,,$e3,:,f,;,},<EOF>''',
                101
            )
        )

    def test_462(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Var _G_,$E:Array [Array [Float ,77],02];$1(_:Array [Array [Array [Array [Boolean ,0b1011],03_56_27_7_2_1],4_6_8],0b1];_G:m){} }''',
                '''Class,_,:,_,{,Var,_G_,,,$E,:,Array,[,Array,[,Float,,,77,],,,02,],;,$1,(,_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1011,],,,035627721,],,,468,],,,0b1,],;,_G,:,m,),{,},},<EOF>''',
                101
            )
        )

    def test_463(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Var bPJ_9,$n42:Array [Array [Array [Array [Array [Array [Array [Array [String ,5],69],0x5],0XE],0X22],06],7_2_8],0b1];Var q:Array [Array [Boolean ,07],0B1];}''',
                '''Class,_,:,_,{,Var,bPJ_9,,,$n42,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,5,],,,69,],,,0x5,],,,0XE,],,,0X22,],,,06,],,,728,],,,0b1,],;,Var,q,:,Array,[,Array,[,Boolean,,,07,],,,0B1,],;,},<EOF>''',
                101
            )
        )

    def test_464(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:_{}Class _{Val p,_:Array [Int ,04_5];fkU(){}Constructor (_n,N_b_:x7){}Constructor (a:String ){}Var _:Array [Boolean ,1];Val _,sy:l_80;}Class _{}Class __26:LXu{Val V__8,$0:E;}''',
                '''Class,__,:,_,{,},Class,_,{,Val,p,,,_,:,Array,[,Int,,,045,],;,fkU,(,),{,},Constructor,(,_n,,,N_b_,:,x7,),{,},Constructor,(,a,:,String,),{,},Var,_,:,Array,[,Boolean,,,1,],;,Val,_,,,sy,:,l_80,;,},Class,_,{,},Class,__26,:,LXu,{,Val,V__8,,,$0,:,E,;,},<EOF>''',
                101
            )
        )

    def test_465(self):
        self.assertTrue(
            TestLexer.test(
                '''Class M_{Constructor (_,H:_){}Constructor (N3_:sX_){} }Class _1y__{Constructor (w9,W,e:Array [Array [Boolean ,0XE],0B111111];i:_){Break ;} }Class _:_2nxI{}''',
                '''Class,M_,{,Constructor,(,_,,,H,:,_,),{,},Constructor,(,N3_,:,sX_,),{,},},Class,_1y__,{,Constructor,(,w9,,,W,,,e,:,Array,[,Array,[,Boolean,,,0XE,],,,0B111111,],;,i,:,_,),{,Break,;,},},Class,_,:,_2nxI,{,},<EOF>''',
                101
            )
        )

    def test_466(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Lb{__(){}Val $W,M:Boolean ;Destructor (){} }Class _E{Constructor (_:Array [Int ,0B1010010]){} }Class y:q{Var _,$__hH:P;}''',
                '''Class,Lb,{,__,(,),{,},Val,$W,,,M,:,Boolean,;,Destructor,(,),{,},},Class,_E,{,Constructor,(,_,:,Array,[,Int,,,0B1010010,],),{,},},Class,y,:,q,{,Var,_,,,$__hH,:,P,;,},<EOF>''',
                101
            )
        )

    def test_467(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Qd:_{}Class o_:_r_4{Val _,$_IC:Array [Array [Float ,01],0b111];}Class _{Var $___,$45:_;Var $_,l:Array [Array [Float ,0b11],0102];Var _:_;}''',
                '''Class,Qd,:,_,{,},Class,o_,:,_r_4,{,Val,_,,,$_IC,:,Array,[,Array,[,Float,,,01,],,,0b111,],;,},Class,_,{,Var,$___,,,$45,:,_,;,Var,$_,,,l,:,Array,[,Array,[,Float,,,0b11,],,,0102,],;,Var,_,:,_,;,},<EOF>''',
                101
            )
        )

    def test_468(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (f,o2,__,M4:Int ;_,_5:Int ;eE1,___W,_,c_7:Array [Array [Boolean ,0B1],01]){}Destructor (){Continue ;}Constructor (){} }''',
                '''Class,_,{,Constructor,(,f,,,o2,,,__,,,M4,:,Int,;,_,,,_5,:,Int,;,eE1,,,___W,,,_,,,c_7,:,Array,[,Array,[,Boolean,,,0B1,],,,01,],),{,},Destructor,(,),{,Continue,;,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_469(self):
        self.assertTrue(
            TestLexer.test(
                '''Class W1:_{Constructor (){Continue ;} }Class K{Var _,$_,y,_4J,y,$E,$Y,$A:Array [Array [Array [Boolean ,0x6],0b111110],0b1];}Class _4:A{}''',
                '''Class,W1,:,_,{,Constructor,(,),{,Continue,;,},},Class,K,{,Var,_,,,$_,,,y,,,_4J,,,y,,,$E,,,$Y,,,$A,:,Array,[,Array,[,Array,[,Boolean,,,0x6,],,,0b111110,],,,0b1,],;,},Class,_4,:,A,{,},<EOF>''',
                101
            )
        )

    def test_470(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:J{_(_:Array [Int ,81];M,F81,F_,u,w,J3N,F,_3:Array [Array [Array [String ,0XD1C9],0B11001],0xC];Y:Array [Int ,017]){}Constructor (){} }Class B:E{}Class H_{}''',
                '''Class,_,:,J,{,_,(,_,:,Array,[,Int,,,81,],;,M,,,F81,,,F_,,,u,,,w,,,J3N,,,F,,,_3,:,Array,[,Array,[,Array,[,String,,,0XD1C9,],,,0B11001,],,,0xC,],;,Y,:,Array,[,Int,,,017,],),{,},Constructor,(,),{,},},Class,B,:,E,{,},Class,H_,{,},<EOF>''',
                101
            )
        )

    def test_471(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E__{Destructor (){} }Class y:_{Constructor (){} }Class _{}Class f:_7VU1{}Class _a8:_{Val $9_6___:Array [Float ,30];}''',
                '''Class,E__,{,Destructor,(,),{,},},Class,y,:,_,{,Constructor,(,),{,},},Class,_,{,},Class,f,:,_7VU1,{,},Class,_a8,:,_,{,Val,$9_6___,:,Array,[,Float,,,30,],;,},<EOF>''',
                101
            )
        )

    def test_472(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:Z8v{Destructor (){Break ;Var B,_,i,p,_:d;Continue ;Continue ;}$YO_(a_ju2,_,_:Array [Int ,0b1011100]){}$_30t(i,G,__,e,l:Boolean ;_:XG){}$4d_4_4(){}Constructor (){Var _:String ;Break ;{Continue ;True .b__D_._8.__();} }}''',
                '''Class,_,:,Z8v,{,Destructor,(,),{,Break,;,Var,B,,,_,,,i,,,p,,,_,:,d,;,Continue,;,Continue,;,},$YO_,(,a_ju2,,,_,,,_,:,Array,[,Int,,,0b1011100,],),{,},$_30t,(,i,,,G,,,__,,,e,,,l,:,Boolean,;,_,:,XG,),{,},$4d_4_4,(,),{,},Constructor,(,),{,Var,_,:,String,;,Break,;,{,Continue,;,True,.,b__D_,.,_8,.,__,(,),;,},},},<EOF>''',
                101
            )
        )

    def test_473(self):
        self.assertTrue(
            TestLexer.test(
                '''Class f8{}Class _:_{$r_(_b:z_;v9,v__:Array [Array [Array [Array [Int ,5_1],0x30],0b111111],0101];h,DU,IE___57:Int ){Var q00_qc,B_:Int ;} }''',
                '''Class,f8,{,},Class,_,:,_,{,$r_,(,_b,:,z_,;,v9,,,v__,:,Array,[,Array,[,Array,[,Array,[,Int,,,51,],,,0x30,],,,0b111111,],,,0101,],;,h,,,DU,,,IE___57,:,Int,),{,Var,q00_qc,,,B_,:,Int,;,},},<EOF>''',
                101
            )
        )

    def test_474(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b0m6__{Constructor (_aC2,_86,y_,f,G:String ;_6:Array [Float ,52];_,P,A,YP3,_,_,H,Z:Array [Array [String ,0B1001],0B1001]){Continue ;Return ;} }''',
                '''Class,b0m6__,{,Constructor,(,_aC2,,,_86,,,y_,,,f,,,G,:,String,;,_6,:,Array,[,Float,,,52,],;,_,,,P,,,A,,,YP3,,,_,,,_,,,H,,,Z,:,Array,[,Array,[,String,,,0B1001,],,,0B1001,],),{,Continue,;,Return,;,},},<EOF>''',
                101
            )
        )

    def test_475(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_4B{Val $_y:Array [Int ,20_18];Val $_B:_1;}Class _{}Class S:__{Constructor (J,O:Array [Array [Array [Array [String ,0b1011010],72],0x27],8];_,_,fe6:j;_,x,_W:Array [Array [Array [Float ,51],0B11],0B111100]){Return ;} }Class R:_{}''',
                '''Class,_,:,_4B,{,Val,$_y,:,Array,[,Int,,,2018,],;,Val,$_B,:,_1,;,},Class,_,{,},Class,S,:,__,{,Constructor,(,J,,,O,:,Array,[,Array,[,Array,[,Array,[,String,,,0b1011010,],,,72,],,,0x27,],,,8,],;,_,,,_,,,fe6,:,j,;,_,,,x,,,_W,:,Array,[,Array,[,Array,[,Float,,,51,],,,0B11,],,,0B111100,],),{,Return,;,},},Class,R,:,_,{,},<EOF>''',
                101
            )
        )

    def test_476(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___{}Class v3RL{Val $G,$614:Array [Array [Array [Array [Array [Array [Array [Boolean ,0102],68],68],0XC_1],0x8],68],04];Constructor (__:Boolean ;_:Array [String ,68]){} }Class _:__{Val G_:O_;Destructor (){} }Class _m:_{}''',
                '''Class,___,{,},Class,v3RL,{,Val,$G,,,$614,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0102,],,,68,],,,68,],,,0XC1,],,,0x8,],,,68,],,,04,],;,Constructor,(,__,:,Boolean,;,_,:,Array,[,String,,,68,],),{,},},Class,_,:,__,{,Val,G_,:,O_,;,Destructor,(,),{,},},Class,_m,:,_,{,},<EOF>''',
                101
            )
        )

    def test_477(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m_{}Class Hhi{Var _,_I,_q:u;Val __,Z,$_:Array [Int ,0X6A];}Class I1{Constructor (s2_7:_xRy){Continue ;}Destructor (){} }''',
                '''Class,m_,{,},Class,Hhi,{,Var,_,,,_I,,,_q,:,u,;,Val,__,,,Z,,,$_,:,Array,[,Int,,,0X6A,],;,},Class,I1,{,Constructor,(,s2_7,:,_xRy,),{,Continue,;,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_478(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __6:x{$05_2__(_9F,__237_0:Array [String ,7];__,_o:_;D:Array [Array [Int ,05],0X38]){}Constructor (E:V_9){} }Class _:PA{Var $S6:Int ;}''',
                '''Class,__6,:,x,{,$05_2__,(,_9F,,,__237_0,:,Array,[,String,,,7,],;,__,,,_o,:,_,;,D,:,Array,[,Array,[,Int,,,05,],,,0X38,],),{,},Constructor,(,E,:,V_9,),{,},},Class,_,:,PA,{,Var,$S6,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_479(self):
        self.assertTrue(
            TestLexer.test(
                '''Class v_8{Val $n_8,_,$_0:String ;Constructor (P,U,_:Float ;_:Array [Array [Array [Int ,060],0X12],48]){ {Z_::$0z5()._._();Break ;}Break ;} }''',
                '''Class,v_8,{,Val,$n_8,,,_,,,$_0,:,String,;,Constructor,(,P,,,U,,,_,:,Float,;,_,:,Array,[,Array,[,Array,[,Int,,,060,],,,0X12,],,,48,],),{,{,Z_,::,$0z5,(,),.,_,.,_,(,),;,Break,;,},Break,;,},},<EOF>''',
                101
            )
        )

    def test_480(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _16{Destructor (){} }Class _{Constructor (W1,_6o_d_:_1_5_o;y,jh:Array [Float ,0X2E]){}$_I_5_3(){Continue ;} }''',
                '''Class,_16,{,Destructor,(,),{,},},Class,_,{,Constructor,(,W1,,,_6o_d_,:,_1_5_o,;,y,,,jh,:,Array,[,Float,,,0X2E,],),{,},$_I_5_3,(,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_481(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q_:__{Var Z6R_,$3_Z_d,_,$_:_;Val $Xj_:Float ;Kd(){} }Class _7:n9TP_{}Class _5T_{Destructor (){Break ;Break ;Break ;{}Var I_r,_,qP:Array [String ,0x3A];Continue ;} }''',
                '''Class,q_,:,__,{,Var,Z6R_,,,$3_Z_d,,,_,,,$_,:,_,;,Val,$Xj_,:,Float,;,Kd,(,),{,},},Class,_7,:,n9TP_,{,},Class,_5T_,{,Destructor,(,),{,Break,;,Break,;,Break,;,{,},Var,I_r,,,_,,,qP,:,Array,[,String,,,0x3A,],;,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_482(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class W6:II{}Class i_{Constructor (k,N,_,_g,_o,_6u,___,_G,__,m:Array [Array [String ,2],0B11010]){ {Return ;} }}''',
                '''Class,_,{,},Class,W6,:,II,{,},Class,i_,{,Constructor,(,k,,,N,,,_,,,_g,,,_o,,,_6u,,,___,,,_G,,,__,,,m,:,Array,[,Array,[,String,,,2,],,,0B11010,],),{,{,Return,;,},},},<EOF>''',
                101
            )
        )

    def test_483(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y050:_{}Class n:_1{Val _978Y:Array [Array [Array [Array [Array [Array [Float ,0X27],0B1],0X3],032],0b10_10],0X27];Var $_3s,$_,w__:Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,06],0b11000],0B1011000],33],0b1],0x2_E9],33],0X27],0x63];}''',
                '''Class,y050,:,_,{,},Class,n,:,_1,{,Val,_978Y,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X27,],,,0B1,],,,0X3,],,,032,],,,0b1010,],,,0X27,],;,Var,$_3s,,,$_,,,w__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,06,],,,0b11000,],,,0B1011000,],,,33,],,,0b1,],,,0x2E9,],,,33,],,,0X27,],,,0x63,],;,},<EOF>''',
                101
            )
        )

    def test_484(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _i{Val $1,$M,x3:Array [Array [Array [Int ,0x4],0B100],0X7];$1__n__6__3(G___a_:Array [Array [String ,0B1010111],013]){}Var E,c:Array [Array [Boolean ,05],0x4_1_0_2_5_284];}''',
                '''Class,_i,{,Val,$1,,,$M,,,x3,:,Array,[,Array,[,Array,[,Int,,,0x4,],,,0B100,],,,0X7,],;,$1__n__6__3,(,G___a_,:,Array,[,Array,[,String,,,0B1010111,],,,013,],),{,},Var,E,,,c,:,Array,[,Array,[,Boolean,,,05,],,,0x41025284,],;,},<EOF>''',
                101
            )
        )

    def test_485(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Var _,$B4:d___0;}Class QXg_:_{}Class _712:__{Var $__,$4A3s,$h,S:Int ;Constructor (veY,wS:Boolean ){}Constructor (){} }Class j_h:a{}''',
                '''Class,_,:,_,{,Var,_,,,$B4,:,d___0,;,},Class,QXg_,:,_,{,},Class,_712,:,__,{,Var,$__,,,$4A3s,,,$h,,,S,:,Int,;,Constructor,(,veY,,,wS,:,Boolean,),{,},Constructor,(,),{,},},Class,j_h,:,a,{,},<EOF>''',
                101
            )
        )

    def test_486(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7:__{Val _,$2m_M:F3;}Class M3{Val $4:Array [Array [Float ,03],0B1010011];Constructor (JS:Array [Float ,0X334];__69,_,sB:Array [Array [Array [Float ,0x5_B],0b10_0],0X5_7]){} }''',
                '''Class,_7,:,__,{,Val,_,,,$2m_M,:,F3,;,},Class,M3,{,Val,$4,:,Array,[,Array,[,Float,,,03,],,,0B1010011,],;,Constructor,(,JS,:,Array,[,Float,,,0X334,],;,__69,,,_,,,sB,:,Array,[,Array,[,Array,[,Float,,,0x5B,],,,0b100,],,,0X57,],),{,},},<EOF>''',
                101
            )
        )

    def test_487(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:W{Var f:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,053],0B1],14_7],053],0b111101],1],02],29];Destructor (){} }Class O_:a8{}Class _{}''',
                '''Class,_,:,W,{,Var,f,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,053,],,,0B1,],,,147,],,,053,],,,0b111101,],,,1,],,,02,],,,29,],;,Destructor,(,),{,},},Class,O_,:,a8,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_488(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:wT26{Constructor (){} }Class _y2{Destructor (){} }Class K583{Var $W2,zx1Z:Vh;Constructor (q,r,_:Array [Array [Int ,0b11100],0143]){} }''',
                '''Class,_,:,wT26,{,Constructor,(,),{,},},Class,_y2,{,Destructor,(,),{,},},Class,K583,{,Var,$W2,,,zx1Z,:,Vh,;,Constructor,(,q,,,r,,,_,:,Array,[,Array,[,Int,,,0b11100,],,,0143,],),{,},},<EOF>''',
                101
            )
        )

    def test_489(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{_D(){}Val $K_,Y:_;Var _5q6:Float ;$1T(){Continue ;Val _,fe:j;} }Class Z2:x{Var __,H,$Y,_r5:h;Var $K_v:Array [Boolean ,0B1_11];}Class _:___{}Class F_{Constructor (B,g_,_L,_:Array [Array [Int ,064],100]){} }''',
                '''Class,_,{,_D,(,),{,},Val,$K_,,,Y,:,_,;,Var,_5q6,:,Float,;,$1T,(,),{,Continue,;,Val,_,,,fe,:,j,;,},},Class,Z2,:,x,{,Var,__,,,H,,,$Y,,,_r5,:,h,;,Var,$K_v,:,Array,[,Boolean,,,0B111,],;,},Class,_,:,___,{,},Class,F_,{,Constructor,(,B,,,g_,,,_L,,,_,:,Array,[,Array,[,Int,,,064,],,,100,],),{,},},<EOF>''',
                101
            )
        )

    def test_490(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Destructor (){Break ;}Destructor (){ {}Continue ;} }Class xL6{Var $J_:Array [Float ,7];$6(_:Array [Array [Array [Array [Float ,62],0x5E],0b1],1]){} }''',
                '''Class,_,{,Destructor,(,),{,Break,;,},Destructor,(,),{,{,},Continue,;,},},Class,xL6,{,Var,$J_,:,Array,[,Float,,,7,],;,$6,(,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,62,],,,0x5E,],,,0b1,],,,1,],),{,},},<EOF>''',
                101
            )
        )

    def test_491(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Z:o5qT{Var L:U;}Class _6{_(_:Int ;h:Boolean ;_:String ;ty_3:Int ;J:Boolean ;__:Array [Int ,0x56];_5:String ){} }''',
                '''Class,Z,:,o5qT,{,Var,L,:,U,;,},Class,_6,{,_,(,_,:,Int,;,h,:,Boolean,;,_,:,String,;,ty_3,:,Int,;,J,:,Boolean,;,__,:,Array,[,Int,,,0x56,],;,_5,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_492(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var $_,$_,$__00Xwo,$_,$m6_:Array [Array [Boolean ,050],0X5C];_(){}Val e9,vJ,$g49z,_,$5_,$8m,$742:_;}Class j{Val $_ge:I3_;Val $4H,$u2:_;}''',
                '''Class,_,{,Var,$_,,,$_,,,$__00Xwo,,,$_,,,$m6_,:,Array,[,Array,[,Boolean,,,050,],,,0X5C,],;,_,(,),{,},Val,e9,,,vJ,,,$g49z,,,_,,,$5_,,,$8m,,,$742,:,_,;,},Class,j,{,Val,$_ge,:,I3_,;,Val,$4H,,,$u2,:,_,;,},<EOF>''',
                101
            )
        )

    def test_493(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __386:X{Destructor (){F::$I6.w();Val _,_:String ;} }Class _:p{Destructor (){}Val $____,D3:Array [Array [Int ,0X15],03];}''',
                '''Class,__386,:,X,{,Destructor,(,),{,F,::,$I6,.,w,(,),;,Val,_,,,_,:,String,;,},},Class,_,:,p,{,Destructor,(,),{,},Val,$____,,,D3,:,Array,[,Array,[,Int,,,0X15,],,,03,],;,},<EOF>''',
                101
            )
        )

    def test_494(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val f_7_:String ;Constructor (_,O,C,yU4_m,_O_,ex,N8,B9,f78,q:Array [Array [Array [String ,050],0XF],045];zU:Array [Int ,0x4];__68,__Gs0:j){Continue ;}Var $_0_,$1_,_1517356,_:Array [Array [Boolean ,0XF],0b1];}''',
                '''Class,_,{,Val,f_7_,:,String,;,Constructor,(,_,,,O,,,C,,,yU4_m,,,_O_,,,ex,,,N8,,,B9,,,f78,,,q,:,Array,[,Array,[,Array,[,String,,,050,],,,0XF,],,,045,],;,zU,:,Array,[,Int,,,0x4,],;,__68,,,__Gs0,:,j,),{,Continue,;,},Var,$_0_,,,$1_,,,_1517356,,,_,:,Array,[,Array,[,Boolean,,,0XF,],,,0b1,],;,},<EOF>''',
                101
            )
        )

    def test_495(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (o2,_,_D,b,CB,V,_S,G:Int ;__,Q:Array [Array [Array [Array [Array [Float ,0140],05],0B10],0X4B],8];S,S62:String ){Continue ;}Val _:String ;_(){} }''',
                '''Class,_,{,Constructor,(,o2,,,_,,,_D,,,b,,,CB,,,V,,,_S,,,G,:,Int,;,__,,,Q,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0140,],,,05,],,,0B10,],,,0X4B,],,,8,],;,S,,,S62,:,String,),{,Continue,;,},Val,_,:,String,;,_,(,),{,},},<EOF>''',
                101
            )
        )

    def test_496(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _3:_{}Class _0{}Class o0{Var _,D91:w3;Var _:K;Val _z:Array [Boolean ,39];Val x,$RH,$_:Array [Array [Int ,050640_46],0x3];}''',
                '''Class,_3,:,_,{,},Class,_0,{,},Class,o0,{,Var,_,,,D91,:,w3,;,Var,_,:,K,;,Val,_z,:,Array,[,Boolean,,,39,],;,Val,x,,,$RH,,,$_,:,Array,[,Array,[,Int,,,05064046,],,,0x3,],;,},<EOF>''',
                101
            )
        )

    def test_497(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _W9Y5:_N{Constructor (__og__32_B,_879_:Array [Float ,67];_,M,__8m:String ;U_w,_:Array [Array [Array [Array [Array [Array [Int ,074_010_2],67],7],057],67],053]){} }''',
                '''Class,_W9Y5,:,_N,{,Constructor,(,__og__32_B,,,_879_,:,Array,[,Float,,,67,],;,_,,,M,,,__8m,:,String,;,U_w,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0740102,],,,67,],,,7,],,,057,],,,67,],,,053,],),{,},},<EOF>''',
                101
            )
        )

    def test_498(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val __,R:Array [Array [Array [String ,01276],0xC7_5F],0X30];}Class __:__{Destructor (){}Var _:Ht;Constructor (){} }''',
                '''Class,_,{,Val,__,,,R,:,Array,[,Array,[,Array,[,String,,,01276,],,,0xC75F,],,,0X30,],;,},Class,__,:,__,{,Destructor,(,),{,},Var,_,:,Ht,;,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_499(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y:_9{}Class k7{Val U_,_K__e,$9,G_:Array [String ,0x59];Constructor (T7_I,o_,__:Boolean ;hkG,z:Array [Int ,0xD_4_3_2_9_A_1B]){} }Class p{}Class w:__{}''',
                '''Class,y,:,_9,{,},Class,k7,{,Val,U_,,,_K__e,,,$9,,,G_,:,Array,[,String,,,0x59,],;,Constructor,(,T7_I,,,o_,,,__,:,Boolean,;,hkG,,,z,:,Array,[,Int,,,0xD4329A1B,],),{,},},Class,p,{,},Class,w,:,__,{,},<EOF>''',
                101
            )
        )

    def test_500(self):
        self.assertTrue(
            TestLexer.test(
                '''Class d:_Dq{Destructor (){}Constructor (l,_:Array [Array [Float ,0XA],0b1001110];r:Array [Boolean ,0X5];I___,_:_;__,j:Boolean ;_:Array [Array [Array [Float ,4],4],0X1]){} }''',
                '''Class,d,:,_Dq,{,Destructor,(,),{,},Constructor,(,l,,,_,:,Array,[,Array,[,Float,,,0XA,],,,0b1001110,],;,r,:,Array,[,Boolean,,,0X5,],;,I___,,,_,:,_,;,__,,,j,:,Boolean,;,_,:,Array,[,Array,[,Array,[,Float,,,4,],,,4,],,,0X1,],),{,},},<EOF>''',
                101
            )
        )

    def test_501(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _3:_4{_(){Val MC,o,_x,nY_78,oj2,m,B1_4__K:Int ;}Constructor (__,_:Int ;_:String ;f__,_,v:Boolean ){} }Class c:_{Var _,I7100Xpw_,$2E,$_,$_,_,$_U2:String ;}Class Z{}''',
                '''Class,_3,:,_4,{,_,(,),{,Val,MC,,,o,,,_x,,,nY_78,,,oj2,,,m,,,B1_4__K,:,Int,;,},Constructor,(,__,,,_,:,Int,;,_,:,String,;,f__,,,_,,,v,:,Boolean,),{,},},Class,c,:,_,{,Var,_,,,I7100Xpw_,,,$2E,,,$_,,,$_,,,_,,,$_U2,:,String,;,},Class,Z,{,},<EOF>''',
                101
            )
        )

    def test_502(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class ep:__{Destructor (){} }Class _:__{Val _8__:Array [Boolean ,030];Var $v,__G_:Float ;}Class B:cH{}Class x41s:_9{}''',
                '''Class,_,{,},Class,ep,:,__,{,Destructor,(,),{,},},Class,_,:,__,{,Val,_8__,:,Array,[,Boolean,,,030,],;,Var,$v,,,__G_,:,Float,;,},Class,B,:,cH,{,},Class,x41s,:,_9,{,},<EOF>''',
                101
            )
        )

    def test_503(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w{Constructor (_yI,_:String ;_:Boolean ){}Val _53,j,$pu_2:Array [Int ,9];Constructor (k,_8aW5,p_:_){} }Class S{Var _:Array [Float ,0xD];}''',
                '''Class,w,{,Constructor,(,_yI,,,_,:,String,;,_,:,Boolean,),{,},Val,_53,,,j,,,$pu_2,:,Array,[,Int,,,9,],;,Constructor,(,k,,,_8aW5,,,p_,:,_,),{,},},Class,S,{,Var,_,:,Array,[,Float,,,0xD,],;,},<EOF>''',
                101
            )
        )

    def test_504(self):
        self.assertTrue(
            TestLexer.test(
                '''Class IzBrD9{Var a9,$m:Array [Array [Array [Array [Array [Array [Int ,16],0b110010],0x11],8],0B111],0x11];Constructor (){}Val $8,_:__;}''',
                '''Class,IzBrD9,{,Var,a9,,,$m,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,16,],,,0b110010,],,,0x11,],,,8,],,,0B111,],,,0x11,],;,Constructor,(,),{,},Val,$8,,,_,:,__,;,},<EOF>''',
                101
            )
        )

    def test_505(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_9_{}Class _w:g_D{Var $_:Array [Array [Array [Array [Boolean ,0X8F],012],02_1],0b1];}Class _{Constructor (){} }Class o:_5g{}''',
                '''Class,_,:,_9_,{,},Class,_w,:,g_D,{,Var,$_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X8F,],,,012,],,,021,],,,0b1,],;,},Class,_,{,Constructor,(,),{,},},Class,o,:,_5g,{,},<EOF>''',
                101
            )
        )

    def test_506(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class E{O_8B6s_(_k8x_4P:Int ;G1,y:Array [Array [Array [Array [Array [Float ,91],0x5E],7],01_1],0X7_F]){}Var $__,In :Array [String ,0135];}Class __h{}''',
                '''Class,_,{,},Class,E,{,O_8B6s_,(,_k8x_4P,:,Int,;,G1,,,y,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,91,],,,0x5E,],,,7,],,,011,],,,0X7F,],),{,},Var,$__,,,In,:,Array,[,String,,,0135,],;,},Class,__h,{,},<EOF>''',
                101
            )
        )

    def test_507(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _1:c_b__{Constructor (o_,_n:String ;_:_dH){} }Class _{}Class DP:vW{$7B(){} }Class _2{Constructor (G6_4l__0R1:Int ){}Destructor (){} }''',
                '''Class,_1,:,c_b__,{,Constructor,(,o_,,,_n,:,String,;,_,:,_dH,),{,},},Class,_,{,},Class,DP,:,vW,{,$7B,(,),{,},},Class,_2,{,Constructor,(,G6_4l__0R1,:,Int,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_508(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:J{Constructor (___,J_,__d,_V:Array [Array [String ,034],0X3B]){} }Class _:_{Constructor (E:_;_6K,w_n:_;_d___,E_,o5A,_6:Array [Float ,1_3]){}Constructor (q,_:_8_I;_,w5:Array [Float ,045];X:Array [Array [Int ,0b111101],88];_:_){Continue ;} }''',
                '''Class,_,:,J,{,Constructor,(,___,,,J_,,,__d,,,_V,:,Array,[,Array,[,String,,,034,],,,0X3B,],),{,},},Class,_,:,_,{,Constructor,(,E,:,_,;,_6K,,,w_n,:,_,;,_d___,,,E_,,,o5A,,,_6,:,Array,[,Float,,,13,],),{,},Constructor,(,q,,,_,:,_8_I,;,_,,,w5,:,Array,[,Float,,,045,],;,X,:,Array,[,Array,[,Int,,,0b111101,],,,88,],;,_,:,_,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_509(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E1:_{Val $__1,_:_;Constructor (){}Val _,e_t,_:Array [Int ,07];}Class I:_z{Constructor (_,M2,_:_;h,_,W:Array [Array [String ,7],0B111011]){G_::$_0_._y()._.L.f();} }''',
                '''Class,E1,:,_,{,Val,$__1,,,_,:,_,;,Constructor,(,),{,},Val,_,,,e_t,,,_,:,Array,[,Int,,,07,],;,},Class,I,:,_z,{,Constructor,(,_,,,M2,,,_,:,_,;,h,,,_,,,W,:,Array,[,Array,[,String,,,7,],,,0B111011,],),{,G_,::,$_0_,.,_y,(,),.,_,.,L,.,f,(,),;,},},<EOF>''',
                101
            )
        )

    def test_510(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l{d(n,_3:Float ){}Var $4:Array [Boolean ,38];Val h1,$2:_;}Class _:e4{}Class G:_{V(){Return ;}Val $0:b4;Destructor (){} }Class _P:g6{}''',
                '''Class,l,{,d,(,n,,,_3,:,Float,),{,},Var,$4,:,Array,[,Boolean,,,38,],;,Val,h1,,,$2,:,_,;,},Class,_,:,e4,{,},Class,G,:,_,{,V,(,),{,Return,;,},Val,$0,:,b4,;,Destructor,(,),{,},},Class,_P,:,g6,{,},<EOF>''',
                101
            )
        )

    def test_511(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q_:v{Val _:Array [Array [Array [Array [Array [Float ,618_0],03],0b1],73],03_1];_1(_2P,m_,K_:Boolean ){} }Class M:_uHSp{}Class Q_4:_{Constructor (){} }''',
                '''Class,q_,:,v,{,Val,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,6180,],,,03,],,,0b1,],,,73,],,,031,],;,_1,(,_2P,,,m_,,,K_,:,Boolean,),{,},},Class,M,:,_uHSp,{,},Class,Q_4,:,_,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_512(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l4__9_:_1{Destructor (){}Val $6:Array [Array [Array [Float ,0xE],04_3_1_5_702],0x28];}Class PG3:__4{}Class _K8{}''',
                '''Class,l4__9_,:,_1,{,Destructor,(,),{,},Val,$6,:,Array,[,Array,[,Array,[,Float,,,0xE,],,,04315702,],,,0x28,],;,},Class,PG3,:,__4,{,},Class,_K8,{,},<EOF>''',
                101
            )
        )

    def test_513(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7_:Z{Var Z,D:Array [Array [Array [Array [Boolean ,0X36],0b111000],3],53];}Class Z__4_{}Class GF3_:__So{}Class H{}Class _:_{}''',
                '''Class,_7_,:,Z,{,Var,Z,,,D,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X36,],,,0b111000,],,,3,],,,53,],;,},Class,Z__4_,{,},Class,GF3_,:,__So,{,},Class,H,{,},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_514(self):
        self.assertTrue(
            TestLexer.test(
                '''Class PC06:_u{Destructor (){}Constructor (_B_:Array [Array [Array [Float ,0B100101],0113],0113];K,_,_75,c:Array [Int ,0113]){Continue ;}Constructor (k,___30_,N__,i9_:String ;__zWW,f:Int ){}hF5(){Var _0,g,_8p:O;Break ;} }Class _3:A9_x{Constructor (_,HF:Array [Array [Float ,0b1_0],0b11011];_2Q:Boolean ;_0n6,_1_:tv;_,v,q6:_mFV_K){} }''',
                '''Class,PC06,:,_u,{,Destructor,(,),{,},Constructor,(,_B_,:,Array,[,Array,[,Array,[,Float,,,0B100101,],,,0113,],,,0113,],;,K,,,_,,,_75,,,c,:,Array,[,Int,,,0113,],),{,Continue,;,},Constructor,(,k,,,___30_,,,N__,,,i9_,:,String,;,__zWW,,,f,:,Int,),{,},hF5,(,),{,Var,_0,,,g,,,_8p,:,O,;,Break,;,},},Class,_3,:,A9_x,{,Constructor,(,_,,,HF,:,Array,[,Array,[,Float,,,0b10,],,,0b11011,],;,_2Q,:,Boolean,;,_0n6,,,_1_,:,tv,;,_,,,v,,,q6,:,_mFV_K,),{,},},<EOF>''',
                101
            )
        )

    def test_515(self):
        self.assertTrue(
            TestLexer.test(
                '''Class B96_6:_D{Constructor (_:Array [Array [Float ,0B1],0X56];U,_,_,_:t;_0_:Int ;_4,_,b,__:Array [Array [Int ,43],05]){} }''',
                '''Class,B96_6,:,_D,{,Constructor,(,_,:,Array,[,Array,[,Float,,,0B1,],,,0X56,],;,U,,,_,,,_,,,_,:,t,;,_0_,:,Int,;,_4,,,_,,,b,,,__,:,Array,[,Array,[,Int,,,43,],,,05,],),{,},},<EOF>''',
                101
            )
        )

    def test_516(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J{c(_4,Z:L_g;_:o){Continue ;Return ;}Val $2,E:Array [Array [Boolean ,1],57];Constructor (s_1Sw:Boolean ;M,Z_W1_D,__,_:Array [Float ,0X33]){Break ;} }''',
                '''Class,J,{,c,(,_4,,,Z,:,L_g,;,_,:,o,),{,Continue,;,Return,;,},Val,$2,,,E,:,Array,[,Array,[,Boolean,,,1,],,,57,],;,Constructor,(,s_1Sw,:,Boolean,;,M,,,Z_W1_D,,,__,,,_,:,Array,[,Float,,,0X33,],),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_517(self):
        self.assertTrue(
            TestLexer.test(
                '''Class u4{Val M,_,$X_2,$7,_G:Array [String ,0b11];a7(){} }Class _d:_{Var _,$c,DP6,lY,_,$_:Array [Array [Int ,05],0B110111];}Class y:s_t{}''',
                '''Class,u4,{,Val,M,,,_,,,$X_2,,,$7,,,_G,:,Array,[,String,,,0b11,],;,a7,(,),{,},},Class,_d,:,_,{,Var,_,,,$c,,,DP6,,,lY,,,_,,,$_,:,Array,[,Array,[,Int,,,05,],,,0B110111,],;,},Class,y,:,s_t,{,},<EOF>''',
                101
            )
        )

    def test_518(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:L_fw7___{Destructor (){}Destructor (){} }Class _:X1{Val e8:_;Val $v2,$96,c_8__,$lC:String ;Var $D:Array [Int ,044];}''',
                '''Class,_,:,L_fw7___,{,Destructor,(,),{,},Destructor,(,),{,},},Class,_,:,X1,{,Val,e8,:,_,;,Val,$v2,,,$96,,,c_8__,,,$lC,:,String,;,Var,$D,:,Array,[,Int,,,044,],;,},<EOF>''',
                101
            )
        )

    def test_519(self):
        self.assertTrue(
            TestLexer.test(
                '''Class r{$_o(){}Var $_:Array [Array [Array [String ,20],0b111],0x2E];}Class _OPg:_{$9_(__:Array [Array [Array [Array [Array [Array [Array [String ,0X4],0x2E],0100],0x2E],0B1001010],79_085_45],04]){}Val $s:Mm_y;}''',
                '''Class,r,{,$_o,(,),{,},Var,$_,:,Array,[,Array,[,Array,[,String,,,20,],,,0b111,],,,0x2E,],;,},Class,_OPg,:,_,{,$9_,(,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X4,],,,0x2E,],,,0100,],,,0x2E,],,,0B1001010,],,,7908545,],,,04,],),{,},Val,$s,:,Mm_y,;,},<EOF>''',
                101
            )
        )

    def test_520(self):
        self.assertTrue(
            TestLexer.test(
                '''Class a:_{Var $_,__zb,$3:Array [Array [Array [Array [Array [Array [String ,071],071],0b10001],05_4_34222],224],0X20];}''',
                '''Class,a,:,_,{,Var,$_,,,__zb,,,$3,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,071,],,,071,],,,0b10001,],,,05434222,],,,224,],,,0X20,],;,},<EOF>''',
                101
            )
        )

    def test_521(self):
        self.assertTrue(
            TestLexer.test(
                '''Class zI:S_P9{}Class G:_4{}Class W:IW{}Class _5K:_{Val s99,$E,$_,e3:String ;}Class _0:E_{}Class C2{Destructor (){} }''',
                '''Class,zI,:,S_P9,{,},Class,G,:,_4,{,},Class,W,:,IW,{,},Class,_5K,:,_,{,Val,s99,,,$E,,,$_,,,e3,:,String,;,},Class,_0,:,E_,{,},Class,C2,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_522(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class v___:__{Constructor (__39:Array [Float ,0X5_E];_:String ){}k(_:Int ){}Constructor (){} }Class _3S:S30_8{}Class KQ{}''',
                '''Class,_,{,},Class,v___,:,__,{,Constructor,(,__39,:,Array,[,Float,,,0X5E,],;,_,:,String,),{,},k,(,_,:,Int,),{,},Constructor,(,),{,},},Class,_3S,:,S30_8,{,},Class,KQ,{,},<EOF>''',
                101
            )
        )

    def test_523(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_A{$5_u(_,I,Z:W;fq:Array [Int ,0b1_100]){}Var n,$_3:Array [Array [Array [Float ,0x2E],032_7],0X11];G7__P(_,_,h9_,__:Int ){} }Class _d_{}''',
                '''Class,_,:,_A,{,$5_u,(,_,,,I,,,Z,:,W,;,fq,:,Array,[,Int,,,0b1100,],),{,},Var,n,,,$_3,:,Array,[,Array,[,Array,[,Float,,,0x2E,],,,0327,],,,0X11,],;,G7__P,(,_,,,_,,,h9_,,,__,:,Int,),{,},},Class,_d_,{,},<EOF>''',
                101
            )
        )

    def test_524(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var $_h,$V,$3_:_;Constructor (__H,_,o8,G_R:Array [Float ,0X4]){} }Class _X_e:n{Constructor (){} }Class _:_{}''',
                '''Class,_,{,Var,$_h,,,$V,,,$3_,:,_,;,Constructor,(,__H,,,_,,,o8,,,G_R,:,Array,[,Float,,,0X4,],),{,},},Class,_X_e,:,n,{,Constructor,(,),{,},},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_525(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _tT{}Class d:S{Val jn5:__I;}Class _1_:_{}Class K:F{Var t5_0_25:Array [Array [Array [Array [Array [Float ,0x4_B_4],99],0X44],0102],06_2];}Class __E:__{}''',
                '''Class,_tT,{,},Class,d,:,S,{,Val,jn5,:,__I,;,},Class,_1_,:,_,{,},Class,K,:,F,{,Var,t5_0_25,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x4B4,],,,99,],,,0X44,],,,0102,],,,062,],;,},Class,__E,:,__,{,},<EOF>''',
                101
            )
        )

    def test_526(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{t(N_,_2___:Array [String ,0B11000]){Break ;}Val Uz,_,o:Array [Array [String ,0x1B],0xA];}Class e:__{}Class _{}''',
                '''Class,__,{,t,(,N_,,,_2___,:,Array,[,String,,,0B11000,],),{,Break,;,},Val,Uz,,,_,,,o,:,Array,[,Array,[,String,,,0x1B,],,,0xA,],;,},Class,e,:,__,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_527(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_a{$w(_w,_K_1,_3:Array [Array [Array [String ,0B1100000],0B1],0b101]){Continue ;}Val $5G:Array [Array [Array [Int ,0B1_0_10],0X11],0X11];Var z5q,x:Aed;Destructor (){} }''',
                '''Class,_,:,_a,{,$w,(,_w,,,_K_1,,,_3,:,Array,[,Array,[,Array,[,String,,,0B1100000,],,,0B1,],,,0b101,],),{,Continue,;,},Val,$5G,:,Array,[,Array,[,Array,[,Int,,,0B1010,],,,0X11,],,,0X11,],;,Var,z5q,,,x,:,Aed,;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_528(self):
        self.assertTrue(
            TestLexer.test(
                '''Class i{}Class t{}Class _:__{}Class R2{_(w_:Array [Array [Array [Int ,0x18],92],5]){Continue ;}Destructor (){}Val j:Int ;Val $D,$n:Boolean ;Var m1:_;}''',
                '''Class,i,{,},Class,t,{,},Class,_,:,__,{,},Class,R2,{,_,(,w_,:,Array,[,Array,[,Array,[,Int,,,0x18,],,,92,],,,5,],),{,Continue,;,},Destructor,(,),{,},Val,j,:,Int,;,Val,$D,,,$n,:,Boolean,;,Var,m1,:,_,;,},<EOF>''',
                101
            )
        )

    def test_529(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7__R_24z:_6{Destructor (){}Constructor (R,t,_12_:Array [Array [String ,42],42];_,ZQ:Float ;_:Array [Int ,1_8];__:__){} }''',
                '''Class,_7__R_24z,:,_6,{,Destructor,(,),{,},Constructor,(,R,,,t,,,_12_,:,Array,[,Array,[,String,,,42,],,,42,],;,_,,,ZQ,:,Float,;,_,:,Array,[,Int,,,18,],;,__,:,__,),{,},},<EOF>''',
                101
            )
        )

    def test_530(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class R:_86{Constructor (L_pc,_:Array [Array [Array [String ,03],063],26]){Break ;Break ;}Val _:Array [Array [Array [Array [Array [Array [String ,0b1_1],0x5B],0X4],063],0b111001],44];Val $__:Array [Array [Array [Array [Array [Int ,0B11100],04],063],0X48],0XE_2];}''',
                '''Class,_,{,},Class,R,:,_86,{,Constructor,(,L_pc,,,_,:,Array,[,Array,[,Array,[,String,,,03,],,,063,],,,26,],),{,Break,;,Break,;,},Val,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b11,],,,0x5B,],,,0X4,],,,063,],,,0b111001,],,,44,],;,Val,$__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B11100,],,,04,],,,063,],,,0X48,],,,0XE2,],;,},<EOF>''',
                101
            )
        )

    def test_531(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _3:_{Var $__,$7,$v,_:_1;Constructor (_Y,_,V,_:a;Q,_INS,O:fl7){} }Class D_{}Class _{Val E:Array [Float ,0B1];Val c,j,$5_Z,$_:Array [Int ,0633];$0_(){Val T,G,_5,_:Array [Array [Array [Boolean ,0x36],44],44];} }Class J{Val $Z:Float ;}Class __:V_{}Class F_6:_{}''',
                '''Class,_3,:,_,{,Var,$__,,,$7,,,$v,,,_,:,_1,;,Constructor,(,_Y,,,_,,,V,,,_,:,a,;,Q,,,_INS,,,O,:,fl7,),{,},},Class,D_,{,},Class,_,{,Val,E,:,Array,[,Float,,,0B1,],;,Val,c,,,j,,,$5_Z,,,$_,:,Array,[,Int,,,0633,],;,$0_,(,),{,Val,T,,,G,,,_5,,,_,:,Array,[,Array,[,Array,[,Boolean,,,0x36,],,,44,],,,44,],;,},},Class,J,{,Val,$Z,:,Float,;,},Class,__,:,V_,{,},Class,F_6,:,_,{,},<EOF>''',
                101
            )
        )

    def test_532(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _bQ_:_{Constructor (c:Int ){}$_Xi6(_mz:Array [Int ,05];w_:Array [Array [String ,073],0B110];_:_){} }Class v_:_3_6F{}''',
                '''Class,_bQ_,:,_,{,Constructor,(,c,:,Int,),{,},$_Xi6,(,_mz,:,Array,[,Int,,,05,],;,w_,:,Array,[,Array,[,String,,,073,],,,0B110,],;,_,:,_,),{,},},Class,v_,:,_3_6F,{,},<EOF>''',
                101
            )
        )

    def test_533(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _v4_R:e_{$I_(_,h:Boolean ;K_,o,_:Array [Array [Array [Array [Array [Array [Array [String ,0X15],0X15],0b10],0X15],63],63],0XDD]){ {} }}Class __{}''',
                '''Class,_v4_R,:,e_,{,$I_,(,_,,,h,:,Boolean,;,K_,,,o,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X15,],,,0X15,],,,0b10,],,,0X15,],,,63,],,,63,],,,0XDD,],),{,{,},},},Class,__,{,},<EOF>''',
                101
            )
        )

    def test_534(self):
        self.assertTrue(
            TestLexer.test(
                '''Class OGp:ly{Var _,$f_,$I_:Int ;$X(){Break ;}Val _:_;Var _,$_F:Int ;}Class i:w_{Destructor (){}Val I8,R:Array [Float ,0xC];}''',
                '''Class,OGp,:,ly,{,Var,_,,,$f_,,,$I_,:,Int,;,$X,(,),{,Break,;,},Val,_,:,_,;,Var,_,,,$_F,:,Int,;,},Class,i,:,w_,{,Destructor,(,),{,},Val,I8,,,R,:,Array,[,Float,,,0xC,],;,},<EOF>''',
                101
            )
        )

    def test_535(self):
        self.assertTrue(
            TestLexer.test(
                '''Class R:_{}Class u{$u(_,_Y,_,_:Array [Array [Array [Array [Array [Int ,0XE],0XB_B],70],0XE],0x4D];_,F,N:__){} }Class _S{}''',
                '''Class,R,:,_,{,},Class,u,{,$u,(,_,,,_Y,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0XE,],,,0XBB,],,,70,],,,0XE,],,,0x4D,],;,_,,,F,,,N,:,__,),{,},},Class,_S,{,},<EOF>''',
                101
            )
        )

    def test_536(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{$2(r:_5;_K,b:Array [Array [Array [Array [Boolean ,0xC],067],3_98],0X2E];E,_2C,YM,qe_3:_;m,z:j;y:Array [Boolean ,0B1_0];i6S2,g:T65;__,z_,_:Array [String ,0x8];__ak__:z){} }''',
                '''Class,_,:,_,{,$2,(,r,:,_5,;,_K,,,b,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0xC,],,,067,],,,398,],,,0X2E,],;,E,,,_2C,,,YM,,,qe_3,:,_,;,m,,,z,:,j,;,y,:,Array,[,Boolean,,,0B10,],;,i6S2,,,g,:,T65,;,__,,,z_,,,_,:,Array,[,String,,,0x8,],;,__ak__,:,z,),{,},},<EOF>''',
                101
            )
        )

    def test_537(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:Xi{Val _,____3,j:W;}Class R4{Val $_,_:t;Val RC,$j,b,OX5_6_,k,$_2:Array [Array [Array [Array [Array [Float ,76],024],024],76],02];}Class W{x_F1__0__(){Break ;} }Class _:qy{}''',
                '''Class,_,:,Xi,{,Val,_,,,____3,,,j,:,W,;,},Class,R4,{,Val,$_,,,_,:,t,;,Val,RC,,,$j,,,b,,,OX5_6_,,,k,,,$_2,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,76,],,,024,],,,024,],,,76,],,,02,],;,},Class,W,{,x_F1__0__,(,),{,Break,;,},},Class,_,:,qy,{,},<EOF>''',
                101
            )
        )

    def test_538(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Z{Val $6_:___Z;p___(ot8_,d:Array [Boolean ,0B1001];_,e:Array [String ,0X44];__:String ;T_:Array [Array [Array [Boolean ,0X44],0B110],0B1_00];__9:Array [String ,0x8];_5_:Array [Array [Boolean ,0632],0B1_0]){} }''',
                '''Class,Z,{,Val,$6_,:,___Z,;,p___,(,ot8_,,,d,:,Array,[,Boolean,,,0B1001,],;,_,,,e,:,Array,[,String,,,0X44,],;,__,:,String,;,T_,:,Array,[,Array,[,Array,[,Boolean,,,0X44,],,,0B110,],,,0B100,],;,__9,:,Array,[,String,,,0x8,],;,_5_,:,Array,[,Array,[,Boolean,,,0632,],,,0B10,],),{,},},<EOF>''',
                101
            )
        )

    def test_539(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X:_S5{$_2IH(__:Array [Array [Boolean ,063],0b1_0];y,__1:Boolean ){Break ;}Destructor (){Break ;}Val $0R6_:O86;}''',
                '''Class,X,:,_S5,{,$_2IH,(,__,:,Array,[,Array,[,Boolean,,,063,],,,0b10,],;,y,,,__1,:,Boolean,),{,Break,;,},Destructor,(,),{,Break,;,},Val,$0R6_,:,O86,;,},<EOF>''',
                101
            )
        )

    def test_540(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2:_3{Var $6_5_,$_6_,$84_x:Array [Array [Array [Array [Array [Array [Int ,015],3],0b111010],0x43],9_76],92];}Class _:_i_7{}''',
                '''Class,_2,:,_3,{,Var,$6_5_,,,$_6_,,,$84_x,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,015,],,,3,],,,0b111010,],,,0x43,],,,976,],,,92,],;,},Class,_,:,_i_7,{,},<EOF>''',
                101
            )
        )

    def test_541(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J:b{}Class lp9:_p{Constructor (){}Val _PSVN_:S;}Class Y_:r{Var _X,$G3Ez:Array [Array [Int ,0100],0100];}Class _6m:_{Destructor (){Break ;{} }}Class __5:__4_{Val $309:Int ;}Class _{}Class _:L_Y210{}''',
                '''Class,J,:,b,{,},Class,lp9,:,_p,{,Constructor,(,),{,},Val,_PSVN_,:,S,;,},Class,Y_,:,r,{,Var,_X,,,$G3Ez,:,Array,[,Array,[,Int,,,0100,],,,0100,],;,},Class,_6m,:,_,{,Destructor,(,),{,Break,;,{,},},},Class,__5,:,__4_,{,Val,$309,:,Int,;,},Class,_,{,},Class,_,:,L_Y210,{,},<EOF>''',
                101
            )
        )

    def test_542(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C_{Var f3:_u1;}Class _{Var _8l:Array [Array [String ,051],0B1010010];}Class XB{}Class k:_{}Class K_3:_{}Class _:_4{$F_(){} }''',
                '''Class,C_,{,Var,f3,:,_u1,;,},Class,_,{,Var,_8l,:,Array,[,Array,[,String,,,051,],,,0B1010010,],;,},Class,XB,{,},Class,k,:,_,{,},Class,K_3,:,_,{,},Class,_,:,_4,{,$F_,(,),{,},},<EOF>''',
                101
            )
        )

    def test_543(self):
        self.assertTrue(
            TestLexer.test(
                '''Class j:x{}Class M{Destructor (){}Val KP:_;Val _6yj:Array [Float ,01];$X(){}Var $Q6f,$S:Int ;$9_(_:String ;_:Array [Float ,78];S1,_,_,_x_:Array [Array [Array [Boolean ,031],0b111011],2]){} }Class _7:_{}Class _{}''',
                '''Class,j,:,x,{,},Class,M,{,Destructor,(,),{,},Val,KP,:,_,;,Val,_6yj,:,Array,[,Float,,,01,],;,$X,(,),{,},Var,$Q6f,,,$S,:,Int,;,$9_,(,_,:,String,;,_,:,Array,[,Float,,,78,],;,S1,,,_,,,_,,,_x_,:,Array,[,Array,[,Array,[,Boolean,,,031,],,,0b111011,],,,2,],),{,},},Class,_7,:,_,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_544(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _28M{}Class _:h{$_(_,bH6:Int ){}D161_5DO6O54T(C_,_3:y;w_E8M:Float ;_c,_,_h,r_:Array [Float ,61];K_,_:Array [Int ,0x50]){} }''',
                '''Class,_28M,{,},Class,_,:,h,{,$_,(,_,,,bH6,:,Int,),{,},D161_5DO6O54T,(,C_,,,_3,:,y,;,w_E8M,:,Float,;,_c,,,_,,,_h,,,r_,:,Array,[,Float,,,61,],;,K_,,,_,:,Array,[,Int,,,0x50,],),{,},},<EOF>''',
                101
            )
        )

    def test_545(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _o5{}Class N_S_:_{Var OR:Array [Float ,0121];$_y_(r:Array [Array [Boolean ,0x6],0b1_1]){ {} }Destructor (){}Val _,$_,$2K,$__8:h0_;}Class _3{}''',
                '''Class,_o5,{,},Class,N_S_,:,_,{,Var,OR,:,Array,[,Float,,,0121,],;,$_y_,(,r,:,Array,[,Array,[,Boolean,,,0x6,],,,0b11,],),{,{,},},Destructor,(,),{,},Val,_,,,$_,,,$2K,,,$__8,:,h0_,;,},Class,_3,{,},<EOF>''',
                101
            )
        )

    def test_546(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2_6{}Class _:__{}Class __:s26{Val $bp9,$9j,i:pk_;_52(Y_3,_,k:_){Break ;}Constructor (_2p7_:String ;Jd___,_:Float ){Break ;} }''',
                '''Class,_2_6,{,},Class,_,:,__,{,},Class,__,:,s26,{,Val,$bp9,,,$9j,,,i,:,pk_,;,_52,(,Y_3,,,_,,,k,:,_,),{,Break,;,},Constructor,(,_2p7_,:,String,;,Jd___,,,_,:,Float,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_547(self):
        self.assertTrue(
            TestLexer.test(
                '''Class R:R{E7(d398_,i:Int ){Break ;{} }}Class u:__w__{Constructor (){}Var $B_:Array [Array [String ,05],0b100000];Destructor (){} }Class _9:_6{}Class _:X_{}Class __Dpk__i:P{}''',
                '''Class,R,:,R,{,E7,(,d398_,,,i,:,Int,),{,Break,;,{,},},},Class,u,:,__w__,{,Constructor,(,),{,},Var,$B_,:,Array,[,Array,[,String,,,05,],,,0b100000,],;,Destructor,(,),{,},},Class,_9,:,_6,{,},Class,_,:,X_,{,},Class,__Dpk__i,:,P,{,},<EOF>''',
                101
            )
        )

    def test_548(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_7_{__(){}$37(__:Array [Float ,06]){i4::$x.__();}Var _N,$_:Array [Array [String ,32],7];Destructor (){}Val k:_;}''',
                '''Class,_,:,_7_,{,__,(,),{,},$37,(,__,:,Array,[,Float,,,06,],),{,i4,::,$x,.,__,(,),;,},Var,_N,,,$_,:,Array,[,Array,[,String,,,32,],,,7,],;,Destructor,(,),{,},Val,k,:,_,;,},<EOF>''',
                101
            )
        )

    def test_549(self):
        self.assertTrue(
            TestLexer.test(
                '''Class BBr4_{Val n_f8___:Int ;Var z__:Array [String ,03];Val $6:_;}Class _6D:n_{Var _:_q;Constructor (_,D:_1;__P,_o_,_3:String ;Q6_,_6:Float ){} }Class d{}''',
                '''Class,BBr4_,{,Val,n_f8___,:,Int,;,Var,z__,:,Array,[,String,,,03,],;,Val,$6,:,_,;,},Class,_6D,:,n_,{,Var,_,:,_q,;,Constructor,(,_,,,D,:,_1,;,__P,,,_o_,,,_3,:,String,;,Q6_,,,_6,:,Float,),{,},},Class,d,{,},<EOF>''',
                101
            )
        )

    def test_550(self):
        self.assertTrue(
            TestLexer.test(
                '''Class YO{}Class x1{Var $ZE_,$_,K:Array [Array [Int ,0b111],0x5_3_1_C_F];Val k:Boolean ;}Class _:w_6{_4_(_4O7,_:Float ){Return ;} }''',
                '''Class,YO,{,},Class,x1,{,Var,$ZE_,,,$_,,,K,:,Array,[,Array,[,Int,,,0b111,],,,0x531CF,],;,Val,k,:,Boolean,;,},Class,_,:,w_6,{,_4_,(,_4O7,,,_,:,Float,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_551(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8{Var a_7,$SU,B2O_,$1,__P_:H;_(_c9_:Array [Array [Array [Boolean ,0X7_1],0x28],05_3];__,h,_7s:Float ){}Constructor (){} }''',
                '''Class,_8,{,Var,a_7,,,$SU,,,B2O_,,,$1,,,__P_,:,H,;,_,(,_c9_,:,Array,[,Array,[,Array,[,Boolean,,,0X71,],,,0x28,],,,053,],;,__,,,h,,,_7s,:,Float,),{,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_552(self):
        self.assertTrue(
            TestLexer.test(
                '''Class a_h{}Class s_:___9{Destructor (){} }Class _{$d(){} }Class g_I:_{_C(L:Array [Array [Int ,86],0b1]){}Constructor (_:Float ){ {}Continue ;} }''',
                '''Class,a_h,{,},Class,s_,:,___9,{,Destructor,(,),{,},},Class,_,{,$d,(,),{,},},Class,g_I,:,_,{,_C,(,L,:,Array,[,Array,[,Int,,,86,],,,0b1,],),{,},Constructor,(,_,:,Float,),{,{,},Continue,;,},},<EOF>''',
                101
            )
        )

    def test_553(self):
        self.assertTrue(
            TestLexer.test(
                '''Class oD:__D{}Class _2H{Constructor (_:j_;_,o,C,_,l:_){}$_(y_:Float ){}Q___3(kf,_,_:Float ){New __().Tv9();} }Class Wf_U_9__5_09{}Class _:A{Var C:P9;}''',
                '''Class,oD,:,__D,{,},Class,_2H,{,Constructor,(,_,:,j_,;,_,,,o,,,C,,,_,,,l,:,_,),{,},$_,(,y_,:,Float,),{,},Q___3,(,kf,,,_,,,_,:,Float,),{,New,__,(,),.,Tv9,(,),;,},},Class,Wf_U_9__5_09,{,},Class,_,:,A,{,Var,C,:,P9,;,},<EOF>''',
                101
            )
        )

    def test_554(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C{Var m__,$Np,m:Array [Array [Boolean ,0x12],0453_4_65];Destructor (){}Destructor (){}Var $08_:Float ;}Class _:_y_{}''',
                '''Class,C,{,Var,m__,,,$Np,,,m,:,Array,[,Array,[,Boolean,,,0x12,],,,0453465,],;,Destructor,(,),{,},Destructor,(,),{,},Var,$08_,:,Float,;,},Class,_,:,_y_,{,},<EOF>''',
                101
            )
        )

    def test_555(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _muD_{}Class _:_{_G(_38,s_,pk,_8,_:Array [Float ,0x3_43];_,_96_,S4_8:KR635G;e:R_;n:F){ {}Break ;}Var _:_b2_;}Class c_4cg0{}''',
                '''Class,_,{,},Class,_muD_,{,},Class,_,:,_,{,_G,(,_38,,,s_,,,pk,,,_8,,,_,:,Array,[,Float,,,0x343,],;,_,,,_96_,,,S4_8,:,KR635G,;,e,:,R_,;,n,:,F,),{,{,},Break,;,},Var,_,:,_b2_,;,},Class,c_4cg0,{,},<EOF>''',
                101
            )
        )

    def test_556(self):
        self.assertTrue(
            TestLexer.test(
                '''Class a:z{Var _,$5,$W9:n_0XF1;Val _,$OI,$9_ha,$_,$8,G,$__:Array [Float ,0b1];}Class as_:y8_{Constructor (__,_,_,_:_;a,_,Q6_t_,__:Float ;_Q_3,_8,K:Float ;ph,DI_:Boolean ;_,eaQ_7,z:Boolean ;pDS__0,_,F,_,LO_:Array [Array [Array [Boolean ,34],016],85]){} }Class ___0:l{}Class _:v{_P(){} }''',
                '''Class,a,:,z,{,Var,_,,,$5,,,$W9,:,n_0XF1,;,Val,_,,,$OI,,,$9_ha,,,$_,,,$8,,,G,,,$__,:,Array,[,Float,,,0b1,],;,},Class,as_,:,y8_,{,Constructor,(,__,,,_,,,_,,,_,:,_,;,a,,,_,,,Q6_t_,,,__,:,Float,;,_Q_3,,,_8,,,K,:,Float,;,ph,,,DI_,:,Boolean,;,_,,,eaQ_7,,,z,:,Boolean,;,pDS__0,,,_,,,F,,,_,,,LO_,:,Array,[,Array,[,Array,[,Boolean,,,34,],,,016,],,,85,],),{,},},Class,___0,:,l,{,},Class,_,:,v,{,_P,(,),{,},},<EOF>''',
                101
            )
        )

    def test_557(self):
        self.assertTrue(
            TestLexer.test(
                '''Class M{Constructor (_:Array [Array [Int ,0141],5_6]){Return ;}Val _:Int ;}Class _{}Class d_4_{Var _,$_7,d,$_:Array [Float ,0b111010];Val _,_,$a,$___6_2:Array [Float ,071_5_3];Val $t:_;}Class G:Q{}''',
                '''Class,M,{,Constructor,(,_,:,Array,[,Array,[,Int,,,0141,],,,56,],),{,Return,;,},Val,_,:,Int,;,},Class,_,{,},Class,d_4_,{,Var,_,,,$_7,,,d,,,$_,:,Array,[,Float,,,0b111010,],;,Val,_,,,_,,,$a,,,$___6_2,:,Array,[,Float,,,07153,],;,Val,$t,:,_,;,},Class,G,:,Q,{,},<EOF>''',
                101
            )
        )

    def test_558(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Var $_Mj:Array [String ,0B1_11];}Class vC3q:P21{Val __u_3,$5:Float ;Destructor (){}Val __n,F:Float ;}''',
                '''Class,_,:,_,{,Var,$_Mj,:,Array,[,String,,,0B111,],;,},Class,vC3q,:,P21,{,Val,__u_3,,,$5,:,Float,;,Destructor,(,),{,},Val,__n,,,F,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_559(self):
        self.assertTrue(
            TestLexer.test(
                '''Class a4:_3{}Class J{Destructor (){Continue ;Continue ;Return ;Var H___,R,B1,_:Boolean ;} }Class t:_I{}Class s_Pp:f{}''',
                '''Class,a4,:,_3,{,},Class,J,{,Destructor,(,),{,Continue,;,Continue,;,Return,;,Var,H___,,,R,,,B1,,,_,:,Boolean,;,},},Class,t,:,_I,{,},Class,s_Pp,:,f,{,},<EOF>''',
                101
            )
        )

    def test_560(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_g_{Val A,$__0,__:Array [Float ,0X2C];Constructor (_:String ;D_:Array [Boolean ,0x9_9]){}__(){ {} }Constructor (){} }''',
                '''Class,_,:,_g_,{,Val,A,,,$__0,,,__,:,Array,[,Float,,,0X2C,],;,Constructor,(,_,:,String,;,D_,:,Array,[,Boolean,,,0x99,],),{,},__,(,),{,{,},},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_561(self):
        self.assertTrue(
            TestLexer.test(
                '''Class sG6_5_sc{}Class aR:d37a_D{$_2(R,J_:Array [Float ,0XF_CF];_Nm,__,__:Float ){}$_(){}$7__(){_33::$_();} }''',
                '''Class,sG6_5_sc,{,},Class,aR,:,d37a_D,{,$_2,(,R,,,J_,:,Array,[,Float,,,0XFCF,],;,_Nm,,,__,,,__,:,Float,),{,},$_,(,),{,},$7__,(,),{,_33,::,$_,(,),;,},},<EOF>''',
                101
            )
        )

    def test_562(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{$7_(_2_:Array [String ,0b1_1];s385:D;_6_V:_){Return ;}Var __:Array [Float ,0b11];}Class g_{Val $_,_y,zA,w_____:Int ;}Class Fz{}''',
                '''Class,_,{,$7_,(,_2_,:,Array,[,String,,,0b11,],;,s385,:,D,;,_6_V,:,_,),{,Return,;,},Var,__,:,Array,[,Float,,,0b11,],;,},Class,g_,{,Val,$_,,,_y,,,zA,,,w_____,:,Int,;,},Class,Fz,{,},<EOF>''',
                101
            )
        )

    def test_563(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P:_Hf_1{Val $__A:Array [Array [Array [Array [Array [Array [String ,01],0b1],0xE1584],01],0x6],3_0];}Class J_:_{}''',
                '''Class,P,:,_Hf_1,{,Val,$__A,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,01,],,,0b1,],,,0xE1584,],,,01,],,,0x6,],,,30,],;,},Class,J_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_564(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o:__X{Val $1:_hsm;}Class _WY_:Z_89{Val _z:Array [Array [Array [Array [Float ,01_2_4],242_3],0x5D_2],0B1000111];Val _D_3:Array [Array [Float ,0B1000111],0X1E];}''',
                '''Class,o,:,__X,{,Val,$1,:,_hsm,;,},Class,_WY_,:,Z_89,{,Val,_z,:,Array,[,Array,[,Array,[,Array,[,Float,,,0124,],,,2423,],,,0x5D2,],,,0B1000111,],;,Val,_D_3,:,Array,[,Array,[,Float,,,0B1000111,],,,0X1E,],;,},<EOF>''',
                101
            )
        )

    def test_565(self):
        self.assertTrue(
            TestLexer.test(
                '''Class K4{Var $_W4_:Int ;Var RHnX:String ;Var $1,$t,$7:Array [Boolean ,0b100011];Destructor (){w::$_.io0();}Constructor (){ {} }}''',
                '''Class,K4,{,Var,$_W4_,:,Int,;,Var,RHnX,:,String,;,Var,$1,,,$t,,,$7,:,Array,[,Boolean,,,0b100011,],;,Destructor,(,),{,w,::,$_,.,io0,(,),;,},Constructor,(,),{,{,},},},<EOF>''',
                101
            )
        )

    def test_566(self):
        self.assertTrue(
            TestLexer.test(
                '''Class i:__d{$9t(_S3,__:y7;o,me:Vf){} }Class _:_{Var __,J_98:_7;Var _3:M0;$0_(){ {Break ;Break ;} }}Class k:_6_51d_{}''',
                '''Class,i,:,__d,{,$9t,(,_S3,,,__,:,y7,;,o,,,me,:,Vf,),{,},},Class,_,:,_,{,Var,__,,,J_98,:,_7,;,Var,_3,:,M0,;,$0_,(,),{,{,Break,;,Break,;,},},},Class,k,:,_6_51d_,{,},<EOF>''',
                101
            )
        )

    def test_567(self):
        self.assertTrue(
            TestLexer.test(
                '''Class xm{}Class __:_{}Class __4_{Destructor (){} }Class _{Val $U:Array [Boolean ,0b1001010];}Class _r5:V_Y_{}Class I1T:e{Val $7:_8E4;Constructor (E50:Int ){} }Class I{}''',
                '''Class,xm,{,},Class,__,:,_,{,},Class,__4_,{,Destructor,(,),{,},},Class,_,{,Val,$U,:,Array,[,Boolean,,,0b1001010,],;,},Class,_r5,:,V_Y_,{,},Class,I1T,:,e,{,Val,$7,:,_8E4,;,Constructor,(,E50,:,Int,),{,},},Class,I,{,},<EOF>''',
                101
            )
        )

    def test_568(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _b{Constructor (_:__;a,L_G,O__n_,_,v,S_:_;_,__:Array [Array [Int ,0b1111],0B110000];_,z1a,_g:S){}Var $_w,$_K_,_:String ;Val p,__,$f:Array [String ,21];}''',
                '''Class,_b,{,Constructor,(,_,:,__,;,a,,,L_G,,,O__n_,,,_,,,v,,,S_,:,_,;,_,,,__,:,Array,[,Array,[,Int,,,0b1111,],,,0B110000,],;,_,,,z1a,,,_g,:,S,),{,},Var,$_w,,,$_K_,,,_,:,String,;,Val,p,,,__,,,$f,:,Array,[,String,,,21,],;,},<EOF>''',
                101
            )
        )

    def test_569(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _c9496_5:__{Val $6j__G:String ;p(F,m_:Int ;_7_v4,m,q:Float ;x:Array [Array [Array [Array [String ,0B1],2],57],0b1011011]){} }Class k:__8i{}''',
                '''Class,_c9496_5,:,__,{,Val,$6j__G,:,String,;,p,(,F,,,m_,:,Int,;,_7_v4,,,m,,,q,:,Float,;,x,:,Array,[,Array,[,Array,[,Array,[,String,,,0B1,],,,2,],,,57,],,,0b1011011,],),{,},},Class,k,:,__8i,{,},<EOF>''',
                101
            )
        )

    def test_570(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:c{Val $X,sv:Array [Array [Boolean ,043],0x2];}Class __:__{_(){}Destructor (){} }Class h{$Q6_8(_,_zbq0:Array [Int ,0xDD_6B]){} }Class S2j4__g:__{}Class k:b{}''',
                '''Class,_,:,c,{,Val,$X,,,sv,:,Array,[,Array,[,Boolean,,,043,],,,0x2,],;,},Class,__,:,__,{,_,(,),{,},Destructor,(,),{,},},Class,h,{,$Q6_8,(,_,,,_zbq0,:,Array,[,Int,,,0xDD6B,],),{,},},Class,S2j4__g,:,__,{,},Class,k,:,b,{,},<EOF>''',
                101
            )
        )

    def test_571(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _Y:K_4_2{Constructor (b:Array [String ,91]){}Constructor (Is,_:_53){}Val $_:Array [Array [String ,76],0x4];}''',
                '''Class,_Y,:,K_4_2,{,Constructor,(,b,:,Array,[,String,,,91,],),{,},Constructor,(,Is,,,_,:,_53,),{,},Val,$_,:,Array,[,Array,[,String,,,76,],,,0x4,],;,},<EOF>''',
                101
            )
        )

    def test_572(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w:_{}Class D7:x{Destructor (){} }Class _:_p{Constructor (_6,_6:Array [Array [Array [Array [Array [Array [Float ,12],0B1_0_00_1],0115],12],0B10010],79]){} }''',
                '''Class,w,:,_,{,},Class,D7,:,x,{,Destructor,(,),{,},},Class,_,:,_p,{,Constructor,(,_6,,,_6,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,12,],,,0B10001,],,,0115,],,,12,],,,0B10010,],,,79,],),{,},},<EOF>''',
                101
            )
        )

    def test_573(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P:T{}Class _Z:_n{Var N:_;}Class fG2:_5{Val $D5,_:String ;}Class A:_{Constructor (_:Int ;_P:Float ){}Var $X5:Array [Boolean ,68];$78_(zQT_,_3:H;_b_W:_;_:_){} }Class Av:K{}''',
                '''Class,P,:,T,{,},Class,_Z,:,_n,{,Var,N,:,_,;,},Class,fG2,:,_5,{,Val,$D5,,,_,:,String,;,},Class,A,:,_,{,Constructor,(,_,:,Int,;,_P,:,Float,),{,},Var,$X5,:,Array,[,Boolean,,,68,],;,$78_,(,zQT_,,,_3,:,H,;,_b_W,:,_,;,_,:,_,),{,},},Class,Av,:,K,{,},<EOF>''',
                101
            )
        )

    def test_574(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (){}Var _H_4:String ;Destructor (){} }Class ES3{Val $U_,$k9,D_,$C:Array [Array [Array [Boolean ,0x6_9_3_8],10],0b11111];}''',
                '''Class,_,{,Constructor,(,),{,},Var,_H_4,:,String,;,Destructor,(,),{,},},Class,ES3,{,Val,$U_,,,$k9,,,D_,,,$C,:,Array,[,Array,[,Array,[,Boolean,,,0x6938,],,,10,],,,0b11111,],;,},<EOF>''',
                101
            )
        )

    def test_575(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:OP{}Class y:V4__{}Class y:St3o__{}Class _52Ad{Destructor (){}Destructor (){}Destructor (){}_0i(){} }Class _K6e:_8{}Class _7_:_f{}''',
                '''Class,_,:,OP,{,},Class,y,:,V4__,{,},Class,y,:,St3o__,{,},Class,_52Ad,{,Destructor,(,),{,},Destructor,(,),{,},Destructor,(,),{,},_0i,(,),{,},},Class,_K6e,:,_8,{,},Class,_7_,:,_f,{,},<EOF>''',
                101
            )
        )

    def test_576(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _oo{}Class O_{}Class Y_532s__:V35_7_6{}Class _CU_:_88_{}Class g__:_{}Class d6_{Destructor (){} }Class _:B7{}''',
                '''Class,_oo,{,},Class,O_,{,},Class,Y_532s__,:,V35_7_6,{,},Class,_CU_,:,_88_,{,},Class,g__,:,_,{,},Class,d6_,{,Destructor,(,),{,},},Class,_,:,B7,{,},<EOF>''',
                101
            )
        )

    def test_577(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9{}Class I4{}Class C:L{Var $66E,_:Array [Float ,0B10];$e__o(_:Array [Boolean ,0b1001]){} }Class n:_{Val $_5_04_j:Array [Array [Boolean ,06],0xF_F1_2];}''',
                '''Class,_9,{,},Class,I4,{,},Class,C,:,L,{,Var,$66E,,,_,:,Array,[,Float,,,0B10,],;,$e__o,(,_,:,Array,[,Boolean,,,0b1001,],),{,},},Class,n,:,_,{,Val,$_5_04_j,:,Array,[,Array,[,Boolean,,,06,],,,0xFF12,],;,},<EOF>''',
                101
            )
        )

    def test_578(self):
        self.assertTrue(
            TestLexer.test(
                '''Class a:___A3_0{Var $_5:String ;Var L,$_,$s:Int ;_(){}Val _4M,g_:Array [Array [Array [Boolean ,9],0x8],0X9];Var $8:Array [Boolean ,026];}Class _{}''',
                '''Class,a,:,___A3_0,{,Var,$_5,:,String,;,Var,L,,,$_,,,$s,:,Int,;,_,(,),{,},Val,_4M,,,g_,:,Array,[,Array,[,Array,[,Boolean,,,9,],,,0x8,],,,0X9,],;,Var,$8,:,Array,[,Boolean,,,026,],;,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_579(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___:P_{Var $4,$5,_:Boolean ;_(E3b:Float ;z3:Array [Boolean ,0B111];o_,_M,_:Array [Array [Array [Boolean ,4_2],01],0X58]){} }''',
                '''Class,___,:,P_,{,Var,$4,,,$5,,,_,:,Boolean,;,_,(,E3b,:,Float,;,z3,:,Array,[,Boolean,,,0B111,],;,o_,,,_M,,,_,:,Array,[,Array,[,Array,[,Boolean,,,42,],,,01,],,,0X58,],),{,},},<EOF>''',
                101
            )
        )

    def test_580(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ____:_Gb2{Constructor (_1,x,j,k_iV4:_;Xr,___3_4,Z_7,dA:Int ;s,C_,_,Zl_,X4P:Array [String ,0b1_0]){}Destructor (){} }Class QX_{}Class _f_:__f{}''',
                '''Class,____,:,_Gb2,{,Constructor,(,_1,,,x,,,j,,,k_iV4,:,_,;,Xr,,,___3_4,,,Z_7,,,dA,:,Int,;,s,,,C_,,,_,,,Zl_,,,X4P,:,Array,[,String,,,0b10,],),{,},Destructor,(,),{,},},Class,QX_,{,},Class,_f_,:,__f,{,},<EOF>''',
                101
            )
        )

    def test_581(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b_{}Class K{Var _u:Int ;Var $p7,e_i:Float ;}Class V:_x{Constructor (Q_:l2;_47__,Y:Array [Array [String ,0x16],02]){} }''',
                '''Class,b_,{,},Class,K,{,Var,_u,:,Int,;,Var,$p7,,,e_i,:,Float,;,},Class,V,:,_x,{,Constructor,(,Q_,:,l2,;,_47__,,,Y,:,Array,[,Array,[,String,,,0x16,],,,02,],),{,},},<EOF>''',
                101
            )
        )

    def test_582(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P:S{Var $fy:Array [Array [Array [Array [Int ,34],0x2D],072],05];Constructor (_,L:Boolean ){Val Z:_;} }Class j480:q5{Var o,b:E;}''',
                '''Class,P,:,S,{,Var,$fy,:,Array,[,Array,[,Array,[,Array,[,Int,,,34,],,,0x2D,],,,072,],,,05,],;,Constructor,(,_,,,L,:,Boolean,),{,Val,Z,:,_,;,},},Class,j480,:,q5,{,Var,o,,,b,:,E,;,},<EOF>''',
                101
            )
        )

    def test_583(self):
        self.assertTrue(
            TestLexer.test(
                '''Class j:J{}Class b3:J{Val __:o_;Val _,$_3,_K_,$_,_:Array [Array [String ,7],0b1];Constructor (_:Int ){} }Class _0:_{}''',
                '''Class,j,:,J,{,},Class,b3,:,J,{,Val,__,:,o_,;,Val,_,,,$_3,,,_K_,,,$_,,,_,:,Array,[,Array,[,String,,,7,],,,0b1,],;,Constructor,(,_,:,Int,),{,},},Class,_0,:,_,{,},<EOF>''',
                101
            )
        )

    def test_584(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t{}Class s{Destructor (){}Constructor (){s::$Tr();Break ;} }Class _U8:z_n0X5Qr6{Constructor (_,_:NU_7){} }Class __{}''',
                '''Class,t,{,},Class,s,{,Destructor,(,),{,},Constructor,(,),{,s,::,$Tr,(,),;,Break,;,},},Class,_U8,:,z_n0X5Qr6,{,Constructor,(,_,,,_,:,NU_7,),{,},},Class,__,{,},<EOF>''',
                101
            )
        )

    def test_585(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _z:_{Destructor (){}Val $1,$8_5_:Array [String ,0b11_0_1];}Class IN0u_{}Class W:_{}Class B_tF{}Class gTo:___{}Class f:_{}Class _{Constructor (J_:Float ;_:Boolean ){}Var $p,$0d1l_,$_,_,O,gw93,__:String ;}Class D:_Y{}''',
                '''Class,_z,:,_,{,Destructor,(,),{,},Val,$1,,,$8_5_,:,Array,[,String,,,0b1101,],;,},Class,IN0u_,{,},Class,W,:,_,{,},Class,B_tF,{,},Class,gTo,:,___,{,},Class,f,:,_,{,},Class,_,{,Constructor,(,J_,:,Float,;,_,:,Boolean,),{,},Var,$p,,,$0d1l_,,,$_,,,_,,,O,,,gw93,,,__,:,String,;,},Class,D,:,_Y,{,},<EOF>''',
                101
            )
        )

    def test_586(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{Var $_Jt:__2_;Destructor (){}$__(kD6Z:Int ;gw,N_663:Array [Array [Boolean ,0x2B],02];_:Array [Array [Array [Float ,066],0b1],0B110101];_6,_29_2,_:P_;__8N_4R97v1:Float ){} }Class t:__{}''',
                '''Class,__,{,Var,$_Jt,:,__2_,;,Destructor,(,),{,},$__,(,kD6Z,:,Int,;,gw,,,N_663,:,Array,[,Array,[,Boolean,,,0x2B,],,,02,],;,_,:,Array,[,Array,[,Array,[,Float,,,066,],,,0b1,],,,0B110101,],;,_6,,,_29_2,,,_,:,P_,;,__8N_4R97v1,:,Float,),{,},},Class,t,:,__,{,},<EOF>''',
                101
            )
        )

    def test_587(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Z:_{Var $3:String ;}Class _{Destructor (){}Val $_:Array [Float ,6];}Class E07{Constructor (n:String ){} }Class c_{}Class Q:_{Val k,$7:Int ;}''',
                '''Class,Z,:,_,{,Var,$3,:,String,;,},Class,_,{,Destructor,(,),{,},Val,$_,:,Array,[,Float,,,6,],;,},Class,E07,{,Constructor,(,n,:,String,),{,},},Class,c_,{,},Class,Q,:,_,{,Val,k,,,$7,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_588(self):
        self.assertTrue(
            TestLexer.test(
                '''Class VlA01{Constructor (){Val p,T,zs:i70;}Var $2:_27;Destructor (){}Constructor (_D2,_:Int ){} }Class f{$v_u6(){}Destructor (){} }''',
                '''Class,VlA01,{,Constructor,(,),{,Val,p,,,T,,,zs,:,i70,;,},Var,$2,:,_27,;,Destructor,(,),{,},Constructor,(,_D2,,,_,:,Int,),{,},},Class,f,{,$v_u6,(,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_589(self):
        self.assertTrue(
            TestLexer.test(
                '''Class O_:m8{}Class _8{}Class c8_{Var V_,$t9:Array [Array [String ,0x7],0x8];Constructor (_:Array [Boolean ,625]){} }''',
                '''Class,O_,:,m8,{,},Class,_8,{,},Class,c8_,{,Var,V_,,,$t9,:,Array,[,Array,[,String,,,0x7,],,,0x8,],;,Constructor,(,_,:,Array,[,Boolean,,,625,],),{,},},<EOF>''',
                101
            )
        )

    def test_590(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _5:i1{Val K1_0,k__b:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,0B1010011],0b1],65],0X7],0X5_7],2],0x55],0xF0],0X7],04_7],0b11110],0x4_C3];}Class _:_m_{}''',
                '''Class,_5,:,i1,{,Val,K1_0,,,k__b,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B1010011,],,,0b1,],,,65,],,,0X7,],,,0X57,],,,2,],,,0x55,],,,0xF0,],,,0X7,],,,047,],,,0b11110,],,,0x4C3,],;,},Class,_,:,_m_,{,},<EOF>''',
                101
            )
        )

    def test_591(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:_0i{$4(B,k,_F,_:_wF){Val G0V5:String ;Break ;Break ;}Var $__,_:Array [Array [Array [Int ,96],0B1],0B10_1_11];}''',
                '''Class,__,:,_0i,{,$4,(,B,,,k,,,_F,,,_,:,_wF,),{,Val,G0V5,:,String,;,Break,;,Break,;,},Var,$__,,,_,:,Array,[,Array,[,Array,[,Int,,,96,],,,0B1,],,,0B10111,],;,},<EOF>''',
                101
            )
        )

    def test_592(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _4{}Class C{Destructor (){ {} }Constructor (){_::$4_J._0();Var hlSK6,kP_4:Array [Array [String ,66],1_20_969];} }Class G{}''',
                '''Class,_4,{,},Class,C,{,Destructor,(,),{,{,},},Constructor,(,),{,_,::,$4_J,.,_0,(,),;,Var,hlSK6,,,kP_4,:,Array,[,Array,[,String,,,66,],,,120969,],;,},},Class,G,{,},<EOF>''',
                101
            )
        )

    def test_593(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0{Constructor (){} }Class q82_:F6{Val $1,_Kc___5J_,lb_075,$8:Boolean ;Var s2o_:String ;}Class i:_{}Class _{}Class C{}''',
                '''Class,_0,{,Constructor,(,),{,},},Class,q82_,:,F6,{,Val,$1,,,_Kc___5J_,,,lb_075,,,$8,:,Boolean,;,Var,s2o_,:,String,;,},Class,i,:,_,{,},Class,_,{,},Class,C,{,},<EOF>''',
                101
            )
        )

    def test_594(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_5_{$_(){}Constructor (Q72,s:_;_,_:Array [Array [Boolean ,041],034_0];_9:Array [String ,03_7_4]){} }Class D{}Class c{}Class _:G{_47cE(_9:Array [Float ,0B1]){} }''',
                '''Class,_,:,_5_,{,$_,(,),{,},Constructor,(,Q72,,,s,:,_,;,_,,,_,:,Array,[,Array,[,Boolean,,,041,],,,0340,],;,_9,:,Array,[,String,,,0374,],),{,},},Class,D,{,},Class,c,{,},Class,_,:,G,{,_47cE,(,_9,:,Array,[,Float,,,0B1,],),{,},},<EOF>''',
                101
            )
        )

    def test_595(self):
        self.assertTrue(
            TestLexer.test(
                '''Class j:_{}Class __{$7__(_,L3_,o,o5:_7k;_:Array [Array [Array [Array [Array [Array [String ,8],0X802_4],8],0x37],8],065];__:xu;_L,K:Array [Boolean ,8]){} }Class _:__A{}Class _m_{}''',
                '''Class,j,:,_,{,},Class,__,{,$7__,(,_,,,L3_,,,o,,,o5,:,_7k,;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,8,],,,0X8024,],,,8,],,,0x37,],,,8,],,,065,],;,__,:,xu,;,_L,,,K,:,Array,[,Boolean,,,8,],),{,},},Class,_,:,__A,{,},Class,_m_,{,},<EOF>''',
                101
            )
        )

    def test_596(self):
        self.assertTrue(
            TestLexer.test(
                '''Class R_:___H{Var j_y:c;Val $8XY__:Array [Int ,39];}Class n{__(_,d:A0____F6K_;_4,_0H_5k:String ;o,QM88:_){Return ;}Destructor (){ {Continue ;Return ;}Var UV:Int ;}Var Q_3:Array [String ,071];Constructor (){} }''',
                '''Class,R_,:,___H,{,Var,j_y,:,c,;,Val,$8XY__,:,Array,[,Int,,,39,],;,},Class,n,{,__,(,_,,,d,:,A0____F6K_,;,_4,,,_0H_5k,:,String,;,o,,,QM88,:,_,),{,Return,;,},Destructor,(,),{,{,Continue,;,Return,;,},Var,UV,:,Int,;,},Var,Q_3,:,Array,[,String,,,071,],;,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_597(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8__g_a:Y{}Class P_:vk_{BC4_(o,B,E5_7n_,ZN,_:Boolean ;_,_,_1,_q,__,_6:Array [Array [Boolean ,014],014]){} }''',
                '''Class,_8__g_a,:,Y,{,},Class,P_,:,vk_,{,BC4_,(,o,,,B,,,E5_7n_,,,ZN,,,_,:,Boolean,;,_,,,_,,,_1,,,_q,,,__,,,_6,:,Array,[,Array,[,Boolean,,,014,],,,014,],),{,},},<EOF>''',
                101
            )
        )

    def test_598(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var xn_:Boolean ;}Class _{i(y6,_36,_:Array [Array [Array [Boolean ,0B11],0B11],0X9]){}Var _,_WW:Int ;}Class a6q:s{}Class _3h_o{Var $vOb5:Array [Boolean ,01];}''',
                '''Class,_,{,Var,xn_,:,Boolean,;,},Class,_,{,i,(,y6,,,_36,,,_,:,Array,[,Array,[,Array,[,Boolean,,,0B11,],,,0B11,],,,0X9,],),{,},Var,_,,,_WW,:,Int,;,},Class,a6q,:,s,{,},Class,_3h_o,{,Var,$vOb5,:,Array,[,Boolean,,,01,],;,},<EOF>''',
                101
            )
        )

    def test_599(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_1{Constructor (__,o:Array [Array [Array [Float ,060],060],47];_,_4:Array [Int ,47]){}Val u,$CD:Array [Int ,07_71_04];}''',
                '''Class,_,:,_1,{,Constructor,(,__,,,o,:,Array,[,Array,[,Array,[,Float,,,060,],,,060,],,,47,],;,_,,,_4,:,Array,[,Int,,,47,],),{,},Val,u,,,$CD,:,Array,[,Int,,,077104,],;,},<EOF>''',
                101
            )
        )

    def test_600(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (w,C_,_8:Array [Array [Array [Array [Array [Boolean ,0X48],05_7],0B11_0_000_1],0X2B],0B1010010];_:Float ){Val _:Float ;}Destructor (){}Val $__:G;}''',
                '''Class,_,{,Constructor,(,w,,,C_,,,_8,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X48,],,,057,],,,0B1100001,],,,0X2B,],,,0B1010010,],;,_,:,Float,),{,Val,_,:,Float,;,},Destructor,(,),{,},Val,$__,:,G,;,},<EOF>''',
                101
            )
        )

    def test_601(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X:_{}Class c{}Class _{$O(Jp,zF_:_;G,_:_;T,IO__:LY;N:Array [String ,01];_,__,_x_8O:h;__,_,_,z,_,P3,d0:_;c,PM57:String ;_21,Q:Float ){} }''',
                '''Class,X,:,_,{,},Class,c,{,},Class,_,{,$O,(,Jp,,,zF_,:,_,;,G,,,_,:,_,;,T,,,IO__,:,LY,;,N,:,Array,[,String,,,01,],;,_,,,__,,,_x_8O,:,h,;,__,,,_,,,_,,,z,,,_,,,P3,,,d0,:,_,;,c,,,PM57,:,String,;,_21,,,Q,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_602(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _w{Val $E4z:Float ;b_8(_J,B:_;p:String ;_,_,p,O,_,_5c,W,_,_:T;_6_,_:Int ;s,_7_:Boolean ){} }Class _A4{}''',
                '''Class,_w,{,Val,$E4z,:,Float,;,b_8,(,_J,,,B,:,_,;,p,:,String,;,_,,,_,,,p,,,O,,,_,,,_5c,,,W,,,_,,,_,:,T,;,_6_,,,_,:,Int,;,s,,,_7_,:,Boolean,),{,},},Class,_A4,{,},<EOF>''',
                101
            )
        )

    def test_603(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:RV9{Var _,$3_4:Array [Array [String ,0b1_0_0],0b1010101];}Class _:A{L_E(){ {}Break ;Return ;}Constructor (){} }''',
                '''Class,_,:,RV9,{,Var,_,,,$3_4,:,Array,[,Array,[,String,,,0b100,],,,0b1010101,],;,},Class,_,:,A,{,L_E,(,),{,{,},Break,;,Return,;,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_604(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _1Fk_0r:d{_o0(_U3G,_56_5:Int ;__J34,_R,v,h:Array [Array [Array [String ,0x6],045],0x6];Wy_6X3,__3,S,_6q:Float ;V_KQ_,_,__k,N:String ){Return ;}$1(I4:Nj____S){}Val g,_:Array [Array [Array [Float ,045],0b1],045];Constructor (){Return ;Val __x_,L:__;} }''',
                '''Class,_1Fk_0r,:,d,{,_o0,(,_U3G,,,_56_5,:,Int,;,__J34,,,_R,,,v,,,h,:,Array,[,Array,[,Array,[,String,,,0x6,],,,045,],,,0x6,],;,Wy_6X3,,,__3,,,S,,,_6q,:,Float,;,V_KQ_,,,_,,,__k,,,N,:,String,),{,Return,;,},$1,(,I4,:,Nj____S,),{,},Val,g,,,_,:,Array,[,Array,[,Array,[,Float,,,045,],,,0b1,],,,045,],;,Constructor,(,),{,Return,;,Val,__x_,,,L,:,__,;,},},<EOF>''',
                101
            )
        )

    def test_605(self):
        self.assertTrue(
            TestLexer.test(
                '''Class e:_aC{Val $0:Array [Array [Array [Boolean ,05],9_81],05];Var $_5:Array [Array [Boolean ,0X1E],0xB];Val $W:Array [Array [Array [String ,0XF4_3],0b1011000],0X1E];}Class h:h{Destructor (){} }''',
                '''Class,e,:,_aC,{,Val,$0,:,Array,[,Array,[,Array,[,Boolean,,,05,],,,981,],,,05,],;,Var,$_5,:,Array,[,Array,[,Boolean,,,0X1E,],,,0xB,],;,Val,$W,:,Array,[,Array,[,Array,[,String,,,0XF43,],,,0b1011000,],,,0X1E,],;,},Class,h,:,h,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_606(self):
        self.assertTrue(
            TestLexer.test(
                '''Class z{Val e0,$_:Array [Array [Array [Array [Array [Array [Array [Array [Int ,0B100110],0b1],0b1011001],0x2C],0xF],2_14],0X40_B],0X3F];Val $41:Float ;Destructor (){O::$5_();} }''',
                '''Class,z,{,Val,e0,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B100110,],,,0b1,],,,0b1011001,],,,0x2C,],,,0xF,],,,214,],,,0X40B,],,,0X3F,],;,Val,$41,:,Float,;,Destructor,(,),{,O,::,$5_,(,),;,},},<EOF>''',
                101
            )
        )

    def test_607(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:Y5{Destructor (){}Destructor (){}Val l0,h_92:Array [Boolean ,0xC];Val _58_:Float ;}Class H7_3:_{}Class K2__{}''',
                '''Class,_,:,Y5,{,Destructor,(,),{,},Destructor,(,),{,},Val,l0,,,h_92,:,Array,[,Boolean,,,0xC,],;,Val,_58_,:,Float,;,},Class,H7_3,:,_,{,},Class,K2__,{,},<EOF>''',
                101
            )
        )

    def test_608(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class Y:h{_t(){}Constructor (X5,_qk,_,A,_v_S:Array [Boolean ,2];_,_40b:s){}Destructor (){}Var _:n1_;}''',
                '''Class,_,{,},Class,Y,:,h,{,_t,(,),{,},Constructor,(,X5,,,_qk,,,_,,,A,,,_v_S,:,Array,[,Boolean,,,2,],;,_,,,_40b,:,s,),{,},Destructor,(,),{,},Var,_,:,n1_,;,},<EOF>''',
                101
            )
        )

    def test_609(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Val $6,$_g__:Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,0X5D30],0b10011],0B100100],0x12],0B1],01],0b1],01_0_3],04];Var nR:_o_Y;}''',
                '''Class,_,:,_,{,Val,$6,,,$_g__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X5D30,],,,0b10011,],,,0B100100,],,,0x12,],,,0B1,],,,01,],,,0b1,],,,0103,],,,04,],;,Var,nR,:,_o_Y,;,},<EOF>''',
                101
            )
        )

    def test_610(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{W(_:Array [Float ,0x2E]){}Constructor (N_M8,_2:_;U:Array [Array [Array [Boolean ,0x2E],02],0x2E];S:Array [Boolean ,063];_m60_,a,S5:Array [Int ,0XB];_97H5_x_:Array [Array [Array [Array [Float ,0B1],0x3],01],1];d9,_:U;_:Array [Array [Float ,0x2E],26]){}Val $r,V,_:Int ;Val u:Array [Array [Array [Array [Array [String ,0b110011],0B11_1110],07],07_3],05_53];Var $E:_K_;Constructor (){} }''',
                '''Class,_,{,W,(,_,:,Array,[,Float,,,0x2E,],),{,},Constructor,(,N_M8,,,_2,:,_,;,U,:,Array,[,Array,[,Array,[,Boolean,,,0x2E,],,,02,],,,0x2E,],;,S,:,Array,[,Boolean,,,063,],;,_m60_,,,a,,,S5,:,Array,[,Int,,,0XB,],;,_97H5_x_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B1,],,,0x3,],,,01,],,,1,],;,d9,,,_,:,U,;,_,:,Array,[,Array,[,Float,,,0x2E,],,,26,],),{,},Val,$r,,,V,,,_,:,Int,;,Val,u,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b110011,],,,0B111110,],,,07,],,,073,],,,0553,],;,Var,$E,:,_K_,;,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_611(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{Val $1:Array [Array [Int ,1],0b101111];}Class X{$_(_:Array [Array [Float ,0x32_F],0B1_0]){ {Var W,j:Array [Array [Array [Array [Array [Int ,02_2],0B1],0B1010110],0b1],011];}Break ;} }Class Zt4{}''',
                '''Class,__,{,Val,$1,:,Array,[,Array,[,Int,,,1,],,,0b101111,],;,},Class,X,{,$_,(,_,:,Array,[,Array,[,Float,,,0x32F,],,,0B10,],),{,{,Var,W,,,j,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,022,],,,0B1,],,,0B1010110,],,,0b1,],,,011,],;,},Break,;,},},Class,Zt4,{,},<EOF>''',
                101
            )
        )

    def test_612(self):
        self.assertTrue(
            TestLexer.test(
                '''Class u:_v_{}Class XE:v__{Constructor (A:c){} }Class _:_{Var $_4_:Array [Array [String ,94],0x7];Val _,$Rg_:Int ;}''',
                '''Class,u,:,_v_,{,},Class,XE,:,v__,{,Constructor,(,A,:,c,),{,},},Class,_,:,_,{,Var,$_4_,:,Array,[,Array,[,String,,,94,],,,0x7,],;,Val,_,,,$Rg_,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_613(self):
        self.assertTrue(
            TestLexer.test(
                '''Class e:_{Var $c_:Array [Array [Float ,35],076];}Class _:_3___30_{Z(u,B,_9W_5,n,xl27__40,_:Boolean ;_U5,a,_:String ){}Destructor (){} }''',
                '''Class,e,:,_,{,Var,$c_,:,Array,[,Array,[,Float,,,35,],,,076,],;,},Class,_,:,_3___30_,{,Z,(,u,,,B,,,_9W_5,,,n,,,xl27__40,,,_,:,Boolean,;,_U5,,,a,,,_,:,String,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_614(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var $5,$2:Array [Boolean ,061];Val N_,$3,D__,$_6:o4;}Class _{}Class _:_{Constructor (B__:Array [String ,0xFA_E_9_9_2F_D_D_0_3]){} }''',
                '''Class,_,{,Var,$5,,,$2,:,Array,[,Boolean,,,061,],;,Val,N_,,,$3,,,D__,,,$_6,:,o4,;,},Class,_,{,},Class,_,:,_,{,Constructor,(,B__,:,Array,[,String,,,0xFAE992FDD03,],),{,},},<EOF>''',
                101
            )
        )

    def test_615(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Q_{Destructor (){}Constructor (SP,v:_1){}Val R_7,$o9_,$3:_;}Class _{}Class _:T_f{Var $3Q,$_6:B2;}Class _{}Class B:_{}''',
                '''Class,Q_,{,Destructor,(,),{,},Constructor,(,SP,,,v,:,_1,),{,},Val,R_7,,,$o9_,,,$3,:,_,;,},Class,_,{,},Class,_,:,T_f,{,Var,$3Q,,,$_6,:,B2,;,},Class,_,{,},Class,B,:,_,{,},<EOF>''',
                101
            )
        )

    def test_616(self):
        self.assertTrue(
            TestLexer.test(
                '''Class U:rs_{}Class s{}Class C_{$1(){}Val $_,$_:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0x50],0b1011110],6],0B1_00],0XC],0x50],0B1101],0B1];}Class _:_{Destructor (){}Destructor (){} }''',
                '''Class,U,:,rs_,{,},Class,s,{,},Class,C_,{,$1,(,),{,},Val,$_,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x50,],,,0b1011110,],,,6,],,,0B100,],,,0XC,],,,0x50,],,,0B1101,],,,0B1,],;,},Class,_,:,_,{,Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_617(self):
        self.assertTrue(
            TestLexer.test(
                '''Class j_c{Val $_Sh,$_l,$E,TV__:Array [Array [Array [Float ,41_30_0],0B111000],0x63];Var $_V:Array [Array [Float ,3],6];}''',
                '''Class,j_c,{,Val,$_Sh,,,$_l,,,$E,,,TV__,:,Array,[,Array,[,Array,[,Float,,,41300,],,,0B111000,],,,0x63,],;,Var,$_V,:,Array,[,Array,[,Float,,,3,],,,6,],;,},<EOF>''',
                101
            )
        )

    def test_618(self):
        self.assertTrue(
            TestLexer.test(
                '''Class u:_{}Class _{UP(){} }Class g6:kt{}Class t{}Class _:_{Constructor (__,_GY:__2_;_,_i4_6,l,_1:Array [Boolean ,72]){} }''',
                '''Class,u,:,_,{,},Class,_,{,UP,(,),{,},},Class,g6,:,kt,{,},Class,t,{,},Class,_,:,_,{,Constructor,(,__,,,_GY,:,__2_,;,_,,,_i4_6,,,l,,,_1,:,Array,[,Boolean,,,72,],),{,},},<EOF>''',
                101
            )
        )

    def test_619(self):
        self.assertTrue(
            TestLexer.test(
                '''Class c2Y:_I62{Constructor (_:Array [Array [Array [Array [Array [Boolean ,0B1000001],0b1_0],0141],7],16];_0__6,_,_,_:_){} }Class z:_1{}''',
                '''Class,c2Y,:,_I62,{,Constructor,(,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1000001,],,,0b10,],,,0141,],,,7,],,,16,],;,_0__6,,,_,,,_,,,_,:,_,),{,},},Class,z,:,_1,{,},<EOF>''',
                101
            )
        )

    def test_620(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E{WO(){}Var $8_d,$_k,_:_;_(_:String ){}Constructor (){} }Class _0H9m:_39{Constructor (_8:_){} }Class _s244:wV7_3{}''',
                '''Class,E,{,WO,(,),{,},Var,$8_d,,,$_k,,,_,:,_,;,_,(,_,:,String,),{,},Constructor,(,),{,},},Class,_0H9m,:,_39,{,Constructor,(,_8,:,_,),{,},},Class,_s244,:,wV7_3,{,},<EOF>''',
                101
            )
        )

    def test_621(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _fJ:x87t_4{}Class _2{}Class V__z_M{}Class a{}Class c_Q{Val o:Array [Array [Array [Int ,0b1],060_3],0X21];}''',
                '''Class,_fJ,:,x87t_4,{,},Class,_2,{,},Class,V__z_M,{,},Class,a,{,},Class,c_Q,{,Val,o,:,Array,[,Array,[,Array,[,Int,,,0b1,],,,0603,],,,0X21,],;,},<EOF>''',
                101
            )
        )

    def test_622(self):
        self.assertTrue(
            TestLexer.test(
                '''Class S{Destructor (){}Destructor (){}Val $6_,$iC_222_2_O9:Int ;Val $6u,$0,$39,$gC_4:Boolean ;}Class P_{$_9(){} }Class _:____H{}''',
                '''Class,S,{,Destructor,(,),{,},Destructor,(,),{,},Val,$6_,,,$iC_222_2_O9,:,Int,;,Val,$6u,,,$0,,,$39,,,$gC_4,:,Boolean,;,},Class,P_,{,$_9,(,),{,},},Class,_,:,____H,{,},<EOF>''',
                101
            )
        )

    def test_623(self):
        self.assertTrue(
            TestLexer.test(
                '''Class G:t{}Class __{Constructor (S_,n_:Array [Array [Float ,062],0X29];l0_,_:Array [String ,0b1_0];_:Array [Float ,0X34];P:__;B:Array [Array [Float ,062],0b110010]){} }''',
                '''Class,G,:,t,{,},Class,__,{,Constructor,(,S_,,,n_,:,Array,[,Array,[,Float,,,062,],,,0X29,],;,l0_,,,_,:,Array,[,String,,,0b10,],;,_,:,Array,[,Float,,,0X34,],;,P,:,__,;,B,:,Array,[,Array,[,Float,,,062,],,,0b110010,],),{,},},<EOF>''',
                101
            )
        )

    def test_624(self):
        self.assertTrue(
            TestLexer.test(
                '''Class S:rG{$3_3_6Q(y:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,041],8],0x6_2_4_F_B2],0x16],0B1],041],0X2E],0x23],5],02];A:Int ;_32,__07e,_M:String ){} }Class _{}''',
                '''Class,S,:,rG,{,$3_3_6Q,(,y,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,041,],,,8,],,,0x624FB2,],,,0x16,],,,0B1,],,,041,],,,0X2E,],,,0x23,],,,5,],,,02,],;,A,:,Int,;,_32,,,__07e,,,_M,:,String,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_625(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $_,____1,$_:Array [Array [Array [Array [String ,0135],0135],0x4_86_E_4],0B1];Val $48x__:Array [Float ,96];}''',
                '''Class,_,{,Val,$_,,,____1,,,$_,:,Array,[,Array,[,Array,[,Array,[,String,,,0135,],,,0135,],,,0x486E4,],,,0B1,],;,Val,$48x__,:,Array,[,Float,,,96,],;,},<EOF>''',
                101
            )
        )

    def test_626(self):
        self.assertTrue(
            TestLexer.test(
                '''Class v{Var _Gj,_9,m:c;_4__4(DH,_I_:Boolean ;_,_:Array [String ,1_8];n,_:Array [Array [Int ,0X4_FA1],0b11000];_:Float ){} }Class _7H5{}Class _{}Class x2__7Z{}''',
                '''Class,v,{,Var,_Gj,,,_9,,,m,:,c,;,_4__4,(,DH,,,_I_,:,Boolean,;,_,,,_,:,Array,[,String,,,18,],;,n,,,_,:,Array,[,Array,[,Int,,,0X4FA1,],,,0b11000,],;,_,:,Float,),{,},},Class,_7H5,{,},Class,_,{,},Class,x2__7Z,{,},<EOF>''',
                101
            )
        )

    def test_627(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m___:l{Constructor (){}Constructor (_:String ;F9t_08s:U;I_3:_;tG205_:Array [Array [Array [Int ,63],0x31],0X5];rx,R:Float ){}Constructor (D8,_,R0,a1igX,oq:Array [Array [Array [String ,0b110_0],0B1],2880]){}Destructor (){Var _F6,__,k,B2,__,_,_:_;} }''',
                '''Class,m___,:,l,{,Constructor,(,),{,},Constructor,(,_,:,String,;,F9t_08s,:,U,;,I_3,:,_,;,tG205_,:,Array,[,Array,[,Array,[,Int,,,63,],,,0x31,],,,0X5,],;,rx,,,R,:,Float,),{,},Constructor,(,D8,,,_,,,R0,,,a1igX,,,oq,:,Array,[,Array,[,Array,[,String,,,0b1100,],,,0B1,],,,2880,],),{,},Destructor,(,),{,Var,_F6,,,__,,,k,,,B2,,,__,,,_,,,_,:,_,;,},},<EOF>''',
                101
            )
        )

    def test_628(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _3{$8(U,N,l,_:Boolean ){Return ;}Z(_,__:Array [Array [String ,0xB_C],57]){} }Class K_2:_O{Destructor (){} }''',
                '''Class,_3,{,$8,(,U,,,N,,,l,,,_,:,Boolean,),{,Return,;,},Z,(,_,,,__,:,Array,[,Array,[,String,,,0xBC,],,,57,],),{,},},Class,K_2,:,_O,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_629(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:__l{Constructor (){}$_7_(_L,E_:_2;T:Boolean ;_:Boolean ;_7,b_,f49_7:Int ){}Constructor (){Val y:Boolean ;}__(){Val _:Array [Float ,0B1001101];}Constructor (c,Fi9,Y_,n,j:Ns;j,__:Array [Float ,0X34]){} }''',
                '''Class,_,:,__l,{,Constructor,(,),{,},$_7_,(,_L,,,E_,:,_2,;,T,:,Boolean,;,_,:,Boolean,;,_7,,,b_,,,f49_7,:,Int,),{,},Constructor,(,),{,Val,y,:,Boolean,;,},__,(,),{,Val,_,:,Array,[,Float,,,0B1001101,],;,},Constructor,(,c,,,Fi9,,,Y_,,,n,,,j,:,Ns,;,j,,,__,:,Array,[,Float,,,0X34,],),{,},},<EOF>''',
                101
            )
        )

    def test_630(self):
        self.assertTrue(
            TestLexer.test(
                '''Class G62:x_{}Class __N{Val $_,_:Int ;}Class a1:x76m071{$0z7_(M:Array [Array [String ,0B1100011],0b100010];I:Array [Array [Float ,98],9_0];_:_){} }''',
                '''Class,G62,:,x_,{,},Class,__N,{,Val,$_,,,_,:,Int,;,},Class,a1,:,x76m071,{,$0z7_,(,M,:,Array,[,Array,[,String,,,0B1100011,],,,0b100010,],;,I,:,Array,[,Array,[,Float,,,98,],,,90,],;,_,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_631(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _4:_{Destructor (){} }Class y:_{}Class F{Destructor (){Continue ;Continue ;Val h:kv86;} }Class _2_juM{}Class _:_0_{}Class X_1_{}Class ___lnL{Destructor (){} }Class k:_{}Class T08:b_{}''',
                '''Class,_4,:,_,{,Destructor,(,),{,},},Class,y,:,_,{,},Class,F,{,Destructor,(,),{,Continue,;,Continue,;,Val,h,:,kv86,;,},},Class,_2_juM,{,},Class,_,:,_0_,{,},Class,X_1_,{,},Class,___lnL,{,Destructor,(,),{,},},Class,k,:,_,{,},Class,T08,:,b_,{,},<EOF>''',
                101
            )
        )

    def test_632(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _6B:P{Destructor (){} }Class N{}Class _6:T{$VA__(_V,k:_;v,__:_rW_;b3:Int ;X,_,__u__,_:Array [Array [Int ,07],07]){Continue ;}Val $7:Boolean ;}''',
                '''Class,_6B,:,P,{,Destructor,(,),{,},},Class,N,{,},Class,_6,:,T,{,$VA__,(,_V,,,k,:,_,;,v,,,__,:,_rW_,;,b3,:,Int,;,X,,,_,,,__u__,,,_,:,Array,[,Array,[,Int,,,07,],,,07,],),{,Continue,;,},Val,$7,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_633(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _D:_Rn{Val F_,$_8:Array [Array [Array [Array [Boolean ,0B1_1],84],0B101],0x1B];Destructor (){Continue ;} }Class Y3{}Class P2:Lr9_H{}Class _:_{}''',
                '''Class,_D,:,_Rn,{,Val,F_,,,$_8,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B11,],,,84,],,,0B101,],,,0x1B,],;,Destructor,(,),{,Continue,;,},},Class,Y3,{,},Class,P2,:,Lr9_H,{,},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_634(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class w:n21{G2(_4:Array [Array [Array [Float ,0XA],06_0_54],014];_,_l__,U__,I:Array [Array [Float ,4_1_4],014];_0:Array [Array [Int ,49],02];y87:_){} }Class ydk9_5:_{}''',
                '''Class,_,{,},Class,w,:,n21,{,G2,(,_4,:,Array,[,Array,[,Array,[,Float,,,0XA,],,,06054,],,,014,],;,_,,,_l__,,,U__,,,I,:,Array,[,Array,[,Float,,,414,],,,014,],;,_0,:,Array,[,Array,[,Int,,,49,],,,02,],;,y87,:,_,),{,},},Class,ydk9_5,:,_,{,},<EOF>''',
                101
            )
        )

    def test_635(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _m{Var _,$5,$p,$2:Array [Array [Array [Boolean ,0121],0121],0X6_8_2];Var $g:Array [Float ,0b1];Val n,_,_:Array [Boolean ,0x64];Val $o:Float ;}''',
                '''Class,_m,{,Var,_,,,$5,,,$p,,,$2,:,Array,[,Array,[,Array,[,Boolean,,,0121,],,,0121,],,,0X682,],;,Var,$g,:,Array,[,Float,,,0b1,],;,Val,n,,,_,,,_,:,Array,[,Boolean,,,0x64,],;,Val,$o,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_636(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class DW:J1a{Destructor (){Break ;}Val D1C:Array [Array [Int ,0x4],07];$3(_,__,_2_,_:Array [Int ,0b100010];x_:Float ){New __()._8_1p9m.O();}Val FT:Array [Int ,0B100];}''',
                '''Class,__,{,},Class,DW,:,J1a,{,Destructor,(,),{,Break,;,},Val,D1C,:,Array,[,Array,[,Int,,,0x4,],,,07,],;,$3,(,_,,,__,,,_2_,,,_,:,Array,[,Int,,,0b100010,],;,x_,:,Float,),{,New,__,(,),.,_8_1p9m,.,O,(,),;,},Val,FT,:,Array,[,Int,,,0B100,],;,},<EOF>''',
                101
            )
        )

    def test_637(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{$1(){} }Class Z_{}Class _{$_(__9:Float ){}Val N:Int ;}Class _:m7_{}Class n{Destructor (){Continue ;}Var ___3_,QW:_f5;}''',
                '''Class,_,{,$1,(,),{,},},Class,Z_,{,},Class,_,{,$_,(,__9,:,Float,),{,},Val,N,:,Int,;,},Class,_,:,m7_,{,},Class,n,{,Destructor,(,),{,Continue,;,},Var,___3_,,,QW,:,_f5,;,},<EOF>''',
                101
            )
        )

    def test_638(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o{Destructor (){ {} }Constructor (){Val S4,C_,_:Array [Array [Array [Boolean ,03],0B1_01],05];Continue ;} }Class _6{}Class W5{Constructor (_:e_;rp,__:Boolean ){}Val $1:Boolean ;}''',
                '''Class,o,{,Destructor,(,),{,{,},},Constructor,(,),{,Val,S4,,,C_,,,_,:,Array,[,Array,[,Array,[,Boolean,,,03,],,,0B101,],,,05,],;,Continue,;,},},Class,_6,{,},Class,W5,{,Constructor,(,_,:,e_,;,rp,,,__,:,Boolean,),{,},Val,$1,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_639(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _V855:__F{Var $n6_9,$J:Array [Float ,0B1100000];Destructor (){} }Class f_l{Constructor (K_6,k2,_80:v){}Destructor (){} }''',
                '''Class,_V855,:,__F,{,Var,$n6_9,,,$J,:,Array,[,Float,,,0B1100000,],;,Destructor,(,),{,},},Class,f_l,{,Constructor,(,K_6,,,k2,,,_80,:,v,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_640(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g{Constructor (X6:b74){}z(__:Array [Array [Array [Boolean ,43],0b1011001],43];_:Array [String ,0X6];nD5_:_I_W_){}Destructor (){Return ;} }''',
                '''Class,g,{,Constructor,(,X6,:,b74,),{,},z,(,__,:,Array,[,Array,[,Array,[,Boolean,,,43,],,,0b1011001,],,,43,],;,_,:,Array,[,String,,,0X6,],;,nD5_,:,_I_W_,),{,},Destructor,(,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_641(self):
        self.assertTrue(
            TestLexer.test(
                '''Class up_{Constructor (G,S:Array [Array [Float ,0x9],0b1];__SM,y:Array [Array [Array [String ,0b1001011],014],1]){} }Class _:_{}Class __{}''',
                '''Class,up_,{,Constructor,(,G,,,S,:,Array,[,Array,[,Float,,,0x9,],,,0b1,],;,__SM,,,y,:,Array,[,Array,[,Array,[,String,,,0b1001011,],,,014,],,,1,],),{,},},Class,_,:,_,{,},Class,__,{,},<EOF>''',
                101
            )
        )

    def test_642(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Z{Var $8:Array [Boolean ,0XE];Val g8s_w,y:Boolean ;}Class _6_5:_{}Class _:_n7{}Class __5{}Class _0{}Class _:n{}''',
                '''Class,Z,{,Var,$8,:,Array,[,Boolean,,,0XE,],;,Val,g8s_w,,,y,:,Boolean,;,},Class,_6_5,:,_,{,},Class,_,:,_n7,{,},Class,__5,{,},Class,_0,{,},Class,_,:,n,{,},<EOF>''',
                101
            )
        )

    def test_643(self):
        self.assertTrue(
            TestLexer.test(
                '''Class om:_698{}Class q__:_0z83{}Class _:_{Var o,$_,__2:String ;$a7Y_(t:__Ej;X_,y8M:Int ){} }Class _{}Class W:_4D0{}Class _:_{}''',
                '''Class,om,:,_698,{,},Class,q__,:,_0z83,{,},Class,_,:,_,{,Var,o,,,$_,,,__2,:,String,;,$a7Y_,(,t,:,__Ej,;,X_,,,y8M,:,Int,),{,},},Class,_,{,},Class,W,:,_4D0,{,},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_644(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t9_c_:d4{}Class _9B:__9{$n_(__3DFU:Array [Array [String ,04_2_704],01_5]){}Constructor (X,_K:String ;__,z,Lu_H:Array [Int ,5];l:i;gX:Array [Boolean ,0B1];B_,_:Array [String ,025]){Break ;} }Class _:i8{}''',
                '''Class,t9_c_,:,d4,{,},Class,_9B,:,__9,{,$n_,(,__3DFU,:,Array,[,Array,[,String,,,042704,],,,015,],),{,},Constructor,(,X,,,_K,:,String,;,__,,,z,,,Lu_H,:,Array,[,Int,,,5,],;,l,:,i,;,gX,:,Array,[,Boolean,,,0B1,],;,B_,,,_,:,Array,[,String,,,025,],),{,Break,;,},},Class,_,:,i8,{,},<EOF>''',
                101
            )
        )

    def test_645(self):
        self.assertTrue(
            TestLexer.test(
                '''Class K:Z{Var $_1,cV,_:Array [Array [Float ,05],06];}Class __2659:_u{}Class _{r(){} }Class _:i7{Constructor (){ {Continue ;} }}''',
                '''Class,K,:,Z,{,Var,$_1,,,cV,,,_,:,Array,[,Array,[,Float,,,05,],,,06,],;,},Class,__2659,:,_u,{,},Class,_,{,r,(,),{,},},Class,_,:,i7,{,Constructor,(,),{,{,Continue,;,},},},<EOF>''',
                101
            )
        )

    def test_646(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __3{_6w(){ {Val D__:Float ;Val u,H,__,_,__I_:_;Break ;Break ;}Break ;Continue ;}Val xV,_0,$8:Array [String ,0xF_C_C];}''',
                '''Class,__3,{,_6w,(,),{,{,Val,D__,:,Float,;,Val,u,,,H,,,__,,,_,,,__I_,:,_,;,Break,;,Break,;,},Break,;,Continue,;,},Val,xV,,,_0,,,$8,:,Array,[,String,,,0xFCC,],;,},<EOF>''',
                101
            )
        )

    def test_647(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_sh8_9M8Y7__{$__DV(u,P,_,D8_:z;__,Q_,q_:Array [Array [Array [Array [Array [Boolean ,93],0XD_9],05],33_3],0B110_0];E9:_V_){} }Class _H_:_{Constructor (){} }''',
                '''Class,_,:,_sh8_9M8Y7__,{,$__DV,(,u,,,P,,,_,,,D8_,:,z,;,__,,,Q_,,,q_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,93,],,,0XD9,],,,05,],,,333,],,,0B1100,],;,E9,:,_V_,),{,},},Class,_H_,:,_,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_648(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var _tm:Float ;}Class _{}Class j{Destructor (){}Var $_,_xl:Float ;Var $3__M_O:Array [Array [Array [Array [Array [Array [String ,033],8],033],0B101000],0x882],0x1F];Var _7,A,_,X,$_L,$K,TT5_,_g,$66AU1G_,$0:_;}''',
                '''Class,_,{,Var,_tm,:,Float,;,},Class,_,{,},Class,j,{,Destructor,(,),{,},Var,$_,,,_xl,:,Float,;,Var,$3__M_O,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,033,],,,8,],,,033,],,,0B101000,],,,0x882,],,,0x1F,],;,Var,_7,,,A,,,_,,,X,,,$_L,,,$K,,,TT5_,,,_g,,,$66AU1G_,,,$0,:,_,;,},<EOF>''',
                101
            )
        )

    def test_649(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class W:_{}Class m4_:_f5{Destructor (){}Var $K:Array [Array [Array [Array [Boolean ,01],72],72],72];}Class D{}''',
                '''Class,_,{,},Class,W,:,_,{,},Class,m4_,:,_f5,{,Destructor,(,),{,},Var,$K,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,01,],,,72,],,,72,],,,72,],;,},Class,D,{,},<EOF>''',
                101
            )
        )

    def test_650(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t5:_{$2(n:B_){}Destructor (){Continue ;}Destructor (){}Var ___,H,$__:Boolean ;Var $_,$T_:Array [Boolean ,023_1];Destructor (){}Val q:_;}''',
                '''Class,t5,:,_,{,$2,(,n,:,B_,),{,},Destructor,(,),{,Continue,;,},Destructor,(,),{,},Var,___,,,H,,,$__,:,Boolean,;,Var,$_,,,$T_,:,Array,[,Boolean,,,0231,],;,Destructor,(,),{,},Val,q,:,_,;,},<EOF>''',
                101
            )
        )

    def test_651(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{___(_I:Array [Array [Array [Array [String ,0B1],0X34],0X34],0X34]){}Val __68:Array [Boolean ,0x1D];}Class r{}''',
                '''Class,_,:,_,{,___,(,_I,:,Array,[,Array,[,Array,[,Array,[,String,,,0B1,],,,0X34,],,,0X34,],,,0X34,],),{,},Val,__68,:,Array,[,Boolean,,,0x1D,],;,},Class,r,{,},<EOF>''',
                101
            )
        )

    def test_652(self):
        self.assertTrue(
            TestLexer.test(
                '''Class f__{}Class z:_{Destructor (){} }Class _{}Class _4V_:S6_4{Destructor (){}Constructor (){Val _9:BL5;}Constructor (){} }Class r{Val UO,$V,$yG,A,E_:Array [Int ,2_4];$_(VJ:F9){} }''',
                '''Class,f__,{,},Class,z,:,_,{,Destructor,(,),{,},},Class,_,{,},Class,_4V_,:,S6_4,{,Destructor,(,),{,},Constructor,(,),{,Val,_9,:,BL5,;,},Constructor,(,),{,},},Class,r,{,Val,UO,,,$V,,,$yG,,,A,,,E_,:,Array,[,Int,,,24,],;,$_,(,VJ,:,F9,),{,},},<EOF>''',
                101
            )
        )

    def test_653(self):
        self.assertTrue(
            TestLexer.test(
                '''Class N_{Val $_X34_:s3;Var _,_:Int ;}Class xD46:_{}Class o{Var $K:Int ;Constructor (G_47,_p0,i_,_:Int ){p::$94_.R5Rh().o();Continue ;} }''',
                '''Class,N_,{,Val,$_X34_,:,s3,;,Var,_,,,_,:,Int,;,},Class,xD46,:,_,{,},Class,o,{,Var,$K,:,Int,;,Constructor,(,G_47,,,_p0,,,i_,,,_,:,Int,),{,p,::,$94_,.,R5Rh,(,),.,o,(,),;,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_654(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _M:s{}Class __2{}Class r:D_{}Class __{Val $0,a_G,$_,_:Float ;Constructor (_,_:Array [Array [Array [Float ,066],066],066]){}Var _k,$_,c_,R:_1;}''',
                '''Class,_M,:,s,{,},Class,__2,{,},Class,r,:,D_,{,},Class,__,{,Val,$0,,,a_G,,,$_,,,_,:,Float,;,Constructor,(,_,,,_,:,Array,[,Array,[,Array,[,Float,,,066,],,,066,],,,066,],),{,},Var,_k,,,$_,,,c_,,,R,:,_1,;,},<EOF>''',
                101
            )
        )

    def test_655(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Val $_WE:Array [Array [Float ,0b110100],0b110100];Var H,_2_:Array [Int ,0134];Constructor (){}Val __b,_,_,$w,$m:_0;}''',
                '''Class,_,:,_,{,Val,$_WE,:,Array,[,Array,[,Float,,,0b110100,],,,0b110100,],;,Var,H,,,_2_,:,Array,[,Int,,,0134,],;,Constructor,(,),{,},Val,__b,,,_,,,_,,,$w,,,$m,:,_0,;,},<EOF>''',
                101
            )
        )

    def test_656(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ca3{jn(_,_:Float ;P,_:Array [Array [Array [Int ,033],0b11_10],0x1DA_A_56];__:Array [Array [String ,0b10000],0B1];D_S,_:y){} }''',
                '''Class,ca3,{,jn,(,_,,,_,:,Float,;,P,,,_,:,Array,[,Array,[,Array,[,Int,,,033,],,,0b1110,],,,0x1DAA56,],;,__,:,Array,[,Array,[,String,,,0b10000,],,,0B1,],;,D_S,,,_,:,y,),{,},},<EOF>''',
                101
            )
        )

    def test_657(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __J{gG0(__J,h0,L:Array [Float ,0B1000111];J:Array [Boolean ,074];_M___2_:dN;Y:Array [Array [Array [Float ,066],92],0b1001100];__,K,Z,vc,_,_,_:_2;B_,j5:Int ){} }''',
                '''Class,__J,{,gG0,(,__J,,,h0,,,L,:,Array,[,Float,,,0B1000111,],;,J,:,Array,[,Boolean,,,074,],;,_M___2_,:,dN,;,Y,:,Array,[,Array,[,Array,[,Float,,,066,],,,92,],,,0b1001100,],;,__,,,K,,,Z,,,vc,,,_,,,_,,,_,:,_2,;,B_,,,j5,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_658(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l1:nr{_eF5_(rtpG2,__Vq_,_:_;_,J:Int ;_,Ft_7,_u_:Array [String ,0x1];Q_qa_:_tS){} }Class _:_52{Constructor (V_9:Boolean ){} }''',
                '''Class,l1,:,nr,{,_eF5_,(,rtpG2,,,__Vq_,,,_,:,_,;,_,,,J,:,Int,;,_,,,Ft_7,,,_u_,:,Array,[,String,,,0x1,],;,Q_qa_,:,_tS,),{,},},Class,_,:,_52,{,Constructor,(,V_9,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_659(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (){Var q,r0,R:El1B28n;} }Class h54:G{}Class _S{Val I,$_,$fZ,$0:Float ;__R(c,h_,_T:N){B__::$_7Q();} }Class Yf{}''',
                '''Class,_,{,Constructor,(,),{,Var,q,,,r0,,,R,:,El1B28n,;,},},Class,h54,:,G,{,},Class,_S,{,Val,I,,,$_,,,$fZ,,,$0,:,Float,;,__R,(,c,,,h_,,,_T,:,N,),{,B__,::,$_7Q,(,),;,},},Class,Yf,{,},<EOF>''',
                101
            )
        )

    def test_660(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t:_{}Class Z2{Var R,$3_g5:Array [Array [Array [Array [Array [Array [Array [String ,0B1000001],054],0xD],7],7],054],054];Val _:_c;Destructor (){} }''',
                '''Class,t,:,_,{,},Class,Z2,{,Var,R,,,$3_g5,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B1000001,],,,054,],,,0xD,],,,7,],,,7,],,,054,],,,054,],;,Val,_,:,_c,;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_661(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _k{}Class _06{Var $_6_1:Float ;}Class a:K0{Val $_:Array [Array [Array [Int ,024],0x8_A_2],06];}Class _:__{}Class _:X{}Class _3D{}Class _:_{}''',
                '''Class,_k,{,},Class,_06,{,Var,$_6_1,:,Float,;,},Class,a,:,K0,{,Val,$_,:,Array,[,Array,[,Array,[,Int,,,024,],,,0x8A2,],,,06,],;,},Class,_,:,__,{,},Class,_,:,X,{,},Class,_3D,{,},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_662(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ____4fM:_6lv{Destructor (){}Q(_,Q,D,l,_:Array [Int ,0XFE8D];y:Array [Array [String ,0X59],7]){Continue ;z::$V0Y=!----Z::$4aK.EG_()*H7::$228()._M*-_::$_u4;} }''',
                '''Class,____4fM,:,_6lv,{,Destructor,(,),{,},Q,(,_,,,Q,,,D,,,l,,,_,:,Array,[,Int,,,0XFE8D,],;,y,:,Array,[,Array,[,String,,,0X59,],,,7,],),{,Continue,;,z,::,$V0Y,=,!,-,-,-,-,Z,::,$4aK,.,EG_,(,),*,H7,::,$228,(,),.,_M,*,-,_,::,$_u4,;,},},<EOF>''',
                101
            )
        )

    def test_663(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o:_R{Var $0D_b:Array [Array [Array [Array [Array [Array [Int ,0xF],010_24_44_33_0],0B10011],0xF],0x8],39];}Class _2V{Constructor (__,__:Array [String ,0b1_00]){}Var $G:Float ;}''',
                '''Class,o,:,_R,{,Var,$0D_b,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0xF,],,,0102444330,],,,0B10011,],,,0xF,],,,0x8,],,,39,],;,},Class,_2V,{,Constructor,(,__,,,__,:,Array,[,String,,,0b100,],),{,},Var,$G,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_664(self):
        self.assertTrue(
            TestLexer.test(
                '''Class f{Destructor (){} }Class P{Val K,$39_:_9;$_(m:Array [Array [Array [Array [Array [String ,0b1001100],0130],0b1001100],0b1001100],03];_7,__,_:String ;_9:Q;pp,_63Z:u1Q_j;Z_,m_,_,__,e,P__:S;nr4M,_,H0,_,I:t32_6Q){} }Class _{}Class __:l_{}''',
                '''Class,f,{,Destructor,(,),{,},},Class,P,{,Val,K,,,$39_,:,_9,;,$_,(,m,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b1001100,],,,0130,],,,0b1001100,],,,0b1001100,],,,03,],;,_7,,,__,,,_,:,String,;,_9,:,Q,;,pp,,,_63Z,:,u1Q_j,;,Z_,,,m_,,,_,,,__,,,e,,,P__,:,S,;,nr4M,,,_,,,H0,,,_,,,I,:,t32_6Q,),{,},},Class,_,{,},Class,__,:,l_,{,},<EOF>''',
                101
            )
        )

    def test_665(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class x{}Class A__{}Class iK56:L{}Class D_{}Class _{v(U_,_:Array [Int ,47];_N:Array [String ,06]){}d(){Break ;}Var ___50:U8_;}''',
                '''Class,_,{,},Class,x,{,},Class,A__,{,},Class,iK56,:,L,{,},Class,D_,{,},Class,_,{,v,(,U_,,,_,:,Array,[,Int,,,47,],;,_N,:,Array,[,String,,,06,],),{,},d,(,),{,Break,;,},Var,___50,:,U8_,;,},<EOF>''',
                101
            )
        )

    def test_666(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y:_3_{Var w17:Array [Boolean ,0B110010];Val $_c:p_AZ;Constructor (){Return ;}Var $4_m,$_,$_,O2:n;Destructor (){} }Class vQP5:Uh{}''',
                '''Class,y,:,_3_,{,Var,w17,:,Array,[,Boolean,,,0B110010,],;,Val,$_c,:,p_AZ,;,Constructor,(,),{,Return,;,},Var,$4_m,,,$_,,,$_,,,O2,:,n,;,Destructor,(,),{,},},Class,vQP5,:,Uh,{,},<EOF>''',
                101
            )
        )

    def test_667(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $_,_6,$2,WLj:Array [Float ,0X59];Constructor (_O,wg_,E_7:String ;_:String ;M,_Y8M1a:rG4n){}Val $_:__e_;}''',
                '''Class,_,{,Val,$_,,,_6,,,$2,,,WLj,:,Array,[,Float,,,0X59,],;,Constructor,(,_O,,,wg_,,,E_7,:,String,;,_,:,String,;,M,,,_Y8M1a,:,rG4n,),{,},Val,$_,:,__e_,;,},<EOF>''',
                101
            )
        )

    def test_668(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _OLZLg{}Class k:U{Val $_,_i___95d93:Boolean ;Du(q1Z,W8_,__5__:Array [Array [Array [Array [Array [Array [Array [String ,6],45_30_789],0B1000111],3],0B1000111],0b1_1],0645_4]){}Destructor (){} }''',
                '''Class,_OLZLg,{,},Class,k,:,U,{,Val,$_,,,_i___95d93,:,Boolean,;,Du,(,q1Z,,,W8_,,,__5__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,6,],,,4530789,],,,0B1000111,],,,3,],,,0B1000111,],,,0b11,],,,06454,],),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_669(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Z7936e:v{}Class _B:_{}Class _54V:_8{Var _7Z6__,y_45_:Array [Array [Int ,0b1_1_0_1],03_3];Val $70_,$0l0,$l,_,$9p:Float ;}''',
                '''Class,Z7936e,:,v,{,},Class,_B,:,_,{,},Class,_54V,:,_8,{,Var,_7Z6__,,,y_45_,:,Array,[,Array,[,Int,,,0b1101,],,,033,],;,Val,$70_,,,$0l0,,,$l,,,_,,,$9p,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_670(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7t8:K64{Constructor (_2,_:Array [Array [Array [Float ,06],0B1],3_86_69_9];W,XH:Int ;_i,b:Array [Float ,0B1001110];_S,x,i:_4){} }''',
                '''Class,_7t8,:,K64,{,Constructor,(,_2,,,_,:,Array,[,Array,[,Array,[,Float,,,06,],,,0B1,],,,386699,],;,W,,,XH,:,Int,;,_i,,,b,:,Array,[,Float,,,0B1001110,],;,_S,,,x,,,i,:,_4,),{,},},<EOF>''',
                101
            )
        )

    def test_671(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b:_{Constructor (P:_){}Destructor (){Continue ;}Constructor (_:f;_I,B:String ;UO:Array [String ,0X48]){Return ;} }Class M_{Val $7,__:Int ;}Class m__{}''',
                '''Class,b,:,_,{,Constructor,(,P,:,_,),{,},Destructor,(,),{,Continue,;,},Constructor,(,_,:,f,;,_I,,,B,:,String,;,UO,:,Array,[,String,,,0X48,],),{,Return,;,},},Class,M_,{,Val,$7,,,__,:,Int,;,},Class,m__,{,},<EOF>''',
                101
            )
        )

    def test_672(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _y{$F(S:Array [Boolean ,5];_,_:Array [Array [Array [Array [Array [Int ,04_3],0101],0b1_1],0B100001],0b1010110]){_C__::$_0r();} }''',
                '''Class,_y,{,$F,(,S,:,Array,[,Boolean,,,5,],;,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,043,],,,0101,],,,0b11,],,,0B100001,],,,0b1010110,],),{,_C__,::,$_0r,(,),;,},},<EOF>''',
                101
            )
        )

    def test_673(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Y{Val $_:Int ;Constructor (__,u_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,8_1_3],0b1],022_5],060],0b1],02],0X11],071],145],59];V_:Int ;E,_27:String ){} }''',
                '''Class,Y,{,Val,$_,:,Int,;,Constructor,(,__,,,u_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,813,],,,0b1,],,,0225,],,,060,],,,0b1,],,,02,],,,0X11,],,,071,],,,145,],,,59,],;,V_,:,Int,;,E,,,_27,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_674(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b8:_{Destructor (){}Constructor (N:Array [Array [Boolean ,0x3],0b10];_:Array [String ,0x33];_Fh_:H){} }Class _:_{Val $_:Array [Array [Array [Array [Int ,26],4],0x33],0105_3];$_1L(){} }Class _l{Destructor (){} }''',
                '''Class,b8,:,_,{,Destructor,(,),{,},Constructor,(,N,:,Array,[,Array,[,Boolean,,,0x3,],,,0b10,],;,_,:,Array,[,String,,,0x33,],;,_Fh_,:,H,),{,},},Class,_,:,_,{,Val,$_,:,Array,[,Array,[,Array,[,Array,[,Int,,,26,],,,4,],,,0x33,],,,01053,],;,$_1L,(,),{,},},Class,_l,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_675(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _j{$N(C2,Fz1,__:i7;_,r,_x,i:Int ;a,_da,e,T_:Int ;c:Float ;Z_:Int ){Continue ;Break ;} }Class ___oN_{Var _,_:Q;Val $2,_,_:Int ;}''',
                '''Class,_j,{,$N,(,C2,,,Fz1,,,__,:,i7,;,_,,,r,,,_x,,,i,:,Int,;,a,,,_da,,,e,,,T_,:,Int,;,c,:,Float,;,Z_,:,Int,),{,Continue,;,Break,;,},},Class,___oN_,{,Var,_,,,_,:,Q,;,Val,$2,,,_,,,_,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_676(self):
        self.assertTrue(
            TestLexer.test(
                '''Class H_2:T{Constructor (_,g:Array [Int ,0b1];_4,D,_,_:z;e:Boolean ;jr__,_,Rj,C2:Float ;_:Float ;__:Boolean ;yv:Array [Float ,05]){} }''',
                '''Class,H_2,:,T,{,Constructor,(,_,,,g,:,Array,[,Int,,,0b1,],;,_4,,,D,,,_,,,_,:,z,;,e,:,Boolean,;,jr__,,,_,,,Rj,,,C2,:,Float,;,_,:,Float,;,__,:,Boolean,;,yv,:,Array,[,Float,,,05,],),{,},},<EOF>''',
                101
            )
        )

    def test_677(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:B{$0(__,_,x:_;_4_,_:Array [Array [Int ,0x8_B],0133];_,_e3:String ;_,K47_1S__:Array [Boolean ,02_1_2_46]){Break ;} }Class w1{Constructor (C:Array [String ,0133]){Continue ;Continue ;}_5(nfH08_1BsM,G,_,F_:xjT;W7Dy:Array [Float ,0B111000]){}Val _o7,$0:Array [Array [Array [Array [String ,05],0133],0XE_BB_22],02_41];}''',
                '''Class,__,:,B,{,$0,(,__,,,_,,,x,:,_,;,_4_,,,_,:,Array,[,Array,[,Int,,,0x8B,],,,0133,],;,_,,,_e3,:,String,;,_,,,K47_1S__,:,Array,[,Boolean,,,021246,],),{,Break,;,},},Class,w1,{,Constructor,(,C,:,Array,[,String,,,0133,],),{,Continue,;,Continue,;,},_5,(,nfH08_1BsM,,,G,,,_,,,F_,:,xjT,;,W7Dy,:,Array,[,Float,,,0B111000,],),{,},Val,_o7,,,$0,:,Array,[,Array,[,Array,[,Array,[,String,,,05,],,,0133,],,,0XEBB22,],,,0241,],;,},<EOF>''',
                101
            )
        )

    def test_678(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w{Var $Z,$Y_Z96ev,$__fa,$0_:Array [Array [String ,0b1],1_5];Constructor (W____5EsX,f5,o_:_;_:Boolean ;T:Int ;_h:Boolean ){} }Class n0{Destructor (){} }''',
                '''Class,w,{,Var,$Z,,,$Y_Z96ev,,,$__fa,,,$0_,:,Array,[,Array,[,String,,,0b1,],,,15,],;,Constructor,(,W____5EsX,,,f5,,,o_,:,_,;,_,:,Boolean,;,T,:,Int,;,_h,:,Boolean,),{,},},Class,n0,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_679(self):
        self.assertTrue(
            TestLexer.test(
                '''Class f:nN{}Class z{Destructor (){Var _:Boolean ;} }Class Sf{Destructor (){}$____(Uaa,E_,_:String ;yf:W4_;C,E,P:__){}Var Q,$_r,$s:Array [String ,05];y_(){} }''',
                '''Class,f,:,nN,{,},Class,z,{,Destructor,(,),{,Var,_,:,Boolean,;,},},Class,Sf,{,Destructor,(,),{,},$____,(,Uaa,,,E_,,,_,:,String,;,yf,:,W4_,;,C,,,E,,,P,:,__,),{,},Var,Q,,,$_r,,,$s,:,Array,[,String,,,05,],;,y_,(,),{,},},<EOF>''',
                101
            )
        )

    def test_680(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _4_s:_{Constructor (y:String ){}Destructor (){}Val R,$U:Array [Array [Array [Boolean ,030],2],50];Var _h_9:Array [Float ,0X16];}''',
                '''Class,_4_s,:,_,{,Constructor,(,y,:,String,),{,},Destructor,(,),{,},Val,R,,,$U,:,Array,[,Array,[,Array,[,Boolean,,,030,],,,2,],,,50,],;,Var,_h_9,:,Array,[,Float,,,0X16,],;,},<EOF>''',
                101
            )
        )

    def test_681(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:___u{Var $6:Array [Array [Array [Array [Array [Array [Array [Array [String ,021_0_1],82],0B1],02_0_04_7_1_5],82],066],02],0x4D];}''',
                '''Class,__,:,___u,{,Var,$6,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,02101,],,,82,],,,0B1,],,,02004715,],,,82,],,,066,],,,02,],,,0x4D,],;,},<EOF>''',
                101
            )
        )

    def test_682(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class U_:_{i(){Continue ;Continue ;} }Class _b{Destructor (){A::$7();Continue ;Continue ;} }Class XX43:Y{Var g,$u:_;}Class _:__g__{Val _,$39J:Array [Boolean ,9];}''',
                '''Class,_,{,},Class,U_,:,_,{,i,(,),{,Continue,;,Continue,;,},},Class,_b,{,Destructor,(,),{,A,::,$7,(,),;,Continue,;,Continue,;,},},Class,XX43,:,Y,{,Var,g,,,$u,:,_,;,},Class,_,:,__g__,{,Val,_,,,$39J,:,Array,[,Boolean,,,9,],;,},<EOF>''',
                101
            )
        )

    def test_683(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var _,A:Boolean ;Val $_,$BRGC_26:Array [Array [Array [Float ,0X31],0X31],0X3D7_7492_0_1];Constructor (){} }''',
                '''Class,_,{,Var,_,,,A,:,Boolean,;,Val,$_,,,$BRGC_26,:,Array,[,Array,[,Array,[,Float,,,0X31,],,,0X31,],,,0X3D7749201,],;,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_684(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __wl{Var $c2,$9,$97:Array [Array [Array [Array [Array [Array [Float ,01_3_0],0xBF],0B101110],0XE],3],0B101110];Var $_6:IG_N;Destructor (){} }Class _:_{Val $R_:Array [String ,0x48];Var _:Array [Array [Array [String ,81],9],0b10001];}Class KIn {}''',
                '''Class,__wl,{,Var,$c2,,,$9,,,$97,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0130,],,,0xBF,],,,0B101110,],,,0XE,],,,3,],,,0B101110,],;,Var,$_6,:,IG_N,;,Destructor,(,),{,},},Class,_,:,_,{,Val,$R_,:,Array,[,String,,,0x48,],;,Var,_,:,Array,[,Array,[,Array,[,String,,,81,],,,9,],,,0b10001,],;,},Class,KIn,{,},<EOF>''',
                101
            )
        )

    def test_685(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9{Val $s_,c_9,$_,$P:Array [Array [Array [Array [Array [Array [Array [String ,41],0b100111],05_3_76],03_4],0x47],0B1011111],0X2F];}''',
                '''Class,_9,{,Val,$s_,,,c_9,,,$_,,,$P,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,41,],,,0b100111,],,,05376,],,,034,],,,0x47,],,,0B1011111,],,,0X2F,],;,},<EOF>''',
                101
            )
        )

    def test_686(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:Z{Constructor (__:_;_,u,_:Float ){}Var _,Y_:Array [Float ,0b101011];Destructor (){}Val _,$6_1,B,$J,$Z3RW:Float ;}''',
                '''Class,_,:,Z,{,Constructor,(,__,:,_,;,_,,,u,,,_,:,Float,),{,},Var,_,,,Y_,:,Array,[,Float,,,0b101011,],;,Destructor,(,),{,},Val,_,,,$6_1,,,B,,,$J,,,$Z3RW,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_687(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _54N:_{c(_q:Array [Array [Float ,05],8646];H,K,J,_:Array [Int ,54];_W,_:Array [Int ,0X2];_,R,_:U){} }Class ___t__Z:_W0B{}Class _tt{}''',
                '''Class,_54N,:,_,{,c,(,_q,:,Array,[,Array,[,Float,,,05,],,,8646,],;,H,,,K,,,J,,,_,:,Array,[,Int,,,54,],;,_W,,,_,:,Array,[,Int,,,0X2,],;,_,,,R,,,_,:,U,),{,},},Class,___t__Z,:,_W0B,{,},Class,_tt,{,},<EOF>''',
                101
            )
        )

    def test_688(self):
        self.assertTrue(
            TestLexer.test(
                '''Class u{Var _RJ_,$D6w,$_,w0Gg6,r:Array [Array [Array [Array [Array [Array [Array [Array [String ,65],65],78],65],3],010],2],65];e(){}$_(){}F_(_____:Int ){Break ;}Constructor (){}Destructor (){Return ;{Break ;} }}''',
                '''Class,u,{,Var,_RJ_,,,$D6w,,,$_,,,w0Gg6,,,r,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,65,],,,65,],,,78,],,,65,],,,3,],,,010,],,,2,],,,65,],;,e,(,),{,},$_,(,),{,},F_,(,_____,:,Int,),{,Break,;,},Constructor,(,),{,},Destructor,(,),{,Return,;,{,Break,;,},},},<EOF>''',
                101
            )
        )

    def test_689(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A_:_1{}Class _{Val $_,X_:Array [Array [Array [Float ,042],0B1010011],042];$ix(__7,v:Array [Array [Array [Int ,0X17],0X7],042];A:Boolean ){} }Class E{$_(){} }''',
                '''Class,A_,:,_1,{,},Class,_,{,Val,$_,,,X_,:,Array,[,Array,[,Array,[,Float,,,042,],,,0B1010011,],,,042,],;,$ix,(,__7,,,v,:,Array,[,Array,[,Array,[,Int,,,0X17,],,,0X7,],,,042,],;,A,:,Boolean,),{,},},Class,E,{,$_,(,),{,},},<EOF>''',
                101
            )
        )

    def test_690(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8:_{}Class f{}Class K:_{__f_(){}Constructor (u_9,__M,m,_5O:_ir){ {Var _,d:Boolean ;} }Var $__,$3:Array [Array [Array [Boolean ,92],92],0B100111];$_P_OsF_M(){}Destructor (){Continue ;Return ;Break ;} }''',
                '''Class,_8,:,_,{,},Class,f,{,},Class,K,:,_,{,__f_,(,),{,},Constructor,(,u_9,,,__M,,,m,,,_5O,:,_ir,),{,{,Var,_,,,d,:,Boolean,;,},},Var,$__,,,$3,:,Array,[,Array,[,Array,[,Boolean,,,92,],,,92,],,,0B100111,],;,$_P_OsF_M,(,),{,},Destructor,(,),{,Continue,;,Return,;,Break,;,},},<EOF>''',
                101
            )
        )

    def test_691(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _X:_{}Class _{$97(){}Var E:Array [Array [Boolean ,0XC],01];Var bX_:Array [Array [Array [Array [Boolean ,012],0B1_10_0],0B10],066];}''',
                '''Class,_X,:,_,{,},Class,_,{,$97,(,),{,},Var,E,:,Array,[,Array,[,Boolean,,,0XC,],,,01,],;,Var,bX_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,012,],,,0B1100,],,,0B10,],,,066,],;,},<EOF>''',
                101
            )
        )

    def test_692(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _R{Constructor (qz,sY_:Float ;_A:k;c____v36L:Boolean ;p:String ;_:__){} }Class _rP{}Class _4:_{Destructor (){}Constructor (){} }''',
                '''Class,_R,{,Constructor,(,qz,,,sY_,:,Float,;,_A,:,k,;,c____v36L,:,Boolean,;,p,:,String,;,_,:,__,),{,},},Class,_rP,{,},Class,_4,:,_,{,Destructor,(,),{,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_693(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l{Constructor (__,_,_:Array [Array [String ,8],0B10];_,e1__:Boolean ;__0_:Array [Array [Array [Int ,062],0XCF_BB],0B1];__,_2,z__,R_:_){} }Class _k{}Class __{Var $57:Array [Array [Array [Array [String ,0XC],89],0b100010],89];}''',
                '''Class,l,{,Constructor,(,__,,,_,,,_,:,Array,[,Array,[,String,,,8,],,,0B10,],;,_,,,e1__,:,Boolean,;,__0_,:,Array,[,Array,[,Array,[,Int,,,062,],,,0XCFBB,],,,0B1,],;,__,,,_2,,,z__,,,R_,:,_,),{,},},Class,_k,{,},Class,__,{,Var,$57,:,Array,[,Array,[,Array,[,Array,[,String,,,0XC,],,,89,],,,0b100010,],,,89,],;,},<EOF>''',
                101
            )
        )

    def test_694(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_U:Boolean ;__,L,p:D7;jR_,_:Boolean ;l,J:Array [Array [String ,44],0X21];__:__7;_:Float ;J:Array [Array [Boolean ,014],0b1000011];_,_H:g){Continue ;Break ;}_d(_M:String ;s,F:_;_:Float ){} }''',
                '''Class,_,{,Constructor,(,_U,:,Boolean,;,__,,,L,,,p,:,D7,;,jR_,,,_,:,Boolean,;,l,,,J,:,Array,[,Array,[,String,,,44,],,,0X21,],;,__,:,__7,;,_,:,Float,;,J,:,Array,[,Array,[,Boolean,,,014,],,,0b1000011,],;,_,,,_H,:,g,),{,Continue,;,Break,;,},_d,(,_M,:,String,;,s,,,F,:,_,;,_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_695(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C_f:_{}Class _{Destructor (){}Destructor (){}Constructor (__8:String ;v,_,X:Array [Boolean ,0107];_86_,g,O_:Array [Float ,0107]){} }''',
                '''Class,C_f,:,_,{,},Class,_,{,Destructor,(,),{,},Destructor,(,),{,},Constructor,(,__8,:,String,;,v,,,_,,,X,:,Array,[,Boolean,,,0107,],;,_86_,,,g,,,O_,:,Array,[,Float,,,0107,],),{,},},<EOF>''',
                101
            )
        )

    def test_696(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{r_(_:Array [Array [Array [Int ,02],0X5A],020]){Continue ;}Destructor (){}Var $9B,$_T_,_v1,$P,$93:m7i;}Class SB{}''',
                '''Class,_,{,r_,(,_,:,Array,[,Array,[,Array,[,Int,,,02,],,,0X5A,],,,020,],),{,Continue,;,},Destructor,(,),{,},Var,$9B,,,$_T_,,,_v1,,,$P,,,$93,:,m7i,;,},Class,SB,{,},<EOF>''',
                101
            )
        )

    def test_697(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{e(__:VD){}Var w9_,$1w_:Int ;Constructor (hx,D:Boolean ;_,Y,_,_,a,_7,_n,_:v){} }Class Q_:q{Destructor (){Break ;} }Class _9b{}''',
                '''Class,_,{,e,(,__,:,VD,),{,},Var,w9_,,,$1w_,:,Int,;,Constructor,(,hx,,,D,:,Boolean,;,_,,,Y,,,_,,,_,,,a,,,_7,,,_n,,,_,:,v,),{,},},Class,Q_,:,q,{,Destructor,(,),{,Break,;,},},Class,_9b,{,},<EOF>''',
                101
            )
        )

    def test_698(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class ____{}Class R:_{Var $_9pt,$7,$XP,$2100__,P,$_:_;Destructor (){}$L(_v:Array [Boolean ,026];_,_5,PX:Int ;z:Array [Array [Int ,05],0b1_1];__:Int ){}_3_(fPB:_7LC){}Destructor (){} }''',
                '''Class,_,{,},Class,____,{,},Class,R,:,_,{,Var,$_9pt,,,$7,,,$XP,,,$2100__,,,P,,,$_,:,_,;,Destructor,(,),{,},$L,(,_v,:,Array,[,Boolean,,,026,],;,_,,,_5,,,PX,:,Int,;,z,:,Array,[,Array,[,Int,,,05,],,,0b11,],;,__,:,Int,),{,},_3_,(,fPB,:,_7LC,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_699(self):
        self.assertTrue(
            TestLexer.test(
                '''Class N{Val t_8:_r;}Class _E7{Val $8:Array [Array [Array [String ,0b1000100],4_6],06];Constructor (){} }Class _{Var V,_:_;}''',
                '''Class,N,{,Val,t_8,:,_r,;,},Class,_E7,{,Val,$8,:,Array,[,Array,[,Array,[,String,,,0b1000100,],,,46,],,,06,],;,Constructor,(,),{,},},Class,_,{,Var,V,,,_,:,_,;,},<EOF>''',
                101
            )
        )

    def test_700(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V:_{}Class M_{$0_(_:Array [Array [Int ,05],0b11001];_H_,_:Boolean ;_:Boolean ;I,_8,_:String ;i:_){}Var $2:Boolean ;}''',
                '''Class,V,:,_,{,},Class,M_,{,$0_,(,_,:,Array,[,Array,[,Int,,,05,],,,0b11001,],;,_H_,,,_,:,Boolean,;,_,:,Boolean,;,I,,,_8,,,_,:,String,;,i,:,_,),{,},Var,$2,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_701(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Tt:H2_{Var $q:Int ;Var $R7:String ;}Class _0u:__A{}Class _:_{Val _9661:Array [Array [Array [Float ,05_4],0X2],0123];Constructor (){Break ;}Val $_,$tc,$W:Float ;}''',
                '''Class,Tt,:,H2_,{,Var,$q,:,Int,;,Var,$R7,:,String,;,},Class,_0u,:,__A,{,},Class,_,:,_,{,Val,_9661,:,Array,[,Array,[,Array,[,Float,,,054,],,,0X2,],,,0123,],;,Constructor,(,),{,Break,;,},Val,$_,,,$tc,,,$W,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_702(self):
        self.assertTrue(
            TestLexer.test(
                '''Class r{}Class h{Val _:Float ;}Class _d{Constructor (){} }Class U{Destructor (){} }Class vc6b{Val $8,$w_:Array [Float ,0114];}Class ___{}Class j59{}''',
                '''Class,r,{,},Class,h,{,Val,_,:,Float,;,},Class,_d,{,Constructor,(,),{,},},Class,U,{,Destructor,(,),{,},},Class,vc6b,{,Val,$8,,,$w_,:,Array,[,Float,,,0114,],;,},Class,___,{,},Class,j59,{,},<EOF>''',
                101
            )
        )

    def test_703(self):
        self.assertTrue(
            TestLexer.test(
                '''Class I6__02:y{Var I,$_:Float ;}Class ___93:_zL5EMm{}Class p{}Class __1{Var _k,P,U,_,$_9H4R:b;Destructor (){} }''',
                '''Class,I6__02,:,y,{,Var,I,,,$_,:,Float,;,},Class,___93,:,_zL5EMm,{,},Class,p,{,},Class,__1,{,Var,_k,,,P,,,U,,,_,,,$_9H4R,:,b,;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_704(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2:k7{$_ky_4(U:Array [Array [Array [Float ,0B1_0],0144],69];h0:Array [String ,0b10110];__,_,Y1,_20_I5_:Array [Array [Array [Array [Array [Array [Boolean ,0105],0x1A],0B10001],0X46],4],0b1];S:_;m,F:_;H:Int ){} }Class X{}Class __5{}Class B___{}''',
                '''Class,_2,:,k7,{,$_ky_4,(,U,:,Array,[,Array,[,Array,[,Float,,,0B10,],,,0144,],,,69,],;,h0,:,Array,[,String,,,0b10110,],;,__,,,_,,,Y1,,,_20_I5_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0105,],,,0x1A,],,,0B10001,],,,0X46,],,,4,],,,0b1,],;,S,:,_,;,m,,,F,:,_,;,H,:,Int,),{,},},Class,X,{,},Class,__5,{,},Class,B___,{,},<EOF>''',
                101
            )
        )

    def test_705(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _22:__{Var __i_0_9E:Array [Array [Array [Int ,0B1101],0x58],0B1101];_8(t_:Float ){}kH1(){}Val b:Array [Array [Array [String ,0XAF_E_1],0xE],01];}''',
                '''Class,_22,:,__,{,Var,__i_0_9E,:,Array,[,Array,[,Array,[,Int,,,0B1101,],,,0x58,],,,0B1101,],;,_8,(,t_,:,Float,),{,},kH1,(,),{,},Val,b,:,Array,[,Array,[,Array,[,String,,,0XAFE1,],,,0xE,],,,01,],;,},<EOF>''',
                101
            )
        )

    def test_706(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _wy:_O{}Class _{Destructor (){} }Class _:l62{}Class _:_{Var u5__,c,_9Iro,$_,_A,B95__5:Array [Boolean ,046];Constructor (){}Constructor (){Return ;} }''',
                '''Class,_wy,:,_O,{,},Class,_,{,Destructor,(,),{,},},Class,_,:,l62,{,},Class,_,:,_,{,Var,u5__,,,c,,,_9Iro,,,$_,,,_A,,,B95__5,:,Array,[,Boolean,,,046,],;,Constructor,(,),{,},Constructor,(,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_707(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Destructor (){Break ;Return ;}Constructor (_,_,____:Array [Array [Float ,35],0X6];JB_9:Array [Array [Float ,036],0b1011001];_6_:Int ;_:Array [Boolean ,0B1]){} }''',
                '''Class,_,{,Destructor,(,),{,Break,;,Return,;,},Constructor,(,_,,,_,,,____,:,Array,[,Array,[,Float,,,35,],,,0X6,],;,JB_9,:,Array,[,Array,[,Float,,,036,],,,0b1011001,],;,_6_,:,Int,;,_,:,Array,[,Boolean,,,0B1,],),{,},},<EOF>''',
                101
            )
        )

    def test_708(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:J{}Class M:_S{}Class Y8{Val WF:Float ;$3i(){}Constructor (CK,g,_,S,k:_;_,_7,F_,_,g1,_,_,_:Boolean ;T,_:d7;_:A5){}$0__(AcS,l8:_;N3_:Int ;__9:Float ;_5_,__,_n:HH;_,ekj2,j_:o043_1){} }Class __{}''',
                '''Class,_,:,J,{,},Class,M,:,_S,{,},Class,Y8,{,Val,WF,:,Float,;,$3i,(,),{,},Constructor,(,CK,,,g,,,_,,,S,,,k,:,_,;,_,,,_7,,,F_,,,_,,,g1,,,_,,,_,,,_,:,Boolean,;,T,,,_,:,d7,;,_,:,A5,),{,},$0__,(,AcS,,,l8,:,_,;,N3_,:,Int,;,__9,:,Float,;,_5_,,,__,,,_n,:,HH,;,_,,,ekj2,,,j_,:,o043_1,),{,},},Class,__,{,},<EOF>''',
                101
            )
        )

    def test_709(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _F_H:lE{Constructor (){} }Class r_:_7xKv48A{}Class q:G35{Constructor (i,yL2:String ){}$__(){ {Continue ;Continue ;} }Var ___:_;}''',
                '''Class,_F_H,:,lE,{,Constructor,(,),{,},},Class,r_,:,_7xKv48A,{,},Class,q,:,G35,{,Constructor,(,i,,,yL2,:,String,),{,},$__,(,),{,{,Continue,;,Continue,;,},},Var,___,:,_,;,},<EOF>''',
                101
            )
        )

    def test_710(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:C{Var __:_;_(){Break ;}_A_0(_K,SF,y_L:__;_:Array [Boolean ,0X1C1];e34,LL0,O,__3v:Array [Array [String ,9],0x3]){} }''',
                '''Class,_,:,C,{,Var,__,:,_,;,_,(,),{,Break,;,},_A_0,(,_K,,,SF,,,y_L,:,__,;,_,:,Array,[,Boolean,,,0X1C1,],;,e34,,,LL0,,,O,,,__3v,:,Array,[,Array,[,String,,,9,],,,0x3,],),{,},},<EOF>''',
                101
            )
        )

    def test_711(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V:B{Constructor (i:Boolean ;_,ts_:Array [Array [String ,04],0xD]){ {}Continue ;}Var $f:Array [Float ,0B1_1];}''',
                '''Class,V,:,B,{,Constructor,(,i,:,Boolean,;,_,,,ts_,:,Array,[,Array,[,String,,,04,],,,0xD,],),{,{,},Continue,;,},Var,$f,:,Array,[,Float,,,0B11,],;,},<EOF>''',
                101
            )
        )

    def test_712(self):
        self.assertTrue(
            TestLexer.test(
                '''Class rJh:D4q{Constructor (){Var _jhH:_a;}X(){Var _D7:Array [Array [Array [Float ,6],073],0b1_0_1];} }Class _{}Class _J:v{Constructor (){}Var $_X:Array [Array [Array [Array [Boolean ,073],1],4_49],0b1];}Class _:q{}''',
                '''Class,rJh,:,D4q,{,Constructor,(,),{,Var,_jhH,:,_a,;,},X,(,),{,Var,_D7,:,Array,[,Array,[,Array,[,Float,,,6,],,,073,],,,0b101,],;,},},Class,_,{,},Class,_J,:,v,{,Constructor,(,),{,},Var,$_X,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,073,],,,1,],,,449,],,,0b1,],;,},Class,_,:,q,{,},<EOF>''',
                101
            )
        )

    def test_713(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _C{}Class _:Y{$_13(_7:L__A;U:Float ){}Destructor (){}Val __,$8__,$61:Int ;Constructor (){} }Class _{y5(__e,R:G){} }''',
                '''Class,_C,{,},Class,_,:,Y,{,$_13,(,_7,:,L__A,;,U,:,Float,),{,},Destructor,(,),{,},Val,__,,,$8__,,,$61,:,Int,;,Constructor,(,),{,},},Class,_,{,y5,(,__e,,,R,:,G,),{,},},<EOF>''',
                101
            )
        )

    def test_714(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J:_9{Constructor (_,_9_:Z_L_1_;R:Array [Array [Array [Array [Array [Array [Array [Int ,0b1],0X3D],0X5_5],0144],0b1],0144],4]){} }Class hoJ{QU_(){} }Class r{Var _,$Y,$1:Array [String ,77];Destructor (){}Var $_30,_:Array [Int ,0B1_11_00];}''',
                '''Class,J,:,_9,{,Constructor,(,_,,,_9_,:,Z_L_1_,;,R,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0b1,],,,0X3D,],,,0X55,],,,0144,],,,0b1,],,,0144,],,,4,],),{,},},Class,hoJ,{,QU_,(,),{,},},Class,r,{,Var,_,,,$Y,,,$1,:,Array,[,String,,,77,],;,Destructor,(,),{,},Var,$_30,,,_,:,Array,[,Int,,,0B11100,],;,},<EOF>''',
                101
            )
        )

    def test_715(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w{}Class S:__{Destructor (){}Var $_,$2,N,$K,EDw,$_,b,ch_,$25:Array [Boolean ,6_56];Var I_2B:String ;$8(){}Destructor (){} }''',
                '''Class,w,{,},Class,S,:,__,{,Destructor,(,),{,},Var,$_,,,$2,,,N,,,$K,,,EDw,,,$_,,,b,,,ch_,,,$25,:,Array,[,Boolean,,,656,],;,Var,I_2B,:,String,;,$8,(,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_716(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _d:_r{$F_s_(M_,K_,f:Boolean ;_:Boolean ;_554__:__;____:Array [Int ,0B1_10]){Break ;} }Class z_3A_{Destructor (){} }''',
                '''Class,_d,:,_r,{,$F_s_,(,M_,,,K_,,,f,:,Boolean,;,_,:,Boolean,;,_554__,:,__,;,____,:,Array,[,Int,,,0B110,],),{,Break,;,},},Class,z_3A_,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_717(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Var _nv:Array [Boolean ,0B100010];}Class e{Var _:Array [Boolean ,0X1C];}Class R{Constructor (){}Var $74:String ;Val h2,__,$_,$j:_;}''',
                '''Class,_,:,_,{,Var,_nv,:,Array,[,Boolean,,,0B100010,],;,},Class,e,{,Var,_,:,Array,[,Boolean,,,0X1C,],;,},Class,R,{,Constructor,(,),{,},Var,$74,:,String,;,Val,h2,,,__,,,$_,,,$j,:,_,;,},<EOF>''',
                101
            )
        )

    def test_718(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (){}Constructor (_:Array [Array [Array [String ,77],0x3_E1],77];_,H:_;_,c,e:l){} }Class Rs:__C{}Class x:_{}''',
                '''Class,_,{,Constructor,(,),{,},Constructor,(,_,:,Array,[,Array,[,Array,[,String,,,77,],,,0x3E1,],,,77,],;,_,,,H,:,_,;,_,,,c,,,e,:,l,),{,},},Class,Rs,:,__C,{,},Class,x,:,_,{,},<EOF>''',
                101
            )
        )

    def test_719(self):
        self.assertTrue(
            TestLexer.test(
                '''Class z:_3M2_{}Class E:w{}Class U:_{}Class V:____3L{Constructor (){Continue ;Break ;}Val $MV_97n:String ;}Class _{}''',
                '''Class,z,:,_3M2_,{,},Class,E,:,w,{,},Class,U,:,_,{,},Class,V,:,____3L,{,Constructor,(,),{,Continue,;,Break,;,},Val,$MV_97n,:,String,;,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_720(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___iF:D{}Class _k:_{Destructor (){}Var $__,$E:Array [Array [Float ,25],0B1_1];Var _:I2;}Class _8X_:Tj{}Class s_6:S{}Class C{Destructor (){} }''',
                '''Class,___iF,:,D,{,},Class,_k,:,_,{,Destructor,(,),{,},Var,$__,,,$E,:,Array,[,Array,[,Float,,,25,],,,0B11,],;,Var,_,:,I2,;,},Class,_8X_,:,Tj,{,},Class,s_6,:,S,{,},Class,C,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_721(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Val _:Array [Array [Float ,5],047]=!!!!s9::$4._4.n_.T()%!!!!---P1K::$o()/_::$0_()._._();}Class _{Constructor (){s::$_();} }Class _{di(X:String ;M,_h,l8LL,V:P7_;E_:Array [Array [Int ,04_4_60_0],0x2A];_,X_,y,_4:Boolean ;z_:Float ;M,U:String ){} }''',
                '''Class,_,:,_,{,Val,_,:,Array,[,Array,[,Float,,,5,],,,047,],=,!,!,!,!,s9,::,$4,.,_4,.,n_,.,T,(,),%,!,!,!,!,-,-,-,P1K,::,$o,(,),/,_,::,$0_,(,),.,_,.,_,(,),;,},Class,_,{,Constructor,(,),{,s,::,$_,(,),;,},},Class,_,{,di,(,X,:,String,;,M,,,_h,,,l8LL,,,V,:,P7_,;,E_,:,Array,[,Array,[,Int,,,044600,],,,0x2A,],;,_,,,X_,,,y,,,_4,:,Boolean,;,z_,:,Float,;,M,,,U,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_722(self):
        self.assertTrue(
            TestLexer.test(
                '''Class j{$_Q(_,_,_3,__O,_z:Float ;f:Array [Array [Float ,0B1_0],05]){} }Class _X:_{}Class _:_{$_6_(){} }Class l{}''',
                '''Class,j,{,$_Q,(,_,,,_,,,_3,,,__O,,,_z,:,Float,;,f,:,Array,[,Array,[,Float,,,0B10,],,,05,],),{,},},Class,_X,:,_,{,},Class,_,:,_,{,$_6_,(,),{,},},Class,l,{,},<EOF>''',
                101
            )
        )

    def test_723(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _5{Constructor (_3Q_:Float ;hnqy97F,_,_8,_g___4:Float ;_:_;Q:Array [Array [Array [Array [String ,015],026],04_3_1],37];i__,K:_){} }Class __:K{}''',
                '''Class,_5,{,Constructor,(,_3Q_,:,Float,;,hnqy97F,,,_,,,_8,,,_g___4,:,Float,;,_,:,_,;,Q,:,Array,[,Array,[,Array,[,Array,[,String,,,015,],,,026,],,,0431,],,,37,],;,i__,,,K,:,_,),{,},},Class,__,:,K,{,},<EOF>''',
                101
            )
        )

    def test_724(self):
        self.assertTrue(
            TestLexer.test(
                '''Class L{$J_(_,_,Ah_,K:_){} }Class P6:_{Var $4jY:Array [Array [Boolean ,0x30],0xB];Var $_,_B7:Array [Array [Array [Boolean ,6],0b1_11_1],07];Destructor (){} }''',
                '''Class,L,{,$J_,(,_,,,_,,,Ah_,,,K,:,_,),{,},},Class,P6,:,_,{,Var,$4jY,:,Array,[,Array,[,Boolean,,,0x30,],,,0xB,],;,Var,$_,,,_B7,:,Array,[,Array,[,Array,[,Boolean,,,6,],,,0b1111,],,,07,],;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_725(self):
        self.assertTrue(
            TestLexer.test(
                '''Class N{Var _:Array [Array [Array [Array [Int ,047],61],0X25],0b111011];}Class n_{Val $39:Array [Array [Array [String ,0x41],0XE],0X25];}Class d{}Class _:__e{}''',
                '''Class,N,{,Var,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,047,],,,61,],,,0X25,],,,0b111011,],;,},Class,n_,{,Val,$39,:,Array,[,Array,[,Array,[,String,,,0x41,],,,0XE,],,,0X25,],;,},Class,d,{,},Class,_,:,__e,{,},<EOF>''',
                101
            )
        )

    def test_726(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _M:p__kP3{Val t_k:O;}Class Yi:_w_{Constructor (H_:Array [String ,0b1]){ {}Continue ;} }Class _1__t4:_{Var D:Int ;}''',
                '''Class,_M,:,p__kP3,{,Val,t_k,:,O,;,},Class,Yi,:,_w_,{,Constructor,(,H_,:,Array,[,String,,,0b1,],),{,{,},Continue,;,},},Class,_1__t4,:,_,{,Var,D,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_727(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:X{Constructor (y:_CoJ_;t:__;I:Array [Array [Float ,0B1001100],0B1]){}Val w,_:Boolean ;Val $9,_,_,$_:Array [Array [Int ,0B11],0b1];}Class _:_{}Class _{}''',
                '''Class,_,:,X,{,Constructor,(,y,:,_CoJ_,;,t,:,__,;,I,:,Array,[,Array,[,Float,,,0B1001100,],,,0B1,],),{,},Val,w,,,_,:,Boolean,;,Val,$9,,,_,,,_,,,$_,:,Array,[,Array,[,Int,,,0B11,],,,0b1,],;,},Class,_,:,_,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_728(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:g{}Class _sG___7:_{}Class _{Destructor (){Val kk,_,_4:String ;Return ;}Destructor (){Val _Q0:Array [Boolean ,0b1000111];} }Class N:_3{Val y:Array [Int ,90];Val $_:Int ;}Class P:_1v{}''',
                '''Class,_,:,g,{,},Class,_sG___7,:,_,{,},Class,_,{,Destructor,(,),{,Val,kk,,,_,,,_4,:,String,;,Return,;,},Destructor,(,),{,Val,_Q0,:,Array,[,Boolean,,,0b1000111,],;,},},Class,N,:,_3,{,Val,y,:,Array,[,Int,,,90,],;,Val,$_,:,Int,;,},Class,P,:,_1v,{,},<EOF>''',
                101
            )
        )

    def test_729(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8Y{Var $45,_,pK,$s:Array [String ,0x49];Constructor (__J:__3_){} }Class BxTh{Val $uSz:g_6;Var Z:Array [Float ,041];Val J__p:Array [Array [Float ,0x49],7];$_(Pi:Array [Array [Array [Array [Array [Array [String ,0x13],0x49],39],0b10011],04],06];w:Float ;_:Array [Array [Array [Float ,0b10011],0x49],0X3]){} }''',
                '''Class,_8Y,{,Var,$45,,,_,,,pK,,,$s,:,Array,[,String,,,0x49,],;,Constructor,(,__J,:,__3_,),{,},},Class,BxTh,{,Val,$uSz,:,g_6,;,Var,Z,:,Array,[,Float,,,041,],;,Val,J__p,:,Array,[,Array,[,Float,,,0x49,],,,7,],;,$_,(,Pi,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0x13,],,,0x49,],,,39,],,,0b10011,],,,04,],,,06,],;,w,:,Float,;,_,:,Array,[,Array,[,Array,[,Float,,,0b10011,],,,0x49,],,,0X3,],),{,},},<EOF>''',
                101
            )
        )

    def test_730(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _5{}Class _{Constructor (_,e5s:String ;Y_:Array [Float ,0101];_,Z,_,A__3_,t,_,V0_,_,_62,w,_r:Array [Array [Float ,0b111_1010_0_0],20];r9b83,v:Array [Float ,47];_F_,d:Int ){} }Class _6{}Class _6:r9{Val $7j9Q,_1:Array [Int ,0X4];}''',
                '''Class,_5,{,},Class,_,{,Constructor,(,_,,,e5s,:,String,;,Y_,:,Array,[,Float,,,0101,],;,_,,,Z,,,_,,,A__3_,,,t,,,_,,,V0_,,,_,,,_62,,,w,,,_r,:,Array,[,Array,[,Float,,,0b111101000,],,,20,],;,r9b83,,,v,:,Array,[,Float,,,47,],;,_F_,,,d,:,Int,),{,},},Class,_6,{,},Class,_6,:,r9,{,Val,$7j9Q,,,_1,:,Array,[,Int,,,0X4,],;,},<EOF>''',
                101
            )
        )

    def test_731(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b{$_oA(D_:_;_,____:Boolean ){Break ;}$W(u3,N,q__,RJ,pi,_Xw,T3,u,_,__n,Er:Int ;Q_,r_,_,t:String ;b:Boolean ;jp,u_,_6D3:n;aQi:_O_;w,Cc,_2:a0n;_,V7:Array [Array [Array [Array [Boolean ,0B1010],0b1010001],0b1_1],1];_1,dr_:_;Y,_:Array [Array [Int ,1],026]){}Constructor (B,_96:Int ;O_5ua:C3l){} }''',
                '''Class,b,{,$_oA,(,D_,:,_,;,_,,,____,:,Boolean,),{,Break,;,},$W,(,u3,,,N,,,q__,,,RJ,,,pi,,,_Xw,,,T3,,,u,,,_,,,__n,,,Er,:,Int,;,Q_,,,r_,,,_,,,t,:,String,;,b,:,Boolean,;,jp,,,u_,,,_6D3,:,n,;,aQi,:,_O_,;,w,,,Cc,,,_2,:,a0n,;,_,,,V7,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1010,],,,0b1010001,],,,0b11,],,,1,],;,_1,,,dr_,:,_,;,Y,,,_,:,Array,[,Array,[,Int,,,1,],,,026,],),{,},Constructor,(,B,,,_96,:,Int,;,O_5ua,:,C3l,),{,},},<EOF>''',
                101
            )
        )

    def test_732(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _B:__{}Class m{$E__(_:Array [Boolean ,0b111110];K:String ){ {} }}Class _3A{Val $6___6,$_U:Array [Boolean ,2];}Class __r:_{Destructor (){} }''',
                '''Class,_B,:,__,{,},Class,m,{,$E__,(,_,:,Array,[,Boolean,,,0b111110,],;,K,:,String,),{,{,},},},Class,_3A,{,Val,$6___6,,,$_U,:,Array,[,Boolean,,,2,],;,},Class,__r,:,_,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_733(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9:J{$__(_,_4_5,_:Float ){}Val _:Array [Array [Array [Array [Array [Array [Array [Float ,0x1D],5_5],0106],064],0x8F_2_B],61],0b10];}''',
                '''Class,_9,:,J,{,$__,(,_,,,_4_5,,,_,:,Float,),{,},Val,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x1D,],,,55,],,,0106,],,,064,],,,0x8F2B,],,,61,],,,0b10,],;,},<EOF>''',
                101
            )
        )

    def test_734(self):
        self.assertTrue(
            TestLexer.test(
                '''Class W:p9Gq{}Class _5{}Class _:T{}Class ax{}Class _{Var V0m,$Ye,$8_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0B110000],95],0B10],0X63],0B1],0B1],86_3_9_8_2],0b110001],06];}''',
                '''Class,W,:,p9Gq,{,},Class,_5,{,},Class,_,:,T,{,},Class,ax,{,},Class,_,{,Var,V0m,,,$Ye,,,$8_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B110000,],,,95,],,,0B10,],,,0X63,],,,0B1,],,,0B1,],,,863982,],,,0b110001,],,,06,],;,},<EOF>''',
                101
            )
        )

    def test_735(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:p5bjY{}Class r:_6{Constructor (e_,d,_:Array [Float ,41];YF,O__:String ){}$_(_m_:String ){}Var $_,$5:Array [Array [Array [Float ,0x3C],41],0x3C];}Class O{_(){}s_2(){Return ;} }''',
                '''Class,_,:,p5bjY,{,},Class,r,:,_6,{,Constructor,(,e_,,,d,,,_,:,Array,[,Float,,,41,],;,YF,,,O__,:,String,),{,},$_,(,_m_,:,String,),{,},Var,$_,,,$5,:,Array,[,Array,[,Array,[,Float,,,0x3C,],,,41,],,,0x3C,],;,},Class,O,{,_,(,),{,},s_2,(,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_736(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _Q:W{Val $__:Array [Int ,70];Val $k9,$_:Float ;$m4(rb:Array [Array [Float ,0X6],0b1011];_3,mM_,_:Boolean ;_n:_;S___l:Int ;C,_,_94,_8i:Float ;_z6:_){Continue ;}_(){} }''',
                '''Class,_Q,:,W,{,Val,$__,:,Array,[,Int,,,70,],;,Val,$k9,,,$_,:,Float,;,$m4,(,rb,:,Array,[,Array,[,Float,,,0X6,],,,0b1011,],;,_3,,,mM_,,,_,:,Boolean,;,_n,:,_,;,S___l,:,Int,;,C,,,_,,,_94,,,_8i,:,Float,;,_z6,:,_,),{,Continue,;,},_,(,),{,},},<EOF>''',
                101
            )
        )

    def test_737(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Eo:_1_{Constructor (Q,_,___:Array [Array [Array [Array [Int ,05],077],6],02];_7R,_N8_,u,e_,g8Q,D,li:Float ){} }Class BQGu{}''',
                '''Class,Eo,:,_1_,{,Constructor,(,Q,,,_,,,___,:,Array,[,Array,[,Array,[,Array,[,Int,,,05,],,,077,],,,6,],,,02,],;,_7R,,,_N8_,,,u,,,e_,,,g8Q,,,D,,,li,:,Float,),{,},},Class,BQGu,{,},<EOF>''',
                101
            )
        )

    def test_738(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V{Destructor (){}Val _,_,$3H65,$_:S;Constructor (){ {} }Constructor (_,_:fL;h:n_1x){}Var $S:String ;Constructor (_23_,Z8:Array [Int ,3_36_2]){}Var $ZJ915,$_:Array [Array [Array [String ,0X63],022],0X9_68];Var wX:_3r;}''',
                '''Class,V,{,Destructor,(,),{,},Val,_,,,_,,,$3H65,,,$_,:,S,;,Constructor,(,),{,{,},},Constructor,(,_,,,_,:,fL,;,h,:,n_1x,),{,},Var,$S,:,String,;,Constructor,(,_23_,,,Z8,:,Array,[,Int,,,3362,],),{,},Var,$ZJ915,,,$_,:,Array,[,Array,[,Array,[,String,,,0X63,],,,022,],,,0X968,],;,Var,wX,:,_3r,;,},<EOF>''',
                101
            )
        )

    def test_739(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:__s_{Constructor (_1ll:String ;I:Int ;_,_9,_,_2_:__e;_:Array [Int ,0X17]){} }Class _:p_Z7{ze9sc(_,E,__,n,Ry:Array [Float ,24];r__0__,__5:Array [Array [Array [String ,0X17],1],0b11];_Y:Float ;_:Array [Boolean ,67];_:Float ;G34:Array [Array [Array [Array [Array [Boolean ,0b110000],0B1],0B1_0_0],24],7];_,X,A7:String ){} }Class n{}''',
                '''Class,_,:,__s_,{,Constructor,(,_1ll,:,String,;,I,:,Int,;,_,,,_9,,,_,,,_2_,:,__e,;,_,:,Array,[,Int,,,0X17,],),{,},},Class,_,:,p_Z7,{,ze9sc,(,_,,,E,,,__,,,n,,,Ry,:,Array,[,Float,,,24,],;,r__0__,,,__5,:,Array,[,Array,[,Array,[,String,,,0X17,],,,1,],,,0b11,],;,_Y,:,Float,;,_,:,Array,[,Boolean,,,67,],;,_,:,Float,;,G34,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b110000,],,,0B1,],,,0B100,],,,24,],,,7,],;,_,,,X,,,A7,:,String,),{,},},Class,n,{,},<EOF>''',
                101
            )
        )

    def test_740(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8_:Q{D_l(y,_F,_n:Boolean ){Var _:Array [Int ,046];}h9_n(_T:Float ;n,L018,_,F0,_6_:l06){Val _9:Float ;} }''',
                '''Class,_8_,:,Q,{,D_l,(,y,,,_F,,,_n,:,Boolean,),{,Var,_,:,Array,[,Int,,,046,],;,},h9_n,(,_T,:,Float,;,n,,,L018,,,_,,,F0,,,_6_,:,l06,),{,Val,_9,:,Float,;,},},<EOF>''',
                101
            )
        )

    def test_741(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class Y:d{$__(N:Boolean ;X,__:H;n_,la__,R:_2y){Break ;} }Class _:Z7t{}Class A:_{Destructor (){} }Class ___{}Class j2J{_(iu_,G,V:v;_:String ;__:Array [Boolean ,1];_Q,o:_6){ {Return ;} }}''',
                '''Class,_,{,},Class,Y,:,d,{,$__,(,N,:,Boolean,;,X,,,__,:,H,;,n_,,,la__,,,R,:,_2y,),{,Break,;,},},Class,_,:,Z7t,{,},Class,A,:,_,{,Destructor,(,),{,},},Class,___,{,},Class,j2J,{,_,(,iu_,,,G,,,V,:,v,;,_,:,String,;,__,:,Array,[,Boolean,,,1,],;,_Q,,,o,:,_6,),{,{,Return,;,},},},<EOF>''',
                101
            )
        )

    def test_742(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w:P_rb6{Val _,$__J,p:Array [String ,03];Constructor (_Lh8_,__y:Array [Array [Float ,0x29],0x29];_:__;d_W,R,e29:Int ){} }Class _:a{}''',
                '''Class,w,:,P_rb6,{,Val,_,,,$__J,,,p,:,Array,[,String,,,03,],;,Constructor,(,_Lh8_,,,__y,:,Array,[,Array,[,Float,,,0x29,],,,0x29,],;,_,:,__,;,d_W,,,R,,,e29,:,Int,),{,},},Class,_,:,a,{,},<EOF>''',
                101
            )
        )

    def test_743(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __S__{Destructor (){Continue ;} }Class X:_q{}Class N{n91(_,xZ:Array [Array [Array [Array [String ,0B1011101],3810_4],031],02];___,_3__:x5){Break ;} }Class J:u{}Class fE_8_{Destructor (){}$76g3(){}Var U,$9_:_;}''',
                '''Class,__S__,{,Destructor,(,),{,Continue,;,},},Class,X,:,_q,{,},Class,N,{,n91,(,_,,,xZ,:,Array,[,Array,[,Array,[,Array,[,String,,,0B1011101,],,,38104,],,,031,],,,02,],;,___,,,_3__,:,x5,),{,Break,;,},},Class,J,:,u,{,},Class,fE_8_,{,Destructor,(,),{,},$76g3,(,),{,},Var,U,,,$9_,:,_,;,},<EOF>''',
                101
            )
        )

    def test_744(self):
        self.assertTrue(
            TestLexer.test(
                '''Class x:_{}Class u{}Class S{}Class k:_{}Class A_0s{}Class b46:_{Var Tw,$gM:LlRU;}Class B1_3{Var _:y_G;}Class _:H{}''',
                '''Class,x,:,_,{,},Class,u,{,},Class,S,{,},Class,k,:,_,{,},Class,A_0s,{,},Class,b46,:,_,{,Var,Tw,,,$gM,:,LlRU,;,},Class,B1_3,{,Var,_,:,y_G,;,},Class,_,:,H,{,},<EOF>''',
                101
            )
        )

    def test_745(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:G4{Destructor (){}$u__(_771Y_,u_y_:Array [String ,0b111000];w_U4Q__,_:String ;_9_2_7Y,y,P:Int ;V0:Int ){} }Class _{}''',
                '''Class,__,:,G4,{,Destructor,(,),{,},$u__,(,_771Y_,,,u_y_,:,Array,[,String,,,0b111000,],;,w_U4Q__,,,_,:,String,;,_9_2_7Y,,,y,,,P,:,Int,;,V0,:,Int,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_746(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __Ml:o_{Constructor (_:String ;_888,o:_;__:_a_){Break ;}Constructor (){} }Class _:_{}Class _:_4_{Destructor (){Break ;} }Class C:_W_{}''',
                '''Class,__Ml,:,o_,{,Constructor,(,_,:,String,;,_888,,,o,:,_,;,__,:,_a_,),{,Break,;,},Constructor,(,),{,},},Class,_,:,_,{,},Class,_,:,_4_,{,Destructor,(,),{,Break,;,},},Class,C,:,_W_,{,},<EOF>''',
                101
            )
        )

    def test_747(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9{$_4o(P,_:Array [Array [Array [Array [Array [String ,02252],0x36],22],22],22]){}Constructor (W,_:O){}$X(_E,_48:c;T,n,u:F;g1,_V:Array [String ,0B1000010]){}$1(__:Array [Array [Array [Boolean ,0xB_4_8],0x36],0b10];j0,_7:Boolean ){} }''',
                '''Class,_9,{,$_4o,(,P,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,02252,],,,0x36,],,,22,],,,22,],,,22,],),{,},Constructor,(,W,,,_,:,O,),{,},$X,(,_E,,,_48,:,c,;,T,,,n,,,u,:,F,;,g1,,,_V,:,Array,[,String,,,0B1000010,],),{,},$1,(,__,:,Array,[,Array,[,Array,[,Boolean,,,0xB48,],,,0x36,],,,0b10,],;,j0,,,_7,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_748(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _4W{Val w:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0b1],0x19],42],051],0B1],42],0X7_D],051];i(j86R,dv0,E:Float ;j_:Array [String ,2_0_4_50];B1v,_1,_i_15,N_,u,u:_;_,_,_Z:_;X4:I4;___P,__,__,_:Int ;F,z:Array [String ,0B1]){}Destructor (){}Constructor (){} }''',
                '''Class,_4W,{,Val,w,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1,],,,0x19,],,,42,],,,051,],,,0B1,],,,42,],,,0X7D,],,,051,],;,i,(,j86R,,,dv0,,,E,:,Float,;,j_,:,Array,[,String,,,20450,],;,B1v,,,_1,,,_i_15,,,N_,,,u,,,u,:,_,;,_,,,_,,,_Z,:,_,;,X4,:,I4,;,___P,,,__,,,__,,,_,:,Int,;,F,,,z,:,Array,[,String,,,0B1,],),{,},Destructor,(,),{,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_749(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n:x1{Val _P:Array [Array [Array [Boolean ,052],7_02_7],0xE_6];Constructor (_,Al,__K,_P4:__;_c:Array [Array [Boolean ,04_1_1],0106]){} }''',
                '''Class,n,:,x1,{,Val,_P,:,Array,[,Array,[,Array,[,Boolean,,,052,],,,7027,],,,0xE6,],;,Constructor,(,_,,,Al,,,__K,,,_P4,:,__,;,_c,:,Array,[,Array,[,Boolean,,,0411,],,,0106,],),{,},},<EOF>''',
                101
            )
        )

    def test_750(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:u{Val $0P:Array [Boolean ,0B1];$1_bmJ(t,_a:Array [Int ,0X13]){}Constructor (z_2,e:Array [Array [Int ,13],895_5];v_:String ;_:String ){Break ;Break ;{} }}''',
                '''Class,_,:,u,{,Val,$0P,:,Array,[,Boolean,,,0B1,],;,$1_bmJ,(,t,,,_a,:,Array,[,Int,,,0X13,],),{,},Constructor,(,z_2,,,e,:,Array,[,Array,[,Int,,,13,],,,8955,],;,v_,:,String,;,_,:,String,),{,Break,;,Break,;,{,},},},<EOF>''',
                101
            )
        )

    def test_751(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0{Destructor (){Var __:Boolean ;} }Class t:zE_{Val $nw6:Q48906;Var $3,d,$u4:w_;_(){} }Class _:F_{}Class F:U{}''',
                '''Class,_0,{,Destructor,(,),{,Var,__,:,Boolean,;,},},Class,t,:,zE_,{,Val,$nw6,:,Q48906,;,Var,$3,,,d,,,$u4,:,w_,;,_,(,),{,},},Class,_,:,F_,{,},Class,F,:,U,{,},<EOF>''',
                101
            )
        )

    def test_752(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k_:L__{Val Z:Array [Array [Array [Array [String ,0x59],03],0b101011],067_7_5];Var L2:Array [Boolean ,063];}Class _:V{Destructor (){}Destructor (){}_3(){Continue ;} }Class O{}Class _8{}''',
                '''Class,k_,:,L__,{,Val,Z,:,Array,[,Array,[,Array,[,Array,[,String,,,0x59,],,,03,],,,0b101011,],,,06775,],;,Var,L2,:,Array,[,Boolean,,,063,],;,},Class,_,:,V,{,Destructor,(,),{,},Destructor,(,),{,},_3,(,),{,Continue,;,},},Class,O,{,},Class,_8,{,},<EOF>''',
                101
            )
        )

    def test_753(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _G4_{Val K:String ;Val $4_,_,$2,eMr,$L0:Array [String ,0B101111];Val $3,$c60_E_e_,b_:String ;}Class X:_k{}Class H_{}''',
                '''Class,_G4_,{,Val,K,:,String,;,Val,$4_,,,_,,,$2,,,eMr,,,$L0,:,Array,[,String,,,0B101111,],;,Val,$3,,,$c60_E_e_,,,b_,:,String,;,},Class,X,:,_k,{,},Class,H_,{,},<EOF>''',
                101
            )
        )

    def test_754(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _4{Constructor (_5_,_4V_:Array [Array [Array [Boolean ,0X36],016],0B100]){Break ;} }Class h51299:G{}Class ___:_{Var Q__w,$2t_,$9,pm:Float ;}''',
                '''Class,_4,{,Constructor,(,_5_,,,_4V_,:,Array,[,Array,[,Array,[,Boolean,,,0X36,],,,016,],,,0B100,],),{,Break,;,},},Class,h51299,:,G,{,},Class,___,:,_,{,Var,Q__w,,,$2t_,,,$9,,,pm,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_755(self):
        self.assertTrue(
            TestLexer.test(
                '''Class R4{Var $P_,$_67Q:Array [Array [Float ,8_550],02_6_24_0_5];Constructor (K8,__,_2N,HW_,X,n:Array [Int ,0X1_D]){}$_B(){} }''',
                '''Class,R4,{,Var,$P_,,,$_67Q,:,Array,[,Array,[,Float,,,8550,],,,0262405,],;,Constructor,(,K8,,,__,,,_2N,,,HW_,,,X,,,n,:,Array,[,Int,,,0X1D,],),{,},$_B,(,),{,},},<EOF>''',
                101
            )
        )

    def test_756(self):
        self.assertTrue(
            TestLexer.test(
                '''Class e{Var ___V9O,f,$__Z,$59,$n,___6:Array [Array [Array [Array [Int ,0605_2],19],0103],0b1000100];Constructor (_,KI,B:Array [Array [String ,0XBB],0x9];O:Array [Array [String ,0B1],19];_:Float ;R__43TZQi:s;_u:Int ){}Destructor (){} }Class u:l_9{}Class u{}''',
                '''Class,e,{,Var,___V9O,,,f,,,$__Z,,,$59,,,$n,,,___6,:,Array,[,Array,[,Array,[,Array,[,Int,,,06052,],,,19,],,,0103,],,,0b1000100,],;,Constructor,(,_,,,KI,,,B,:,Array,[,Array,[,String,,,0XBB,],,,0x9,],;,O,:,Array,[,Array,[,String,,,0B1,],,,19,],;,_,:,Float,;,R__43TZQi,:,s,;,_u,:,Int,),{,},Destructor,(,),{,},},Class,u,:,l_9,{,},Class,u,{,},<EOF>''',
                101
            )
        )

    def test_757(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0_P:__{}Class W1:f0{Var _:Array [Int ,0b10];}Class _6{$g(c,_,q_E6_:i;G_:Array [Boolean ,9]){}Var $e,$_Q,c,E__0I1:Int ;}Class V__4:Z{}''',
                '''Class,_0_P,:,__,{,},Class,W1,:,f0,{,Var,_,:,Array,[,Int,,,0b10,],;,},Class,_6,{,$g,(,c,,,_,,,q_E6_,:,i,;,G_,:,Array,[,Boolean,,,9,],),{,},Var,$e,,,$_Q,,,c,,,E__0I1,:,Int,;,},Class,V__4,:,Z,{,},<EOF>''',
                101
            )
        )

    def test_758(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___:H{Constructor (__,w_,P_,__,i_1___,Z:Int ;_3,_q,_,_,A1,X,J7:Int ;B,_r_:Boolean ){Return ;}Var $2j_,oG,_W7,$__,_:String ;Constructor (){}Destructor (){Val w,v0,_8,_,Q,_b,z:String ;} }''',
                '''Class,___,:,H,{,Constructor,(,__,,,w_,,,P_,,,__,,,i_1___,,,Z,:,Int,;,_3,,,_q,,,_,,,_,,,A1,,,X,,,J7,:,Int,;,B,,,_r_,:,Boolean,),{,Return,;,},Var,$2j_,,,oG,,,_W7,,,$__,,,_,:,String,;,Constructor,(,),{,},Destructor,(,),{,Val,w,,,v0,,,_8,,,_,,,Q,,,_b,,,z,:,String,;,},},<EOF>''',
                101
            )
        )

    def test_759(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:__2{}Class J:_1T4{}Class _1{}Class __O:___2{Var a,$1:Array [Array [Array [Array [Array [Array [Array [Array [String ,711_77],0b1001111],0x87_C_A3_B],0b1001111],0b1],0b1],0X5],05];Val $h,w9,$w7,$5g,_,_Ae94g:Boolean ;}''',
                '''Class,__,:,__2,{,},Class,J,:,_1T4,{,},Class,_1,{,},Class,__O,:,___2,{,Var,a,,,$1,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,71177,],,,0b1001111,],,,0x87CA3B,],,,0b1001111,],,,0b1,],,,0b1,],,,0X5,],,,05,],;,Val,$h,,,w9,,,$w7,,,$5g,,,_,,,_Ae94g,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_760(self):
        self.assertTrue(
            TestLexer.test(
                '''Class L{_(c__,T:_;_:Array [Int ,0x4A]){}Val $5,Z_,$70:Boolean ;Constructor (){}Var _,_:Array [Array [Array [Boolean ,0x4A],0B1001110],0B1001110];Val _:Array [Boolean ,0X5];Destructor (){ {} }Constructor (_9_,_eBX__6_j:r){Continue ;Val _,_:Float ;} }''',
                '''Class,L,{,_,(,c__,,,T,:,_,;,_,:,Array,[,Int,,,0x4A,],),{,},Val,$5,,,Z_,,,$70,:,Boolean,;,Constructor,(,),{,},Var,_,,,_,:,Array,[,Array,[,Array,[,Boolean,,,0x4A,],,,0B1001110,],,,0B1001110,],;,Val,_,:,Array,[,Boolean,,,0X5,],;,Destructor,(,),{,{,},},Constructor,(,_9_,,,_eBX__6_j,:,r,),{,Continue,;,Val,_,,,_,:,Float,;,},},<EOF>''',
                101
            )
        )

    def test_761(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:__T{Val $_:__;$x(){} }Class g{}Class k_:N{}Class _:q_{Constructor (){} }Class __{}Class Y:p{Var $9g:Ehn;}Class _2:P72{}Class __98{}Class _{}''',
                '''Class,_,:,__T,{,Val,$_,:,__,;,$x,(,),{,},},Class,g,{,},Class,k_,:,N,{,},Class,_,:,q_,{,Constructor,(,),{,},},Class,__,{,},Class,Y,:,p,{,Var,$9g,:,Ehn,;,},Class,_2,:,P72,{,},Class,__98,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_762(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n{}Class _{Constructor (_,if,_j:Int ;F,_RX___:Int ;Gm1,_W_9:_;N2,_:Array [Array [Array [String ,0X1E],0b110110],54];_,rn4Dw66_,_:Boolean ){}Constructor (_,__,_F:t){} }''',
                '''Class,n,{,},Class,_,{,Constructor,(,_,,,if,,,_j,:,Int,;,F,,,_RX___,:,Int,;,Gm1,,,_W_9,:,_,;,N2,,,_,:,Array,[,Array,[,Array,[,String,,,0X1E,],,,0b110110,],,,54,],;,_,,,rn4Dw66_,,,_,:,Boolean,),{,},Constructor,(,_,,,__,,,_F,:,t,),{,},},<EOF>''',
                101
            )
        )

    def test_763(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:g{Val $86,$W,uV,$5_:Array [Array [Array [Array [Boolean ,9_8],0B111000],0B111000],02];}Class G5__:D{Constructor (){} }''',
                '''Class,_,:,g,{,Val,$86,,,$W,,,uV,,,$5_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,98,],,,0B111000,],,,0B111000,],,,02,],;,},Class,G5__,:,D,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_764(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:K0{Destructor (){}Var $w,_1:Array [Float ,0b110100];}Class _G_5:J__{Destructor (){}qS(_0__0:Array [Array [Boolean ,33],4]){} }''',
                '''Class,_,:,K0,{,Destructor,(,),{,},Var,$w,,,_1,:,Array,[,Float,,,0b110100,],;,},Class,_G_5,:,J__,{,Destructor,(,),{,},qS,(,_0__0,:,Array,[,Array,[,Boolean,,,33,],,,4,],),{,},},<EOF>''',
                101
            )
        )

    def test_765(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __j:j{}Class DRP_d_:_h{_(){ {}{}Val w,p,ZD,__o:Array [Array [Array [Array [Boolean ,0x2],18],0B1001011],0143];} }Class _{}''',
                '''Class,__j,:,j,{,},Class,DRP_d_,:,_h,{,_,(,),{,{,},{,},Val,w,,,p,,,ZD,,,__o,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x2,],,,18,],,,0B1001011,],,,0143,],;,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_766(self):
        self.assertTrue(
            TestLexer.test(
                '''Class e{Val $9__,___,$F2_:Int ;Destructor (){Val _Z:__;}Val $9u_,W4,$1:Array [Float ,02];Var w:W;Constructor (){} }''',
                '''Class,e,{,Val,$9__,,,___,,,$F2_,:,Int,;,Destructor,(,),{,Val,_Z,:,__,;,},Val,$9u_,,,W4,,,$1,:,Array,[,Float,,,02,],;,Var,w,:,W,;,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_767(self):
        self.assertTrue(
            TestLexer.test(
                '''Class i2{$x_(I:M;K:String ;V,_36,k_,I:String ;_:Float ;_,__:String ;_60___2,_C,__,n_C_,____,_c_1,_,_:Float ){} }''',
                '''Class,i2,{,$x_,(,I,:,M,;,K,:,String,;,V,,,_36,,,k_,,,I,:,String,;,_,:,Float,;,_,,,__,:,String,;,_60___2,,,_C,,,__,,,n_C_,,,____,,,_c_1,,,_,,,_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_768(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _q_:O5{Constructor (_:Array [Boolean ,0135]){}Constructor (){}$e_dx38_(su,Dm1,Tdj0O,_o_,_8iq,_7:Array [Float ,0X4];y:Array [Int ,01]){} }Class _65__:E{}Class DT:_{}''',
                '''Class,_q_,:,O5,{,Constructor,(,_,:,Array,[,Boolean,,,0135,],),{,},Constructor,(,),{,},$e_dx38_,(,su,,,Dm1,,,Tdj0O,,,_o_,,,_8iq,,,_7,:,Array,[,Float,,,0X4,],;,y,:,Array,[,Int,,,01,],),{,},},Class,_65__,:,E,{,},Class,DT,:,_,{,},<EOF>''',
                101
            )
        )

    def test_769(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _X_9:_N{Constructor (g_:Array [Array [Array [String ,56],0b1],0x1_F_B_0_56_B];_a:Array [Boolean ,0x5];C:Float ;___,h:g){} }''',
                '''Class,_X_9,:,_N,{,Constructor,(,g_,:,Array,[,Array,[,Array,[,String,,,56,],,,0b1,],,,0x1FB056B,],;,_a,:,Array,[,Boolean,,,0x5,],;,C,:,Float,;,___,,,h,:,g,),{,},},<EOF>''',
                101
            )
        )

    def test_770(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class b{Constructor (G,_B:_0;_,_,U_:Array [Array [Array [String ,51],51],017];_A2_,Xr1,a,o:Int ){Continue ;} }Class G:_8__{Val $D:Array [Float ,0x22];}Class R_{}''',
                '''Class,_,{,},Class,b,{,Constructor,(,G,,,_B,:,_0,;,_,,,_,,,U_,:,Array,[,Array,[,Array,[,String,,,51,],,,51,],,,017,],;,_A2_,,,Xr1,,,a,,,o,:,Int,),{,Continue,;,},},Class,G,:,_8__,{,Val,$D,:,Array,[,Float,,,0x22,],;,},Class,R_,{,},<EOF>''',
                101
            )
        )

    def test_771(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_2_{Val _:Array [Boolean ,0B1];Constructor (__q:Array [Boolean ,011];_K_:String ;r:Array [Array [Int ,5],78];c13_G:Array [Array [Boolean ,011],077];_b,_:u){} }''',
                '''Class,_,:,_2_,{,Val,_,:,Array,[,Boolean,,,0B1,],;,Constructor,(,__q,:,Array,[,Boolean,,,011,],;,_K_,:,String,;,r,:,Array,[,Array,[,Int,,,5,],,,78,],;,c13_G,:,Array,[,Array,[,Boolean,,,011,],,,077,],;,_b,,,_,:,u,),{,},},<EOF>''',
                101
            )
        )

    def test_772(self):
        self.assertTrue(
            TestLexer.test(
                '''Class G__3:_1_0{}Class _G_:_{Var _4:Boolean ;}Class P_:__{Var $__,$Q,$4,$_,$zZp:Array [Float ,94_8_4];}Class __{}''',
                '''Class,G__3,:,_1_0,{,},Class,_G_,:,_,{,Var,_4,:,Boolean,;,},Class,P_,:,__,{,Var,$__,,,$Q,,,$4,,,$_,,,$zZp,:,Array,[,Float,,,9484,],;,},Class,__,{,},<EOF>''',
                101
            )
        )

    def test_773(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:_{I(){}$i(__Vp0V,_:Array [Boolean ,0B1];ZFPkn2:Array [Int ,89];pLe,D_C,n0,x,__tS:_;_,p:String ;_:Boolean ){}Constructor (_P____,_,i:Int ;_:Array [Float ,0X4C]){}Destructor (){} }''',
                '''Class,__,:,_,{,I,(,),{,},$i,(,__Vp0V,,,_,:,Array,[,Boolean,,,0B1,],;,ZFPkn2,:,Array,[,Int,,,89,],;,pLe,,,D_C,,,n0,,,x,,,__tS,:,_,;,_,,,p,:,String,;,_,:,Boolean,),{,},Constructor,(,_P____,,,_,,,i,:,Int,;,_,:,Array,[,Float,,,0X4C,],),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_774(self):
        self.assertTrue(
            TestLexer.test(
                '''Class c_g{Var Z:Array [Array [String ,0b1_1],01];$_(p:Float ){}$11A(_,Le:Array [Boolean ,0b1];n_:Array [Array [Float ,0b1],0B1];_2,_,_1_N:Array [Int ,0110]){}Var $__,$3,F:_8;}''',
                '''Class,c_g,{,Var,Z,:,Array,[,Array,[,String,,,0b11,],,,01,],;,$_,(,p,:,Float,),{,},$11A,(,_,,,Le,:,Array,[,Boolean,,,0b1,],;,n_,:,Array,[,Array,[,Float,,,0b1,],,,0B1,],;,_2,,,_,,,_1_N,:,Array,[,Int,,,0110,],),{,},Var,$__,,,$3,,,F,:,_8,;,},<EOF>''',
                101
            )
        )

    def test_775(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_w,_,_m_B,_:Array [Array [Float ,0x3],0B1101];A:Int ;M9_,T,J,h_1Z:Array [Array [String ,0X38],0B1_1_0];Z,Og,_:Array [Float ,055];_,_,_:Float ;_,_,_:Float ;_,p8,_,_2,__,_:Array [Array [Array [Int ,9],25],0X38]){ {Var c,_4,Cn_,_,Ho:T8_y582;} }Val $g9,$3_2,_,$_,_:String ;}''',
                '''Class,_,{,Constructor,(,_w,,,_,,,_m_B,,,_,:,Array,[,Array,[,Float,,,0x3,],,,0B1101,],;,A,:,Int,;,M9_,,,T,,,J,,,h_1Z,:,Array,[,Array,[,String,,,0X38,],,,0B110,],;,Z,,,Og,,,_,:,Array,[,Float,,,055,],;,_,,,_,,,_,:,Float,;,_,,,_,,,_,:,Float,;,_,,,p8,,,_,,,_2,,,__,,,_,:,Array,[,Array,[,Array,[,Int,,,9,],,,25,],,,0X38,],),{,{,Var,c,,,_4,,,Cn_,,,_,,,Ho,:,T8_y582,;,},},Val,$g9,,,$3_2,,,_,,,$_,,,_,:,String,;,},<EOF>''',
                101
            )
        )

    def test_776(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7:_{}Class _38:O{$__(P7M,__S_:Boolean ;H,_vC_9_:Float ;c18_,E,_:Array [String ,96];_5,Qcy__:_){}Var $y,$_:String ;Val R85,$_:G;_(i:Int ;__,_,_5,a,_:Array [Int ,075]){} }Class C{}''',
                '''Class,_7,:,_,{,},Class,_38,:,O,{,$__,(,P7M,,,__S_,:,Boolean,;,H,,,_vC_9_,:,Float,;,c18_,,,E,,,_,:,Array,[,String,,,96,],;,_5,,,Qcy__,:,_,),{,},Var,$y,,,$_,:,String,;,Val,R85,,,$_,:,G,;,_,(,i,:,Int,;,__,,,_,,,_5,,,a,,,_,:,Array,[,Int,,,075,],),{,},},Class,C,{,},<EOF>''',
                101
            )
        )

    def test_777(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __X:_h7{Constructor (N,_Pv4_:Array [Array [Boolean ,027],0x1B];_,t_,y5__:Array [Array [Boolean ,3],47_6];_4,_,_,_,_O,q1_27V,_v9L_bD_:Array [Array [Int ,40],0XD];Z,b_:_;_:String ;V5_,_0,w_2H_,_:Array [Int ,07];_y,__:_;I:Array [Int ,3]){}Val __h,$_4:Array [Array [String ,6_3],0576];}''',
                '''Class,__X,:,_h7,{,Constructor,(,N,,,_Pv4_,:,Array,[,Array,[,Boolean,,,027,],,,0x1B,],;,_,,,t_,,,y5__,:,Array,[,Array,[,Boolean,,,3,],,,476,],;,_4,,,_,,,_,,,_,,,_O,,,q1_27V,,,_v9L_bD_,:,Array,[,Array,[,Int,,,40,],,,0XD,],;,Z,,,b_,:,_,;,_,:,String,;,V5_,,,_0,,,w_2H_,,,_,:,Array,[,Int,,,07,],;,_y,,,__,:,_,;,I,:,Array,[,Int,,,3,],),{,},Val,__h,,,$_4,:,Array,[,Array,[,String,,,63,],,,0576,],;,},<EOF>''',
                101
            )
        )

    def test_778(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val _:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0B1011001],01],0b1011010],0x39],0B1011001],0B1011001],10_581],0b1_000];}Class _{Var $4:Array [Array [Array [Array [Array [Boolean ,8],62],01_20_3],0b10_01],62];}''',
                '''Class,_,{,Val,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1011001,],,,01,],,,0b1011010,],,,0x39,],,,0B1011001,],,,0B1011001,],,,10581,],,,0b1000,],;,},Class,_,{,Var,$4,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,8,],,,62,],,,01203,],,,0b1001,],,,62,],;,},<EOF>''',
                101
            )
        )

    def test_779(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ____{Constructor (w:Array [Array [Boolean ,0b1_01],0XE];W:__3;h,w,y:Array [Int ,0b10];f7,_207Zq6,L0,_,_,_3,H,g,k_,o:Int ){} }''',
                '''Class,____,{,Constructor,(,w,:,Array,[,Array,[,Boolean,,,0b101,],,,0XE,],;,W,:,__3,;,h,,,w,,,y,:,Array,[,Int,,,0b10,],;,f7,,,_207Zq6,,,L0,,,_,,,_,,,_3,,,H,,,g,,,k_,,,o,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_780(self):
        self.assertTrue(
            TestLexer.test(
                '''Class H6:_S_{}Class Z{Destructor (){}Var JV7_,r,$36_,R_,$Z_:Array [String ,0b1_00];Destructor (){}$x0(__2:Float ;l:Array [Boolean ,034]){}Var $9y66,p:_;}''',
                '''Class,H6,:,_S_,{,},Class,Z,{,Destructor,(,),{,},Var,JV7_,,,r,,,$36_,,,R_,,,$Z_,:,Array,[,String,,,0b100,],;,Destructor,(,),{,},$x0,(,__2,:,Float,;,l,:,Array,[,Boolean,,,034,],),{,},Var,$9y66,,,p,:,_,;,},<EOF>''',
                101
            )
        )

    def test_781(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P:F0{}Class g_d:_{Constructor (__:_;V:Array [Array [Boolean ,0x1],0x2F]){}Destructor (){}Var T5:_;}Class l:l{}''',
                '''Class,P,:,F0,{,},Class,g_d,:,_,{,Constructor,(,__,:,_,;,V,:,Array,[,Array,[,Boolean,,,0x1,],,,0x2F,],),{,},Destructor,(,),{,},Var,T5,:,_,;,},Class,l,:,l,{,},<EOF>''',
                101
            )
        )

    def test_782(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{$_(){} }Class _n6p:__{Var _,$8,_:Array [Array [Array [Array [Array [Array [String ,88],0B110_1],0XC],7],02],88];}Class cc{Constructor (){} }Class S_{}''',
                '''Class,__,{,$_,(,),{,},},Class,_n6p,:,__,{,Var,_,,,$8,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,88,],,,0B1101,],,,0XC,],,,7,],,,02,],,,88,],;,},Class,cc,{,Constructor,(,),{,},},Class,S_,{,},<EOF>''',
                101
            )
        )

    def test_783(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _C:_2{Var _b,$6,$_72:Int ;Val z:String ;Var $h8_,__:Array [Float ,07];}Class _{Val _:Array [Array [Boolean ,0120],0B1];}Class k0{Constructor (_:_){} }''',
                '''Class,_C,:,_2,{,Var,_b,,,$6,,,$_72,:,Int,;,Val,z,:,String,;,Var,$h8_,,,__,:,Array,[,Float,,,07,],;,},Class,_,{,Val,_,:,Array,[,Array,[,Boolean,,,0120,],,,0B1,],;,},Class,k0,{,Constructor,(,_,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_784(self):
        self.assertTrue(
            TestLexer.test(
                '''Class O_{Constructor (__ay,J:Array [Array [Boolean ,0X95],0B1];_5q__y__,_,C:Array [Array [Array [Array [Boolean ,0b111001],0X23],0112],34];B:Array [Array [Float ,0xB],067];A,Y_,_Z51:__){} }''',
                '''Class,O_,{,Constructor,(,__ay,,,J,:,Array,[,Array,[,Boolean,,,0X95,],,,0B1,],;,_5q__y__,,,_,,,C,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b111001,],,,0X23,],,,0112,],,,34,],;,B,:,Array,[,Array,[,Float,,,0xB,],,,067,],;,A,,,Y_,,,_Z51,:,__,),{,},},<EOF>''',
                101
            )
        )

    def test_785(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_4,D,r:Array [Array [Int ,0B1],052];f:Array [Array [Array [Float ,0b1],46],0b101000];_:String ){Break ;} }Class c:__63{Destructor (){ {} }}''',
                '''Class,_,{,Constructor,(,_4,,,D,,,r,:,Array,[,Array,[,Int,,,0B1,],,,052,],;,f,:,Array,[,Array,[,Array,[,Float,,,0b1,],,,46,],,,0b101000,],;,_,:,String,),{,Break,;,},},Class,c,:,__63,{,Destructor,(,),{,{,},},},<EOF>''',
                101
            )
        )

    def test_786(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _n{Var $07_,_,$_C:String ;Constructor (U,P,MUD_,_:a2__;Z:Array [Boolean ,0x27];_1,_,__,_:Array [Array [Float ,0b1],2]){}$_(){Continue ;Var V,_,_X7:_;Break ;} }''',
                '''Class,_n,{,Var,$07_,,,_,,,$_C,:,String,;,Constructor,(,U,,,P,,,MUD_,,,_,:,a2__,;,Z,:,Array,[,Boolean,,,0x27,],;,_1,,,_,,,__,,,_,:,Array,[,Array,[,Float,,,0b1,],,,2,],),{,},$_,(,),{,Continue,;,Var,V,,,_,,,_X7,:,_,;,Break,;,},},<EOF>''',
                101
            )
        )

    def test_787(self):
        self.assertTrue(
            TestLexer.test(
                '''Class D{Constructor (){} }Class __:_Sm{_57(_:Array [Array [Int ,0B1],04_66];N_9,F8,_,_J0_:Boolean ){} }Class A{}Class Q__:_2{}Class N{}Class j{}''',
                '''Class,D,{,Constructor,(,),{,},},Class,__,:,_Sm,{,_57,(,_,:,Array,[,Array,[,Int,,,0B1,],,,0466,],;,N_9,,,F8,,,_,,,_J0_,:,Boolean,),{,},},Class,A,{,},Class,Q__,:,_2,{,},Class,N,{,},Class,j,{,},<EOF>''',
                101
            )
        )

    def test_788(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _l{}Class _2:_9{}Class __:_7{G(WQ_,g9,IZ:Array [Array [Array [Boolean ,0b10_1],0x5D],0B1_0]){}$u_(R:Array [Array [Float ,7],0B10_1_0]){} }''',
                '''Class,_l,{,},Class,_2,:,_9,{,},Class,__,:,_7,{,G,(,WQ_,,,g9,,,IZ,:,Array,[,Array,[,Array,[,Boolean,,,0b101,],,,0x5D,],,,0B10,],),{,},$u_,(,R,:,Array,[,Array,[,Float,,,7,],,,0B1010,],),{,},},<EOF>''',
                101
            )
        )

    def test_789(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:__579_{}Class _38:_{Constructor (h,_1B,EY:Array [String ,0x2]){}Val $F,a,$V:String ;}Class G4___z87FE___:e2__{}Class __:_{Destructor (){} }''',
                '''Class,__,:,__579_,{,},Class,_38,:,_,{,Constructor,(,h,,,_1B,,,EY,:,Array,[,String,,,0x2,],),{,},Val,$F,,,a,,,$V,:,String,;,},Class,G4___z87FE___,:,e2__,{,},Class,__,:,_,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_790(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9Qnc{Constructor (){}Destructor (){} }Class _{Var _,Z,$2_,_1_:Array [Boolean ,0b101011];}Class _7_{Var _8:Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,5],0x1E],5],012],0X5F],0B10_0_11],0B11],3],0X5F];}Class u_:_{Constructor (t0_,Mh_:t3_;_9,U,n7,QC6,q,__:Boolean ;zo_L_:String ;_5:l;_50:Array [Array [String ,0b1],016];_,_,_W,D1Zd_3:Array [Float ,0XCA_8_F_C]){} }Class H{}''',
                '''Class,_9Qnc,{,Constructor,(,),{,},Destructor,(,),{,},},Class,_,{,Var,_,,,Z,,,$2_,,,_1_,:,Array,[,Boolean,,,0b101011,],;,},Class,_7_,{,Var,_8,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,5,],,,0x1E,],,,5,],,,012,],,,0X5F,],,,0B10011,],,,0B11,],,,3,],,,0X5F,],;,},Class,u_,:,_,{,Constructor,(,t0_,,,Mh_,:,t3_,;,_9,,,U,,,n7,,,QC6,,,q,,,__,:,Boolean,;,zo_L_,:,String,;,_5,:,l,;,_50,:,Array,[,Array,[,String,,,0b1,],,,016,],;,_,,,_,,,_W,,,D1Zd_3,:,Array,[,Float,,,0XCA8FC,],),{,},},Class,H,{,},<EOF>''',
                101
            )
        )

    def test_791(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Vw{}Class _X:_n_{_(_,_Dc,m,_1,U,K_:Array [Array [Int ,37_1],54];C,i,yY,__:Int ;N8_,c_g2,__,_:String ){}Constructor (){} }''',
                '''Class,Vw,{,},Class,_X,:,_n_,{,_,(,_,,,_Dc,,,m,,,_1,,,U,,,K_,:,Array,[,Array,[,Int,,,371,],,,54,],;,C,,,i,,,yY,,,__,:,Int,;,N8_,,,c_g2,,,__,,,_,:,String,),{,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_792(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_4h{$_(z_E,_W23_:Boolean ){Continue ;Break ;}Constructor (d__LB:Array [Float ,32];Z,_,f:Array [String ,0B1001010]){} }Class z6{}''',
                '''Class,_,:,_4h,{,$_,(,z_E,,,_W23_,:,Boolean,),{,Continue,;,Break,;,},Constructor,(,d__LB,:,Array,[,Float,,,32,],;,Z,,,_,,,f,:,Array,[,String,,,0B1001010,],),{,},},Class,z6,{,},<EOF>''',
                101
            )
        )

    def test_793(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X{Val $2:Array [Array [Array [Array [Array [Boolean ,013],0X93],0x9],6],0b111001];}Class _{Constructor (_91,y,UW:_t62;eL8,sK7,m,JZ_141:___h1){} }''',
                '''Class,X,{,Val,$2,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,013,],,,0X93,],,,0x9,],,,6,],,,0b111001,],;,},Class,_,{,Constructor,(,_91,,,y,,,UW,:,_t62,;,eL8,,,sK7,,,m,,,JZ_141,:,___h1,),{,},},<EOF>''',
                101
            )
        )

    def test_794(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __a{}Class UI:_{__(s:Array [Array [Array [Array [String ,0x29],0x29],06],0B1]){}Destructor (){}Val _,___,Y_:Array [Array [Float ,11],071];Destructor (){Break ;Continue ;} }''',
                '''Class,__a,{,},Class,UI,:,_,{,__,(,s,:,Array,[,Array,[,Array,[,Array,[,String,,,0x29,],,,0x29,],,,06,],,,0B1,],),{,},Destructor,(,),{,},Val,_,,,___,,,Y_,:,Array,[,Array,[,Float,,,11,],,,071,],;,Destructor,(,),{,Break,;,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_795(self):
        self.assertTrue(
            TestLexer.test(
                '''Class u:___{}Class ___{}Class ___{Constructor (X,_:J_;_u___,o:Array [Float ,2];_91,_:Array [Array [Array [Array [String ,67],0B1],0101],0X49]){} }''',
                '''Class,u,:,___,{,},Class,___,{,},Class,___,{,Constructor,(,X,,,_,:,J_,;,_u___,,,o,:,Array,[,Float,,,2,],;,_91,,,_,:,Array,[,Array,[,Array,[,Array,[,String,,,67,],,,0B1,],,,0101,],,,0X49,],),{,},},<EOF>''',
                101
            )
        )

    def test_796(self):
        self.assertTrue(
            TestLexer.test(
                '''Class iS{Constructor (o_Z:S;M:String ){}Var _:_;Destructor (){}Destructor (){}Var $g:Boolean ;Val $1F:String ;}''',
                '''Class,iS,{,Constructor,(,o_Z,:,S,;,M,:,String,),{,},Var,_,:,_,;,Destructor,(,),{,},Destructor,(,),{,},Var,$g,:,Boolean,;,Val,$1F,:,String,;,},<EOF>''',
                101
            )
        )

    def test_797(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2tHp_{_(__V,M:Array [Array [Array [Int ,0X10],0B110110],022];i9:u_;_0,_:Float ){}Var P,k,$4G:e;Val k,$K,_:H;}Class _:n_{}Class s:_{}Class _:ZS{}Class __3D8_{Val _:Float ;Destructor (){} }''',
                '''Class,_2tHp_,{,_,(,__V,,,M,:,Array,[,Array,[,Array,[,Int,,,0X10,],,,0B110110,],,,022,],;,i9,:,u_,;,_0,,,_,:,Float,),{,},Var,P,,,k,,,$4G,:,e,;,Val,k,,,$K,,,_,:,H,;,},Class,_,:,n_,{,},Class,s,:,_,{,},Class,_,:,ZS,{,},Class,__3D8_,{,Val,_,:,Float,;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_798(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E_{}Class C:q{Var $_128:Int ;Destructor (){}Constructor (jb008:Array [String ,61];_,H_3:Array [String ,0b11001];_:String ;_,_Za10V_:Array [Array [Array [Float ,61],61],0114];e__,T,in:Int ;h:L){}Var $7__B_7_Fsq,_,$g,$g7M:_;Var $m,$R,z,__:String ;}''',
                '''Class,E_,{,},Class,C,:,q,{,Var,$_128,:,Int,;,Destructor,(,),{,},Constructor,(,jb008,:,Array,[,String,,,61,],;,_,,,H_3,:,Array,[,String,,,0b11001,],;,_,:,String,;,_,,,_Za10V_,:,Array,[,Array,[,Array,[,Float,,,61,],,,61,],,,0114,],;,e__,,,T,,,in,:,Int,;,h,:,L,),{,},Var,$7__B_7_Fsq,,,_,,,$g,,,$g7M,:,_,;,Var,$m,,,$R,,,z,,,__,:,String,;,},<EOF>''',
                101
            )
        )

    def test_799(self):
        self.assertTrue(
            TestLexer.test(
                '''Class M{Constructor (g55,_g_:Int ;_:Boolean ;NX_:Array [Array [Boolean ,0142],34];_,dz67_g:Array [Boolean ,0xD8]){} }''',
                '''Class,M,{,Constructor,(,g55,,,_g_,:,Int,;,_,:,Boolean,;,NX_,:,Array,[,Array,[,Boolean,,,0142,],,,34,],;,_,,,dz67_g,:,Array,[,Boolean,,,0xD8,],),{,},},<EOF>''',
                101
            )
        )

    def test_800(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $Qt,X:__8;Val $4_g:Boolean ;}Class B{Constructor (u,_W_2,_9w,I,_j,s:Int ;D,X,h:__;_3:H0;VB_:Array [Array [Int ,0b110001],1]){ {} }}Class C0{}''',
                '''Class,_,{,Val,$Qt,,,X,:,__8,;,Val,$4_g,:,Boolean,;,},Class,B,{,Constructor,(,u,,,_W_2,,,_9w,,,I,,,_j,,,s,:,Int,;,D,,,X,,,h,:,__,;,_3,:,H0,;,VB_,:,Array,[,Array,[,Int,,,0b110001,],,,1,],),{,{,},},},Class,C0,{,},<EOF>''',
                101
            )
        )

    def test_801(self):
        self.assertTrue(
            TestLexer.test(
                '''Class on{}Class F_{Var $_:Array [Array [Array [Array [Array [String ,0XD_9_A],0B11],0X82],0X12],0B110];Var $_:_1;}''',
                '''Class,on,{,},Class,F_,{,Var,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0XD9A,],,,0B11,],,,0X82,],,,0X12,],,,0B110,],;,Var,$_,:,_1,;,},<EOF>''',
                101
            )
        )

    def test_802(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Eda1_5{}Class ___V_{Val $s:v;Destructor (){_C::$_();_::$_();Break ;}Constructor (_:Array [Boolean ,0X4]){}_8(){} }''',
                '''Class,Eda1_5,{,},Class,___V_,{,Val,$s,:,v,;,Destructor,(,),{,_C,::,$_,(,),;,_,::,$_,(,),;,Break,;,},Constructor,(,_,:,Array,[,Boolean,,,0X4,],),{,},_8,(,),{,},},<EOF>''',
                101
            )
        )

    def test_803(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (){}$_7(__pqC:Array [Boolean ,16]){Val _,e_852k,v_:z;Continue ;}Var $_,$32,$H,$_gm6:Array [Array [Array [Array [Boolean ,0B1100],044_7_4],9],0X5A];Val $cj__:String ;Constructor (_:P;R,T4X2,_5_6,b:_;_,_d,u:_2;_U,_j:Boolean ){} }Class _{}''',
                '''Class,_,{,Constructor,(,),{,},$_7,(,__pqC,:,Array,[,Boolean,,,16,],),{,Val,_,,,e_852k,,,v_,:,z,;,Continue,;,},Var,$_,,,$32,,,$H,,,$_gm6,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1100,],,,04474,],,,9,],,,0X5A,],;,Val,$cj__,:,String,;,Constructor,(,_,:,P,;,R,,,T4X2,,,_5_6,,,b,:,_,;,_,,,_d,,,u,:,_2,;,_U,,,_j,:,Boolean,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_804(self):
        self.assertTrue(
            TestLexer.test(
                '''Class c_4:Hr{Constructor (V6:Array [Array [Array [Array [Array [Array [String ,0x14],30],06],0b1],01_57],30]){} }Class _:_y{$M(){} }''',
                '''Class,c_4,:,Hr,{,Constructor,(,V6,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0x14,],,,30,],,,06,],,,0b1,],,,0157,],,,30,],),{,},},Class,_,:,_y,{,$M,(,),{,},},<EOF>''',
                101
            )
        )

    def test_805(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class __{}Class S_{}Class pV:_3{}Class _0s{}Class _{}Class __:__{__(_,KG:Float ){} }Class _70_:___{}Class __s:m{}''',
                '''Class,_,:,_,{,},Class,__,{,},Class,S_,{,},Class,pV,:,_3,{,},Class,_0s,{,},Class,_,{,},Class,__,:,__,{,__,(,_,,,KG,:,Float,),{,},},Class,_70_,:,___,{,},Class,__s,:,m,{,},<EOF>''',
                101
            )
        )

    def test_806(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7{}Class _i:__{Constructor (gF,_:V;_2___,_:Y){}Constructor (_9_,_,_:Boolean ;_,_:Array [Boolean ,0X12]){} }''',
                '''Class,_7,{,},Class,_i,:,__,{,Constructor,(,gF,,,_,:,V,;,_2___,,,_,:,Y,),{,},Constructor,(,_9_,,,_,,,_,:,Boolean,;,_,,,_,:,Array,[,Boolean,,,0X12,],),{,},},<EOF>''',
                101
            )
        )

    def test_807(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_1{Destructor (){Break ;}$T8(w_,b:Boolean ;_,_:Array [String ,96];__,_,_,W_:Array [Array [Array [Array [Boolean ,023],0104],034_67],06]){} }Class _1{}''',
                '''Class,_,:,_1,{,Destructor,(,),{,Break,;,},$T8,(,w_,,,b,:,Boolean,;,_,,,_,:,Array,[,String,,,96,],;,__,,,_,,,_,,,W_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,023,],,,0104,],,,03467,],,,06,],),{,},},Class,_1,{,},<EOF>''',
                101
            )
        )

    def test_808(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___R_Z:eL_{Constructor (T___:Boolean ;r_j,_31:Array [String ,41]){Var _,x:Float ;} }Class _:Iv_z{Val $iUD_,$7,_,$_:Array [Array [Array [Array [Boolean ,0b1_0],0b1001101],41],0xE];}''',
                '''Class,___R_Z,:,eL_,{,Constructor,(,T___,:,Boolean,;,r_j,,,_31,:,Array,[,String,,,41,],),{,Var,_,,,x,:,Float,;,},},Class,_,:,Iv_z,{,Val,$iUD_,,,$7,,,_,,,$_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b10,],,,0b1001101,],,,41,],,,0xE,],;,},<EOF>''',
                101
            )
        )

    def test_809(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k:z{Constructor (t,_3,_:_Pg;M,J,_K_,___:Array [Array [Array [String ,7],0x9_7],0x21]){Continue ;Break ;}Constructor (N_:Float ;_2Pf:String ;_:Array [Int ,70]){}Val _3,w,$0_56g2:Int ;}''',
                '''Class,k,:,z,{,Constructor,(,t,,,_3,,,_,:,_Pg,;,M,,,J,,,_K_,,,___,:,Array,[,Array,[,Array,[,String,,,7,],,,0x97,],,,0x21,],),{,Continue,;,Break,;,},Constructor,(,N_,:,Float,;,_2Pf,:,String,;,_,:,Array,[,Int,,,70,],),{,},Val,_3,,,w,,,$0_56g2,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_810(self):
        self.assertTrue(
            TestLexer.test(
                '''Class G:_9__{Constructor (){}Val $__,_G:Array [Array [String ,05],035];Var $p,$1:Boolean ;Constructor (_:Array [Array [Array [Float ,0x3E],0b1000001],89];y2g,_:_2;N,_C,_:Array [Float ,0xC_F]){} }''',
                '''Class,G,:,_9__,{,Constructor,(,),{,},Val,$__,,,_G,:,Array,[,Array,[,String,,,05,],,,035,],;,Var,$p,,,$1,:,Boolean,;,Constructor,(,_,:,Array,[,Array,[,Array,[,Float,,,0x3E,],,,0b1000001,],,,89,],;,y2g,,,_,:,_2,;,N,,,_C,,,_,:,Array,[,Float,,,0xCF,],),{,},},<EOF>''',
                101
            )
        )

    def test_811(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_:Array [String ,0x9]){}Val $i,x:Int ;}Class M_k:_0f{}Class c{Val $3,$__,$S52oZ6K,Q,$7_,__,D,$7S,$64,F31Q,$i38_,_,_:Array [Int ,02];}''',
                '''Class,_,{,Constructor,(,_,:,Array,[,String,,,0x9,],),{,},Val,$i,,,x,:,Int,;,},Class,M_k,:,_0f,{,},Class,c,{,Val,$3,,,$__,,,$S52oZ6K,,,Q,,,$7_,,,__,,,D,,,$7S,,,$64,,,F31Q,,,$i38_,,,_,,,_,:,Array,[,Int,,,02,],;,},<EOF>''',
                101
            )
        )

    def test_812(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{d_(){} }Class _{Destructor (){}$_u(D,_:_0_){}_C_(){}Constructor (C,_7,_,_,_b1S,_:Boolean ;_,__,u_0217_2W_k,f65:Boolean ;_:n1H;_1,X,_:_0_){} }Class M_{}Class Y{}''',
                '''Class,__,{,d_,(,),{,},},Class,_,{,Destructor,(,),{,},$_u,(,D,,,_,:,_0_,),{,},_C_,(,),{,},Constructor,(,C,,,_7,,,_,,,_,,,_b1S,,,_,:,Boolean,;,_,,,__,,,u_0217_2W_k,,,f65,:,Boolean,;,_,:,n1H,;,_1,,,X,,,_,:,_0_,),{,},},Class,M_,{,},Class,Y,{,},<EOF>''',
                101
            )
        )

    def test_813(self):
        self.assertTrue(
            TestLexer.test(
                '''Class rTS0_:Y{}Class _{}Class W:j{Constructor (){} }Class _:_{Val $4__:Array [Array [Array [Boolean ,15],15],017_06];}''',
                '''Class,rTS0_,:,Y,{,},Class,_,{,},Class,W,:,j,{,Constructor,(,),{,},},Class,_,:,_,{,Val,$4__,:,Array,[,Array,[,Array,[,Boolean,,,15,],,,15,],,,01706,],;,},<EOF>''',
                101
            )
        )

    def test_814(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val L:Array [Array [Array [Float ,01],3],0x64];Var L:T;}Class O_:_Wi{Var Y_:Boolean ;}Class A{Val $7j6:Array [String ,85_8];Constructor (){} }''',
                '''Class,_,{,Val,L,:,Array,[,Array,[,Array,[,Float,,,01,],,,3,],,,0x64,],;,Var,L,:,T,;,},Class,O_,:,_Wi,{,Var,Y_,:,Boolean,;,},Class,A,{,Val,$7j6,:,Array,[,String,,,858,],;,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_815(self):
        self.assertTrue(
            TestLexer.test(
                '''Class HN:_{Constructor (){}$00in_(P_5,_a24:x8u88;A,X749__,Z:_){Break ;}Var S:F;Constructor (){}$_(){Break ;} }''',
                '''Class,HN,:,_,{,Constructor,(,),{,},$00in_,(,P_5,,,_a24,:,x8u88,;,A,,,X749__,,,Z,:,_,),{,Break,;,},Var,S,:,F,;,Constructor,(,),{,},$_,(,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_816(self):
        self.assertTrue(
            TestLexer.test(
                '''Class U{U(){Return ;Break ;} }Class _r64{}Class s_:vA{Constructor (){} }Class aI{}Class __:U_{Var $9:Array [Array [Int ,0X2F],07];Destructor (){}Val _,_4,$Sr:y;}''',
                '''Class,U,{,U,(,),{,Return,;,Break,;,},},Class,_r64,{,},Class,s_,:,vA,{,Constructor,(,),{,},},Class,aI,{,},Class,__,:,U_,{,Var,$9,:,Array,[,Array,[,Int,,,0X2F,],,,07,],;,Destructor,(,),{,},Val,_,,,_4,,,$Sr,:,y,;,},<EOF>''',
                101
            )
        )

    def test_817(self):
        self.assertTrue(
            TestLexer.test(
                '''Class h_{Val _,_E:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0b1011010],0B1001],0123],0B1_00],0123],87],0b1011010],0X64];}''',
                '''Class,h_,{,Val,_,,,_E,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1011010,],,,0B1001,],,,0123,],,,0B100,],,,0123,],,,87,],,,0b1011010,],,,0X64,],;,},<EOF>''',
                101
            )
        )

    def test_818(self):
        self.assertTrue(
            TestLexer.test(
                '''Class N:_{_(F_,M88n_,B,__,Vy_,J,Z__8F6:Array [Array [Array [Array [Array [Boolean ,0b10100],0X20],062_7_7],0b10100],7_7]){}Destructor (){} }''',
                '''Class,N,:,_,{,_,(,F_,,,M88n_,,,B,,,__,,,Vy_,,,J,,,Z__8F6,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b10100,],,,0X20,],,,06277,],,,0b10100,],,,77,],),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_819(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:o{Constructor (s:Array [Array [Float ,05],0101];_:Array [Array [Array [Array [Int ,022],0b1001010],4],53];_2,_s,Ggw,_1:n;__,_w_,_,Kg6__M:Float ){} }Class _{}''',
                '''Class,_,:,o,{,Constructor,(,s,:,Array,[,Array,[,Float,,,05,],,,0101,],;,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,022,],,,0b1001010,],,,4,],,,53,],;,_2,,,_s,,,Ggw,,,_1,:,n,;,__,,,_w_,,,_,,,Kg6__M,:,Float,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_820(self):
        self.assertTrue(
            TestLexer.test(
                '''Class W{}Class qQ{_e_k(){} }Class __9_H3:_{}Class rx9{Cu(_,E_7,_o6h4_I:___;P_,_:Array [Int ,0b1];__:Float ){} }Class f{Z__(){} }''',
                '''Class,W,{,},Class,qQ,{,_e_k,(,),{,},},Class,__9_H3,:,_,{,},Class,rx9,{,Cu,(,_,,,E_7,,,_o6h4_I,:,___,;,P_,,,_,:,Array,[,Int,,,0b1,],;,__,:,Float,),{,},},Class,f,{,Z__,(,),{,},},<EOF>''',
                101
            )
        )

    def test_821(self):
        self.assertTrue(
            TestLexer.test(
                '''Class a:G_{}Class fD376:k{Constructor (___,_t,_,L:Int ;_P,F,J,m46:L_){}Constructor (){}Var $_:Array [Array [Float ,0X30],0x43];}Class V9_27z{Destructor (){} }Class oMQ_{Destructor (){Continue ;} }''',
                '''Class,a,:,G_,{,},Class,fD376,:,k,{,Constructor,(,___,,,_t,,,_,,,L,:,Int,;,_P,,,F,,,J,,,m46,:,L_,),{,},Constructor,(,),{,},Var,$_,:,Array,[,Array,[,Float,,,0X30,],,,0x43,],;,},Class,V9_27z,{,Destructor,(,),{,},},Class,oMQ_,{,Destructor,(,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_822(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _3{$Q(__:Array [Boolean ,40];_h2__,q0:_;E,_G0,l:String ){}Constructor (____P,By ,_04_:kH){ {} }}Class A:_4{h_(_,p:FH_z5;c,k_L:a;dS82,T2:Array [Array [Array [Array [String ,3],0110],0X9],0x1];l_43,_,V9Y5_,x:Array [Int ,0b10]){} }''',
                '''Class,_3,{,$Q,(,__,:,Array,[,Boolean,,,40,],;,_h2__,,,q0,:,_,;,E,,,_G0,,,l,:,String,),{,},Constructor,(,____P,,,By,,,_04_,:,kH,),{,{,},},},Class,A,:,_4,{,h_,(,_,,,p,:,FH_z5,;,c,,,k_L,:,a,;,dS82,,,T2,:,Array,[,Array,[,Array,[,Array,[,String,,,3,],,,0110,],,,0X9,],,,0x1,],;,l_43,,,_,,,V9Y5_,,,x,:,Array,[,Int,,,0b10,],),{,},},<EOF>''',
                101
            )
        )

    def test_823(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8:_{}Class r:E{}Class _N_:_0y2{$6(E_0_,IF,_:Int ;_:Float ){}Constructor (_,c:Array [String ,03];__,_:Float ){} }''',
                '''Class,_8,:,_,{,},Class,r,:,E,{,},Class,_N_,:,_0y2,{,$6,(,E_0_,,,IF,,,_,:,Int,;,_,:,Float,),{,},Constructor,(,_,,,c,:,Array,[,String,,,03,],;,__,,,_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_824(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{Constructor (G4n,_:__;_:Array [Float ,025_76_6];_:String ){}J_M(U:Array [Array [Boolean ,97_4],02];___:Array [Array [Float ,0B1],4];_:Boolean ){} }Class m{}''',
                '''Class,__,{,Constructor,(,G4n,,,_,:,__,;,_,:,Array,[,Float,,,025766,],;,_,:,String,),{,},J_M,(,U,:,Array,[,Array,[,Boolean,,,974,],,,02,],;,___,:,Array,[,Array,[,Float,,,0B1,],,,4,],;,_,:,Boolean,),{,},},Class,m,{,},<EOF>''',
                101
            )
        )

    def test_825(self):
        self.assertTrue(
            TestLexer.test(
                '''Class z:_{}Class _AN_x{}Class S:_{}Class j7:h__{Destructor (){} }Class _v_:_7_{}Class f:_{Val _4Y,$32:_8;Constructor (){} }''',
                '''Class,z,:,_,{,},Class,_AN_x,{,},Class,S,:,_,{,},Class,j7,:,h__,{,Destructor,(,),{,},},Class,_v_,:,_7_,{,},Class,f,:,_,{,Val,_4Y,,,$32,:,_8,;,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_826(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Destructor (){Val _,k8,_H_:Array [Array [Boolean ,82],07_01];Continue ;}Constructor (){ {Break ;Self ._._();Break ;} }Constructor (a:Array [Int ,013]){} }Class w:h9{}Class J:s{}''',
                '''Class,_,{,Destructor,(,),{,Val,_,,,k8,,,_H_,:,Array,[,Array,[,Boolean,,,82,],,,0701,],;,Continue,;,},Constructor,(,),{,{,Break,;,Self,.,_,.,_,(,),;,Break,;,},},Constructor,(,a,:,Array,[,Int,,,013,],),{,},},Class,w,:,h9,{,},Class,J,:,s,{,},<EOF>''',
                101
            )
        )

    def test_827(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:__S_6M{}Class A:ae{}Class _{}Class K:jF{}Class Y:X_{_(){}Val $4,$_7,_4_,$__,$_,w6,T,$M6_z:String ;}Class x:_C_{}''',
                '''Class,_,:,__S_6M,{,},Class,A,:,ae,{,},Class,_,{,},Class,K,:,jF,{,},Class,Y,:,X_,{,_,(,),{,},Val,$4,,,$_7,,,_4_,,,$__,,,$_,,,w6,,,T,,,$M6_z,:,String,;,},Class,x,:,_C_,{,},<EOF>''',
                101
            )
        )

    def test_828(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Q{}Class _H2:H6{Var z:String ;Constructor (___33y:Array [Boolean ,017];J:Array [Array [Array [Array [String ,0XA],93],01],0134]){} }''',
                '''Class,Q,{,},Class,_H2,:,H6,{,Var,z,:,String,;,Constructor,(,___33y,:,Array,[,Boolean,,,017,],;,J,:,Array,[,Array,[,Array,[,Array,[,String,,,0XA,],,,93,],,,01,],,,0134,],),{,},},<EOF>''',
                101
            )
        )

    def test_829(self):
        self.assertTrue(
            TestLexer.test(
                '''Class s_:_{Destructor (){Var V_51qZ2,_,s___:Float ;Break ;Val t,g,L5:Array [Array [Array [String ,0b110100],3],0B1001];}Val __:_T;}Class _{Destructor (){} }''',
                '''Class,s_,:,_,{,Destructor,(,),{,Var,V_51qZ2,,,_,,,s___,:,Float,;,Break,;,Val,t,,,g,,,L5,:,Array,[,Array,[,Array,[,String,,,0b110100,],,,3,],,,0B1001,],;,},Val,__,:,_T,;,},Class,_,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_830(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9{Constructor (_o_d,Q:Boolean ;z,I,_i:_4;T___:Float ){} }Class _{}Class _9xT_{Var $5:Int ;Var H_W_,_8h:Float ;}''',
                '''Class,_9,{,Constructor,(,_o_d,,,Q,:,Boolean,;,z,,,I,,,_i,:,_4,;,T___,:,Float,),{,},},Class,_,{,},Class,_9xT_,{,Var,$5,:,Int,;,Var,H_W_,,,_8h,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_831(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _o{}Class _z7{Constructor (_2:_3;MI,w6J_,_,_:Array [Int ,031]){ {} }Val _,R,_,_,B,H366:_3_;}Class _v{Var A__,$6,_d3:Array [Array [Array [Array [Int ,100],031],02],0246_3];}''',
                '''Class,_o,{,},Class,_z7,{,Constructor,(,_2,:,_3,;,MI,,,w6J_,,,_,,,_,:,Array,[,Int,,,031,],),{,{,},},Val,_,,,R,,,_,,,_,,,B,,,H366,:,_3_,;,},Class,_v,{,Var,A__,,,$6,,,_d3,:,Array,[,Array,[,Array,[,Array,[,Int,,,100,],,,031,],,,02,],,,02463,],;,},<EOF>''',
                101
            )
        )

    def test_832(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:D0{Var Y42,$_:Array [String ,0b11];$_q(i99_9g2:Array [Array [Array [Boolean ,0B1000100],07],04]){} }Class n{_(K__,N:Array [Array [Array [Array [Array [Int ,42],0X24],0B1],0B1],0x44CBBC]){Break ;Return ;} }''',
                '''Class,_,:,D0,{,Var,Y42,,,$_,:,Array,[,String,,,0b11,],;,$_q,(,i99_9g2,:,Array,[,Array,[,Array,[,Boolean,,,0B1000100,],,,07,],,,04,],),{,},},Class,n,{,_,(,K__,,,N,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,42,],,,0X24,],,,0B1,],,,0B1,],,,0x44CBBC,],),{,Break,;,Return,;,},},<EOF>''',
                101
            )
        )

    def test_833(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class _{Var x:Array [Array [Array [Array [Array [Boolean ,07_3_4],39],035],96],05];Var $B,__,K:b_E;}Class pD_9:_{}Class _{$7(){}Var $7:_;}''',
                '''Class,_,:,_,{,},Class,_,{,Var,x,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0734,],,,39,],,,035,],,,96,],,,05,],;,Var,$B,,,__,,,K,:,b_E,;,},Class,pD_9,:,_,{,},Class,_,{,$7,(,),{,},Var,$7,:,_,;,},<EOF>''',
                101
            )
        )

    def test_834(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y_{}Class q:J_{}Class ___:R_{Var $8X,$8,$4:Array [Int ,0X4];}Class g:Jr{}Class _{Val LO781:Array [String ,031];}''',
                '''Class,y_,{,},Class,q,:,J_,{,},Class,___,:,R_,{,Var,$8X,,,$8,,,$4,:,Array,[,Int,,,0X4,],;,},Class,g,:,Jr,{,},Class,_,{,Val,LO781,:,Array,[,String,,,031,],;,},<EOF>''',
                101
            )
        )

    def test_835(self):
        self.assertTrue(
            TestLexer.test(
                '''Class gk:_Hw{Destructor (){Break ;}Constructor (B2:Array [Array [Array [Boolean ,0b1],0XC],0141]){}Var $_:String ;Destructor (){}Val $9_n,$5:Km;Constructor (){} }Class n_:__{}Class __:__O{Val i_7,__,$9,Lk:Float ;}''',
                '''Class,gk,:,_Hw,{,Destructor,(,),{,Break,;,},Constructor,(,B2,:,Array,[,Array,[,Array,[,Boolean,,,0b1,],,,0XC,],,,0141,],),{,},Var,$_,:,String,;,Destructor,(,),{,},Val,$9_n,,,$5,:,Km,;,Constructor,(,),{,},},Class,n_,:,__,{,},Class,__,:,__O,{,Val,i_7,,,__,,,$9,,,Lk,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_836(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:t{Constructor (___0:Array [Array [Array [Array [String ,07_5],0x57],014],0x29];_,_q,h,Y_,_,_:Array [Array [Array [Float ,014],9_44_54_4_84562],0b100101]){b::$___();Continue ;}Val _,_:__;}Class _5_{}Class _:___{k(){}_(){} }Class O98_{}''',
                '''Class,_,:,t,{,Constructor,(,___0,:,Array,[,Array,[,Array,[,Array,[,String,,,075,],,,0x57,],,,014,],,,0x29,],;,_,,,_q,,,h,,,Y_,,,_,,,_,:,Array,[,Array,[,Array,[,Float,,,014,],,,94454484562,],,,0b100101,],),{,b,::,$___,(,),;,Continue,;,},Val,_,,,_,:,__,;,},Class,_5_,{,},Class,_,:,___,{,k,(,),{,},_,(,),{,},},Class,O98_,{,},<EOF>''',
                101
            )
        )

    def test_837(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q{}Class __K{Constructor (){}Var $4_,$_84,XG7Kv:i;}Class _{}Class _D{}Class p{Destructor (){} }Class _{QU2(CQ_l_,_:Int ;p:Array [String ,0xC3];P18_,_t25,P,a,f,C:_cG_;OX:Array [Boolean ,0B1]){} }''',
                '''Class,q,{,},Class,__K,{,Constructor,(,),{,},Var,$4_,,,$_84,,,XG7Kv,:,i,;,},Class,_,{,},Class,_D,{,},Class,p,{,Destructor,(,),{,},},Class,_,{,QU2,(,CQ_l_,,,_,:,Int,;,p,:,Array,[,String,,,0xC3,],;,P18_,,,_t25,,,P,,,a,,,f,,,C,:,_cG_,;,OX,:,Array,[,Boolean,,,0B1,],),{,},},<EOF>''',
                101
            )
        )

    def test_838(self):
        self.assertTrue(
            TestLexer.test(
                '''Class N:Jb{v(_,_:Float ){Break ;}Constructor (){} }Class __{}Class __{Val $5:Array [Boolean ,69];Val _,w,i2_:Boolean ;}''',
                '''Class,N,:,Jb,{,v,(,_,,,_,:,Float,),{,Break,;,},Constructor,(,),{,},},Class,__,{,},Class,__,{,Val,$5,:,Array,[,Boolean,,,69,],;,Val,_,,,w,,,i2_,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_839(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{Constructor (){ {} }Var $___,eP:Float ;Destructor (){Var _7,_G,_:_;}Val $3:Array [Array [String ,56],01];Var $i:Boolean ;A(_,_vj:Array [Array [Int ,052],0x92B1B_E]){Break ;} }Class ha6:_{}Class x{}''',
                '''Class,__,{,Constructor,(,),{,{,},},Var,$___,,,eP,:,Float,;,Destructor,(,),{,Var,_7,,,_G,,,_,:,_,;,},Val,$3,:,Array,[,Array,[,String,,,56,],,,01,],;,Var,$i,:,Boolean,;,A,(,_,,,_vj,:,Array,[,Array,[,Int,,,052,],,,0x92B1BE,],),{,Break,;,},},Class,ha6,:,_,{,},Class,x,{,},<EOF>''',
                101
            )
        )

    def test_840(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b:J{$92_(){} }Class t{}Class J8__3:bJ{Constructor (M:Array [Boolean ,02_4];T94_,h:Array [Boolean ,94];V,M:Int ;Y5,m,_8,Z,_,_2:q7;B:Array [Int ,0b11];_Ci:Array [Boolean ,0b100011];_0:_f07;_:Boolean ;Ve:Int ){} }''',
                '''Class,b,:,J,{,$92_,(,),{,},},Class,t,{,},Class,J8__3,:,bJ,{,Constructor,(,M,:,Array,[,Boolean,,,024,],;,T94_,,,h,:,Array,[,Boolean,,,94,],;,V,,,M,:,Int,;,Y5,,,m,,,_8,,,Z,,,_,,,_2,:,q7,;,B,:,Array,[,Int,,,0b11,],;,_Ci,:,Array,[,Boolean,,,0b100011,],;,_0,:,_f07,;,_,:,Boolean,;,Ve,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_841(self):
        self.assertTrue(
            TestLexer.test(
                '''Class r:S_{Constructor (){} }Class _:e{Constructor (___,_,_K:_3;t,g_,_,_U,o:String ){} }Class n__{Var $_:P3D_3;}Class W3:_{}''',
                '''Class,r,:,S_,{,Constructor,(,),{,},},Class,_,:,e,{,Constructor,(,___,,,_,,,_K,:,_3,;,t,,,g_,,,_,,,_U,,,o,:,String,),{,},},Class,n__,{,Var,$_,:,P3D_3,;,},Class,W3,:,_,{,},<EOF>''',
                101
            )
        )

    def test_842(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T:y{Constructor (V_eRU6_,r9:Array [Int ,2_7];u,_:String ;_:String ;__,d,_,c:Array [Boolean ,0b10];_,Y,OM,_:String ;R,_VpE:Float ;k,_:Array [Float ,03];P_:Boolean ){Continue ;} }''',
                '''Class,T,:,y,{,Constructor,(,V_eRU6_,,,r9,:,Array,[,Int,,,27,],;,u,,,_,:,String,;,_,:,String,;,__,,,d,,,_,,,c,:,Array,[,Boolean,,,0b10,],;,_,,,Y,,,OM,,,_,:,String,;,R,,,_VpE,:,Float,;,k,,,_,:,Array,[,Float,,,03,],;,P_,:,Boolean,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_843(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2:S{Constructor (__q4_5O:Array [Array [Int ,0B1],0x1A];fbV_:F55;N7_:Float ){} }Class z:__{Var $b_:f=--RT::$_()._;}''',
                '''Class,_2,:,S,{,Constructor,(,__q4_5O,:,Array,[,Array,[,Int,,,0B1,],,,0x1A,],;,fbV_,:,F55,;,N7_,:,Float,),{,},},Class,z,:,__,{,Var,$b_,:,f,=,-,-,RT,::,$_,(,),.,_,;,},<EOF>''',
                101
            )
        )

    def test_844(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _za:_{N9(){Return -3_21.e+90||!-Null .UE().y_.t_V_-!!!_6::$__;} }Class j7mr:_{Val $_4TY,$4_6t:Array [Array [Array [Int ,71],0140],0b101110];}''',
                '''Class,_za,:,_,{,N9,(,),{,Return,-,321.e+90,||,!,-,Null,.,UE,(,),.,y_,.,t_V_,-,!,!,!,_6,::,$__,;,},},Class,j7mr,:,_,{,Val,$_4TY,,,$4_6t,:,Array,[,Array,[,Array,[,Int,,,71,],,,0140,],,,0b101110,],;,},<EOF>''',
                101
            )
        )

    def test_845(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_S{Val $_ONY4_,$_p:Array [String ,0X7_3_E];$_(z:Array [Array [Boolean ,0x9F7_9],0X55];_5_r01,pX_U8,t0,z,a,_:Boolean ;_:Int ;_Pgl:Boolean ;w:String ;_:Array [Array [Int ,0B1_1],0B1_11]){} }Class Ia{}Class _{Var _0t__0_2:Array [Float ,03];}''',
                '''Class,_,:,_S,{,Val,$_ONY4_,,,$_p,:,Array,[,String,,,0X73E,],;,$_,(,z,:,Array,[,Array,[,Boolean,,,0x9F79,],,,0X55,],;,_5_r01,,,pX_U8,,,t0,,,z,,,a,,,_,:,Boolean,;,_,:,Int,;,_Pgl,:,Boolean,;,w,:,String,;,_,:,Array,[,Array,[,Int,,,0B11,],,,0B111,],),{,},},Class,Ia,{,},Class,_,{,Var,_0t__0_2,:,Array,[,Float,,,03,],;,},<EOF>''',
                101
            )
        )

    def test_846(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8Fs:p{}Class __:_{Var _2,_R1:Array [Array [Array [Array [Int ,0X62],0X62],0B1],0141];}Class _7_:_l0_{Constructor (wV,_y,_p:N;k_PE:Int ){} }Class V:_{}Class _:_{}Class K0:M8N{}''',
                '''Class,_8Fs,:,p,{,},Class,__,:,_,{,Var,_2,,,_R1,:,Array,[,Array,[,Array,[,Array,[,Int,,,0X62,],,,0X62,],,,0B1,],,,0141,],;,},Class,_7_,:,_l0_,{,Constructor,(,wV,,,_y,,,_p,:,N,;,k_PE,:,Int,),{,},},Class,V,:,_,{,},Class,_,:,_,{,},Class,K0,:,M8N,{,},<EOF>''',
                101
            )
        )

    def test_847(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __C{Val _,___:Boolean ;P__U2(b8_:Boolean ;_,y_:Array [Int ,0b10]){} }Class _c__1{}Class s8_F{Val SO,$__B,_:Int ;}Class __KI2{Destructor (){}Val $xv,$1_5_:Array [Float ,0B11100];}''',
                '''Class,__C,{,Val,_,,,___,:,Boolean,;,P__U2,(,b8_,:,Boolean,;,_,,,y_,:,Array,[,Int,,,0b10,],),{,},},Class,_c__1,{,},Class,s8_F,{,Val,SO,,,$__B,,,_,:,Int,;,},Class,__KI2,{,Destructor,(,),{,},Val,$xv,,,$1_5_,:,Array,[,Float,,,0B11100,],;,},<EOF>''',
                101
            )
        )

    def test_848(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:oa{Constructor (){}__G_aX(_,_,x,_19,_:Boolean ;R:Int ;_,___D_:Array [Int ,0143];_:B){}Constructor (){}Val $D,D2,$_,FM,R:f_;}Class _{Destructor (){Continue ;} }''',
                '''Class,__,:,oa,{,Constructor,(,),{,},__G_aX,(,_,,,_,,,x,,,_19,,,_,:,Boolean,;,R,:,Int,;,_,,,___D_,:,Array,[,Int,,,0143,],;,_,:,B,),{,},Constructor,(,),{,},Val,$D,,,D2,,,$_,,,FM,,,R,:,f_,;,},Class,_,{,Destructor,(,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_849(self):
        self.assertTrue(
            TestLexer.test(
                '''Class K:Y{Val _8,$39,Y_0_u_:Boolean ;Var $2:Array [Array [Array [Array [Boolean ,551],0xCF_5_26],0X3F],0123];}Class _6{}Class _{}Class L:__{}Class _{}''',
                '''Class,K,:,Y,{,Val,_8,,,$39,,,Y_0_u_,:,Boolean,;,Var,$2,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,551,],,,0xCF526,],,,0X3F,],,,0123,],;,},Class,_6,{,},Class,_,{,},Class,L,:,__,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_850(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class x1{Constructor (_x0C_,T,w2,__,_D,_7I:Array [Array [String ,0B1],0x28];g:Boolean ;D:Boolean ;w:_yxz;__5:Float ){} }''',
                '''Class,_,{,},Class,x1,{,Constructor,(,_x0C_,,,T,,,w2,,,__,,,_D,,,_7I,:,Array,[,Array,[,String,,,0B1,],,,0x28,],;,g,:,Boolean,;,D,:,Boolean,;,w,:,_yxz,;,__5,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_851(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J_x{Constructor (_:Array [Int ,69];_,_:_){}of(){_2::$_5t8();}__(M52J:String ){}_o(){Val _,_ru:Float ;}Val $_:Z;Val _:Float ;}Class Q:_7W0B7{Var $N__4_82,_,u:Float ;}Class __{$bbn(D:Boolean ){Continue ;Break ;{} }}''',
                '''Class,J_x,{,Constructor,(,_,:,Array,[,Int,,,69,],;,_,,,_,:,_,),{,},of,(,),{,_2,::,$_5t8,(,),;,},__,(,M52J,:,String,),{,},_o,(,),{,Val,_,,,_ru,:,Float,;,},Val,$_,:,Z,;,Val,_,:,Float,;,},Class,Q,:,_7W0B7,{,Var,$N__4_82,,,_,,,u,:,Float,;,},Class,__,{,$bbn,(,D,:,Boolean,),{,Continue,;,Break,;,{,},},},<EOF>''',
                101
            )
        )

    def test_852(self):
        self.assertTrue(
            TestLexer.test(
                '''Class v{Val $R,$5:L;}Class _{Destructor (){} }Class _{Constructor (XG_,_:Int ;_:Array [Float ,0x34];_z_,p_,_,p:Array [Int ,052];U__U_,__CA,Z790:Array [Array [Float ,0b1010100],40]){} }Class _:Al_h{}Class _{_G(){} }Class T{$T41(){}Var $98_,_05_,v_:z_;$I9_(_0:String ){} }''',
                '''Class,v,{,Val,$R,,,$5,:,L,;,},Class,_,{,Destructor,(,),{,},},Class,_,{,Constructor,(,XG_,,,_,:,Int,;,_,:,Array,[,Float,,,0x34,],;,_z_,,,p_,,,_,,,p,:,Array,[,Int,,,052,],;,U__U_,,,__CA,,,Z790,:,Array,[,Array,[,Float,,,0b1010100,],,,40,],),{,},},Class,_,:,Al_h,{,},Class,_,{,_G,(,),{,},},Class,T,{,$T41,(,),{,},Var,$98_,,,_05_,,,v_,:,z_,;,$I9_,(,_0,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_853(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___{Constructor (){Continue ;}$Y(_:Float ;___,M1_:Array [Array [Array [Float ,040],0B10_0_0],04_2];_:Float ;_:Float ){Return ;} }Class f__2{Val _x,$_,$_,$02_,_:String ;}''',
                '''Class,___,{,Constructor,(,),{,Continue,;,},$Y,(,_,:,Float,;,___,,,M1_,:,Array,[,Array,[,Array,[,Float,,,040,],,,0B1000,],,,042,],;,_,:,Float,;,_,:,Float,),{,Return,;,},},Class,f__2,{,Val,_x,,,$_,,,$_,,,$02_,,,_,:,String,;,},<EOF>''',
                101
            )
        )

    def test_854(self):
        self.assertTrue(
            TestLexer.test(
                '''Class r_:KQ{Constructor (Y,__Mjo9_13_,egU,__,L0_q:Array [Array [Array [Float ,2],07_23_442],6];V:_;_:_;R,Y_:Boolean ){} }''',
                '''Class,r_,:,KQ,{,Constructor,(,Y,,,__Mjo9_13_,,,egU,,,__,,,L0_q,:,Array,[,Array,[,Array,[,Float,,,2,],,,0723442,],,,6,],;,V,:,_,;,_,:,_,;,R,,,Y_,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_855(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y76u{}Class __:_{}Class _0_{}Class X{Var $_:Array [Array [Array [Boolean ,0B111111],033],0B1011_10];Destructor (){Break ;} }''',
                '''Class,y76u,{,},Class,__,:,_,{,},Class,_0_,{,},Class,X,{,Var,$_,:,Array,[,Array,[,Array,[,Boolean,,,0B111111,],,,033,],,,0B101110,],;,Destructor,(,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_856(self):
        self.assertTrue(
            TestLexer.test(
                '''Class I__:___{}Class Z:_x{_(_5d7_:Array [Array [Float ,07],0x2B];_49,W:Boolean ){Var _:Float ;G::$804fx();}Val Q4:Int ;Constructor (A11_:String ){} }Class b{Val $V3,$__,_097:U;Var $_,$_,Er_9,Ve,_Xq:U;}''',
                '''Class,I__,:,___,{,},Class,Z,:,_x,{,_,(,_5d7_,:,Array,[,Array,[,Float,,,07,],,,0x2B,],;,_49,,,W,:,Boolean,),{,Var,_,:,Float,;,G,::,$804fx,(,),;,},Val,Q4,:,Int,;,Constructor,(,A11_,:,String,),{,},},Class,b,{,Val,$V3,,,$__,,,_097,:,U,;,Var,$_,,,$_,,,Er_9,,,Ve,,,_Xq,:,U,;,},<EOF>''',
                101
            )
        )

    def test_857(self):
        self.assertTrue(
            TestLexer.test(
                '''Class h:_{Val _,$0f,kMl:Array [Array [Array [Array [Array [Array [Array [String ,0X3A],0B11_1],06],04_7_6_3],0x3F],50],0X3A];}''',
                '''Class,h,:,_,{,Val,_,,,$0f,,,kMl,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X3A,],,,0B111,],,,06,],,,04763,],,,0x3F,],,,50,],,,0X3A,],;,},<EOF>''',
                101
            )
        )

    def test_858(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _5G_:q__{Val _,_,$_R:Boolean ;Constructor (p,X_,d:vs;U_:f8t;_:Array [String ,0321];_:z2;L,t_4cI,n__,_,_,_3_:OJf){Val T6:_;} }''',
                '''Class,_5G_,:,q__,{,Val,_,,,_,,,$_R,:,Boolean,;,Constructor,(,p,,,X_,,,d,:,vs,;,U_,:,f8t,;,_,:,Array,[,String,,,0321,],;,_,:,z2,;,L,,,t_4cI,,,n__,,,_,,,_,,,_3_,:,OJf,),{,Val,T6,:,_,;,},},<EOF>''',
                101
            )
        )

    def test_859(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C:_{Destructor (){Continue ;Break ;Break ;} }Class __{}Class _:_{Var N1m3,_9:Array [Array [Array [Array [Array [Array [Array [String ,86],0b1011000],023],6_1_03],0B101010],8],023];Destructor (){}Constructor (_7_6:Array [Float ,0b1]){}Destructor (){Continue ;} }''',
                '''Class,C,:,_,{,Destructor,(,),{,Continue,;,Break,;,Break,;,},},Class,__,{,},Class,_,:,_,{,Var,N1m3,,,_9,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,86,],,,0b1011000,],,,023,],,,6103,],,,0B101010,],,,8,],,,023,],;,Destructor,(,),{,},Constructor,(,_7_6,:,Array,[,Float,,,0b1,],),{,},Destructor,(,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_860(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:I4j{}Class _{Constructor (__5,__,W,k,e,_2:_;c_:Array [Float ,6];f,_:O_){} }Class Q0n_{Destructor (){} }Class _7D_:H9_{}''',
                '''Class,__,:,I4j,{,},Class,_,{,Constructor,(,__5,,,__,,,W,,,k,,,e,,,_2,:,_,;,c_,:,Array,[,Float,,,6,],;,f,,,_,:,O_,),{,},},Class,Q0n_,{,Destructor,(,),{,},},Class,_7D_,:,H9_,{,},<EOF>''',
                101
            )
        )

    def test_861(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Y{}Class _7_3b:_8{}Class __{}Class ___{}Class z_PJ:_I{Var __66,$sS3:Array [Array [Array [String ,6],6],071];}Class _{}Class __:_{}''',
                '''Class,Y,{,},Class,_7_3b,:,_8,{,},Class,__,{,},Class,___,{,},Class,z_PJ,:,_I,{,Var,__66,,,$sS3,:,Array,[,Array,[,Array,[,String,,,6,],,,6,],,,071,],;,},Class,_,{,},Class,__,:,_,{,},<EOF>''',
                101
            )
        )

    def test_862(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A8:_9_KE{Constructor (N:_F7;U:_0){}Constructor (){}Val _:Array [Float ,98_2009_7_31];Var O27_1:_;}Class _4YNc{Var $1_,__,$s,$3,$K,$cUb:_;}''',
                '''Class,A8,:,_9_KE,{,Constructor,(,N,:,_F7,;,U,:,_0,),{,},Constructor,(,),{,},Val,_,:,Array,[,Float,,,982009731,],;,Var,O27_1,:,_,;,},Class,_4YNc,{,Var,$1_,,,__,,,$s,,,$3,,,$K,,,$cUb,:,_,;,},<EOF>''',
                101
            )
        )

    def test_863(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9{Val $94,b:_tC;Destructor (){}Val $_:Array [Boolean ,0B1_1];_(VO_66Qc:String ){} }Class c:_{Val $_,$_:Int ;}''',
                '''Class,_9,{,Val,$94,,,b,:,_tC,;,Destructor,(,),{,},Val,$_,:,Array,[,Boolean,,,0B11,],;,_,(,VO_66Qc,:,String,),{,},},Class,c,:,_,{,Val,$_,,,$_,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_864(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A{}Class K3:m{Constructor (E,_X22,_,s:z_;R,a_:Boolean ){}Val $M_Y:Array [Array [Array [Array [String ,0b1_0],26],0b11110],0X33];$_0(){} }Class j_0:_9{}Class _Rq{}''',
                '''Class,A,{,},Class,K3,:,m,{,Constructor,(,E,,,_X22,,,_,,,s,:,z_,;,R,,,a_,:,Boolean,),{,},Val,$M_Y,:,Array,[,Array,[,Array,[,Array,[,String,,,0b10,],,,26,],,,0b11110,],,,0X33,],;,$_0,(,),{,},},Class,j_0,:,_9,{,},Class,_Rq,{,},<EOF>''',
                101
            )
        )

    def test_865(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:Y{Constructor (_6_,S,_XZb,_,_C:Array [Boolean ,2];R_0:Array [String ,0B1_1];_:Array [Array [Array [Int ,06_56],04],05_4420]){} }''',
                '''Class,_,:,Y,{,Constructor,(,_6_,,,S,,,_XZb,,,_,,,_C,:,Array,[,Boolean,,,2,],;,R_0,:,Array,[,String,,,0B11,],;,_,:,Array,[,Array,[,Array,[,Int,,,0656,],,,04,],,,054420,],),{,},},<EOF>''',
                101
            )
        )

    def test_866(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X:K_{}Class A{Constructor (Z,P,_,H,x_,_5,_O3:String ;H:Array [Array [Array [Array [Int ,0b1001100],0B1110],0B1110],2];u,_,H,_:__;W__2,m3,C:_;__,AW,_:Array [Int ,0XA_B2_0_1_7_6];R_j_:Array [Int ,04];f_W,_:Array [Array [Float ,0B1_1],0b11];_c,u__:String ){Var w,_:String ;}Var _:_3;Destructor (){} }''',
                '''Class,X,:,K_,{,},Class,A,{,Constructor,(,Z,,,P,,,_,,,H,,,x_,,,_5,,,_O3,:,String,;,H,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b1001100,],,,0B1110,],,,0B1110,],,,2,],;,u,,,_,,,H,,,_,:,__,;,W__2,,,m3,,,C,:,_,;,__,,,AW,,,_,:,Array,[,Int,,,0XAB20176,],;,R_j_,:,Array,[,Int,,,04,],;,f_W,,,_,:,Array,[,Array,[,Float,,,0B11,],,,0b11,],;,_c,,,u__,:,String,),{,Var,w,,,_,:,String,;,},Var,_,:,_3,;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_867(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _{Destructor (){}Constructor (R:Int ;_:Boolean ;_,_v7:_2;_:ey;y_,_1_5c:Array [String ,0135]){} }Class w12tEwW0:u_q{}Class s{}''',
                '''Class,_,{,},Class,_,{,Destructor,(,),{,},Constructor,(,R,:,Int,;,_,:,Boolean,;,_,,,_v7,:,_2,;,_,:,ey,;,y_,,,_1_5c,:,Array,[,String,,,0135,],),{,},},Class,w12tEwW0,:,u_q,{,},Class,s,{,},<EOF>''',
                101
            )
        )

    def test_868(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val _W5V,_4,$_,$K,$Is,aZ__5:Array [Array [Array [Array [Array [String ,02_1],045],045],07],0b110011];Var $XF,$7r_83r:Array [Int ,0B11100];}''',
                '''Class,_,{,Val,_W5V,,,_4,,,$_,,,$K,,,$Is,,,aZ__5,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,021,],,,045,],,,045,],,,07,],,,0b110011,],;,Var,$XF,,,$7r_83r,:,Array,[,Int,,,0B11100,],;,},<EOF>''',
                101
            )
        )

    def test_869(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _I44___:_H2_7T_{$3wV_1q7(L:Array [Array [String ,0x30],025];_e,s8,_nT,z__J_,N,J,kF0F_:Array [Boolean ,0x30]){} }''',
                '''Class,_I44___,:,_H2_7T_,{,$3wV_1q7,(,L,:,Array,[,Array,[,String,,,0x30,],,,025,],;,_e,,,s8,,,_nT,,,z__J_,,,N,,,J,,,kF0F_,:,Array,[,Boolean,,,0x30,],),{,},},<EOF>''',
                101
            )
        )

    def test_870(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var z:Array [Array [Boolean ,5_1_760],0B10000];Val B:Array [Array [Array [Array [Array [Array [String ,0xAD9852_1_8],0B1110],0x1E],69],69],1];}''',
                '''Class,_,{,Var,z,:,Array,[,Array,[,Boolean,,,51760,],,,0B10000,],;,Val,B,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0xAD985218,],,,0B1110,],,,0x1E,],,,69,],,,69,],,,1,],;,},<EOF>''',
                101
            )
        )

    def test_871(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w:_9{$2(y_G:Array [Int ,0B10011]){}Val _,$4,_:_;}Class e:_0{}Class _:_{}Class t:z{Constructor (){} }Class p1_5__:U{Val _,$w_3:Array [Boolean ,8];}Class y_w3{}''',
                '''Class,w,:,_9,{,$2,(,y_G,:,Array,[,Int,,,0B10011,],),{,},Val,_,,,$4,,,_,:,_,;,},Class,e,:,_0,{,},Class,_,:,_,{,},Class,t,:,z,{,Constructor,(,),{,},},Class,p1_5__,:,U,{,Val,_,,,$w_3,:,Array,[,Boolean,,,8,],;,},Class,y_w3,{,},<EOF>''',
                101
            )
        )

    def test_872(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _S:__7{Constructor (N,X,S:String ;P,_Da_,f:Array [Array [Array [Float ,31],0XD],8]){Var _:Boolean ;}Constructor (){}Val $4:Boolean ;Val N_:String ;}''',
                '''Class,_S,:,__7,{,Constructor,(,N,,,X,,,S,:,String,;,P,,,_Da_,,,f,:,Array,[,Array,[,Array,[,Float,,,31,],,,0XD,],,,8,],),{,Var,_,:,Boolean,;,},Constructor,(,),{,},Val,$4,:,Boolean,;,Val,N_,:,String,;,},<EOF>''',
                101
            )
        )

    def test_873(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:b{Var $_:Array [Float ,7];$_2(RX,C0,h3C,_2,_53_3CG_,c2,_,v5:VO){}Val l5,$F:ZP4;G_0h_(_:Float ;cF,_:Boolean ){}Var _f_e:_3;Val __,__,$_,I_:Array [Array [Int ,0B1],05];}Class L_:C_{Var $____,$49An,e:Array [Int ,28];Constructor (){}Constructor (){}Val $v0:Int ;}''',
                '''Class,_,:,b,{,Var,$_,:,Array,[,Float,,,7,],;,$_2,(,RX,,,C0,,,h3C,,,_2,,,_53_3CG_,,,c2,,,_,,,v5,:,VO,),{,},Val,l5,,,$F,:,ZP4,;,G_0h_,(,_,:,Float,;,cF,,,_,:,Boolean,),{,},Var,_f_e,:,_3,;,Val,__,,,__,,,$_,,,I_,:,Array,[,Array,[,Int,,,0B1,],,,05,],;,},Class,L_,:,C_,{,Var,$____,,,$49An,,,e,:,Array,[,Int,,,28,],;,Constructor,(,),{,},Constructor,(,),{,},Val,$v0,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_874(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var p0,$_k,$9:Array [Array [Array [String ,38],0106],0106];Constructor (__:Array [Array [String ,0B101],07];_v:Float ;_:E_1;_l:String ;n66S,_,_,_:r__;u,_4i,__:_6){}$G(y,_:G_g_9){} }''',
                '''Class,_,{,Var,p0,,,$_k,,,$9,:,Array,[,Array,[,Array,[,String,,,38,],,,0106,],,,0106,],;,Constructor,(,__,:,Array,[,Array,[,String,,,0B101,],,,07,],;,_v,:,Float,;,_,:,E_1,;,_l,:,String,;,n66S,,,_,,,_,,,_,:,r__,;,u,,,_4i,,,__,:,_6,),{,},$G,(,y,,,_,:,G_g_9,),{,},},<EOF>''',
                101
            )
        )

    def test_875(self):
        self.assertTrue(
            TestLexer.test(
                '''Class F{}Class AZ{$__4(){} }Class _x6Q_{}Class F__:_{}Class __{}Class Z_U{Val b:Array [Array [Array [Array [Boolean ,0b1],050],0435],01];_(){}Destructor (){}Val $4_,$O,B,_:Array [Array [Array [Array [Int ,74],0x3],03],0X45];}''',
                '''Class,F,{,},Class,AZ,{,$__4,(,),{,},},Class,_x6Q_,{,},Class,F__,:,_,{,},Class,__,{,},Class,Z_U,{,Val,b,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1,],,,050,],,,0435,],,,01,],;,_,(,),{,},Destructor,(,),{,},Val,$4_,,,$O,,,B,,,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,74,],,,0x3,],,,03,],,,0X45,],;,},<EOF>''',
                101
            )
        )

    def test_876(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T_{Constructor (q8:Array [Boolean ,0b110_0];___:Array [String ,0107]){}Constructor (O:Boolean ;_0:Boolean ;w:N){Continue ;} }''',
                '''Class,T_,{,Constructor,(,q8,:,Array,[,Boolean,,,0b1100,],;,___,:,Array,[,String,,,0107,],),{,},Constructor,(,O,:,Boolean,;,_0,:,Boolean,;,w,:,N,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_877(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _s_:_p{Constructor (MN,c44_G,_B7JN:Array [Array [Array [Boolean ,0X46],0x3A],053560]){}Constructor (){}f2(I_q:Int ;q_:Array [Int ,0X4C_5];y_S,GI:Array [Array [Int ,0xF_9_A],05]){}Constructor (){}__Q(_8:____;f_:_;bs_,p:_48dF;_:Float ){} }''',
                '''Class,_s_,:,_p,{,Constructor,(,MN,,,c44_G,,,_B7JN,:,Array,[,Array,[,Array,[,Boolean,,,0X46,],,,0x3A,],,,053560,],),{,},Constructor,(,),{,},f2,(,I_q,:,Int,;,q_,:,Array,[,Int,,,0X4C5,],;,y_S,,,GI,:,Array,[,Array,[,Int,,,0xF9A,],,,05,],),{,},Constructor,(,),{,},__Q,(,_8,:,____,;,f_,:,_,;,bs_,,,p,:,_48dF,;,_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_878(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{Constructor (){}$Q(_6,_u,_3_:Array [Array [String ,063],060]){}_v(){ {} }}Class gw_f{}Class uEl:Ta{}Class Ok{}''',
                '''Class,__,{,Constructor,(,),{,},$Q,(,_6,,,_u,,,_3_,:,Array,[,Array,[,String,,,063,],,,060,],),{,},_v,(,),{,{,},},},Class,gw_f,{,},Class,uEl,:,Ta,{,},Class,Ok,{,},<EOF>''',
                101
            )
        )

    def test_879(self):
        self.assertTrue(
            TestLexer.test(
                '''Class x:M_1__v9_4_6{Destructor (){} }Class _:_s2H9{Val $_:Array [Array [Array [Array [Int ,0X3],071_61_5_3],0B11_1],076];}Class fZ3R:_{}''',
                '''Class,x,:,M_1__v9_4_6,{,Destructor,(,),{,},},Class,_,:,_s2H9,{,Val,$_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0X3,],,,0716153,],,,0B111,],,,076,],;,},Class,fZ3R,:,_,{,},<EOF>''',
                101
            )
        )

    def test_880(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var $1,_:Array [Array [Array [Boolean ,010],7],51];}Class g:h{Val __2:_WT_;Val $7,$n4_0,$A__,$g,_,k_:_;}Class _5p:_{}''',
                '''Class,_,{,Var,$1,,,_,:,Array,[,Array,[,Array,[,Boolean,,,010,],,,7,],,,51,],;,},Class,g,:,h,{,Val,__2,:,_WT_,;,Val,$7,,,$n4_0,,,$A__,,,$g,,,_,,,k_,:,_,;,},Class,_5p,:,_,{,},<EOF>''',
                101
            )
        )

    def test_881(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{_(_,_:Float ;_,O:_;H,__9:Array [Array [Float ,89],89];X,D:_;W,Ta,O__:Int ){} }Class u:ec{Var $94t:_2;}''',
                '''Class,_,:,_,{,_,(,_,,,_,:,Float,;,_,,,O,:,_,;,H,,,__9,:,Array,[,Array,[,Float,,,89,],,,89,],;,X,,,D,:,_,;,W,,,Ta,,,O__,:,Int,),{,},},Class,u,:,ec,{,Var,$94t,:,_2,;,},<EOF>''',
                101
            )
        )

    def test_882(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _p:y{$_0(){}Destructor (){}z(_____:Array [Array [Array [Boolean ,0b11],0127],0b101];wv2:Float ;tU:Boolean ){} }''',
                '''Class,_p,:,y,{,$_0,(,),{,},Destructor,(,),{,},z,(,_____,:,Array,[,Array,[,Array,[,Boolean,,,0b11,],,,0127,],,,0b101,],;,wv2,:,Float,;,tU,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_883(self):
        self.assertTrue(
            TestLexer.test(
                '''Class f{Val q,$_o,K,_,$_:Array [Boolean ,0b1001011];Destructor (){}Var $5_oSq45,$77,$_:Boolean ;}Class C{}Class A_{$n4(){Return ;Continue ;Continue ;} }Class _q__rR{}Class Iaq:_1Ou4{}''',
                '''Class,f,{,Val,q,,,$_o,,,K,,,_,,,$_,:,Array,[,Boolean,,,0b1001011,],;,Destructor,(,),{,},Var,$5_oSq45,,,$77,,,$_,:,Boolean,;,},Class,C,{,},Class,A_,{,$n4,(,),{,Return,;,Continue,;,Continue,;,},},Class,_q__rR,{,},Class,Iaq,:,_1Ou4,{,},<EOF>''',
                101
            )
        )

    def test_884(self):
        self.assertTrue(
            TestLexer.test(
                '''Class L0{}Class A:_Y{}Class R94w_:_{}Class u_9:O{}Class _:_{}Class o0{Val $h,v5k2,_6,$_,$B_9_S:String ;Var $6_,$_5,Zx:__;}''',
                '''Class,L0,{,},Class,A,:,_Y,{,},Class,R94w_,:,_,{,},Class,u_9,:,O,{,},Class,_,:,_,{,},Class,o0,{,Val,$h,,,v5k2,,,_6,,,$_,,,$B_9_S,:,String,;,Var,$6_,,,$_5,,,Zx,:,__,;,},<EOF>''',
                101
            )
        )

    def test_885(self):
        self.assertTrue(
            TestLexer.test(
                '''Class u:_{Destructor (){Val _:Array [Array [Array [Boolean ,0XA9_D_D_06],0x5_0],0b10_0];}Var $T,_:Int ;Destructor (){Break ;}Val _c:Boolean ;Val t_,$0:_;}''',
                '''Class,u,:,_,{,Destructor,(,),{,Val,_,:,Array,[,Array,[,Array,[,Boolean,,,0XA9DD06,],,,0x50,],,,0b100,],;,},Var,$T,,,_,:,Int,;,Destructor,(,),{,Break,;,},Val,_c,:,Boolean,;,Val,t_,,,$0,:,_,;,},<EOF>''',
                101
            )
        )

    def test_886(self):
        self.assertTrue(
            TestLexer.test(
                '''Class r_{}Class _I1{Val r_:Float ;Constructor (x,NV:J_;__:Array [Array [Array [Int ,0X1A],0b1_01_0_1_0],010];T,i_:_;BRa_:Array [Array [Boolean ,07_3],1]){} }''',
                '''Class,r_,{,},Class,_I1,{,Val,r_,:,Float,;,Constructor,(,x,,,NV,:,J_,;,__,:,Array,[,Array,[,Array,[,Int,,,0X1A,],,,0b101010,],,,010,],;,T,,,i_,:,_,;,BRa_,:,Array,[,Array,[,Boolean,,,073,],,,1,],),{,},},<EOF>''',
                101
            )
        )

    def test_887(self):
        self.assertTrue(
            TestLexer.test(
                '''Class xgrI:__{Constructor (_:Int ;Z2,C:Array [Int ,0B1001111];_,U19_:Array [Boolean ,0b1];_:__1){} }Class x{Constructor (I:_07v0__2_){} }''',
                '''Class,xgrI,:,__,{,Constructor,(,_,:,Int,;,Z2,,,C,:,Array,[,Int,,,0B1001111,],;,_,,,U19_,:,Array,[,Boolean,,,0b1,],;,_,:,__1,),{,},},Class,x,{,Constructor,(,I,:,_07v0__2_,),{,},},<EOF>''',
                101
            )
        )

    def test_888(self):
        self.assertTrue(
            TestLexer.test(
                '''Class p72{Var $8_:gMf_2594;}Class _7o:__{$___(Q:Array [Int ,92];_N:Array [Boolean ,0B1111];_:String ;_2_,_:M06;_K,L:_){} }Class _3:_00{}''',
                '''Class,p72,{,Var,$8_,:,gMf_2594,;,},Class,_7o,:,__,{,$___,(,Q,:,Array,[,Int,,,92,],;,_N,:,Array,[,Boolean,,,0B1111,],;,_,:,String,;,_2_,,,_,:,M06,;,_K,,,L,:,_,),{,},},Class,_3,:,_00,{,},<EOF>''',
                101
            )
        )

    def test_889(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (J:Array [Array [Array [Boolean ,0XC],2],0x4E]){}Var c:Float ;Val _52_,$4r_5,$o0:String ;}Class g41P2_:_{}''',
                '''Class,_,{,Constructor,(,J,:,Array,[,Array,[,Array,[,Boolean,,,0XC,],,,2,],,,0x4E,],),{,},Var,c,:,Float,;,Val,_52_,,,$4r_5,,,$o0,:,String,;,},Class,g41P2_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_890(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _K8_:NF{Constructor (_:Array [Array [Array [Array [Array [Int ,0xD3_08],5],0B1],0x3B],0XD];_D8,_m_hx:Float ){}Var $C_:Boolean ;}Class _96:__28_{}''',
                '''Class,_K8_,:,NF,{,Constructor,(,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0xD308,],,,5,],,,0B1,],,,0x3B,],,,0XD,],;,_D8,,,_m_hx,:,Float,),{,},Var,$C_,:,Boolean,;,},Class,_96,:,__28_,{,},<EOF>''',
                101
            )
        )

    def test_891(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _kJN_{_f(){}Constructor (){Val _,_3_:Array [Boolean ,0b1];}x71E9m9(){}Var _:_;$_R(_:Array [Array [Int ,021],0XCF];__:Int ){} }Class _{}''',
                '''Class,_kJN_,{,_f,(,),{,},Constructor,(,),{,Val,_,,,_3_,:,Array,[,Boolean,,,0b1,],;,},x71E9m9,(,),{,},Var,_,:,_,;,$_R,(,_,:,Array,[,Array,[,Int,,,021,],,,0XCF,],;,__,:,Int,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_892(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __p:_{Constructor (Vt3C,n,_:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,46],03],3_070],0x2_5_F],0b1],034_5],066],54]){}Var $_4,G:j;}Class _{}Class I0_{}''',
                '''Class,__p,:,_,{,Constructor,(,Vt3C,,,n,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,46,],,,03,],,,3070,],,,0x25F,],,,0b1,],,,0345,],,,066,],,,54,],),{,},Var,$_4,,,G,:,j,;,},Class,_,{,},Class,I0_,{,},<EOF>''',
                101
            )
        )

    def test_893(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{$_Y(){}Var Bx,$L3:Array [Array [Boolean ,02],02];Val c_,h5_,q_:Array [Array [Int ,0X8_9],60];}Class _{}Class _70_9:Z1{}Class _9:Y8{Val $6:Array [Float ,0xC];}''',
                '''Class,_,{,$_Y,(,),{,},Var,Bx,,,$L3,:,Array,[,Array,[,Boolean,,,02,],,,02,],;,Val,c_,,,h5_,,,q_,:,Array,[,Array,[,Int,,,0X89,],,,60,],;,},Class,_,{,},Class,_70_9,:,Z1,{,},Class,_9,:,Y8,{,Val,$6,:,Array,[,Float,,,0xC,],;,},<EOF>''',
                101
            )
        )

    def test_894(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2{Constructor (p8:_){Break ;} }Class _{}Class i:_H0_65_{Destructor (){Val C66:Array [Boolean ,0x652_1];} }Class Nv_p_1:___{}''',
                '''Class,_2,{,Constructor,(,p8,:,_,),{,Break,;,},},Class,_,{,},Class,i,:,_H0_65_,{,Destructor,(,),{,Val,C66,:,Array,[,Boolean,,,0x6521,],;,},},Class,Nv_p_1,:,___,{,},<EOF>''',
                101
            )
        )

    def test_895(self):
        self.assertTrue(
            TestLexer.test(
                '''Class uH{}Class _:DU79{}Class zs{Var _f:Array [Array [Array [Array [Array [Array [Array [Array [Int ,0x3],06_61_2],0b1000110],02],0X34],0b1_00],0X3],0xA];}''',
                '''Class,uH,{,},Class,_,:,DU79,{,},Class,zs,{,Var,_f,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x3,],,,06612,],,,0b1000110,],,,02,],,,0X34,],,,0b100,],,,0X3,],,,0xA,],;,},<EOF>''',
                101
            )
        )

    def test_896(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _Tp{Val $8,$r_:Int ;$2(__:Array [Int ,0B101011];e_:Array [Array [Float ,0X17],3]){}Val _,Ex,__:Float ;Destructor (){} }''',
                '''Class,_Tp,{,Val,$8,,,$r_,:,Int,;,$2,(,__,:,Array,[,Int,,,0B101011,],;,e_,:,Array,[,Array,[,Float,,,0X17,],,,3,],),{,},Val,_,,,Ex,,,__,:,Float,;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_897(self):
        self.assertTrue(
            TestLexer.test(
                '''Class S_:_2{$_R1(){} }Class E_:i{Constructor (){Break ;}Constructor (){}Var _,__d7,$_,l,_R,$r:Array [Array [Int ,056551],0104];}''',
                '''Class,S_,:,_2,{,$_R1,(,),{,},},Class,E_,:,i,{,Constructor,(,),{,Break,;,},Constructor,(,),{,},Var,_,,,__d7,,,$_,,,l,,,_R,,,$r,:,Array,[,Array,[,Int,,,056551,],,,0104,],;,},<EOF>''',
                101
            )
        )

    def test_898(self):
        self.assertTrue(
            TestLexer.test(
                '''Class z:___F_{}Class _:_{Var A:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0b1],0xF_1_5F],1],0b1],05_20_6_3],841_87],0x53],6];}''',
                '''Class,z,:,___F_,{,},Class,_,:,_,{,Var,A,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1,],,,0xF15F,],,,1,],,,0b1,],,,052063,],,,84187,],,,0x53,],,,6,],;,},<EOF>''',
                101
            )
        )

    def test_899(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ____{}Class _{}Class qr{Var G:c;}Class KK:_{}Class gdC_I{}Class O{Var $40:_;Var _3_,x:Float ;Constructor (){Break ;} }''',
                '''Class,____,{,},Class,_,{,},Class,qr,{,Var,G,:,c,;,},Class,KK,:,_,{,},Class,gdC_I,{,},Class,O,{,Var,$40,:,_,;,Var,_3_,,,x,:,Float,;,Constructor,(,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_900(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __7{Destructor (){} }Class zl4P{}Class _T{}Class _0S{Var $P,$2,_,$_,$6940_,$eL:String ;}Class Wy:Tv5{}Class E__t{}''',
                '''Class,__7,{,Destructor,(,),{,},},Class,zl4P,{,},Class,_T,{,},Class,_0S,{,Var,$P,,,$2,,,_,,,$_,,,$6940_,,,$eL,:,String,;,},Class,Wy,:,Tv5,{,},Class,E__t,{,},<EOF>''',
                101
            )
        )

    def test_901(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_y{}Class W5:v4{_pac(_2,D_,__:Array [Array [Array [Float ,0B11],0xE],066];____1,_:Array [Boolean ,71]){Val _1,a6:Array [Array [Array [Float ,066],066],0x3E];} }Class _Gn{}Class __a{}''',
                '''Class,_,:,_y,{,},Class,W5,:,v4,{,_pac,(,_2,,,D_,,,__,:,Array,[,Array,[,Array,[,Float,,,0B11,],,,0xE,],,,066,],;,____1,,,_,:,Array,[,Boolean,,,71,],),{,Val,_1,,,a6,:,Array,[,Array,[,Array,[,Float,,,066,],,,066,],,,0x3E,],;,},},Class,_Gn,{,},Class,__a,{,},<EOF>''',
                101
            )
        )

    def test_902(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _pI_{Constructor (_E_9,D,q_0:Array [Boolean ,2]){_::$0();}$x3(__,g,k__:Boolean ;_,e,_:Float ;j,Qc,_:String ){}Var $F,$r5_36_,_:Array [Float ,0XB];}Class _:t7{Val _,_v:Array [Int ,0xF3A];Val __,_jk,q,_18:Array [String ,0XE_E];}''',
                '''Class,_pI_,{,Constructor,(,_E_9,,,D,,,q_0,:,Array,[,Boolean,,,2,],),{,_,::,$0,(,),;,},$x3,(,__,,,g,,,k__,:,Boolean,;,_,,,e,,,_,:,Float,;,j,,,Qc,,,_,:,String,),{,},Var,$F,,,$r5_36_,,,_,:,Array,[,Float,,,0XB,],;,},Class,_,:,t7,{,Val,_,,,_v,:,Array,[,Int,,,0xF3A,],;,Val,__,,,_jk,,,q,,,_18,:,Array,[,String,,,0XEE,],;,},<EOF>''',
                101
            )
        )

    def test_903(self):
        self.assertTrue(
            TestLexer.test(
                '''Class K7VlL43{}Class t1:J28{}Class _k_{Constructor (_,o_,l,_2:el4;__:Array [Array [Array [Int ,0B1],0b1_0_1],037];efk,_64x,_:Array [String ,0b110_1];v3,KT,_Lu,E,_BY:b06A;_,Dz:Array [Float ,03_4_30_6_25]){}Val $__:String ;}Class L3{}''',
                '''Class,K7VlL43,{,},Class,t1,:,J28,{,},Class,_k_,{,Constructor,(,_,,,o_,,,l,,,_2,:,el4,;,__,:,Array,[,Array,[,Array,[,Int,,,0B1,],,,0b101,],,,037,],;,efk,,,_64x,,,_,:,Array,[,String,,,0b1101,],;,v3,,,KT,,,_Lu,,,E,,,_BY,:,b06A,;,_,,,Dz,:,Array,[,Float,,,03430625,],),{,},Val,$__,:,String,;,},Class,L3,{,},<EOF>''',
                101
            )
        )

    def test_904(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class V:t8{}Class v:q{}Class oD_{D(A,_,_:_3;_:Array [Array [String ,55],64_9]){} }Class PKd7{}Class _{}''',
                '''Class,__,{,},Class,V,:,t8,{,},Class,v,:,q,{,},Class,oD_,{,D,(,A,,,_,,,_,:,_3,;,_,:,Array,[,Array,[,String,,,55,],,,649,],),{,},},Class,PKd7,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_905(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q{_(F58X:Int ){} }Class _zQ:R{}Class b:e_CCG___e__52{}Class KKDK:J{__O_h(o__J__,H3X,_h_3:Array [String ,0X33]){} }Class _2:w{}Class _15{}Class _{Val $7,_6v,$_:q;}''',
                '''Class,q,{,_,(,F58X,:,Int,),{,},},Class,_zQ,:,R,{,},Class,b,:,e_CCG___e__52,{,},Class,KKDK,:,J,{,__O_h,(,o__J__,,,H3X,,,_h_3,:,Array,[,String,,,0X33,],),{,},},Class,_2,:,w,{,},Class,_15,{,},Class,_,{,Val,$7,,,_6v,,,$_,:,q,;,},<EOF>''',
                101
            )
        )

    def test_906(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b{}Class _9:w36{Val $j4,$__,_,$n,___:Array [Array [Array [Float ,0B1],06],0x1];w(__:__;O:Array [Boolean ,023]){} }''',
                '''Class,b,{,},Class,_9,:,w36,{,Val,$j4,,,$__,,,_,,,$n,,,___,:,Array,[,Array,[,Array,[,Float,,,0B1,],,,06,],,,0x1,],;,w,(,__,:,__,;,O,:,Array,[,Boolean,,,023,],),{,},},<EOF>''',
                101
            )
        )

    def test_907(self):
        self.assertTrue(
            TestLexer.test(
                '''Class il{$__4(_il,Z,xa,_X422_y_,_,J,t,r__,___,_:Array [Array [Float ,47_76],96];_rb,v_,N,W,m_:Array [Int ,0B1010];_:_){ {} }}''',
                '''Class,il,{,$__4,(,_il,,,Z,,,xa,,,_X422_y_,,,_,,,J,,,t,,,r__,,,___,,,_,:,Array,[,Array,[,Float,,,4776,],,,96,],;,_rb,,,v_,,,N,,,W,,,m_,:,Array,[,Int,,,0B1010,],;,_,:,_,),{,{,},},},<EOF>''',
                101
            )
        )

    def test_908(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:P{}Class n{Destructor (){}Destructor (){_::$e();Continue ;} }Class __{}Class _:_{}Class E{}Class _P_9_W{}''',
                '''Class,_,:,P,{,},Class,n,{,Destructor,(,),{,},Destructor,(,),{,_,::,$e,(,),;,Continue,;,},},Class,__,{,},Class,_,:,_,{,},Class,E,{,},Class,_P_9_W,{,},<EOF>''',
                101
            )
        )

    def test_909(self):
        self.assertTrue(
            TestLexer.test(
                '''Class wU{m(){B_::$1();Var U:_;G::$d8_4.dT()._39();} }Class R{_P(_:Float ;_:Int ){}Val $_e1a8:_;Destructor (){}Destructor (){} }''',
                '''Class,wU,{,m,(,),{,B_,::,$1,(,),;,Var,U,:,_,;,G,::,$d8_4,.,dT,(,),.,_39,(,),;,},},Class,R,{,_P,(,_,:,Float,;,_,:,Int,),{,},Val,$_e1a8,:,_,;,Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_910(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class DE9{Constructor (u,H1Y:r3q;_V40,s2B_,_r_fM,RN:Array [Array [Float ,5],0X5];_7:Array [Int ,0X63]){} }''',
                '''Class,_,{,},Class,DE9,{,Constructor,(,u,,,H1Y,:,r3q,;,_V40,,,s2B_,,,_r_fM,,,RN,:,Array,[,Array,[,Float,,,5,],,,0X5,],;,_7,:,Array,[,Int,,,0X63,],),{,},},<EOF>''',
                101
            )
        )

    def test_911(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9S:N_4{Constructor (_,_FCV__,_,W,h,g_,_,_:Array [String ,75_7_6];_:_;uT:Array [Array [Array [Boolean ,0X41],80],02_7_3]){}Destructor (){}$L(Q,r,_:Boolean ){} }''',
                '''Class,_9S,:,N_4,{,Constructor,(,_,,,_FCV__,,,_,,,W,,,h,,,g_,,,_,,,_,:,Array,[,String,,,7576,],;,_,:,_,;,uT,:,Array,[,Array,[,Array,[,Boolean,,,0X41,],,,80,],,,0273,],),{,},Destructor,(,),{,},$L,(,Q,,,r,,,_,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_912(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _3{$a(){} }Class _:_{}Class __:G{Var $j2__:_6;_(_:Array [Array [Array [String ,0x57],7],0x3]){}Constructor (x:Boolean ){}Destructor (){} }Class _{}''',
                '''Class,_3,{,$a,(,),{,},},Class,_,:,_,{,},Class,__,:,G,{,Var,$j2__,:,_6,;,_,(,_,:,Array,[,Array,[,Array,[,String,,,0x57,],,,7,],,,0x3,],),{,},Constructor,(,x,:,Boolean,),{,},Destructor,(,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_913(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _tt:_G8i{Val $60,M5,n,$_:Array [Float ,0xA];_Zg(_,c,_,f:String ){Continue ;Continue ;} }Class i_{Var $zr8,$37:String ;}Class _:_{}''',
                '''Class,_tt,:,_G8i,{,Val,$60,,,M5,,,n,,,$_,:,Array,[,Float,,,0xA,],;,_Zg,(,_,,,c,,,_,,,f,:,String,),{,Continue,;,Continue,;,},},Class,i_,{,Var,$zr8,,,$37,:,String,;,},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_914(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b{Constructor (){}Constructor (_:_;j,C,__,__:Array [Array [Array [Int ,040],075],0b1_0];w:Float ){} }Class _:_{Destructor (){} }Class b_{}''',
                '''Class,b,{,Constructor,(,),{,},Constructor,(,_,:,_,;,j,,,C,,,__,,,__,:,Array,[,Array,[,Array,[,Int,,,040,],,,075,],,,0b10,],;,w,:,Float,),{,},},Class,_,:,_,{,Destructor,(,),{,},},Class,b_,{,},<EOF>''',
                101
            )
        )

    def test_915(self):
        self.assertTrue(
            TestLexer.test(
                '''Class B2J1{Destructor (){}$_(b,_U,_:Int ;r,A:__;XU_:Array [Array [Array [Boolean ,60_8],59],0x60];x79S,F:Float ){Return ;} }Class _{}''',
                '''Class,B2J1,{,Destructor,(,),{,},$_,(,b,,,_U,,,_,:,Int,;,r,,,A,:,__,;,XU_,:,Array,[,Array,[,Array,[,Boolean,,,608,],,,59,],,,0x60,],;,x79S,,,F,:,Float,),{,Return,;,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_916(self):
        self.assertTrue(
            TestLexer.test(
                '''Class h:y_{}Class k{Destructor (){}Val $2_a1:Array [Array [Float ,0X58],91];Val $51,$_T:Array [Float ,0x479];}Class W{}Class S___{}Class P__B:_b{}''',
                '''Class,h,:,y_,{,},Class,k,{,Destructor,(,),{,},Val,$2_a1,:,Array,[,Array,[,Float,,,0X58,],,,91,],;,Val,$51,,,$_T,:,Array,[,Float,,,0x479,],;,},Class,W,{,},Class,S___,{,},Class,P__B,:,_b,{,},<EOF>''',
                101
            )
        )

    def test_917(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A:q{Var _,_2,R4:Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,9],0x1],0106],0X87],7],037],0106],0X48],4_26];}''',
                '''Class,A,:,q,{,Var,_,,,_2,,,R4,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,9,],,,0x1,],,,0106,],,,0X87,],,,7,],,,037,],,,0106,],,,0X48,],,,426,],;,},<EOF>''',
                101
            )
        )

    def test_918(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_375V{Val $s,$C:Boolean ;_(sU:g;C:Float ;_,N:Array [Array [Array [String ,0B1_0],0106],0XB];P,C32382,_9,W,__z2:String ){} }''',
                '''Class,_,:,_375V,{,Val,$s,,,$C,:,Boolean,;,_,(,sU,:,g,;,C,:,Float,;,_,,,N,:,Array,[,Array,[,Array,[,String,,,0B10,],,,0106,],,,0XB,],;,P,,,C32382,,,_9,,,W,,,__z2,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_919(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q8{Val xR,$_91,_7,O_A:_C;Destructor (){ {{}{Return ;_o4o::$Hr_.i();If (!-k::$_5_v0_){}Else {} }}Continue ;}$_d(_:String ;y:Array [Boolean ,0X5D_7]){} }Class A{}''',
                '''Class,q8,{,Val,xR,,,$_91,,,_7,,,O_A,:,_C,;,Destructor,(,),{,{,{,},{,Return,;,_o4o,::,$Hr_,.,i,(,),;,If,(,!,-,k,::,$_5_v0_,),{,},Else,{,},},},Continue,;,},$_d,(,_,:,String,;,y,:,Array,[,Boolean,,,0X5D7,],),{,},},Class,A,{,},<EOF>''',
                101
            )
        )

    def test_920(self):
        self.assertTrue(
            TestLexer.test(
                '''Class KnC_99f:w8_{Destructor (){}Destructor (){} }Class _2_7{}Class _{Var $T_8:Array [Float ,0x18];}Class L:H{M__R(_,_:_){}Val Gr,$Y7,$F:Array [Int ,05];Var $___P2_:Array [Array [String ,060],0b101001];Destructor (){}$5Q2(_:Boolean ;_I:_2;e,J,_,g,N,X___pa_:Array [Array [Boolean ,0x48],33]){}Constructor (){} }''',
                '''Class,KnC_99f,:,w8_,{,Destructor,(,),{,},Destructor,(,),{,},},Class,_2_7,{,},Class,_,{,Var,$T_8,:,Array,[,Float,,,0x18,],;,},Class,L,:,H,{,M__R,(,_,,,_,:,_,),{,},Val,Gr,,,$Y7,,,$F,:,Array,[,Int,,,05,],;,Var,$___P2_,:,Array,[,Array,[,String,,,060,],,,0b101001,],;,Destructor,(,),{,},$5Q2,(,_,:,Boolean,;,_I,:,_2,;,e,,,J,,,_,,,g,,,N,,,X___pa_,:,Array,[,Array,[,Boolean,,,0x48,],,,33,],),{,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_921(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _T_H9C__91_{Constructor (){} }Class _{Destructor (){} }Class Q{Destructor (){} }Class J:f{Constructor (){}Constructor (r4:O9;_A,C,_,W:Array [Array [String ,04],0615];_q,C8:Array [Array [Array [Float ,02],57],5]){New d7().K();Var _,O:Boolean ;Continue ;}Destructor (){} }Class k{}''',
                '''Class,_T_H9C__91_,{,Constructor,(,),{,},},Class,_,{,Destructor,(,),{,},},Class,Q,{,Destructor,(,),{,},},Class,J,:,f,{,Constructor,(,),{,},Constructor,(,r4,:,O9,;,_A,,,C,,,_,,,W,:,Array,[,Array,[,String,,,04,],,,0615,],;,_q,,,C8,:,Array,[,Array,[,Array,[,Float,,,02,],,,57,],,,5,],),{,New,d7,(,),.,K,(,),;,Var,_,,,O,:,Boolean,;,Continue,;,},Destructor,(,),{,},},Class,k,{,},<EOF>''',
                101
            )
        )

    def test_922(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __g6{Constructor (_U,_3,e,_,r:String ){}Destructor (){}Destructor (){} }Class ___{$5(_:Float ){}__(){Val _q,_,_:Array [Array [Int ,0270_2_05_30_2],0B111000];}Var W,Ju0,$001___,_,c,$6,_,$MP_,$Y:_;}''',
                '''Class,__g6,{,Constructor,(,_U,,,_3,,,e,,,_,,,r,:,String,),{,},Destructor,(,),{,},Destructor,(,),{,},},Class,___,{,$5,(,_,:,Float,),{,},__,(,),{,Val,_q,,,_,,,_,:,Array,[,Array,[,Int,,,0270205302,],,,0B111000,],;,},Var,W,,,Ju0,,,$001___,,,_,,,c,,,$6,,,_,,,$MP_,,,$Y,:,_,;,},<EOF>''',
                101
            )
        )

    def test_923(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:o7{}Class _o_{$5(a_,_L_,__6,m:Array [Array [Array [Float ,053],0xB],0B10]){}Var _J:Array [Array [Array [Array [Int ,065_44],0B1],0X21],032];}''',
                '''Class,__,:,o7,{,},Class,_o_,{,$5,(,a_,,,_L_,,,__6,,,m,:,Array,[,Array,[,Array,[,Float,,,053,],,,0xB,],,,0B10,],),{,},Var,_J,:,Array,[,Array,[,Array,[,Array,[,Int,,,06544,],,,0B1,],,,0X21,],,,032,],;,},<EOF>''',
                101
            )
        )

    def test_924(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _b{H(_n7:Array [Int ,0X998];_:Array [Float ,07_0];m:Array [Array [Array [Array [Int ,053],0B1],0XF],0B1]){} }''',
                '''Class,_b,{,H,(,_n7,:,Array,[,Int,,,0X998,],;,_,:,Array,[,Float,,,070,],;,m,:,Array,[,Array,[,Array,[,Array,[,Int,,,053,],,,0B1,],,,0XF,],,,0B1,],),{,},},<EOF>''',
                101
            )
        )

    def test_925(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_,g,_,q,r:__;L:String ;_R_,x,N:Array [Int ,0X2];L:Array [Int ,03_6]){Continue ;}Var $2,$_U:Boolean ;Val Q,$4j,___P9_:Array [Int ,0B10100];}''',
                '''Class,_,{,Constructor,(,_,,,g,,,_,,,q,,,r,:,__,;,L,:,String,;,_R_,,,x,,,N,:,Array,[,Int,,,0X2,],;,L,:,Array,[,Int,,,036,],),{,Continue,;,},Var,$2,,,$_U,:,Boolean,;,Val,Q,,,$4j,,,___P9_,:,Array,[,Int,,,0B10100,],;,},<EOF>''',
                101
            )
        )

    def test_926(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n_:W{}Class y:M_7t{Var $e9,k8_v:Boolean ;Destructor (){Return ;Continue ;} }Class _6:n_{Destructor (){}Val $_:E;}''',
                '''Class,n_,:,W,{,},Class,y,:,M_7t,{,Var,$e9,,,k8_v,:,Boolean,;,Destructor,(,),{,Return,;,Continue,;,},},Class,_6,:,n_,{,Destructor,(,),{,},Val,$_,:,E,;,},<EOF>''',
                101
            )
        )

    def test_927(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _j0:TZ{Var _,$Z4,$2A,E4,$8uQ,$70:Int ;}Class _{Var _g:Array [Array [Int ,0B100110],0x63];Var a2,$F:Array [Float ,0X2A];}Class ___{}''',
                '''Class,_j0,:,TZ,{,Var,_,,,$Z4,,,$2A,,,E4,,,$8uQ,,,$70,:,Int,;,},Class,_,{,Var,_g,:,Array,[,Array,[,Int,,,0B100110,],,,0x63,],;,Var,a2,,,$F,:,Array,[,Float,,,0X2A,],;,},Class,___,{,},<EOF>''',
                101
            )
        )

    def test_928(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C_:E{Var t:Array [Float ,02_6];}Class d:_29{Val $6:String ;Val m:Boolean ;Val $1,$__0____,W,$7:Array [Boolean ,070];Val G_7,___,$d:Boolean ;}Class K:Pd_i1{}''',
                '''Class,C_,:,E,{,Var,t,:,Array,[,Float,,,026,],;,},Class,d,:,_29,{,Val,$6,:,String,;,Val,m,:,Boolean,;,Val,$1,,,$__0____,,,W,,,$7,:,Array,[,Boolean,,,070,],;,Val,G_7,,,___,,,$d,:,Boolean,;,},Class,K,:,Pd_i1,{,},<EOF>''',
                101
            )
        )

    def test_929(self):
        self.assertTrue(
            TestLexer.test(
                '''Class d_:Zj1R8_{}Class y40:E{Destructor (){Continue ;}Destructor (){}_(S:_;ts:v){Break ;}Constructor (){Null .q();} }''',
                '''Class,d_,:,Zj1R8_,{,},Class,y40,:,E,{,Destructor,(,),{,Continue,;,},Destructor,(,),{,},_,(,S,:,_,;,ts,:,v,),{,Break,;,},Constructor,(,),{,Null,.,q,(,),;,},},<EOF>''',
                101
            )
        )

    def test_930(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:UmI0T__942{Val _,_:Array [Array [Boolean ,0X46],07];Constructor (){} }Class _:q{Destructor (){}Var _:Array [Array [Boolean ,2_7_4],04_5_1];}''',
                '''Class,_,:,UmI0T__942,{,Val,_,,,_,:,Array,[,Array,[,Boolean,,,0X46,],,,07,],;,Constructor,(,),{,},},Class,_,:,q,{,Destructor,(,),{,},Var,_,:,Array,[,Array,[,Boolean,,,274,],,,0451,],;,},<EOF>''',
                101
            )
        )

    def test_931(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Y:n{_M5_(K_,__:Array [Array [Array [Float ,50],0x1B],0B111000];H_5:Array [String ,50]){}Val $4:X;Var nV,Y,u,l8_:Int ;$9(){} }''',
                '''Class,Y,:,n,{,_M5_,(,K_,,,__,:,Array,[,Array,[,Array,[,Float,,,50,],,,0x1B,],,,0B111000,],;,H_5,:,Array,[,String,,,50,],),{,},Val,$4,:,X,;,Var,nV,,,Y,,,u,,,l8_,:,Int,;,$9,(,),{,},},<EOF>''',
                101
            )
        )

    def test_932(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Var _:C;}Class C_:L7{_(c_7,__,r:Array [Float ,0X55];G,_:Array [Boolean ,0xC];H83x:Int ){} }Class XQ:__{}''',
                '''Class,_,:,_,{,Var,_,:,C,;,},Class,C_,:,L7,{,_,(,c_7,,,__,,,r,:,Array,[,Float,,,0X55,],;,G,,,_,:,Array,[,Boolean,,,0xC,],;,H83x,:,Int,),{,},},Class,XQ,:,__,{,},<EOF>''',
                101
            )
        )

    def test_933(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _iW:__6{}Class e:_{Destructor (){}Constructor (_:Array [Array [Float ,26_4_4],0B1_0];_,_:String ;_:_;oj0:_){Break ;} }''',
                '''Class,_iW,:,__6,{,},Class,e,:,_,{,Destructor,(,),{,},Constructor,(,_,:,Array,[,Array,[,Float,,,2644,],,,0B10,],;,_,,,_,:,String,;,_,:,_,;,oj0,:,_,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_934(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class r21:_{}Class U:Cq5{}Class q6Y_{}Class E_CH_w:__i{$x(){Val r,_:Array [Array [Array [Array [Boolean ,3],13],2],13];} }Class L:l_Pg9{Val i6:_;}''',
                '''Class,_,{,},Class,r21,:,_,{,},Class,U,:,Cq5,{,},Class,q6Y_,{,},Class,E_CH_w,:,__i,{,$x,(,),{,Val,r,,,_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,3,],,,13,],,,2,],,,13,],;,},},Class,L,:,l_Pg9,{,Val,i6,:,_,;,},<EOF>''',
                101
            )
        )

    def test_935(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var $_z:Array [Array [Array [Array [Array [Array [Array [String ,0107],0X76_0],0x3_F9_F_1],0X1F],2],0107],5];}Class q:__{}Class _{}Class KV:_R{Constructor (_D,_:_w;P,h,J:_){} }Class _{Val $9,$7:Array [Array [String ,0107],0107];}Class FT8{}''',
                '''Class,_,{,Var,$_z,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0107,],,,0X760,],,,0x3F9F1,],,,0X1F,],,,2,],,,0107,],,,5,],;,},Class,q,:,__,{,},Class,_,{,},Class,KV,:,_R,{,Constructor,(,_D,,,_,:,_w,;,P,,,h,,,J,:,_,),{,},},Class,_,{,Val,$9,,,$7,:,Array,[,Array,[,String,,,0107,],,,0107,],;,},Class,FT8,{,},<EOF>''',
                101
            )
        )

    def test_936(self):
        self.assertTrue(
            TestLexer.test(
                '''Class j{_(_:Array [Array [Array [Array [Array [Int ,0x9],0124],0x5F],0x8B7],1];_f5:Boolean ;x:Array [Boolean ,0b1011_1];Y,R5:Float ;f5_,_,R,F,D,_:Array [Array [Int ,0X61],0x5F];_Ty,T3_c4,P_,x6_Q_:g0){Var _eH4Xrf,_5_,n:String ;} }''',
                '''Class,j,{,_,(,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x9,],,,0124,],,,0x5F,],,,0x8B7,],,,1,],;,_f5,:,Boolean,;,x,:,Array,[,Boolean,,,0b10111,],;,Y,,,R5,:,Float,;,f5_,,,_,,,R,,,F,,,D,,,_,:,Array,[,Array,[,Int,,,0X61,],,,0x5F,],;,_Ty,,,T3_c4,,,P_,,,x6_Q_,:,g0,),{,Var,_eH4Xrf,,,_5_,,,n,:,String,;,},},<EOF>''',
                101
            )
        )

    def test_937(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Vk{}Class Qi{Destructor (){}$_537x(){ {} }$_(_,r_,_:S){} }Class n_{}Class _6{}Class ___79_{Var $5I3:R0;Constructor (){} }Class y:__{}''',
                '''Class,Vk,{,},Class,Qi,{,Destructor,(,),{,},$_537x,(,),{,{,},},$_,(,_,,,r_,,,_,:,S,),{,},},Class,n_,{,},Class,_6,{,},Class,___79_,{,Var,$5I3,:,R0,;,Constructor,(,),{,},},Class,y,:,__,{,},<EOF>''',
                101
            )
        )

    def test_938(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l_7{}Class _:g56a{Var _:_;Constructor (){_::$_ug46.I_h__().R.mN();{}Continue ;} }Class rT__NI6wt{Var N:Array [Int ,056];}''',
                '''Class,l_7,{,},Class,_,:,g56a,{,Var,_,:,_,;,Constructor,(,),{,_,::,$_ug46,.,I_h__,(,),.,R,.,mN,(,),;,{,},Continue,;,},},Class,rT__NI6wt,{,Var,N,:,Array,[,Int,,,056,],;,},<EOF>''',
                101
            )
        )

    def test_939(self):
        self.assertTrue(
            TestLexer.test(
                '''Class B:_{}Class _gV{}Class q_078s__4H{I_(R9:String ){}$2_Y3(R_:S9;_:Boolean ;_:Array [Array [Array [Int ,0b1_0_1],0B1010001],8];b:Int ;u,__:__750AO;_:String ){}Destructor (){} }Class _{}Class kM6{}Class _k_:Y{}''',
                '''Class,B,:,_,{,},Class,_gV,{,},Class,q_078s__4H,{,I_,(,R9,:,String,),{,},$2_Y3,(,R_,:,S9,;,_,:,Boolean,;,_,:,Array,[,Array,[,Array,[,Int,,,0b101,],,,0B1010001,],,,8,],;,b,:,Int,;,u,,,__,:,__750AO,;,_,:,String,),{,},Destructor,(,),{,},},Class,_,{,},Class,kM6,{,},Class,_k_,:,Y,{,},<EOF>''',
                101
            )
        )

    def test_940(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9{Destructor (){}N(p__5_:Array [Array [Array [Array [Array [String ,064],0B1001],36],0B110],0xF];hI,V,a5:Sa){Break ;} }''',
                '''Class,_9,{,Destructor,(,),{,},N,(,p__5_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,064,],,,0B1001,],,,36,],,,0B110,],,,0xF,],;,hI,,,V,,,a5,:,Sa,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_941(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _X_:_{Var _0H,$2F,$5w:Array [Float ,0B110011];Val CF,__:Array [Array [Boolean ,0b1],0130];Constructor (){Break ;}Val N,q5J:_;}''',
                '''Class,_X_,:,_,{,Var,_0H,,,$2F,,,$5w,:,Array,[,Float,,,0B110011,],;,Val,CF,,,__,:,Array,[,Array,[,Boolean,,,0b1,],,,0130,],;,Constructor,(,),{,Break,;,},Val,N,,,q5J,:,_,;,},<EOF>''',
                101
            )
        )

    def test_942(self):
        self.assertTrue(
            TestLexer.test(
                '''Class H_:__{}Class y_L:_{Var $5k,$L,$_6:Array [Array [Array [Array [Int ,4],0b1],03],0B1];}Class _{}Class _:u8{_(){} }''',
                '''Class,H_,:,__,{,},Class,y_L,:,_,{,Var,$5k,,,$L,,,$_6,:,Array,[,Array,[,Array,[,Array,[,Int,,,4,],,,0b1,],,,03,],,,0B1,],;,},Class,_,{,},Class,_,:,u8,{,_,(,),{,},},<EOF>''',
                101
            )
        )

    def test_943(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o:P_{$3B(){}Var P8,_Z,$_v:_Y4;Val c,_,$_,dk,_:Array [Array [String ,0X18],0B1000000];$B(){}Constructor (Bi,SyR_,_03:_5_;Pr___,_,z_f7:_;_,__cU2:_){Continue ;Continue ;}Destructor (){} }Class N_:_{Constructor (){} }Class _02_:_w{Val $_LL2:Boolean ;}''',
                '''Class,o,:,P_,{,$3B,(,),{,},Var,P8,,,_Z,,,$_v,:,_Y4,;,Val,c,,,_,,,$_,,,dk,,,_,:,Array,[,Array,[,String,,,0X18,],,,0B1000000,],;,$B,(,),{,},Constructor,(,Bi,,,SyR_,,,_03,:,_5_,;,Pr___,,,_,,,z_f7,:,_,;,_,,,__cU2,:,_,),{,Continue,;,Continue,;,},Destructor,(,),{,},},Class,N_,:,_,{,Constructor,(,),{,},},Class,_02_,:,_w,{,Val,$_LL2,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_944(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E{Var $e2K_:Float ;Constructor (){}Val l:tQ;}Class _{Var $49_Z_,$45:Int ;Constructor (_:X;_,l:Array [Array [Int ,3],0b1];_:Array [Int ,0X53_EA8]){Return ;}Var $7:e_;}Class y{}Class _{}''',
                '''Class,E,{,Var,$e2K_,:,Float,;,Constructor,(,),{,},Val,l,:,tQ,;,},Class,_,{,Var,$49_Z_,,,$45,:,Int,;,Constructor,(,_,:,X,;,_,,,l,:,Array,[,Array,[,Int,,,3,],,,0b1,],;,_,:,Array,[,Int,,,0X53EA8,],),{,Return,;,},Var,$7,:,e_,;,},Class,y,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_945(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{Constructor (Z:Float ;_:Int ;_15,_1_,__:_;l_a5S,_8,_VS,UO_,__2,H_,P,_:Boolean ;ZI9:Array [Int ,0X2_5E0_63];_:Array [Int ,0b1_100];_:_){m::$_();}Constructor (_:Array [Float ,0b10];_,_,o_A,h,W,_,_,_,U_:h){_::$__QFD();} }Class _ae{Val _T4__,$05:_;}Class _:o_{}''',
                '''Class,__,{,Constructor,(,Z,:,Float,;,_,:,Int,;,_15,,,_1_,,,__,:,_,;,l_a5S,,,_8,,,_VS,,,UO_,,,__2,,,H_,,,P,,,_,:,Boolean,;,ZI9,:,Array,[,Int,,,0X25E063,],;,_,:,Array,[,Int,,,0b1100,],;,_,:,_,),{,m,::,$_,(,),;,},Constructor,(,_,:,Array,[,Float,,,0b10,],;,_,,,_,,,o_A,,,h,,,W,,,_,,,_,,,_,,,U_,:,h,),{,_,::,$__QFD,(,),;,},},Class,_ae,{,Val,_T4__,,,$05,:,_,;,},Class,_,:,o_,{,},<EOF>''',
                101
            )
        )

    def test_946(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _w:_2GD_{Val $_:Int ;Destructor (){}$2(_,_0c:Array [Array [Array [Boolean ,066],44],2_590];p,_:_L_X;j3:_){}_(){} }Class S:_N{Destructor (){} }''',
                '''Class,_w,:,_2GD_,{,Val,$_,:,Int,;,Destructor,(,),{,},$2,(,_,,,_0c,:,Array,[,Array,[,Array,[,Boolean,,,066,],,,44,],,,2590,],;,p,,,_,:,_L_X,;,j3,:,_,),{,},_,(,),{,},},Class,S,:,_N,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_947(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _O_0{Constructor (_,Y:Array [String ,0XAB_B];__1sU,O6:D67;E,_D,j2:Array [String ,74];a,R_:A_2){Break ;} }''',
                '''Class,_O_0,{,Constructor,(,_,,,Y,:,Array,[,String,,,0XABB,],;,__1sU,,,O6,:,D67,;,E,,,_D,,,j2,:,Array,[,String,,,74,],;,a,,,R_,:,A_2,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_948(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class _{Var _:Boolean ;Var _:Array [Array [Array [Float ,4],86],0x8];Var $y,$0Q2:Array [Int ,0b1];Constructor (__,Z_:Boolean ){} }''',
                '''Class,_,:,_,{,},Class,_,{,Var,_,:,Boolean,;,Var,_,:,Array,[,Array,[,Array,[,Float,,,4,],,,86,],,,0x8,],;,Var,$y,,,$0Q2,:,Array,[,Int,,,0b1,],;,Constructor,(,__,,,Z_,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_949(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k8:X{g0(E_RK,v__D:Float ){}_(X:Array [Array [String ,0x3E],2];___,__,O11,V:Array [Int ,50];__V,l:Array [Array [Array [Array [Array [Array [Boolean ,0x9],01],0b1_0],0b10_1],0X24],0B100000]){} }''',
                '''Class,k8,:,X,{,g0,(,E_RK,,,v__D,:,Float,),{,},_,(,X,:,Array,[,Array,[,String,,,0x3E,],,,2,],;,___,,,__,,,O11,,,V,:,Array,[,Int,,,50,],;,__V,,,l,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x9,],,,01,],,,0b10,],,,0b101,],,,0X24,],,,0B100000,],),{,},},<EOF>''',
                101
            )
        )

    def test_950(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _c__{Val _r8m_b,_:Array [Boolean ,06546_6752];Var $__,$8_1r,$_IU,EP:Array [Float ,0X3C];$T_(){Return ;Break ;} }Class _5:_H7_{}''',
                '''Class,_c__,{,Val,_r8m_b,,,_,:,Array,[,Boolean,,,065466752,],;,Var,$__,,,$8_1r,,,$_IU,,,EP,:,Array,[,Float,,,0X3C,],;,$T_,(,),{,Return,;,Break,;,},},Class,_5,:,_H7_,{,},<EOF>''',
                101
            )
        )

    def test_951(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{$7(_,O3_,_:_;Q:Array [String ,0x32];c7P4_w,O_:Array [Array [Array [Array [Float ,55],016],0X59],05_11]){}Val _,__R_:Array [Float ,0B1001101];}''',
                '''Class,_,{,$7,(,_,,,O3_,,,_,:,_,;,Q,:,Array,[,String,,,0x32,],;,c7P4_w,,,O_,:,Array,[,Array,[,Array,[,Array,[,Float,,,55,],,,016,],,,0X59,],,,0511,],),{,},Val,_,,,__R_,:,Array,[,Float,,,0B1001101,],;,},<EOF>''',
                101
            )
        )

    def test_952(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_a{Destructor (){}_(cUr:Int ;__,_:H){}Constructor (_75:String ;__cw_T,_2GL:O5__w4;e:String ;_jg:_q){} }''',
                '''Class,_,:,_a,{,Destructor,(,),{,},_,(,cUr,:,Int,;,__,,,_,:,H,),{,},Constructor,(,_75,:,String,;,__cw_T,,,_2GL,:,O5__w4,;,e,:,String,;,_jg,:,_q,),{,},},<EOF>''',
                101
            )
        )

    def test_953(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n{Constructor (Ws,_:Array [Array [String ,36],07_70];_892H53l,_,s_7:Array [Array [Array [Array [Array [String ,0xC2_8],6],015],0B1],48];a,_,_:Boolean ;_:_3;_:A___I_){}Val R:Float ;}''',
                '''Class,n,{,Constructor,(,Ws,,,_,:,Array,[,Array,[,String,,,36,],,,0770,],;,_892H53l,,,_,,,s_7,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0xC28,],,,6,],,,015,],,,0B1,],,,48,],;,a,,,_,,,_,:,Boolean,;,_,:,_3,;,_,:,A___I_,),{,},Val,R,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_954(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Vx6:_{$_j(u5:_){}$g(_07:_v0X7;g,D:Array [Boolean ,03]){Break ;}Destructor (){Val I,yv_,v:Array [Array [Array [Array [Boolean ,4],4],0143],0x8];} }Class h_:z{$1V(_:Array [Int ,0b1_0_0];_:Boolean ){} }''',
                '''Class,Vx6,:,_,{,$_j,(,u5,:,_,),{,},$g,(,_07,:,_v0X7,;,g,,,D,:,Array,[,Boolean,,,03,],),{,Break,;,},Destructor,(,),{,Val,I,,,yv_,,,v,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,4,],,,4,],,,0143,],,,0x8,],;,},},Class,h_,:,z,{,$1V,(,_,:,Array,[,Int,,,0b100,],;,_,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_955(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ks_7_{Var $n:U72_m;Destructor (){}Val $y,WP3,$76,$k1,H9:Array [Array [Array [Array [Array [Float ,0X2],060_7],0X9_0],064],1];BJ(__:Array [Array [Array [String ,0b1000100],0X5_C],064]){}$0V_(_X,Y:LD;X,_:Array [Array [Int ,0X7],4]){} }Class _:__{}''',
                '''Class,ks_7_,{,Var,$n,:,U72_m,;,Destructor,(,),{,},Val,$y,,,WP3,,,$76,,,$k1,,,H9,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X2,],,,0607,],,,0X90,],,,064,],,,1,],;,BJ,(,__,:,Array,[,Array,[,Array,[,String,,,0b1000100,],,,0X5C,],,,064,],),{,},$0V_,(,_X,,,Y,:,LD,;,X,,,_,:,Array,[,Array,[,Int,,,0X7,],,,4,],),{,},},Class,_,:,__,{,},<EOF>''',
                101
            )
        )

    def test_956(self):
        self.assertTrue(
            TestLexer.test(
                '''Class L{Val n:D;}Class _2:_{}Class D{Var $d,$h_8:Array [Array [Float ,22],0X55];Val $1_,_,$Oy,$_:I;Var _:_;$7(_:Array [Array [Array [Array [Int ,0117],05],0b1000111],0b1000111];_:_){}Constructor (){} }''',
                '''Class,L,{,Val,n,:,D,;,},Class,_2,:,_,{,},Class,D,{,Var,$d,,,$h_8,:,Array,[,Array,[,Float,,,22,],,,0X55,],;,Val,$1_,,,_,,,$Oy,,,$_,:,I,;,Var,_,:,_,;,$7,(,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0117,],,,05,],,,0b1000111,],,,0b1000111,],;,_,:,_,),{,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_957(self):
        self.assertTrue(
            TestLexer.test(
                '''Class KL:_H{Constructor (){} }Class _6T:Tr_f_{}Class k{Constructor (){}Constructor (_:Array [Array [Array [Array [Array [Array [Boolean ,025],55],0B11010],0X35],0B1],0X35];g_L,_F,N:D9){Break ;} }''',
                '''Class,KL,:,_H,{,Constructor,(,),{,},},Class,_6T,:,Tr_f_,{,},Class,k,{,Constructor,(,),{,},Constructor,(,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,025,],,,55,],,,0B11010,],,,0X35,],,,0B1,],,,0X35,],;,g_L,,,_F,,,N,:,D9,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_958(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class _{Var k:Array [Array [Array [Array [Int ,83],0XC],0117],0X9_C];Constructor (_:Int ){Var _d5G,d:Array [Int ,0117];} }''',
                '''Class,_,:,_,{,},Class,_,{,Var,k,:,Array,[,Array,[,Array,[,Array,[,Int,,,83,],,,0XC,],,,0117,],,,0X9C,],;,Constructor,(,_,:,Int,),{,Var,_d5G,,,d,:,Array,[,Int,,,0117,],;,},},<EOF>''',
                101
            )
        )

    def test_959(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _1_4_:l1{}Class _:Tg{Val N_,_l:W;_B(){} }Class D_{wg__5t(_:Array [Array [Array [Int ,6_9_16],0b100010],88];__:String ){}Var _,_,u0,_,$Zz83,$0,$v6:t;Destructor (){} }Class pV:a{}Class R{}''',
                '''Class,_1_4_,:,l1,{,},Class,_,:,Tg,{,Val,N_,,,_l,:,W,;,_B,(,),{,},},Class,D_,{,wg__5t,(,_,:,Array,[,Array,[,Array,[,Int,,,6916,],,,0b100010,],,,88,],;,__,:,String,),{,},Var,_,,,_,,,u0,,,_,,,$Zz83,,,$0,,,$v6,:,t,;,Destructor,(,),{,},},Class,pV,:,a,{,},Class,R,{,},<EOF>''',
                101
            )
        )

    def test_960(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{AVS1_I(_,_Tr:l;_:Boolean ;_v:Boolean ;Z_8:u;C5__1,DF0H,g:Array [Array [Array [Boolean ,0xD],014],0b1];d,RY,xr,O:String ;F,_:Array [Float ,0525]){Break ;}Var $0,_8__4D:Array [Array [Array [Array [Array [Array [String ,25],01],0b111],3],0B1_0],1];}''',
                '''Class,_,{,AVS1_I,(,_,,,_Tr,:,l,;,_,:,Boolean,;,_v,:,Boolean,;,Z_8,:,u,;,C5__1,,,DF0H,,,g,:,Array,[,Array,[,Array,[,Boolean,,,0xD,],,,014,],,,0b1,],;,d,,,RY,,,xr,,,O,:,String,;,F,,,_,:,Array,[,Float,,,0525,],),{,Break,;,},Var,$0,,,_8__4D,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,25,],,,01,],,,0b111,],,,3,],,,0B10,],,,1,],;,},<EOF>''',
                101
            )
        )

    def test_961(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _N{}Class _J{Destructor (){Var Pa:Array [Array [Boolean ,063],0XD40];}Constructor (Z0,w,U0:String ){}Constructor (_,a,i,_R,_4_,S,_yE,v0,___,_:Array [Int ,063]){Break ;}Destructor (){} }''',
                '''Class,_N,{,},Class,_J,{,Destructor,(,),{,Var,Pa,:,Array,[,Array,[,Boolean,,,063,],,,0XD40,],;,},Constructor,(,Z0,,,w,,,U0,:,String,),{,},Constructor,(,_,,,a,,,i,,,_R,,,_4_,,,S,,,_yE,,,v0,,,___,,,_,:,Array,[,Int,,,063,],),{,Break,;,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_962(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:N4{Var dk,$_8Fh:Array [Array [Array [Array [Array [Array [Array [Boolean ,06],0x4_C3],0x48],0b1],4],0B1011011],0B1_1];}Class o:w_C_{Var $_,$18:Int ;}''',
                '''Class,_,:,N4,{,Var,dk,,,$_8Fh,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,06,],,,0x4C3,],,,0x48,],,,0b1,],,,4,],,,0B1011011,],,,0B11,],;,},Class,o,:,w_C_,{,Var,$_,,,$18,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_963(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _:_{}Class M38{}Class zu:_{$x(_,n_2:___2_;_,P6_:Array [Array [Int ,0B1_0],93];_:_;_,_oSdM,c,__6:Boolean ;_:e2;N:Array [Array [Boolean ,0x47],067];_fA,_,_8:Array [String ,19]){F7_v8__5::$QF.vp._();} }''',
                '''Class,_,{,},Class,_,:,_,{,},Class,M38,{,},Class,zu,:,_,{,$x,(,_,,,n_2,:,___2_,;,_,,,P6_,:,Array,[,Array,[,Int,,,0B10,],,,93,],;,_,:,_,;,_,,,_oSdM,,,c,,,__6,:,Boolean,;,_,:,e2,;,N,:,Array,[,Array,[,Boolean,,,0x47,],,,067,],;,_fA,,,_,,,_8,:,Array,[,String,,,19,],),{,F7_v8__5,::,$QF,.,vp,.,_,(,),;,},},<EOF>''',
                101
            )
        )

    def test_964(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _H:_{$_y_(r_,rs:Int ;b,__,WSFc,_:Array [Array [Array [Int ,042],042],06]){}$__Z(_:Array [Array [Array [Float ,01],0b1100],03]){Return ;_::$_();} }''',
                '''Class,_H,:,_,{,$_y_,(,r_,,,rs,:,Int,;,b,,,__,,,WSFc,,,_,:,Array,[,Array,[,Array,[,Int,,,042,],,,042,],,,06,],),{,},$__Z,(,_,:,Array,[,Array,[,Array,[,Float,,,01,],,,0b1100,],,,03,],),{,Return,;,_,::,$_,(,),;,},},<EOF>''',
                101
            )
        )

    def test_965(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T_5___{Var $05,$_4,$v:Array [Float ,0604];Val y__:_8;}Class nIVk7{$Y_3___M7_(UV,w:__;_s,_:Boolean ){} }''',
                '''Class,T_5___,{,Var,$05,,,$_4,,,$v,:,Array,[,Float,,,0604,],;,Val,y__,:,_8,;,},Class,nIVk7,{,$Y_3___M7_,(,UV,,,w,:,__,;,_s,,,_,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_966(self):
        self.assertTrue(
            TestLexer.test(
                '''Class a_26{Var x:Array [Int ,074];Val $ak:Array [Array [Array [Array [Array [Array [Boolean ,0b1],0x45],56],0x45],0x45],0B1];Val o,_,_,__,ck,s:L;}Class _w98P{}''',
                '''Class,a_26,{,Var,x,:,Array,[,Int,,,074,],;,Val,$ak,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1,],,,0x45,],,,56,],,,0x45,],,,0x45,],,,0B1,],;,Val,o,,,_,,,_,,,__,,,ck,,,s,:,L,;,},Class,_w98P,{,},<EOF>''',
                101
            )
        )

    def test_967(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X0:k{Constructor (){}$G8(C,_MV_:Array [Array [Array [Array [Array [Float ,0x3],053_7],71],0x4B],0xB_6_0_4]){Return ;} }Class k:_z{Constructor (__:__4_;_g:_;p,_,__,Be,r:String ){Continue ;}Var I:Array [Boolean ,5];}''',
                '''Class,X0,:,k,{,Constructor,(,),{,},$G8,(,C,,,_MV_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x3,],,,0537,],,,71,],,,0x4B,],,,0xB604,],),{,Return,;,},},Class,k,:,_z,{,Constructor,(,__,:,__4_,;,_g,:,_,;,p,,,_,,,__,,,Be,,,r,:,String,),{,Continue,;,},Var,I,:,Array,[,Boolean,,,5,],;,},<EOF>''',
                101
            )
        )

    def test_968(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9:_{Destructor (){} }Class _{Val $I,_O0q,_6_:P;Destructor (){}Var $3_,$P__:j5;$2(__,uh,ib,_T:String ){} }''',
                '''Class,_9,:,_,{,Destructor,(,),{,},},Class,_,{,Val,$I,,,_O0q,,,_6_,:,P,;,Destructor,(,),{,},Var,$3_,,,$P__,:,j5,;,$2,(,__,,,uh,,,ib,,,_T,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_969(self):
        self.assertTrue(
            TestLexer.test(
                '''Class R_6:_{$____x(r,q1,y6,_Ba:String ;Qq:Array [Float ,0b10000];t,k_:Array [Array [Array [Array [Array [Int ,022],0B1000110],022],15],0B1_1];_GQ_v:Float ){Return ;} }''',
                '''Class,R_6,:,_,{,$____x,(,r,,,q1,,,y6,,,_Ba,:,String,;,Qq,:,Array,[,Float,,,0b10000,],;,t,,,k_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,022,],,,0B1000110,],,,022,],,,15,],,,0B11,],;,_GQ_v,:,Float,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_970(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Rw{}Class _{Var $_:String ;}Class Y:jf{Destructor (){Continue ;Val kN_0_,l_35,S:Float ;Break ;{} }}Class n{}Class _d9_2{}''',
                '''Class,Rw,{,},Class,_,{,Var,$_,:,String,;,},Class,Y,:,jf,{,Destructor,(,),{,Continue,;,Val,kN_0_,,,l_35,,,S,:,Float,;,Break,;,{,},},},Class,n,{,},Class,_d9_2,{,},<EOF>''',
                101
            )
        )

    def test_971(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t{Destructor (){}$_(_Fa:Array [Array [Array [Array [String ,0124],0124],96],9_1_3_69]){}Destructor (){}Var $I,T_:Boolean ;}''',
                '''Class,t,{,Destructor,(,),{,},$_,(,_Fa,:,Array,[,Array,[,Array,[,Array,[,String,,,0124,],,,0124,],,,96,],,,91369,],),{,},Destructor,(,),{,},Var,$I,,,T_,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_972(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:m_y{}Class _:___d_{Constructor (V__:Array [Boolean ,0xA6];A:Array [Array [Float ,0XF],0B10111];p:Array [Boolean ,0B11]){} }Class Af{}Class Q_:_8{}''',
                '''Class,_,:,m_y,{,},Class,_,:,___d_,{,Constructor,(,V__,:,Array,[,Boolean,,,0xA6,],;,A,:,Array,[,Array,[,Float,,,0XF,],,,0B10111,],;,p,:,Array,[,Boolean,,,0B11,],),{,},},Class,Af,{,},Class,Q_,:,_8,{,},<EOF>''',
                101
            )
        )

    def test_973(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:d{Constructor (mw_:Ju;_,k_5so,_4,H_4:Float ){Var _:Int ;}Var qt,$JP0:Array [Array [Array [Array [Array [Array [Array [Boolean ,077],0B1_0],0x6],8],8],060],0b1];}Class _sm:_K0i3nq{}''',
                '''Class,_,:,d,{,Constructor,(,mw_,:,Ju,;,_,,,k_5so,,,_4,,,H_4,:,Float,),{,Var,_,:,Int,;,},Var,qt,,,$JP0,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,077,],,,0B10,],,,0x6,],,,8,],,,8,],,,060,],,,0b1,],;,},Class,_sm,:,_K0i3nq,{,},<EOF>''',
                101
            )
        )

    def test_974(self):
        self.assertTrue(
            TestLexer.test(
                '''Class S{}Class G_:D{Destructor (){}$_l5a4xs(_,_w4,_Q:D;_,hN:g_6J;__4_,_2,___,_Q:_8;_,q,_:Array [Array [Array [Array [Array [Array [String ,5],0b11_0],8],7],0104],0x8];M_:Array [Array [Int ,05],8]){} }Class x{}Class __{Var _0,M:Array [Array [Boolean ,04],0b1];Var $3_:_;Val $Q,$yy:Boolean ;Val $M:Array [Array [Array [Array [Array [Boolean ,0B1011010],92],03],8],0b110000];R(){} }Class _{}Class _{}''',
                '''Class,S,{,},Class,G_,:,D,{,Destructor,(,),{,},$_l5a4xs,(,_,,,_w4,,,_Q,:,D,;,_,,,hN,:,g_6J,;,__4_,,,_2,,,___,,,_Q,:,_8,;,_,,,q,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,5,],,,0b110,],,,8,],,,7,],,,0104,],,,0x8,],;,M_,:,Array,[,Array,[,Int,,,05,],,,8,],),{,},},Class,x,{,},Class,__,{,Var,_0,,,M,:,Array,[,Array,[,Boolean,,,04,],,,0b1,],;,Var,$3_,:,_,;,Val,$Q,,,$yy,:,Boolean,;,Val,$M,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1011010,],,,92,],,,03,],,,8,],,,0b110000,],;,R,(,),{,},},Class,_,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_975(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:I{Val $_,v:Int ;Var _,$_:Int ;Val __:Int ;Var a,$_:String ;Destructor (){}Destructor (){Continue ;Continue ;Val _3:Array [String ,6_0_5];} }''',
                '''Class,_,:,I,{,Val,$_,,,v,:,Int,;,Var,_,,,$_,:,Int,;,Val,__,:,Int,;,Var,a,,,$_,:,String,;,Destructor,(,),{,},Destructor,(,),{,Continue,;,Continue,;,Val,_3,:,Array,[,String,,,605,],;,},},<EOF>''',
                101
            )
        )

    def test_976(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class R_:__n4{_(_:Array [String ,042]){}Destructor (){}$zi(){Break ;""._2()._().pBn().__G._();Var tz,__H:String ;} }''',
                '''Class,_,{,},Class,R_,:,__n4,{,_,(,_,:,Array,[,String,,,042,],),{,},Destructor,(,),{,},$zi,(,),{,Break,;,,.,_2,(,),.,_,(,),.,pBn,(,),.,__G,.,_,(,),;,Var,tz,,,__H,:,String,;,},},<EOF>''',
                101
            )
        )

    def test_977(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _S3:_{rm(){} }Class Mf{$1(){Val _:Array [Boolean ,29];Continue ;}Constructor (_,_v4,n8,U:KG){} }Class ZP3_:dV{Constructor (_,_,g2,T1,P2___,Fh6_,Y2:_){} }Class _{}''',
                '''Class,_S3,:,_,{,rm,(,),{,},},Class,Mf,{,$1,(,),{,Val,_,:,Array,[,Boolean,,,29,],;,Continue,;,},Constructor,(,_,,,_v4,,,n8,,,U,:,KG,),{,},},Class,ZP3_,:,dV,{,Constructor,(,_,,,_,,,g2,,,T1,,,P2___,,,Fh6_,,,Y2,:,_,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_978(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Kr4:_1578{_(_T_:__;y:String ;_:Array [Array [Array [Float ,0x4F],05],0B1010110]){}Constructor (){}Constructor (){} }Class _{Destructor (){} }''',
                '''Class,Kr4,:,_1578,{,_,(,_T_,:,__,;,y,:,String,;,_,:,Array,[,Array,[,Array,[,Float,,,0x4F,],,,05,],,,0B1010110,],),{,},Constructor,(,),{,},Constructor,(,),{,},},Class,_,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_979(self):
        self.assertTrue(
            TestLexer.test(
                '''Class u7:_Q{_(){}Destructor (){}Var jO_,$uQ,$g,nX:Array [Array [Int ,04],0B1_1_0];$9(_:Boolean ;_4,r4:Boolean ){Break ;} }''',
                '''Class,u7,:,_Q,{,_,(,),{,},Destructor,(,),{,},Var,jO_,,,$uQ,,,$g,,,nX,:,Array,[,Array,[,Int,,,04,],,,0B110,],;,$9,(,_,:,Boolean,;,_4,,,r4,:,Boolean,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_980(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _U_8{Val _,$_,v,$_,$_63,_s:_;Var $_,_:Array [Array [Array [Int ,30],0b1],076];Var $___:Array [Boolean ,03_6_70];}Class _:_{Val k:__=n::$__;Val $1:Float ;}''',
                '''Class,_U_8,{,Val,_,,,$_,,,v,,,$_,,,$_63,,,_s,:,_,;,Var,$_,,,_,:,Array,[,Array,[,Array,[,Int,,,30,],,,0b1,],,,076,],;,Var,$___,:,Array,[,Boolean,,,03670,],;,},Class,_,:,_,{,Val,k,:,__,=,n,::,$__,;,Val,$1,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_981(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:x{_(e:_;d:Array [Int ,0X20_0];_3_,_I:Array [Array [Int ,0117],42];zy__5D:_0){} }Class _{}Class KEW{}Class ys{}Class p:N{}''',
                '''Class,_,:,x,{,_,(,e,:,_,;,d,:,Array,[,Int,,,0X200,],;,_3_,,,_I,:,Array,[,Array,[,Int,,,0117,],,,42,],;,zy__5D,:,_0,),{,},},Class,_,{,},Class,KEW,{,},Class,ys,{,},Class,p,:,N,{,},<EOF>''',
                101
            )
        )

    def test_982(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _We{Destructor (){}Var $_:Array [Array [Array [Array [Array [Int ,32],034],0X3],0X9],0b11_1];}Class n_:___0{}''',
                '''Class,_We,{,Destructor,(,),{,},Var,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,32,],,,034,],,,0X3,],,,0X9,],,,0b111,],;,},Class,n_,:,___0,{,},<EOF>''',
                101
            )
        )

    def test_983(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{Val _:_;Var _,_:Array [String ,0x36];Destructor (){} }Class _{}Class F:l{}Class __{Var $3_:Array [Int ,0b1011100]=-_;}Class _:_{}''',
                '''Class,__,{,Val,_,:,_,;,Var,_,,,_,:,Array,[,String,,,0x36,],;,Destructor,(,),{,},},Class,_,{,},Class,F,:,l,{,},Class,__,{,Var,$3_,:,Array,[,Int,,,0b1011100,],=,-,_,;,},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_984(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __S0r4{_(I,_:_;__,_:Array [Array [Array [Array [Boolean ,0X640A],0X1E],49],0X1E];_:Boolean ){}Destructor (){} }Class _3{ufk9(){} }Class _5{}Class _{}''',
                '''Class,__S0r4,{,_,(,I,,,_,:,_,;,__,,,_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X640A,],,,0X1E,],,,49,],,,0X1E,],;,_,:,Boolean,),{,},Destructor,(,),{,},},Class,_3,{,ufk9,(,),{,},},Class,_5,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_985(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Constructor (C:Boolean ;C,_act,_:y__;_3XVz:_;_,M,__s,_,Re_,O,_j,R__:Array [Float ,2_36];_Gj_,_,k,wH,U_2_:Array [Array [Array [Array [Float ,0XAC_4_A_5_C],0b11],0X17],0B1010010];_Y,s,_0,_0:Array [Array [Int ,0XB],056];q:_){} }''',
                '''Class,_,:,_,{,Constructor,(,C,:,Boolean,;,C,,,_act,,,_,:,y__,;,_3XVz,:,_,;,_,,,M,,,__s,,,_,,,Re_,,,O,,,_j,,,R__,:,Array,[,Float,,,236,],;,_Gj_,,,_,,,k,,,wH,,,U_2_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0XAC4A5C,],,,0b11,],,,0X17,],,,0B1010010,],;,_Y,,,s,,,_0,,,_0,:,Array,[,Array,[,Int,,,0XB,],,,056,],;,q,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_986(self):
        self.assertTrue(
            TestLexer.test(
                '''Class tV3{Val _,kL,$4:f;Var $E60,n,$506,_3_,_2d__I,$7_:Array [Array [Array [Array [Array [Array [Boolean ,82],0115],05],06],01_0],0b110101];}''',
                '''Class,tV3,{,Val,_,,,kL,,,$4,:,f,;,Var,$E60,,,n,,,$506,,,_3_,,,_2d__I,,,$7_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,82,],,,0115,],,,05,],,,06,],,,010,],,,0b110101,],;,},<EOF>''',
                101
            )
        )

    def test_987(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (){}$t_(w,_:Int ;Q2_:Int ;_,_,x:Array [Int ,89]){_A::$SJx4();}Var $_,_6,$_:Array [Array [Array [String ,074_5],0B1_0],2_9];}Class Z__0_:_{Constructor (ep_6h978,_5_l_:_e_mG){Return ;Continue ;}Constructor (Z_:Array [Array [Int ,89],2];__:__;T:String ){}Val $0,$O3,T:_M;}''',
                '''Class,_,{,Constructor,(,),{,},$t_,(,w,,,_,:,Int,;,Q2_,:,Int,;,_,,,_,,,x,:,Array,[,Int,,,89,],),{,_A,::,$SJx4,(,),;,},Var,$_,,,_6,,,$_,:,Array,[,Array,[,Array,[,String,,,0745,],,,0B10,],,,29,],;,},Class,Z__0_,:,_,{,Constructor,(,ep_6h978,,,_5_l_,:,_e_mG,),{,Return,;,Continue,;,},Constructor,(,Z_,:,Array,[,Array,[,Int,,,89,],,,2,],;,__,:,__,;,T,:,String,),{,},Val,$0,,,$O3,,,T,:,_M,;,},<EOF>''',
                101
            )
        )

    def test_988(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $2:Fv;}Class _:K{}Class _:__{Constructor (){Var eU5,__:Int ;} }Class _vE{Destructor (){ {}Break ;} }Class _{}''',
                '''Class,_,{,Val,$2,:,Fv,;,},Class,_,:,K,{,},Class,_,:,__,{,Constructor,(,),{,Var,eU5,,,__,:,Int,;,},},Class,_vE,{,Destructor,(,),{,{,},Break,;,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_989(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J_3{}Class _:RyU{Constructor (_8,M1_O,z,_d8v_,P3,A67m:Array [Array [Boolean ,0b11101],0b11101];_,_,A,_15:u){}Val e_xk:i;Val $_:_6_;Destructor (){} }''',
                '''Class,J_3,{,},Class,_,:,RyU,{,Constructor,(,_8,,,M1_O,,,z,,,_d8v_,,,P3,,,A67m,:,Array,[,Array,[,Boolean,,,0b11101,],,,0b11101,],;,_,,,_,,,A,,,_15,:,u,),{,},Val,e_xk,:,i,;,Val,$_,:,_6_,;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_990(self):
        self.assertTrue(
            TestLexer.test(
                '''Class M{Constructor (_99xd:j9_;_,_S3,_a_2,___9Gt:Array [Array [Array [Array [Float ,0X43],0XE_5D],0B1],0x58]){}Destructor (){}Val _:Array [Int ,41];Var t,_:Array [Int ,0XE_0_F_EC];Destructor (){} }Class _{}''',
                '''Class,M,{,Constructor,(,_99xd,:,j9_,;,_,,,_S3,,,_a_2,,,___9Gt,:,Array,[,Array,[,Array,[,Array,[,Float,,,0X43,],,,0XE5D,],,,0B1,],,,0x58,],),{,},Destructor,(,),{,},Val,_,:,Array,[,Int,,,41,],;,Var,t,,,_,:,Array,[,Int,,,0XE0FEC,],;,Destructor,(,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_991(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Q_{Constructor (){}Constructor (py,_,_:Int ;__,J_t:Array [Array [Boolean ,04_0_33],0XA56_2_6_0];_,_d:Array [Int ,01]){}Constructor (){}Var $B:Array [Float ,0X1D];}Class _{}Class b_b:Uk1{}''',
                '''Class,Q_,{,Constructor,(,),{,},Constructor,(,py,,,_,,,_,:,Int,;,__,,,J_t,:,Array,[,Array,[,Boolean,,,04033,],,,0XA56260,],;,_,,,_d,:,Array,[,Int,,,01,],),{,},Constructor,(,),{,},Var,$B,:,Array,[,Float,,,0X1D,],;,},Class,_,{,},Class,b_b,:,Uk1,{,},<EOF>''',
                101
            )
        )

    def test_992(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n{Constructor (_,___,_,v,_,v0_,s9l:Array [String ,055];_,p:Array [Float ,39];v,_,zW9:Array [Int ,0X8];q,_D,A1,Y,g2:f;Q,AY,q__,l,_:yK){}Var $U,_:Array [Boolean ,8236];}''',
                '''Class,n,{,Constructor,(,_,,,___,,,_,,,v,,,_,,,v0_,,,s9l,:,Array,[,String,,,055,],;,_,,,p,:,Array,[,Float,,,39,],;,v,,,_,,,zW9,:,Array,[,Int,,,0X8,],;,q,,,_D,,,A1,,,Y,,,g2,:,f,;,Q,,,AY,,,q__,,,l,,,_,:,yK,),{,},Var,$U,,,_,:,Array,[,Boolean,,,8236,],;,},<EOF>''',
                101
            )
        )

    def test_993(self):
        self.assertTrue(
            TestLexer.test(
                '''Class N5q{}Class _{Constructor (m2,_i,o_e,_,di,U_,_:String ;k_p,_:nNo6_0n_;__,_,__:Float ;C,_,u:Array [Array [Boolean ,0X1],0B1];_:Array [Array [Int ,0136],01_36]){}Val $_U:_Z;Constructor (s2,y6,__:_;_N:JC_m){} }Class M{}''',
                '''Class,N5q,{,},Class,_,{,Constructor,(,m2,,,_i,,,o_e,,,_,,,di,,,U_,,,_,:,String,;,k_p,,,_,:,nNo6_0n_,;,__,,,_,,,__,:,Float,;,C,,,_,,,u,:,Array,[,Array,[,Boolean,,,0X1,],,,0B1,],;,_,:,Array,[,Array,[,Int,,,0136,],,,0136,],),{,},Val,$_U,:,_Z,;,Constructor,(,s2,,,y6,,,__,:,_,;,_N,:,JC_m,),{,},},Class,M,{,},<EOF>''',
                101
            )
        )

    def test_994(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _m:_3_{}Class C:_6{Constructor (){Return ;Break ;}Var P1,_,_I:Int ;Var $9_,_,AoG:Array [String ,0b1_0];}Class W_f{Var $_2:Float ;}Class _{Constructor (z,_0:Array [Array [Array [Array [Array [Array [Array [Float ,06],84],19_9631_2],0B1],034_7],0B1001000],0131]){} }''',
                '''Class,_m,:,_3_,{,},Class,C,:,_6,{,Constructor,(,),{,Return,;,Break,;,},Var,P1,,,_,,,_I,:,Int,;,Var,$9_,,,_,,,AoG,:,Array,[,String,,,0b10,],;,},Class,W_f,{,Var,$_2,:,Float,;,},Class,_,{,Constructor,(,z,,,_0,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,06,],,,84,],,,1996312,],,,0B1,],,,0347,],,,0B1001000,],,,0131,],),{,},},<EOF>''',
                101
            )
        )

    def test_995(self):
        self.assertTrue(
            TestLexer.test(
                '''Class s{}Class __:S{f___(fc,Ut:Float ;X,v7f:_;qX,__,F,t_3,_Y:Boolean ;_,_m,__:Array [String ,0B100111]){}Constructor (){}n(){}Val _,$7Ah_,$N:Boolean ;}''',
                '''Class,s,{,},Class,__,:,S,{,f___,(,fc,,,Ut,:,Float,;,X,,,v7f,:,_,;,qX,,,__,,,F,,,t_3,,,_Y,:,Boolean,;,_,,,_m,,,__,:,Array,[,String,,,0B100111,],),{,},Constructor,(,),{,},n,(,),{,},Val,_,,,$7Ah_,,,$N,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_996(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T{}Class jB:F{Val _,$5,$7:Array [Array [Int ,07],20_0];}Class _{_(_yj_,_h,I:H;_s___:Array [Float ,0B111100]){} }Class _:v661{}''',
                '''Class,T,{,},Class,jB,:,F,{,Val,_,,,$5,,,$7,:,Array,[,Array,[,Int,,,07,],,,200,],;,},Class,_,{,_,(,_yj_,,,_h,,,I,:,H,;,_s___,:,Array,[,Float,,,0B111100,],),{,},},Class,_,:,v661,{,},<EOF>''',
                101
            )
        )

    def test_997(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:__{$_D9_(){Continue ;} }Class _H:_{}Class _{Val _,$_7:Float ;}Class __W_{}Class _q:T__{Destructor (){} }Class j_{}''',
                '''Class,_,:,__,{,$_D9_,(,),{,Continue,;,},},Class,_H,:,_,{,},Class,_,{,Val,_,,,$_7,:,Float,;,},Class,__W_,{,},Class,_q,:,T__,{,Destructor,(,),{,},},Class,j_,{,},<EOF>''',
                101
            )
        )

    def test_998(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _3_6{}Class _:_{Var v:Array [Array [Array [Array [Array [Boolean ,0140],0XD],0B1],0B1000001],0B1];Val $N:String ;}Class l:E{Val NY,$_,$M_W37:Array [Array [Boolean ,3],0140];Constructor (_3:U;Q,D,R8___,_:Array [Array [Array [Array [Array [Float ,01_1_2],3],0140],0XEE_6],06];J:Int ;_:_9){}$8__8(_:Array [Array [Int ,0227],0X46]){} }Class ___:y_{}''',
                '''Class,_3_6,{,},Class,_,:,_,{,Var,v,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0140,],,,0XD,],,,0B1,],,,0B1000001,],,,0B1,],;,Val,$N,:,String,;,},Class,l,:,E,{,Val,NY,,,$_,,,$M_W37,:,Array,[,Array,[,Boolean,,,3,],,,0140,],;,Constructor,(,_3,:,U,;,Q,,,D,,,R8___,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0112,],,,3,],,,0140,],,,0XEE6,],,,06,],;,J,:,Int,;,_,:,_9,),{,},$8__8,(,_,:,Array,[,Array,[,Int,,,0227,],,,0X46,],),{,},},Class,___,:,y_,{,},<EOF>''',
                101
            )
        )

    def test_999(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _h93_{Val $2,$q__:Array [Array [Array [Array [Array [Float ,045],436],6],0XF],0B10_11];Destructor (){} }Class OD{}Class __:_{}Class _{Var _,$e,$xM1:r_;}Class _{}''',
                '''Class,_h93_,{,Val,$2,,,$q__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,045,],,,436,],,,6,],,,0XF,],,,0B1011,],;,Destructor,(,),{,},},Class,OD,{,},Class,__,:,_,{,},Class,_,{,Var,_,,,$e,,,$xM1,:,r_,;,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_1000(self):
        self.assertTrue(
            TestLexer.test(
                '''Class B3{Var _,$3:Boolean ;Val $88:m_;Var Nd1:String ;}Class i{$__(){} }Class S{Constructor (){}Val F_,A3:Array [String ,68];}''',
                '''Class,B3,{,Var,_,,,$3,:,Boolean,;,Val,$88,:,m_,;,Var,Nd1,:,String,;,},Class,i,{,$__,(,),{,},},Class,S,{,Constructor,(,),{,},Val,F_,,,A3,:,Array,[,String,,,68,],;,},<EOF>''',
                101
            )
        )

    def test_1001(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class _7:j{Destructor (){}$e(){} }Class i_57__23{}Class _f7:b{}Class y{Constructor (){}$0(_Q:Array [Boolean ,063];m1,_,_:String ){} }''',
                '''Class,_,:,_,{,},Class,_7,:,j,{,Destructor,(,),{,},$e,(,),{,},},Class,i_57__23,{,},Class,_f7,:,b,{,},Class,y,{,Constructor,(,),{,},$0,(,_Q,:,Array,[,Boolean,,,063,],;,m1,,,_,,,_,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_1002(self):
        self.assertTrue(
            TestLexer.test(
                '''Class U:_r4{Var $_:Int ;Constructor (){} }Class _:f{$__(t_:Array [Boolean ,0B1];_,r,E,x:Float ;m_:String ){}Var j:Array [Float ,2];}Class _:n9_{Var $f:Int ;}Class s3q{}''',
                '''Class,U,:,_r4,{,Var,$_,:,Int,;,Constructor,(,),{,},},Class,_,:,f,{,$__,(,t_,:,Array,[,Boolean,,,0B1,],;,_,,,r,,,E,,,x,:,Float,;,m_,:,String,),{,},Var,j,:,Array,[,Float,,,2,],;,},Class,_,:,n9_,{,Var,$f,:,Int,;,},Class,s3q,{,},<EOF>''',
                101
            )
        )

    def test_1003(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __Ao_9:f{Val $4_8:Array [Array [Boolean ,14],0x4];Destructor (){Break ;}Constructor (_,_:Array [Int ,054]){Break ;} }''',
                '''Class,__Ao_9,:,f,{,Val,$4_8,:,Array,[,Array,[,Boolean,,,14,],,,0x4,],;,Destructor,(,),{,Break,;,},Constructor,(,_,,,_,:,Array,[,Int,,,054,],),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_1004(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:oK6LF14{Var $7F:Array [Array [Array [Float ,047],02_22],05];}Class J{Val u,$d_:Float ;Constructor (){} }Class J{Constructor (){} }''',
                '''Class,_,:,oK6LF14,{,Var,$7F,:,Array,[,Array,[,Array,[,Float,,,047,],,,0222,],,,05,],;,},Class,J,{,Val,u,,,$d_,:,Float,;,Constructor,(,),{,},},Class,J,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1005(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __0{o(_,_p9,_,u_:Array [Array [Array [Boolean ,42],0b1_1],0X55];jq5_,Y2:Array [Int ,012];_:v){}Val $9_P:Array [Array [Array [Array [Array [String ,3],022],42],42],0B10100];}''',
                '''Class,__0,{,o,(,_,,,_p9,,,_,,,u_,:,Array,[,Array,[,Array,[,Boolean,,,42,],,,0b11,],,,0X55,],;,jq5_,,,Y2,:,Array,[,Int,,,012,],;,_,:,v,),{,},Val,$9_P,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,3,],,,022,],,,42,],,,42,],,,0B10100,],;,},<EOF>''',
                101
            )
        )

    def test_1006(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __0:_{Constructor (f_g,__p,C:m;mo:Int ;___:_){}$o_(){}Var B,b,$G_,$__P,_,$m9,$C8:Boolean ;}Class _{$2(_fr_,_4_:__){} }''',
                '''Class,__0,:,_,{,Constructor,(,f_g,,,__p,,,C,:,m,;,mo,:,Int,;,___,:,_,),{,},$o_,(,),{,},Var,B,,,b,,,$G_,,,$__P,,,_,,,$m9,,,$C8,:,Boolean,;,},Class,_,{,$2,(,_fr_,,,_4_,:,__,),{,},},<EOF>''',
                101
            )
        )

    def test_1007(self):
        self.assertTrue(
            TestLexer.test(
                '''Class v:j6_{$_(r_,_,u,_9:Array [Array [Array [Float ,5],0B1000111],0b1010111];d,i,__r:Array [Array [String ,0b1_10],47];y3,u,p7:Float ;_:Boolean ;_:_9;A9_,___,_:Array [Array [Int ,0B1_0_0_1_1_1_01_11],0b1]){} }''',
                '''Class,v,:,j6_,{,$_,(,r_,,,_,,,u,,,_9,:,Array,[,Array,[,Array,[,Float,,,5,],,,0B1000111,],,,0b1010111,],;,d,,,i,,,__r,:,Array,[,Array,[,String,,,0b110,],,,47,],;,y3,,,u,,,p7,:,Float,;,_,:,Boolean,;,_,:,_9,;,A9_,,,___,,,_,:,Array,[,Array,[,Int,,,0B1001110111,],,,0b1,],),{,},},<EOF>''',
                101
            )
        )

    def test_1008(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X0:W{x(I0874,_:Array [Array [Int ,055],2]){}$V(){}Destructor (){} }Class X03:_{Constructor (_6_,q,_0,_,A_Y,_:_){} }''',
                '''Class,X0,:,W,{,x,(,I0874,,,_,:,Array,[,Array,[,Int,,,055,],,,2,],),{,},$V,(,),{,},Destructor,(,),{,},},Class,X03,:,_,{,Constructor,(,_6_,,,q,,,_0,,,_,,,A_Y,,,_,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_1009(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J{Val $ZI_D,$V1,_2O_3_,$1_3:Array [Array [Int ,3],85];Var _:N;}Class D:p{}Class ja__9li:zFJ{Constructor (){} }''',
                '''Class,J,{,Val,$ZI_D,,,$V1,,,_2O_3_,,,$1_3,:,Array,[,Array,[,Int,,,3,],,,85,],;,Var,_,:,N,;,},Class,D,:,p,{,},Class,ja__9li,:,zFJ,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1010(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _N{Constructor (_,t:Array [Array [Float ,0115],7];n,_:Array [Int ,0115];j,_0_,_wN,D18,_,_,S:Array [String ,0xC_6]){}Val $f:Float ;}''',
                '''Class,_N,{,Constructor,(,_,,,t,:,Array,[,Array,[,Float,,,0115,],,,7,],;,n,,,_,:,Array,[,Int,,,0115,],;,j,,,_0_,,,_wN,,,D18,,,_,,,_,,,S,:,Array,[,String,,,0xC6,],),{,},Val,$f,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_1011(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:X{Destructor (){}Var $_:Array [Array [Array [Array [Array [Array [Boolean ,0b10],98],0xD],0X55],0b1000011],05];}''',
                '''Class,_,:,X,{,Destructor,(,),{,},Var,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b10,],,,98,],,,0xD,],,,0X55,],,,0b1000011,],,,05,],;,},<EOF>''',
                101
            )
        )

    def test_1012(self):
        self.assertTrue(
            TestLexer.test(
                '''Class K{}Class _{}Class C{Var $_j,$___,_4m,_,$N_2qS7_,$d8oX_:Array [Array [Int ,0B11_0],06_1];}Class y:__4_{Val $u,$5:Array [Array [String ,68],0B1100];}Class B_4{}''',
                '''Class,K,{,},Class,_,{,},Class,C,{,Var,$_j,,,$___,,,_4m,,,_,,,$N_2qS7_,,,$d8oX_,:,Array,[,Array,[,Int,,,0B110,],,,061,],;,},Class,y,:,__4_,{,Val,$u,,,$5,:,Array,[,Array,[,String,,,68,],,,0B1100,],;,},Class,B_4,{,},<EOF>''',
                101
            )
        )

    def test_1013(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _4:Z0__{$_(j:Boolean ;Jz:Float ;_,__,g,_N_t_4:w_;_6:Array [Array [Array [String ,50],05_3],0b1];t,O:Array [Boolean ,070]){} }Class R{}''',
                '''Class,_4,:,Z0__,{,$_,(,j,:,Boolean,;,Jz,:,Float,;,_,,,__,,,g,,,_N_t_4,:,w_,;,_6,:,Array,[,Array,[,Array,[,String,,,50,],,,053,],,,0b1,],;,t,,,O,:,Array,[,Boolean,,,070,],),{,},},Class,R,{,},<EOF>''',
                101
            )
        )

    def test_1014(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t_L4{d(R,_:Array [Array [Boolean ,100],02];z:Float ;_9_,D___v0,_,W,_,C:_){Continue ;}Val Y:Array [Float ,0125];}''',
                '''Class,t_L4,{,d,(,R,,,_,:,Array,[,Array,[,Boolean,,,100,],,,02,],;,z,:,Float,;,_9_,,,D___v0,,,_,,,W,,,_,,,C,:,_,),{,Continue,;,},Val,Y,:,Array,[,Float,,,0125,],;,},<EOF>''',
                101
            )
        )

    def test_1015(self):
        self.assertTrue(
            TestLexer.test(
                '''Class O:c{Val _:Int ;Constructor (V_6:Array [Float ,10];_:Int ;c_,X:_;b_:Array [Array [Float ,0b1101],0XF_7_0_E_873_5];L6:wc__;_,_HG,__5,l:_P0;z:Array [String ,0x9_7E_7]){} }''',
                '''Class,O,:,c,{,Val,_,:,Int,;,Constructor,(,V_6,:,Array,[,Float,,,10,],;,_,:,Int,;,c_,,,X,:,_,;,b_,:,Array,[,Array,[,Float,,,0b1101,],,,0XF70E8735,],;,L6,:,wc__,;,_,,,_HG,,,__5,,,l,:,_P0,;,z,:,Array,[,String,,,0x97E7,],),{,},},<EOF>''',
                101
            )
        )

    def test_1016(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:g{Constructor (es:p;_T__,_43KO,k,b,B,_7D:Array [Array [String ,0b1100011],0B1];y:Float ;_,_7_3,_Y_:_;Z,R:f_){} }''',
                '''Class,_,:,g,{,Constructor,(,es,:,p,;,_T__,,,_43KO,,,k,,,b,,,B,,,_7D,:,Array,[,Array,[,String,,,0b1100011,],,,0B1,],;,y,:,Float,;,_,,,_7_3,,,_Y_,:,_,;,Z,,,R,:,f_,),{,},},<EOF>''',
                101
            )
        )

    def test_1017(self):
        self.assertTrue(
            TestLexer.test(
                '''Class p:V{Constructor (_,f,N,_,ue11E_0c:_1W){Break ;}$8__3f_(){Continue ;}_(E,U,_4:Boolean ){Continue ;}Val _1,$_:String ;}''',
                '''Class,p,:,V,{,Constructor,(,_,,,f,,,N,,,_,,,ue11E_0c,:,_1W,),{,Break,;,},$8__3f_,(,),{,Continue,;,},_,(,E,,,U,,,_4,:,Boolean,),{,Continue,;,},Val,_1,,,$_,:,String,;,},<EOF>''',
                101
            )
        )

    def test_1018(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _4_IU:_17e{}Class _:u{}Class _:_{_(__,O0_zM,___,RO,kbS_4,__,A_F,_,a:l;RZ_,_,P,X,h,_NE,qSx14c:Int ;en4_,r,_:e;__,x,_,_:q;__1,RP:Array [Array [Float ,0x54],03];Z,D,_,a,GL:Array [String ,0X5C];__fr_,h___E_,_53:Array [Array [Array [Boolean ,0xD_3_4],0X5C],0xE4]){} }''',
                '''Class,_4_IU,:,_17e,{,},Class,_,:,u,{,},Class,_,:,_,{,_,(,__,,,O0_zM,,,___,,,RO,,,kbS_4,,,__,,,A_F,,,_,,,a,:,l,;,RZ_,,,_,,,P,,,X,,,h,,,_NE,,,qSx14c,:,Int,;,en4_,,,r,,,_,:,e,;,__,,,x,,,_,,,_,:,q,;,__1,,,RP,:,Array,[,Array,[,Float,,,0x54,],,,03,],;,Z,,,D,,,_,,,a,,,GL,:,Array,[,String,,,0X5C,],;,__fr_,,,h___E_,,,_53,:,Array,[,Array,[,Array,[,Boolean,,,0xD34,],,,0X5C,],,,0xE4,],),{,},},<EOF>''',
                101
            )
        )

    def test_1019(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:Q{Constructor (_,j3U:__3u;X,_908:_8;f8m,_W,__u:Array [Boolean ,0B1010010];B,C:_){Return ;}Constructor (){} }''',
                '''Class,_,:,Q,{,Constructor,(,_,,,j3U,:,__3u,;,X,,,_908,:,_8,;,f8m,,,_W,,,__u,:,Array,[,Boolean,,,0B1010010,],;,B,,,C,:,_,),{,Return,;,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1020(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_7:__;K,y:f9;__06,tC:String ;_,p,D,_:Array [Float ,54]){Continue ;}Var $8,$Z,_,$7,F:Float ;}''',
                '''Class,_,{,Constructor,(,_7,:,__,;,K,,,y,:,f9,;,__06,,,tC,:,String,;,_,,,p,,,D,,,_,:,Array,[,Float,,,54,],),{,Continue,;,},Var,$8,,,$Z,,,_,,,$7,,,F,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_1021(self):
        self.assertTrue(
            TestLexer.test(
                '''Class D{}Class _{}Class _u{Constructor (D752h_z,_:Array [Array [Array [Float ,0b1],0B10_01],0120]){} }Class A:_{Destructor (){} }Class uR6_{}''',
                '''Class,D,{,},Class,_,{,},Class,_u,{,Constructor,(,D752h_z,,,_,:,Array,[,Array,[,Array,[,Float,,,0b1,],,,0B1001,],,,0120,],),{,},},Class,A,:,_,{,Destructor,(,),{,},},Class,uR6_,{,},<EOF>''',
                101
            )
        )

    def test_1022(self):
        self.assertTrue(
            TestLexer.test(
                '''Class z___{Constructor (){ {}{} }$A(){}Constructor (__e1__1_3__:String ;He:Array [Array [Array [Array [Array [Float ,4],0x54],0b1010100],5],061];__,_E:Int ){} }''',
                '''Class,z___,{,Constructor,(,),{,{,},{,},},$A,(,),{,},Constructor,(,__e1__1_3__,:,String,;,He,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,4,],,,0x54,],,,0b1010100,],,,5,],,,061,],;,__,,,_E,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_1023(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ZG:K_2{}Class _:k_____{Constructor (n,_,d,XR6:Int ){}$wh(_,M:_;_,v_t86i_,i:X;_:Boolean ;Q:k){}Val b_:F;}''',
                '''Class,ZG,:,K_2,{,},Class,_,:,k_____,{,Constructor,(,n,,,_,,,d,,,XR6,:,Int,),{,},$wh,(,_,,,M,:,_,;,_,,,v_t86i_,,,i,:,X,;,_,:,Boolean,;,Q,:,k,),{,},Val,b_,:,F,;,},<EOF>''',
                101
            )
        )

    def test_1024(self):
        self.assertTrue(
            TestLexer.test(
                '''Class vgF_:dl{}Class m:_a{Val $__,$5Z_2O_K,$1:String ;Var d_epY,__,N:Array [Float ,07_2];Constructor (){}Var $_:Float ;Constructor (_,_:String ){}Destructor (){} }''',
                '''Class,vgF_,:,dl,{,},Class,m,:,_a,{,Val,$__,,,$5Z_2O_K,,,$1,:,String,;,Var,d_epY,,,__,,,N,:,Array,[,Float,,,072,],;,Constructor,(,),{,},Var,$_,:,Float,;,Constructor,(,_,,,_,:,String,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1025(self):
        self.assertTrue(
            TestLexer.test(
                '''Class I:_{Var v:Array [Array [Int ,0b1000_01],063];}Class Xz_:bt{Val L0:Float ;}Class G_4_S:__t{Destructor (){} }''',
                '''Class,I,:,_,{,Var,v,:,Array,[,Array,[,Int,,,0b100001,],,,063,],;,},Class,Xz_,:,bt,{,Val,L0,:,Float,;,},Class,G_4_S,:,__t,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1026(self):
        self.assertTrue(
            TestLexer.test(
                '''Class L{}Class _:_q3U{Var _,$_7xu_:Int ;}Class SRk7_:_m{Constructor (__D2,_k,__:Array [Float ,01];_1:String ;_:Int ;_,T_:Float ){} }''',
                '''Class,L,{,},Class,_,:,_q3U,{,Var,_,,,$_7xu_,:,Int,;,},Class,SRk7_,:,_m,{,Constructor,(,__D2,,,_k,,,__,:,Array,[,Float,,,01,],;,_1,:,String,;,_,:,Int,;,_,,,T_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_1027(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _{Val _,$z_7e9:Array [Float ,6_8719];Constructor (_:_a_){}Val _:Array [Float ,51];Destructor (){} }''',
                '''Class,_,{,},Class,_,{,Val,_,,,$z_7e9,:,Array,[,Float,,,68719,],;,Constructor,(,_,:,_a_,),{,},Val,_,:,Array,[,Float,,,51,],;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1028(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n{}Class __{}Class _:_{Val $k,$_F:Array [Array [Boolean ,0b1],063];}Class H{Destructor (){}Constructor (d,_:Boolean ;v5,Q___n,n:Boolean ){} }''',
                '''Class,n,{,},Class,__,{,},Class,_,:,_,{,Val,$k,,,$_F,:,Array,[,Array,[,Boolean,,,0b1,],,,063,],;,},Class,H,{,Destructor,(,),{,},Constructor,(,d,,,_,:,Boolean,;,v5,,,Q___n,,,n,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_1029(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2__35{Var $131,_,$_:Array [String ,7_0];}Class S:_{Val $6,W:Array [Array [Int ,0b1011111],1];}Class _0_:_6tJ{}''',
                '''Class,_2__35,{,Var,$131,,,_,,,$_,:,Array,[,String,,,70,],;,},Class,S,:,_,{,Val,$6,,,W,:,Array,[,Array,[,Int,,,0b1011111,],,,1,],;,},Class,_0_,:,_6tJ,{,},<EOF>''',
                101
            )
        )

    def test_1030(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class _:_{}Class F:F_{Constructor (_,_9,__:_;_L:Array [Array [Int ,074],074];F:Array [Array [String ,0143],0x1B_2_7_D];_,S:String ){} }''',
                '''Class,__,{,},Class,_,:,_,{,},Class,F,:,F_,{,Constructor,(,_,,,_9,,,__,:,_,;,_L,:,Array,[,Array,[,Int,,,074,],,,074,],;,F,:,Array,[,Array,[,String,,,0143,],,,0x1B27D,],;,_,,,S,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_1031(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Tx:__7{Val R___:Boolean ;$P(){}Constructor (W_,_:t_Z6){}Constructor (H_8,Tv6:Array [Float ,0B1000100];b,y_9o,__,_2x:K;_,_:l){} }''',
                '''Class,Tx,:,__7,{,Val,R___,:,Boolean,;,$P,(,),{,},Constructor,(,W_,,,_,:,t_Z6,),{,},Constructor,(,H_8,,,Tv6,:,Array,[,Float,,,0B1000100,],;,b,,,y_9o,,,__,,,_2x,:,K,;,_,,,_,:,l,),{,},},<EOF>''',
                101
            )
        )

    def test_1032(self):
        self.assertTrue(
            TestLexer.test(
                '''Class SX:ZJB{Var $x_,$t_,XS:Array [Array [Int ,0X53],024];}Class __:N{Constructor (_4,_4__:Boolean ){_::$_();Break ;} }''',
                '''Class,SX,:,ZJB,{,Var,$x_,,,$t_,,,XS,:,Array,[,Array,[,Int,,,0X53,],,,024,],;,},Class,__,:,N,{,Constructor,(,_4,,,_4__,:,Boolean,),{,_,::,$_,(,),;,Break,;,},},<EOF>''',
                101
            )
        )

    def test_1033(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _F{}Class z{Val $__:wg;Constructor (){}Var _d_q:Array [Array [Array [Float ,060435],04_6],0710];Val __,V:T_;}Class _:P{Val O,$__,$u,A:Int ;}''',
                '''Class,_F,{,},Class,z,{,Val,$__,:,wg,;,Constructor,(,),{,},Var,_d_q,:,Array,[,Array,[,Array,[,Float,,,060435,],,,046,],,,0710,],;,Val,__,,,V,:,T_,;,},Class,_,:,P,{,Val,O,,,$__,,,$u,,,A,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_1034(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _WdZ:i{}Class g{Val Q_4:Z;Destructor (){v_0::$0();}Var $Q:Array [Boolean ,57];}Class _:_{}Class __:__4Q59Y_M_P{O(){} }''',
                '''Class,_WdZ,:,i,{,},Class,g,{,Val,Q_4,:,Z,;,Destructor,(,),{,v_0,::,$0,(,),;,},Var,$Q,:,Array,[,Boolean,,,57,],;,},Class,_,:,_,{,},Class,__,:,__4Q59Y_M_P,{,O,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1035(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $mzW_:_;Destructor (){} }Class e3g:z_{Constructor (jy:Int ;_,kM,_8:Array [Array [Float ,05],0b101010]){} }''',
                '''Class,_,{,Val,$mzW_,:,_,;,Destructor,(,),{,},},Class,e3g,:,z_,{,Constructor,(,jy,:,Int,;,_,,,kM,,,_8,:,Array,[,Array,[,Float,,,05,],,,0b101010,],),{,},},<EOF>''',
                101
            )
        )

    def test_1036(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _FH:J{}Class b__{Constructor (N,_P:Array [Array [Array [Array [Array [Array [Boolean ,0X2B],0x42],0B11],10],0x42],010]){ {} }}''',
                '''Class,_FH,:,J,{,},Class,b__,{,Constructor,(,N,,,_P,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X2B,],,,0x42,],,,0B11,],,,10,],,,0x42,],,,010,],),{,{,},},},<EOF>''',
                101
            )
        )

    def test_1037(self):
        self.assertTrue(
            TestLexer.test(
                '''Class x:s{Var $_,__,$4,_:Float ;Val k54_:String ;Var _4,$0,_,_,_:Float ;Val $_,$hu_7:O;}Class n_{$0(t,__64:Array [Int ,0xF];Oj_:Float ){} }''',
                '''Class,x,:,s,{,Var,$_,,,__,,,$4,,,_,:,Float,;,Val,k54_,:,String,;,Var,_4,,,$0,,,_,,,_,,,_,:,Float,;,Val,$_,,,$hu_7,:,O,;,},Class,n_,{,$0,(,t,,,__64,:,Array,[,Int,,,0xF,],;,Oj_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_1038(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{Val $_Av_:Array [Array [String ,99],0B111000];$T(_5,Wp,O:_2){} }Class D_:n{}Class g_:i_17{Var _f8W:Array [Array [Array [Float ,0130],0xAD9],05];}''',
                '''Class,__,{,Val,$_Av_,:,Array,[,Array,[,String,,,99,],,,0B111000,],;,$T,(,_5,,,Wp,,,O,:,_2,),{,},},Class,D_,:,n,{,},Class,g_,:,i_17,{,Var,_f8W,:,Array,[,Array,[,Array,[,Float,,,0130,],,,0xAD9,],,,05,],;,},<EOF>''',
                101
            )
        )

    def test_1039(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _ux9:_{Val $9_8,q:h;Val $_h_,fE_,W,_W_:Array [Array [Array [Array [String ,0x5F],0x9],0b111011],60];Constructor (){Continue ;} }''',
                '''Class,_ux9,:,_,{,Val,$9_8,,,q,:,h,;,Val,$_h_,,,fE_,,,W,,,_W_,:,Array,[,Array,[,Array,[,Array,[,String,,,0x5F,],,,0x9,],,,0b111011,],,,60,],;,Constructor,(,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_1040(self):
        self.assertTrue(
            TestLexer.test(
                '''Class uz:_{}Class __2:b72__9{}Class _5:c{__(Coeb:_jy;_:Int ){} }Class TZ_8o{}Class _:fA_{Var _:Array [Array [Int ,96],074];Destructor (){} }''',
                '''Class,uz,:,_,{,},Class,__2,:,b72__9,{,},Class,_5,:,c,{,__,(,Coeb,:,_jy,;,_,:,Int,),{,},},Class,TZ_8o,{,},Class,_,:,fA_,{,Var,_,:,Array,[,Array,[,Int,,,96,],,,074,],;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1041(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class IS:_{$f(_:Float ){} }Class F2:__YM{Var _:Array [String ,9_5_0_2];$__ZE_4(AoU,s,_b:Array [Array [Array [String ,0B1001001],0B1],04];_55,zf,e0:Array [Float ,0b110000];j,n,_E,_:_){} }Class _:____{}''',
                '''Class,_,{,},Class,IS,:,_,{,$f,(,_,:,Float,),{,},},Class,F2,:,__YM,{,Var,_,:,Array,[,String,,,9502,],;,$__ZE_4,(,AoU,,,s,,,_b,:,Array,[,Array,[,Array,[,String,,,0B1001001,],,,0B1,],,,04,],;,_55,,,zf,,,e0,:,Array,[,Float,,,0b110000,],;,j,,,n,,,_E,,,_,:,_,),{,},},Class,_,:,____,{,},<EOF>''',
                101
            )
        )

    def test_1042(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g_UYdh:_4K8{Val $_T,P_,m:Array [Float ,0B1001000];Destructor (){} }Class __15{Val $0,_:x;Val $2_:Array [Boolean ,05];Var $_,Cy50:Array [Array [Array [Boolean ,0x23],0B1001000],64];}''',
                '''Class,g_UYdh,:,_4K8,{,Val,$_T,,,P_,,,m,:,Array,[,Float,,,0B1001000,],;,Destructor,(,),{,},},Class,__15,{,Val,$0,,,_,:,x,;,Val,$2_,:,Array,[,Boolean,,,05,],;,Var,$_,,,Cy50,:,Array,[,Array,[,Array,[,Boolean,,,0x23,],,,0B1001000,],,,64,],;,},<EOF>''',
                101
            )
        )

    def test_1043(self):
        self.assertTrue(
            TestLexer.test(
                '''Class hH:MB{}Class V:_{Constructor (mSY07,f_:Array [Array [Float ,0b1],0b1]){}Val _:Array [String ,0B1001100];}Class _{}''',
                '''Class,hH,:,MB,{,},Class,V,:,_,{,Constructor,(,mSY07,,,f_,:,Array,[,Array,[,Float,,,0b1,],,,0b1,],),{,},Val,_,:,Array,[,String,,,0B1001100,],;,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_1044(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n2b:_{Destructor (){} }Class _:D{E(_,_:b4_M;f:Array [Array [Array [Float ,0X1_54_97],0X18],04];nE:G2;l,_9r3,N,H_3,__,_A,Im:Boolean ){yQ::$y();} }''',
                '''Class,n2b,:,_,{,Destructor,(,),{,},},Class,_,:,D,{,E,(,_,,,_,:,b4_M,;,f,:,Array,[,Array,[,Array,[,Float,,,0X15497,],,,0X18,],,,04,],;,nE,:,G2,;,l,,,_9r3,,,N,,,H_3,,,__,,,_A,,,Im,:,Boolean,),{,yQ,::,$y,(,),;,},},<EOF>''',
                101
            )
        )

    def test_1045(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class v_:_{$__M3(e:_2){}Val _:Int ;}Class P_:_{Destructor (){} }Class _{$E(i,_d,dc:_4_A){} }Class U:H8{Val $_58:k;}Class _:F{}''',
                '''Class,_,{,},Class,v_,:,_,{,$__M3,(,e,:,_2,),{,},Val,_,:,Int,;,},Class,P_,:,_,{,Destructor,(,),{,},},Class,_,{,$E,(,i,,,_d,,,dc,:,_4_A,),{,},},Class,U,:,H8,{,Val,$_58,:,k,;,},Class,_,:,F,{,},<EOF>''',
                101
            )
        )

    def test_1046(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T_:_J{}Class ac_{Constructor (U3,Cc:Array [Array [Array [Array [Boolean ,05_6_624],0X4],0143],0B1]){}$_(){} }Class _:B{}''',
                '''Class,T_,:,_J,{,},Class,ac_,{,Constructor,(,U3,,,Cc,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,056624,],,,0X4,],,,0143,],,,0B1,],),{,},$_,(,),{,},},Class,_,:,B,{,},<EOF>''',
                101
            )
        )

    def test_1047(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7h{}Class R:_724l6_{Constructor (l,_k,_,X:_;_:Array [Array [Array [String ,057],0B1010010],0x33];_:Q2;_8,_14k:H){}Destructor (){} }Class __07{Val O,a:Array [String ,6450];NHeg146(){} }''',
                '''Class,_7h,{,},Class,R,:,_724l6_,{,Constructor,(,l,,,_k,,,_,,,X,:,_,;,_,:,Array,[,Array,[,Array,[,String,,,057,],,,0B1010010,],,,0x33,],;,_,:,Q2,;,_8,,,_14k,:,H,),{,},Destructor,(,),{,},},Class,__07,{,Val,O,,,a,:,Array,[,String,,,6450,],;,NHeg146,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1048(self):
        self.assertTrue(
            TestLexer.test(
                '''Class B_Z{Constructor (){} }Class X9_:R76h{_tW(){ {} }Var h,$_:Lh;Val E3,$9,$_,W2,$u_x,$p_:Array [String ,0142];Constructor (_,_,f:String ;L,R,_:Array [Array [Array [Int ,0X1_7_7],0142],0b10_01]){} }''',
                '''Class,B_Z,{,Constructor,(,),{,},},Class,X9_,:,R76h,{,_tW,(,),{,{,},},Var,h,,,$_,:,Lh,;,Val,E3,,,$9,,,$_,,,W2,,,$u_x,,,$p_,:,Array,[,String,,,0142,],;,Constructor,(,_,,,_,,,f,:,String,;,L,,,R,,,_,:,Array,[,Array,[,Array,[,Int,,,0X177,],,,0142,],,,0b1001,],),{,},},<EOF>''',
                101
            )
        )

    def test_1049(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8Z:e{Var $_,_T:Array [Array [Array [Boolean ,05],040],0x45];}Class _{}Class v{Constructor (){}Var $6:Array [String ,074];}''',
                '''Class,_8Z,:,e,{,Var,$_,,,_T,:,Array,[,Array,[,Array,[,Boolean,,,05,],,,040,],,,0x45,],;,},Class,_,{,},Class,v,{,Constructor,(,),{,},Var,$6,:,Array,[,String,,,074,],;,},<EOF>''',
                101
            )
        )

    def test_1050(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o:_Q{Constructor (){}Constructor (){}Constructor (__:Int ;Y,f_,_:Array [Int ,07]){}Var $3:Array [Array [Boolean ,55],0x34];_5(xT:r;c_g,__,i0,Q2_,T,___,o:_;K,_N:Array [Array [Array [Boolean ,012],05],012];_:Int ){Continue ;}Destructor (){Return ;Break ;}Destructor (){}Var _l,$8P:Array [Array [String ,0x34],02_6];Destructor (){} }''',
                '''Class,o,:,_Q,{,Constructor,(,),{,},Constructor,(,),{,},Constructor,(,__,:,Int,;,Y,,,f_,,,_,:,Array,[,Int,,,07,],),{,},Var,$3,:,Array,[,Array,[,Boolean,,,55,],,,0x34,],;,_5,(,xT,:,r,;,c_g,,,__,,,i0,,,Q2_,,,T,,,___,,,o,:,_,;,K,,,_N,:,Array,[,Array,[,Array,[,Boolean,,,012,],,,05,],,,012,],;,_,:,Int,),{,Continue,;,},Destructor,(,),{,Return,;,Break,;,},Destructor,(,),{,},Var,_l,,,$8P,:,Array,[,Array,[,String,,,0x34,],,,026,],;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1051(self):
        self.assertTrue(
            TestLexer.test(
                '''Class oN7{Constructor (___,Xn:G;Z_,_,_,_v6:Array [Array [Boolean ,0b1_1],0143];_:Array [Float ,9_0]){}$R(wo_:Int ){} }''',
                '''Class,oN7,{,Constructor,(,___,,,Xn,:,G,;,Z_,,,_,,,_,,,_v6,:,Array,[,Array,[,Boolean,,,0b11,],,,0143,],;,_,:,Array,[,Float,,,90,],),{,},$R,(,wo_,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_1052(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _X_:_E_{Val fP__,$k6:Boolean ;Val _5,$3,w,z8,$Q4:_;}Class _{w(){}Constructor (q:Array [Int ,054];p:R;j,y,_f,_:_){Break ;}Var W_,$D7:_;Val $_,_,__,$8CY:String ;}''',
                '''Class,_X_,:,_E_,{,Val,fP__,,,$k6,:,Boolean,;,Val,_5,,,$3,,,w,,,z8,,,$Q4,:,_,;,},Class,_,{,w,(,),{,},Constructor,(,q,:,Array,[,Int,,,054,],;,p,:,R,;,j,,,y,,,_f,,,_,:,_,),{,Break,;,},Var,W_,,,$D7,:,_,;,Val,$_,,,_,,,__,,,$8CY,:,String,;,},<EOF>''',
                101
            )
        )

    def test_1053(self):
        self.assertTrue(
            TestLexer.test(
                '''Class c{}Class d8{$q_176h(s_:Boolean ){}Constructor (_3,__,C,FB_,P:_mSa){Return ;}Var $__,G4N,$_:Array [String ,0X1];}Class _:v__G{}Class _Z:D{}''',
                '''Class,c,{,},Class,d8,{,$q_176h,(,s_,:,Boolean,),{,},Constructor,(,_3,,,__,,,C,,,FB_,,,P,:,_mSa,),{,Return,;,},Var,$__,,,G4N,,,$_,:,Array,[,String,,,0X1,],;,},Class,_,:,v__G,{,},Class,_Z,:,D,{,},<EOF>''',
                101
            )
        )

    def test_1054(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C_5:_{Var __:Array [Array [Array [String ,0XB],76],0B1100010];}Class __:_{Destructor (){Return ;_::$0_.Z()._();} }''',
                '''Class,C_5,:,_,{,Var,__,:,Array,[,Array,[,Array,[,String,,,0XB,],,,76,],,,0B1100010,],;,},Class,__,:,_,{,Destructor,(,),{,Return,;,_,::,$0_,.,Z,(,),.,_,(,),;,},},<EOF>''',
                101
            )
        )

    def test_1055(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Var $37_,_,__,$g8:Array [Boolean ,98];Constructor (s,_3BV4:Array [Boolean ,0x2A];_,wwK_z,_V:Array [Boolean ,9]){Val RCExQH,H_,__96,Z,__O,_w:TO3;}Constructor (){}$__(){} }Class y{}Class A_:sc{Var _:Int ;}Class _{}Class _:l{Destructor (){} }''',
                '''Class,_,:,_,{,Var,$37_,,,_,,,__,,,$g8,:,Array,[,Boolean,,,98,],;,Constructor,(,s,,,_3BV4,:,Array,[,Boolean,,,0x2A,],;,_,,,wwK_z,,,_V,:,Array,[,Boolean,,,9,],),{,Val,RCExQH,,,H_,,,__96,,,Z,,,__O,,,_w,:,TO3,;,},Constructor,(,),{,},$__,(,),{,},},Class,y,{,},Class,A_,:,sc,{,Var,_,:,Int,;,},Class,_,{,},Class,_,:,l,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1056(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Q8_:Es2{$O(_:_i3qU;d:Array [Array [String ,041],0B1_0_0];_:Array [Array [Array [Array [Array [String ,0b111011],0x49],89],0x1],0X48];I,_,_:Int ){} }''',
                '''Class,Q8_,:,Es2,{,$O,(,_,:,_i3qU,;,d,:,Array,[,Array,[,String,,,041,],,,0B100,],;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b111011,],,,0x49,],,,89,],,,0x1,],,,0X48,],;,I,,,_,,,_,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_1057(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _b6{l(_,_,Pi:__hc8;_,T30BD,__:Array [Array [Array [String ,013],0X3F_943],077];p7,_:Array [Array [Array [Array [Array [Array [Array [Array [Int ,03],0X28],0X28],077],0b111010],0b111010],0B1_0_0_0],02]){} }Class d36{}''',
                '''Class,_b6,{,l,(,_,,,_,,,Pi,:,__hc8,;,_,,,T30BD,,,__,:,Array,[,Array,[,Array,[,String,,,013,],,,0X3F943,],,,077,],;,p7,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,03,],,,0X28,],,,0X28,],,,077,],,,0b111010,],,,0b111010,],,,0B1000,],,,02,],),{,},},Class,d36,{,},<EOF>''',
                101
            )
        )

    def test_1058(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:W{}Class k{}Class _M_{d9_(y:_86;__1C:k_59){Continue ;}Var _,J_l_m,$5,$I:Array [Array [Array [Array [String ,0X61],07],0xC],0b101_10_1_0];}''',
                '''Class,_,:,W,{,},Class,k,{,},Class,_M_,{,d9_,(,y,:,_86,;,__1C,:,k_59,),{,Continue,;,},Var,_,,,J_l_m,,,$5,,,$I,:,Array,[,Array,[,Array,[,Array,[,String,,,0X61,],,,07,],,,0xC,],,,0b1011010,],;,},<EOF>''',
                101
            )
        )

    def test_1059(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _H:x_{Val Rk:p;Val i8:_T_L;Val $__,$yJR_,__:Float ;Destructor (){Break ;Break ;{} }$Ab9(C,_:_5;_,_xs,_,os_3,gN,_,_1_0:Float ;y95,q:W){Break ;}$Y(){}Constructor (V_iA:_1;l,_:Array [String ,56];nY,_:String ){} }''',
                '''Class,_H,:,x_,{,Val,Rk,:,p,;,Val,i8,:,_T_L,;,Val,$__,,,$yJR_,,,__,:,Float,;,Destructor,(,),{,Break,;,Break,;,{,},},$Ab9,(,C,,,_,:,_5,;,_,,,_xs,,,_,,,os_3,,,gN,,,_,,,_1_0,:,Float,;,y95,,,q,:,W,),{,Break,;,},$Y,(,),{,},Constructor,(,V_iA,:,_1,;,l,,,_,:,Array,[,String,,,56,],;,nY,,,_,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_1060(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _{}Class _3:__{Constructor (_d7:Boolean ){} }Class _97_F{}Class S:a_{}Class __:a{Var _,_X,$4:__h;}Class r0:Z{Var $D:Eb_;Val $3w:e;Destructor (){}Destructor (){} }Class B:_{}''',
                '''Class,_,{,},Class,_,{,},Class,_3,:,__,{,Constructor,(,_d7,:,Boolean,),{,},},Class,_97_F,{,},Class,S,:,a_,{,},Class,__,:,a,{,Var,_,,,_X,,,$4,:,__h,;,},Class,r0,:,Z,{,Var,$D,:,Eb_,;,Val,$3w,:,e,;,Destructor,(,),{,},Destructor,(,),{,},},Class,B,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1061(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n_:q74p{Constructor (M:_;L:Array [Array [String ,066],0X6996]){} }Class Q{Var __:String ;}Class ___:P_41T{}''',
                '''Class,n_,:,q74p,{,Constructor,(,M,:,_,;,L,:,Array,[,Array,[,String,,,066,],,,0X6996,],),{,},},Class,Q,{,Var,__,:,String,;,},Class,___,:,P_41T,{,},<EOF>''',
                101
            )
        )

    def test_1062(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w{Constructor (_fN_0,H7,_:k_){Val _cJ_,F__,_,aF7,V6xNS,_:Array [Boolean ,83];Return ;}Val $_:Array [Array [Float ,0136],0XF];}''',
                '''Class,w,{,Constructor,(,_fN_0,,,H7,,,_,:,k_,),{,Val,_cJ_,,,F__,,,_,,,aF7,,,V6xNS,,,_,:,Array,[,Boolean,,,83,],;,Return,;,},Val,$_,:,Array,[,Array,[,Float,,,0136,],,,0XF,],;,},<EOF>''',
                101
            )
        )

    def test_1063(self):
        self.assertTrue(
            TestLexer.test(
                '''Class SF{Var $N16___,p,$_:String ;}Class __4_:_{}Class _{Val $_5_vRE_,$0,$5,$__M:String ;}Class I435{}Class _X_{}Class __:N{}''',
                '''Class,SF,{,Var,$N16___,,,p,,,$_,:,String,;,},Class,__4_,:,_,{,},Class,_,{,Val,$_5_vRE_,,,$0,,,$5,,,$__M,:,String,;,},Class,I435,{,},Class,_X_,{,},Class,__,:,N,{,},<EOF>''',
                101
            )
        )

    def test_1064(self):
        self.assertTrue(
            TestLexer.test(
                '''Class bV{Var _:Array [Array [Array [Boolean ,27],0B1],27];}Class UU674_{V(){} }Class ___{Destructor (){Continue ;} }''',
                '''Class,bV,{,Var,_,:,Array,[,Array,[,Array,[,Boolean,,,27,],,,0B1,],,,27,],;,},Class,UU674_,{,V,(,),{,},},Class,___,{,Destructor,(,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_1065(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:I{Constructor (K,_,_o__733_,h:_RE_;_3,p657,_5,B_,O:Array [String ,88];o_3,f,_,_:Boolean ){} }Class _8_{Constructor (){} }''',
                '''Class,__,:,I,{,Constructor,(,K,,,_,,,_o__733_,,,h,:,_RE_,;,_3,,,p657,,,_5,,,B_,,,O,:,Array,[,String,,,88,],;,o_3,,,f,,,_,,,_,:,Boolean,),{,},},Class,_8_,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1066(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __l{Val _,_,$_y:Float ;}Class a:K{GQ__(BK_:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0B1_1_0],4],02],0115],0XE],0b1],0XB],0b1]){} }Class Y{}''',
                '''Class,__l,{,Val,_,,,_,,,$_y,:,Float,;,},Class,a,:,K,{,GQ__,(,BK_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B110,],,,4,],,,02,],,,0115,],,,0XE,],,,0b1,],,,0XB,],,,0b1,],),{,},},Class,Y,{,},<EOF>''',
                101
            )
        )

    def test_1067(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y0_e:b{Constructor (_:Int ){ {} }Constructor (o:_;M:Array [Array [Int ,36],8];t:String ;lS,n_:Array [Array [Int ,0401_3_2],0B1010100];_:_C){Var n:Int ;}Val $C_4:R;}''',
                '''Class,y0_e,:,b,{,Constructor,(,_,:,Int,),{,{,},},Constructor,(,o,:,_,;,M,:,Array,[,Array,[,Int,,,36,],,,8,],;,t,:,String,;,lS,,,n_,:,Array,[,Array,[,Int,,,040132,],,,0B1010100,],;,_,:,_C,),{,Var,n,:,Int,;,},Val,$C_4,:,R,;,},<EOF>''',
                101
            )
        )

    def test_1068(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class L{Constructor (kG,H:_;W0t10wT,_:Array [Array [Int ,0B11],0b110_01];l6_7,___4:r_){} }Class l:b3{}''',
                '''Class,_,{,},Class,L,{,Constructor,(,kG,,,H,:,_,;,W0t10wT,,,_,:,Array,[,Array,[,Int,,,0B11,],,,0b11001,],;,l6_7,,,___4,:,r_,),{,},},Class,l,:,b3,{,},<EOF>''',
                101
            )
        )

    def test_1069(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9{Val _,$2_,$w:Array [Array [Array [String ,0b10011],0x8A],01];T(Fb_,_3Lz,R,H,Y_L:Array [Array [Int ,07],0B1010010];Y:a;_2r6_Q:Array [Int ,02]){} }Class L:R{}''',
                '''Class,_9,{,Val,_,,,$2_,,,$w,:,Array,[,Array,[,Array,[,String,,,0b10011,],,,0x8A,],,,01,],;,T,(,Fb_,,,_3Lz,,,R,,,H,,,Y_L,:,Array,[,Array,[,Int,,,07,],,,0B1010010,],;,Y,:,a,;,_2r6_Q,:,Array,[,Int,,,02,],),{,},},Class,L,:,R,{,},<EOF>''',
                101
            )
        )

    def test_1070(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X_0y_D_:_{Constructor (_0G,L:Z;z1:__){Break ;}Constructor (m,_b5:a;M8:_W;_,j:Boolean ;l,A:Array [Boolean ,99]){} }Class L2:S_L{$oe(){ {} }}''',
                '''Class,X_0y_D_,:,_,{,Constructor,(,_0G,,,L,:,Z,;,z1,:,__,),{,Break,;,},Constructor,(,m,,,_b5,:,a,;,M8,:,_W,;,_,,,j,:,Boolean,;,l,,,A,:,Array,[,Boolean,,,99,],),{,},},Class,L2,:,S_L,{,$oe,(,),{,{,},},},<EOF>''',
                101
            )
        )

    def test_1071(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _qb_22:q7{$_(Ot:Array [Array [Boolean ,77],05];_3:Array [Int ,06_2_3];_,_,snJ3_,__,VZv,y_:Array [Array [Array [String ,0b1010111],0B1],0B11];g,I0,__9:String ){} }''',
                '''Class,_qb_22,:,q7,{,$_,(,Ot,:,Array,[,Array,[,Boolean,,,77,],,,05,],;,_3,:,Array,[,Int,,,0623,],;,_,,,_,,,snJ3_,,,__,,,VZv,,,y_,:,Array,[,Array,[,Array,[,String,,,0b1010111,],,,0B1,],,,0B11,],;,g,,,I0,,,__9,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_1072(self):
        self.assertTrue(
            TestLexer.test(
                '''Class f:_a{}Class g_E:R{Constructor (y:Array [Array [Int ,0b1],0X2]){}Val $_:__;Var $1,L:Array [Int ,7];}Class _:_{}''',
                '''Class,f,:,_a,{,},Class,g_E,:,R,{,Constructor,(,y,:,Array,[,Array,[,Int,,,0b1,],,,0X2,],),{,},Val,$_,:,__,;,Var,$1,,,L,:,Array,[,Int,,,7,],;,},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1073(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:v14{Constructor (){} }Class v7u87:L3_M{Val $_,$_8or_:g;Constructor (Cy:Array [Array [Array [Array [Array [String ,0x2D],060_33_2_3],027],0xB],7_9];W,_3,_58,_:Float ){} }''',
                '''Class,__,:,v14,{,Constructor,(,),{,},},Class,v7u87,:,L3_M,{,Val,$_,,,$_8or_,:,g,;,Constructor,(,Cy,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0x2D,],,,0603323,],,,027,],,,0xB,],,,79,],;,W,,,_3,,,_58,,,_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_1074(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _v__{}Class I{Var $5:Float ;}Class c:K6J4{Constructor (){} }Class _6:___{Constructor (y1,_:q){} }Class J{Var $_,$z_:Float ;_(){Val Ga_V58:Boolean ;} }''',
                '''Class,_,{,},Class,_v__,{,},Class,I,{,Var,$5,:,Float,;,},Class,c,:,K6J4,{,Constructor,(,),{,},},Class,_6,:,___,{,Constructor,(,y1,,,_,:,q,),{,},},Class,J,{,Var,$_,,,$z_,:,Float,;,_,(,),{,Val,Ga_V58,:,Boolean,;,},},<EOF>''',
                101
            )
        )

    def test_1075(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __p0_:_{ko(){}Constructor (uS,x,YD,c,_,_5,c:Array [Array [Array [Boolean ,26],26],063];Q,B:_;_,L_9UT:_){} }''',
                '''Class,__p0_,:,_,{,ko,(,),{,},Constructor,(,uS,,,x,,,YD,,,c,,,_,,,_5,,,c,:,Array,[,Array,[,Array,[,Boolean,,,26,],,,26,],,,063,],;,Q,,,B,:,_,;,_,,,L_9UT,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_1076(self):
        self.assertTrue(
            TestLexer.test(
                '''Class O:J{Constructor (_4_467,D:Array [Boolean ,015]){}Val $MX:_=!!!!!-_::$w_/---tS::$P_7()._Z335()&&!------New tA()._._95._._.x_B();}''',
                '''Class,O,:,J,{,Constructor,(,_4_467,,,D,:,Array,[,Boolean,,,015,],),{,},Val,$MX,:,_,=,!,!,!,!,!,-,_,::,$w_,/,-,-,-,tS,::,$P_7,(,),.,_Z335,(,),&&,!,-,-,-,-,-,-,New,tA,(,),.,_,.,_95,.,_,.,_,.,x_B,(,),;,},<EOF>''',
                101
            )
        )

    def test_1077(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Q:U_{}Class RE:_{}Class _6_:q{Var $U6,J_3,g:_6;$_(){Break ;} }Class _0:_{Destructor (){} }Class l:S{}Class l{}Class CKwP_{Destructor (){} }Class _{}''',
                '''Class,Q,:,U_,{,},Class,RE,:,_,{,},Class,_6_,:,q,{,Var,$U6,,,J_3,,,g,:,_6,;,$_,(,),{,Break,;,},},Class,_0,:,_,{,Destructor,(,),{,},},Class,l,:,S,{,},Class,l,{,},Class,CKwP_,{,Destructor,(,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_1078(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val O:_;Val $3vDQ:Array [Array [Int ,0X21],0XE];Val $_,m,D:Array [Array [Array [Array [Boolean ,026],86],0B1_01],0X3_FAF];}''',
                '''Class,_,{,Val,O,:,_,;,Val,$3vDQ,:,Array,[,Array,[,Int,,,0X21,],,,0XE,],;,Val,$_,,,m,,,D,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,026,],,,86,],,,0B101,],,,0X3FAF,],;,},<EOF>''',
                101
            )
        )

    def test_1079(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:J{}Class o:y{Val $4W0w:Float ;}Class __G:F1_{Var _07,$Jc,$s0,$_,vd9,$N1,$S,$w_:Array [Array [Array [Array [Array [Array [Boolean ,0x7],0115],7],0b1100],0B10],0x69];}''',
                '''Class,_,:,J,{,},Class,o,:,y,{,Val,$4W0w,:,Float,;,},Class,__G,:,F1_,{,Var,_07,,,$Jc,,,$s0,,,$_,,,vd9,,,$N1,,,$S,,,$w_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x7,],,,0115,],,,7,],,,0b1100,],,,0B10,],,,0x69,],;,},<EOF>''',
                101
            )
        )

    def test_1080(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __5:q{Var H,N_,$_F:Array [Float ,04];$9(T:Array [Int ,0111];Uw9J,R,a,_:Array [Array [Array [Array [Boolean ,99],0111],0b11_1_1],06];M:Boolean ){}$_6R7(){}Var _,AcF7__A:String ;}''',
                '''Class,__5,:,q,{,Var,H,,,N_,,,$_F,:,Array,[,Float,,,04,],;,$9,(,T,:,Array,[,Int,,,0111,],;,Uw9J,,,R,,,a,,,_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,99,],,,0111,],,,0b1111,],,,06,],;,M,:,Boolean,),{,},$_6R7,(,),{,},Var,_,,,AcF7__A,:,String,;,},<EOF>''',
                101
            )
        )

    def test_1081(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P_:C_{}Class _:_d_{Var _,$_id03V,$m,$1,_:Int ;Constructor (_Z:Array [Int ,3];_,K,_:Array [Array [Boolean ,0130],72]){} }''',
                '''Class,P_,:,C_,{,},Class,_,:,_d_,{,Var,_,,,$_id03V,,,$m,,,$1,,,_,:,Int,;,Constructor,(,_Z,:,Array,[,Int,,,3,],;,_,,,K,,,_,:,Array,[,Array,[,Boolean,,,0130,],,,72,],),{,},},<EOF>''',
                101
            )
        )

    def test_1082(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{_M(){} }Class _{Val $3,O,j2,a,$e:Array [Array [Array [Float ,34],0b111110],0x52];}Class u{}Class I_:_{Constructor (){} }Class X:X{}''',
                '''Class,_,{,_M,(,),{,},},Class,_,{,Val,$3,,,O,,,j2,,,a,,,$e,:,Array,[,Array,[,Array,[,Float,,,34,],,,0b111110,],,,0x52,],;,},Class,u,{,},Class,I_,:,_,{,Constructor,(,),{,},},Class,X,:,X,{,},<EOF>''',
                101
            )
        )

    def test_1083(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q0:j_{}Class B{}Class nS:_{}Class _:_5{Val $h2_:_;$_M_(){} }Class _r{Val $_g_,__,$1fh:String ;}Class w_:e7{Var B,i,$W,j,_:P;Var $4:Array [Float ,0X1C];Destructor (){}Constructor (Q,___:Int ;_,_:String ){} }Class _{}''',
                '''Class,q0,:,j_,{,},Class,B,{,},Class,nS,:,_,{,},Class,_,:,_5,{,Val,$h2_,:,_,;,$_M_,(,),{,},},Class,_r,{,Val,$_g_,,,__,,,$1fh,:,String,;,},Class,w_,:,e7,{,Var,B,,,i,,,$W,,,j,,,_,:,P,;,Var,$4,:,Array,[,Float,,,0X1C,],;,Destructor,(,),{,},Constructor,(,Q,,,___,:,Int,;,_,,,_,:,String,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_1084(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Z9:V{Constructor (D:Array [Array [Float ,0XC],0x4];__5,k22:Array [Float ,17];__:Int ;_:Array [Boolean ,17]){Continue ;Continue ;}Destructor (){} }''',
                '''Class,Z9,:,V,{,Constructor,(,D,:,Array,[,Array,[,Float,,,0XC,],,,0x4,],;,__5,,,k22,:,Array,[,Float,,,17,],;,__,:,Int,;,_,:,Array,[,Boolean,,,17,],),{,Continue,;,Continue,;,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1085(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _{Constructor (__,_a,Dl:String ;_F,_,_3,A:Int ;N,qe:Array [String ,0B100010]){} }Class _{}Class n:D{$___(){} }''',
                '''Class,_,{,},Class,_,{,Constructor,(,__,,,_a,,,Dl,:,String,;,_F,,,_,,,_3,,,A,:,Int,;,N,,,qe,:,Array,[,String,,,0B100010,],),{,},},Class,_,{,},Class,n,:,D,{,$___,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1086(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9:__{$Dr(l5:Array [Array [Int ,0B110],0x5];n,_,_,o,c_,V:_2;p2_:d;_:Float ;__,_,_42j,N:Array [Array [Array [String ,7],32],0XB];J,v1,_:Array [Array [Array [Float ,0b1],0XB],32]){}Var $m:_;}''',
                '''Class,_9,:,__,{,$Dr,(,l5,:,Array,[,Array,[,Int,,,0B110,],,,0x5,],;,n,,,_,,,_,,,o,,,c_,,,V,:,_2,;,p2_,:,d,;,_,:,Float,;,__,,,_,,,_42j,,,N,:,Array,[,Array,[,Array,[,String,,,7,],,,32,],,,0XB,],;,J,,,v1,,,_,:,Array,[,Array,[,Array,[,Float,,,0b1,],,,0XB,],,,32,],),{,},Var,$m,:,_,;,},<EOF>''',
                101
            )
        )

    def test_1087(self):
        self.assertTrue(
            TestLexer.test(
                '''Class r:__b{}Class _P:_k{Val _,d_,___4:_234;}Class T{Constructor (){}Constructor (_K:___e4;T:Array [Boolean ,04_1];_:z;sYa:Boolean ){} }''',
                '''Class,r,:,__b,{,},Class,_P,:,_k,{,Val,_,,,d_,,,___4,:,_234,;,},Class,T,{,Constructor,(,),{,},Constructor,(,_K,:,___e4,;,T,:,Array,[,Boolean,,,041,],;,_,:,z,;,sYa,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_1088(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:X8{}Class I{}Class j7v:l{Constructor (_:W;_3_:_7hL;t:iq;_7,U:Int ;Gd:Float ;_N:String ;i:String ;q9,_,_:_G;p:_7){} }''',
                '''Class,_,:,X8,{,},Class,I,{,},Class,j7v,:,l,{,Constructor,(,_,:,W,;,_3_,:,_7hL,;,t,:,iq,;,_7,,,U,:,Int,;,Gd,:,Float,;,_N,:,String,;,i,:,String,;,q9,,,_,,,_,:,_G,;,p,:,_7,),{,},},<EOF>''',
                101
            )
        )

    def test_1089(self):
        self.assertTrue(
            TestLexer.test(
                '''Class D4{Var $___:Boolean ;Constructor (a,V,_G,_,_:_;Wj,_,a6:_5;__u,V,_KR_:Array [Array [Float ,05_2],61_2];_,p25:Array [Float ,23];j6:Boolean ){} }''',
                '''Class,D4,{,Var,$___,:,Boolean,;,Constructor,(,a,,,V,,,_G,,,_,,,_,:,_,;,Wj,,,_,,,a6,:,_5,;,__u,,,V,,,_KR_,:,Array,[,Array,[,Float,,,052,],,,612,],;,_,,,p25,:,Array,[,Float,,,23,],;,j6,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_1090(self):
        self.assertTrue(
            TestLexer.test(
                '''Class u:_27{}Class _{}Class HW7_9:J{}Class z{Val $_9:Array [Array [Array [Boolean ,0B111011],075],0b1_1];$U(L5_7:Array [String ,0b1010101];_:Array [String ,01];_:Array [Array [Array [Array [Float ,0B111011],02],87],87]){u::$qL()._m_._();}Constructor (){} }Class _s:C3{}''',
                '''Class,u,:,_27,{,},Class,_,{,},Class,HW7_9,:,J,{,},Class,z,{,Val,$_9,:,Array,[,Array,[,Array,[,Boolean,,,0B111011,],,,075,],,,0b11,],;,$U,(,L5_7,:,Array,[,String,,,0b1010101,],;,_,:,Array,[,String,,,01,],;,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B111011,],,,02,],,,87,],,,87,],),{,u,::,$qL,(,),.,_m_,.,_,(,),;,},Constructor,(,),{,},},Class,_s,:,C3,{,},<EOF>''',
                101
            )
        )

    def test_1091(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o_:_{}Class o4_8_2{Destructor (){Val T0,__,_:Array [Array [String ,0b10_01],0b1];Break ;Continue ;Return ;{} }Destructor (){} }Class N{}''',
                '''Class,o_,:,_,{,},Class,o4_8_2,{,Destructor,(,),{,Val,T0,,,__,,,_,:,Array,[,Array,[,String,,,0b1001,],,,0b1,],;,Break,;,Continue,;,Return,;,{,},},Destructor,(,),{,},},Class,N,{,},<EOF>''',
                101
            )
        )

    def test_1092(self):
        self.assertTrue(
            TestLexer.test(
                '''Class wI73SN_7{Constructor (v,T_,Y__:String ;__,h:Array [Array [Array [Array [Array [Array [Int ,064],0X3],39],0B10_1_00],39],0b10000]){}Destructor (){} }Class ___:__l{}Class _{}''',
                '''Class,wI73SN_7,{,Constructor,(,v,,,T_,,,Y__,:,String,;,__,,,h,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,064,],,,0X3,],,,39,],,,0B10100,],,,39,],,,0b10000,],),{,},Destructor,(,),{,},},Class,___,:,__l,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_1093(self):
        self.assertTrue(
            TestLexer.test(
                '''Class nF____:__e{Destructor (){}Constructor (){Continue ;}B_5(){}$W(p:_;_:String ;xor_c,q:Array [Array [Array [Int ,0x21],0b1],3];_,y:_8){}Constructor (v0,__,g8m4_hg,__g,_:Array [Float ,0XC];j8d:Float ;_5:Int ){} }''',
                '''Class,nF____,:,__e,{,Destructor,(,),{,},Constructor,(,),{,Continue,;,},B_5,(,),{,},$W,(,p,:,_,;,_,:,String,;,xor_c,,,q,:,Array,[,Array,[,Array,[,Int,,,0x21,],,,0b1,],,,3,],;,_,,,y,:,_8,),{,},Constructor,(,v0,,,__,,,g8m4_hg,,,__g,,,_,:,Array,[,Float,,,0XC,],;,j8d,:,Float,;,_5,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_1094(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C54BD:_v{}Class _{}Class l:_{Constructor (a:Array [Array [String ,0b1010110],034]){} }Class _07947gs:_p{}Class E_:Rp{}''',
                '''Class,C54BD,:,_v,{,},Class,_,{,},Class,l,:,_,{,Constructor,(,a,:,Array,[,Array,[,String,,,0b1010110,],,,034,],),{,},},Class,_07947gs,:,_p,{,},Class,E_,:,Rp,{,},<EOF>''',
                101
            )
        )

    def test_1095(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{_(){}Val _7,$1:Int ;}Class M:_6M5_{$B(){_::$R9=!!Z_::$04.m._.__6()._B._e().W._._8._.J();} }Class z{}''',
                '''Class,_,{,_,(,),{,},Val,_7,,,$1,:,Int,;,},Class,M,:,_6M5_,{,$B,(,),{,_,::,$R9,=,!,!,Z_,::,$04,.,m,.,_,.,__6,(,),.,_B,.,_e,(,),.,W,.,_,.,_8,.,_,.,J,(,),;,},},Class,z,{,},<EOF>''',
                101
            )
        )

    def test_1096(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:Y{$_(jv15,_8_:Array [Float ,0b10];_,_v,_,v,_x:Array [Array [Array [Array [Int ,0b110111],070],0B1011001],0X12];_,_,_,L2:Array [Array [Array [Array [String ,0B1011001],0x3E],18],0X12];_,__:h_8b;_:Array [Array [Float ,04],8];a:String ){}$Z(n,__8,J1:G){} }''',
                '''Class,_,:,Y,{,$_,(,jv15,,,_8_,:,Array,[,Float,,,0b10,],;,_,,,_v,,,_,,,v,,,_x,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b110111,],,,070,],,,0B1011001,],,,0X12,],;,_,,,_,,,_,,,L2,:,Array,[,Array,[,Array,[,Array,[,String,,,0B1011001,],,,0x3E,],,,18,],,,0X12,],;,_,,,__,:,h_8b,;,_,:,Array,[,Array,[,Float,,,04,],,,8,],;,a,:,String,),{,},$Z,(,n,,,__8,,,J1,:,G,),{,},},<EOF>''',
                101
            )
        )

    def test_1097(self):
        self.assertTrue(
            TestLexer.test(
                '''Class M6i{}Class _76{O(c,c8:Array [Array [Array [Int ,012],0b1_10],7];_:y;_,_,_4_5q3_:Array [Boolean ,0b10];__0:Array [Array [Array [Float ,045_60342],0x4A],06_0]){}Constructor (G:Array [Array [Array [Boolean ,7],0x4A],0X47];l,C,_:Array [Float ,6];_,___i,_:Array [Int ,0XE]){}Destructor (){} }''',
                '''Class,M6i,{,},Class,_76,{,O,(,c,,,c8,:,Array,[,Array,[,Array,[,Int,,,012,],,,0b110,],,,7,],;,_,:,y,;,_,,,_,,,_4_5q3_,:,Array,[,Boolean,,,0b10,],;,__0,:,Array,[,Array,[,Array,[,Float,,,04560342,],,,0x4A,],,,060,],),{,},Constructor,(,G,:,Array,[,Array,[,Array,[,Boolean,,,7,],,,0x4A,],,,0X47,],;,l,,,C,,,_,:,Array,[,Float,,,6,],;,_,,,___i,,,_,:,Array,[,Int,,,0XE,],),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1098(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (){} }Class h{Val $76T,_:Int ;Val $_:Array [Int ,0b110100];}Class B{Constructor (){} }Class __k:_Eb{Constructor (){}Val $W_4:Array [Int ,0x32];}Class b:y{Constructor (){} }Class mc:_Aw{}''',
                '''Class,_,{,Constructor,(,),{,},},Class,h,{,Val,$76T,,,_,:,Int,;,Val,$_,:,Array,[,Int,,,0b110100,],;,},Class,B,{,Constructor,(,),{,},},Class,__k,:,_Eb,{,Constructor,(,),{,},Val,$W_4,:,Array,[,Int,,,0x32,],;,},Class,b,:,y,{,Constructor,(,),{,},},Class,mc,:,_Aw,{,},<EOF>''',
                101
            )
        )

    def test_1099(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:__{}Class Yw{}Class _9{Var $__O_,$G,_8I:Array [Array [Array [Array [Array [Boolean ,01_7711],91],02],91],0x34];}''',
                '''Class,__,:,__,{,},Class,Yw,{,},Class,_9,{,Var,$__O_,,,$G,,,_8I,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,017711,],,,91,],,,02,],,,91,],,,0x34,],;,},<EOF>''',
                101
            )
        )

    def test_1100(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __1i9{}Class S:__{Val $5_:Array [Int ,0XA6];}Class O{Var $__:Array [String ,0X19];Constructor (aE,bwq:Boolean ){} }''',
                '''Class,__1i9,{,},Class,S,:,__,{,Val,$5_,:,Array,[,Int,,,0XA6,],;,},Class,O,{,Var,$__,:,Array,[,String,,,0X19,],;,Constructor,(,aE,,,bwq,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_1101(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P:b{Val Pn:String ;Destructor (){Break ;}Constructor (){}o(Q:Q_6WjZB){} }Class _:_3{Val dIDY,$X:_U6r;_(D:u){Break ;} }''',
                '''Class,P,:,b,{,Val,Pn,:,String,;,Destructor,(,),{,Break,;,},Constructor,(,),{,},o,(,Q,:,Q_6WjZB,),{,},},Class,_,:,_3,{,Val,dIDY,,,$X,:,_U6r,;,_,(,D,:,u,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_1102(self):
        self.assertTrue(
            TestLexer.test(
                '''Class M_{Val p:Boolean ;W(_B_:Boolean ;R7X:_;dF,_:Array [Array [Array [Int ,0XD],0B1],0127]){_::$u5();} }Class _c{Constructor (h9,H2:Array [String ,05_0]){} }''',
                '''Class,M_,{,Val,p,:,Boolean,;,W,(,_B_,:,Boolean,;,R7X,:,_,;,dF,,,_,:,Array,[,Array,[,Array,[,Int,,,0XD,],,,0B1,],,,0127,],),{,_,::,$u5,(,),;,},},Class,_c,{,Constructor,(,h9,,,H2,:,Array,[,String,,,050,],),{,},},<EOF>''',
                101
            )
        )

    def test_1103(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:Y85__{}Class y:_{A(O:P_0){Var ___:Array [Array [Int ,041],91_4_4];} }Class ___98:_{Val p8,Q83t_7,$7,_S:Array [Float ,0x16];}''',
                '''Class,__,:,Y85__,{,},Class,y,:,_,{,A,(,O,:,P_0,),{,Var,___,:,Array,[,Array,[,Int,,,041,],,,9144,],;,},},Class,___98,:,_,{,Val,p8,,,Q83t_7,,,$7,,,_S,:,Array,[,Float,,,0x16,],;,},<EOF>''',
                101
            )
        )

    def test_1104(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___{Constructor (){ {}_::$U();} }Class a:_2_{__(_,T8X:Boolean ;_,_2_64K6_q:Array [Array [Array [Array [Array [Array [String ,0B1000100],0B1000100],0b1],74],046_21],0B1_0];_,h,_24,w:____){} }Class m{}''',
                '''Class,___,{,Constructor,(,),{,{,},_,::,$U,(,),;,},},Class,a,:,_2_,{,__,(,_,,,T8X,:,Boolean,;,_,,,_2_64K6_q,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B1000100,],,,0B1000100,],,,0b1,],,,74,],,,04621,],,,0B10,],;,_,,,h,,,_24,,,w,:,____,),{,},},Class,m,{,},<EOF>''',
                101
            )
        )

    def test_1105(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class J{X_(G91,O:Array [String ,4];jW:_){Var __D2:Array [Array [Array [Array [Int ,05],3],03],0b111101];}Destructor (){Break ;} }''',
                '''Class,_,{,},Class,J,{,X_,(,G91,,,O,:,Array,[,String,,,4,],;,jW,:,_,),{,Var,__D2,:,Array,[,Array,[,Array,[,Array,[,Int,,,05,],,,3,],,,03,],,,0b111101,],;,},Destructor,(,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_1106(self):
        self.assertTrue(
            TestLexer.test(
                '''Class i_:_{}Class X:S__{a(_,Q5,_:Array [Array [Array [String ,59],0x3],0B1000110];___,k:Ai){}H(O6,C,B_0q8,Fp,E,L0:Float ){}Destructor (){} }Class _{}Class _{}''',
                '''Class,i_,:,_,{,},Class,X,:,S__,{,a,(,_,,,Q5,,,_,:,Array,[,Array,[,Array,[,String,,,59,],,,0x3,],,,0B1000110,],;,___,,,k,:,Ai,),{,},H,(,O6,,,C,,,B_0q8,,,Fp,,,E,,,L0,:,Float,),{,},Destructor,(,),{,},},Class,_,{,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_1107(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J:h{Val h,TLP:Array [Array [Float ,063],31_7_0_1];B(b,D__,_:Array [Array [Array [Array [Float ,0B100011],37],0x57_3],4];_:Array [String ,0x2F]){Continue ;Break ;}$0_(){} }''',
                '''Class,J,:,h,{,Val,h,,,TLP,:,Array,[,Array,[,Float,,,063,],,,31701,],;,B,(,b,,,D__,,,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B100011,],,,37,],,,0x573,],,,4,],;,_,:,Array,[,String,,,0x2F,],),{,Continue,;,Break,;,},$0_,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1108(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _G:_{}Class q_e{Var $f_Nb,_E:Float ;__(z:String ;L2:D7){}Var $_5,_k2:Array [Array [String ,01],0B10110];}Class __4:S{Constructor (){} }''',
                '''Class,_G,:,_,{,},Class,q_e,{,Var,$f_Nb,,,_E,:,Float,;,__,(,z,:,String,;,L2,:,D7,),{,},Var,$_5,,,_k2,:,Array,[,Array,[,String,,,01,],,,0B10110,],;,},Class,__4,:,S,{,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1109(self):
        self.assertTrue(
            TestLexer.test(
                '''Class fO1__{Constructor (){}Val $6e,_,$_,$_:Array [Array [Array [Array [Float ,66_0],0b1011000],0x60],7_6];Val $__:Float ;}Class _2:_{}''',
                '''Class,fO1__,{,Constructor,(,),{,},Val,$6e,,,_,,,$_,,,$_,:,Array,[,Array,[,Array,[,Array,[,Float,,,660,],,,0b1011000,],,,0x60,],,,76,],;,Val,$__,:,Float,;,},Class,_2,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1110(self):
        self.assertTrue(
            TestLexer.test(
                '''Class jv:Ty{Var $0b_,_:Float ;$_7(){} }Class _:_{}Class _:_{Var _x2_r4_:_9;}Class _P1{Val $72a,$_:Array [String ,7_9_1];Constructor (){Break ;} }Class n{}''',
                '''Class,jv,:,Ty,{,Var,$0b_,,,_,:,Float,;,$_7,(,),{,},},Class,_,:,_,{,},Class,_,:,_,{,Var,_x2_r4_,:,_9,;,},Class,_P1,{,Val,$72a,,,$_,:,Array,[,String,,,791,],;,Constructor,(,),{,Break,;,},},Class,n,{,},<EOF>''',
                101
            )
        )

    def test_1111(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Val _,__6_,S:__8;$2(_,F,o,_:Array [Float ,0B1_0];_:Float ){} }Class _:O9{Val $5:_;Constructor (X_6__:_C){}Var __:Array [Array [String ,0x27],0x4_C_A13D];}Class ___:_{}''',
                '''Class,_,:,_,{,Val,_,,,__6_,,,S,:,__8,;,$2,(,_,,,F,,,o,,,_,:,Array,[,Float,,,0B10,],;,_,:,Float,),{,},},Class,_,:,O9,{,Val,$5,:,_,;,Constructor,(,X_6__,:,_C,),{,},Var,__,:,Array,[,Array,[,String,,,0x27,],,,0x4CA13D,],;,},Class,___,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1112(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:vx{Var $w1S,$_W:Boolean ;Val pQ6_:Array [Array [Array [Boolean ,79],0x39],0x39];Constructor (_,_6:Array [Boolean ,0B111_0];_,Z94,_5,R,_16_,W,_,__u73f,P:Float ;_:Float ){} }''',
                '''Class,_,:,vx,{,Var,$w1S,,,$_W,:,Boolean,;,Val,pQ6_,:,Array,[,Array,[,Array,[,Boolean,,,79,],,,0x39,],,,0x39,],;,Constructor,(,_,,,_6,:,Array,[,Boolean,,,0B1110,],;,_,,,Z94,,,_5,,,R,,,_16_,,,W,,,_,,,__u73f,,,P,:,Float,;,_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_1113(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A{$_(){}Constructor (_,C,L,j2,x_,s,_H,NP8,_,g,_:_;_,b:String ){} }Class __:_9_{}Class W9{Destructor (){} }''',
                '''Class,A,{,$_,(,),{,},Constructor,(,_,,,C,,,L,,,j2,,,x_,,,s,,,_H,,,NP8,,,_,,,g,,,_,:,_,;,_,,,b,:,String,),{,},},Class,__,:,_9_,{,},Class,W9,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1114(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _932fS:j2{Constructor (_,a,C0:Boolean ){} }Class g:_n_{$_(I_o:Array [Array [String ,4],077_33];_9:Array [Float ,0121]){} }''',
                '''Class,_932fS,:,j2,{,Constructor,(,_,,,a,,,C0,:,Boolean,),{,},},Class,g,:,_n_,{,$_,(,I_o,:,Array,[,Array,[,String,,,4,],,,07733,],;,_9,:,Array,[,Float,,,0121,],),{,},},<EOF>''',
                101
            )
        )

    def test_1115(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _w:C{Var $_B_5y_Fe,I4:Array [Array [Array [Array [String ,0X2C],0131],03],75];Val $A9__9Ao:T;}Class _{Var __,$_:H;Val _1u_,_o_,T:Array [Boolean ,0131];Var $0,Gc:_;}Class r:__{}''',
                '''Class,_w,:,C,{,Var,$_B_5y_Fe,,,I4,:,Array,[,Array,[,Array,[,Array,[,String,,,0X2C,],,,0131,],,,03,],,,75,],;,Val,$A9__9Ao,:,T,;,},Class,_,{,Var,__,,,$_,:,H,;,Val,_1u_,,,_o_,,,T,:,Array,[,Boolean,,,0131,],;,Var,$0,,,Gc,:,_,;,},Class,r,:,__,{,},<EOF>''',
                101
            )
        )

    def test_1116(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E:_{}Class e:j_{Constructor (){}Constructor (R_4:String ;_K7,b_:Array [Array [Array [Array [Array [Int ,9_7],886],93],2],03];__V:Array [Array [Int ,0xC],041];i0464,B:H;x,_W,_4_Q:Array [String ,6_5_701]){Continue ;} }''',
                '''Class,E,:,_,{,},Class,e,:,j_,{,Constructor,(,),{,},Constructor,(,R_4,:,String,;,_K7,,,b_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,97,],,,886,],,,93,],,,2,],,,03,],;,__V,:,Array,[,Array,[,Int,,,0xC,],,,041,],;,i0464,,,B,:,H,;,x,,,_W,,,_4_Q,:,Array,[,String,,,65701,],),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_1117(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_n{}Class __:y9_{}Class Q{}Class _o_:g{Constructor (O__:Int ;h,U1,L:Array [String ,0b1];_:Float ;u,ny__J,x_,__0:k;_1,rp,_:i8;_,_:Array [Array [Array [Boolean ,9_9],0x6],0x9];___:Boolean ;_,b:X_vk___){}$_o(_:Boolean ){Return ;} }''',
                '''Class,_,:,_n,{,},Class,__,:,y9_,{,},Class,Q,{,},Class,_o_,:,g,{,Constructor,(,O__,:,Int,;,h,,,U1,,,L,:,Array,[,String,,,0b1,],;,_,:,Float,;,u,,,ny__J,,,x_,,,__0,:,k,;,_1,,,rp,,,_,:,i8,;,_,,,_,:,Array,[,Array,[,Array,[,Boolean,,,99,],,,0x6,],,,0x9,],;,___,:,Boolean,;,_,,,b,:,X_vk___,),{,},$_o,(,_,:,Boolean,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_1118(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __3_:_{Destructor (){_::$D_();}Var P,$36d:Boolean ;Var l,_4Z,_8:Array [Array [Int ,8],0X35];Constructor (k,R,A,D,_7,W_,_2dyi:Array [Boolean ,20]){} }''',
                '''Class,__3_,:,_,{,Destructor,(,),{,_,::,$D_,(,),;,},Var,P,,,$36d,:,Boolean,;,Var,l,,,_4Z,,,_8,:,Array,[,Array,[,Int,,,8,],,,0X35,],;,Constructor,(,k,,,R,,,A,,,D,,,_7,,,W_,,,_2dyi,:,Array,[,Boolean,,,20,],),{,},},<EOF>''',
                101
            )
        )

    def test_1119(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J_54_{Constructor (_l,U,z_,X:String ;_,_,_,__3:_P;_,_:Array [Array [Int ,9],0b1100011];_9,Et3,C315v__U,__w,__a,_6:String ){}Val $6,J:Array [Int ,3_7];Constructor (){} }''',
                '''Class,J_54_,{,Constructor,(,_l,,,U,,,z_,,,X,:,String,;,_,,,_,,,_,,,__3,:,_P,;,_,,,_,:,Array,[,Array,[,Int,,,9,],,,0b1100011,],;,_9,,,Et3,,,C315v__U,,,__w,,,__a,,,_6,:,String,),{,},Val,$6,,,J,:,Array,[,Int,,,37,],;,Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1120(self):
        self.assertTrue(
            TestLexer.test(
                '''Class h7a7R{$l(Z0a7:Array [Array [String ,0x3A],0x3A];_,x:Array [Array [Array [Array [Array [Float ,0x2_988A],07_1_71],48],05],0116]){} }Class _:d{}Class _{Var $__,W:String ;Var $_7ex3u:Boolean ;}Class _{}''',
                '''Class,h7a7R,{,$l,(,Z0a7,:,Array,[,Array,[,String,,,0x3A,],,,0x3A,],;,_,,,x,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x2988A,],,,07171,],,,48,],,,05,],,,0116,],),{,},},Class,_,:,d,{,},Class,_,{,Var,$__,,,W,:,String,;,Var,$_7ex3u,:,Boolean,;,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_1121(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g:Q{$I04_5W3av_(G:Array [Array [String ,0b1_10],0b1];YjW:v__K){}$_C(V:Array [Float ,0B1];_8,__:I;_:Array [Float ,06]){} }''',
                '''Class,g,:,Q,{,$I04_5W3av_,(,G,:,Array,[,Array,[,String,,,0b110,],,,0b1,],;,YjW,:,v__K,),{,},$_C,(,V,:,Array,[,Float,,,0B1,],;,_8,,,__,:,I,;,_,:,Array,[,Float,,,06,],),{,},},<EOF>''',
                101
            )
        )

    def test_1122(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (){Break ;Break ;}Var $_,$A,$_N:_6;Destructor (){}Val _:Array [Array [Boolean ,0b1],010];Val __n:Array [Float ,0X5_E_28];}Class e{}''',
                '''Class,_,{,Constructor,(,),{,Break,;,Break,;,},Var,$_,,,$A,,,$_N,:,_6,;,Destructor,(,),{,},Val,_,:,Array,[,Array,[,Boolean,,,0b1,],,,010,],;,Val,__n,:,Array,[,Float,,,0X5E28,],;,},Class,e,{,},<EOF>''',
                101
            )
        )

    def test_1123(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V_y_:E{_Oa_3P(ei:Array [Array [Array [String ,6_3_4177],0X9],0125]){}U(wk7__,_Z:Array [Boolean ,0X3]){Continue ;} }''',
                '''Class,V_y_,:,E,{,_Oa_3P,(,ei,:,Array,[,Array,[,Array,[,String,,,634177,],,,0X9,],,,0125,],),{,},U,(,wk7__,,,_Z,:,Array,[,Boolean,,,0X3,],),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_1124(self):
        self.assertTrue(
            TestLexer.test(
                '''Class sa6:M{}Class Zvb9t{M(_q_:Array [Int ,0B1001001]){Break ;} }Class l:D{Val $T_81,L4:Array [Array [Array [Array [Array [Boolean ,53],01],0b111111],0X1_18],044];}''',
                '''Class,sa6,:,M,{,},Class,Zvb9t,{,M,(,_q_,:,Array,[,Int,,,0B1001001,],),{,Break,;,},},Class,l,:,D,{,Val,$T_81,,,L4,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,53,],,,01,],,,0b111111,],,,0X118,],,,044,],;,},<EOF>''',
                101
            )
        )

    def test_1125(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _50Wh:Rj{z(_E:Array [Array [Array [Array [String ,0b1],0b1010100],0X52],0xC];_,_,j,_:Int ){} }Class _{}Class _A{}''',
                '''Class,_50Wh,:,Rj,{,z,(,_E,:,Array,[,Array,[,Array,[,Array,[,String,,,0b1,],,,0b1010100,],,,0X52,],,,0xC,],;,_,,,_,,,j,,,_,:,Int,),{,},},Class,_,{,},Class,_A,{,},<EOF>''',
                101
            )
        )

    def test_1126(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E245:S{}Class o4{Var _,$B,__,z51,$_,_,$UaP0:Array [Array [Array [String ,0B110010],0X1],0b1_0];}Class w__{}Class _:D{}''',
                '''Class,E245,:,S,{,},Class,o4,{,Var,_,,,$B,,,__,,,z51,,,$_,,,_,,,$UaP0,:,Array,[,Array,[,Array,[,String,,,0B110010,],,,0X1,],,,0b10,],;,},Class,w__,{,},Class,_,:,D,{,},<EOF>''',
                101
            )
        )

    def test_1127(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k_x_:_d{N_f(_,_,e,y,_031:Array [Int ,8]){} }Class Ha{Val Nl5_x5:Array [Array [Float ,0b100_1],024_4_1];}Class I:h{}''',
                '''Class,k_x_,:,_d,{,N_f,(,_,,,_,,,e,,,y,,,_031,:,Array,[,Int,,,8,],),{,},},Class,Ha,{,Val,Nl5_x5,:,Array,[,Array,[,Float,,,0b1001,],,,02441,],;,},Class,I,:,h,{,},<EOF>''',
                101
            )
        )

    def test_1128(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val oz8_,m_94:Array [Array [Array [Float ,037],0X6],037];Val $I3,_:_;}Class __:O{Var g_,__9g3,_,$X_:_3;Destructor (){} }Class w:_JD{}''',
                '''Class,_,{,Val,oz8_,,,m_94,:,Array,[,Array,[,Array,[,Float,,,037,],,,0X6,],,,037,],;,Val,$I3,,,_,:,_,;,},Class,__,:,O,{,Var,g_,,,__9g3,,,_,,,$X_,:,_3,;,Destructor,(,),{,},},Class,w,:,_JD,{,},<EOF>''',
                101
            )
        )

    def test_1129(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:J{Constructor (_B_:Array [Array [Int ,9],03];N:Int ;_d__m,q_,_,qKKa,_,_:Array [Float ,0X52];w:_;_8:__){} }Class _{}''',
                '''Class,_,:,J,{,Constructor,(,_B_,:,Array,[,Array,[,Int,,,9,],,,03,],;,N,:,Int,;,_d__m,,,q_,,,_,,,qKKa,,,_,,,_,:,Array,[,Float,,,0X52,],;,w,:,_,;,_8,:,__,),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_1130(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:w_{Constructor (W_r,_W0,Ph__q,__:Array [Float ,0XF];_:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0x2B],4],0XF],056],46],056],0B1],33]){} }Class _:F{}''',
                '''Class,_,:,w_,{,Constructor,(,W_r,,,_W0,,,Ph__q,,,__,:,Array,[,Float,,,0XF,],;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x2B,],,,4,],,,0XF,],,,056,],,,46,],,,056,],,,0B1,],,,33,],),{,},},Class,_,:,F,{,},<EOF>''',
                101
            )
        )

    def test_1131(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _Bm:L{}Class _{n(q:Array [Int ,0x20];J:i){}Destructor (){Break ;}Constructor (E,_,T,f:Array [Boolean ,047]){} }Class _{$9(__:String ;W,O,V2,l0:_){} }''',
                '''Class,_Bm,:,L,{,},Class,_,{,n,(,q,:,Array,[,Int,,,0x20,],;,J,:,i,),{,},Destructor,(,),{,Break,;,},Constructor,(,E,,,_,,,T,,,f,:,Array,[,Boolean,,,047,],),{,},},Class,_,{,$9,(,__,:,String,;,W,,,O,,,V2,,,l0,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_1132(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _Q_h:q{Constructor (_,_,_4:Array [Array [String ,0B11000],0b1];W,_:Array [String ,2_240];s36,_,_:Array [Float ,0xF]){Break ;}Constructor (u1__:Float ){}e(_9A_8,_8_,_,r:Array [Array [Array [Array [Boolean ,0XDD8_E_9_E],0130],6],4];_,_,R__,_,__,_X,R:__;N:v;_,__l:Int ;_6:Array [Array [Array [Array [Float ,0x4],0B1],05_1_33],4]){}Val hB__:M;}''',
                '''Class,_Q_h,:,q,{,Constructor,(,_,,,_,,,_4,:,Array,[,Array,[,String,,,0B11000,],,,0b1,],;,W,,,_,:,Array,[,String,,,2240,],;,s36,,,_,,,_,:,Array,[,Float,,,0xF,],),{,Break,;,},Constructor,(,u1__,:,Float,),{,},e,(,_9A_8,,,_8_,,,_,,,r,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0XDD8E9E,],,,0130,],,,6,],,,4,],;,_,,,_,,,R__,,,_,,,__,,,_X,,,R,:,__,;,N,:,v,;,_,,,__l,:,Int,;,_6,:,Array,[,Array,[,Array,[,Array,[,Float,,,0x4,],,,0B1,],,,05133,],,,4,],),{,},Val,hB__,:,M,;,},<EOF>''',
                101
            )
        )

    def test_1133(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _5__v6{$t(){}Var $_nI,$0,e,eaR,$2a:Array [Float ,83_2];Constructor (__,R,__1:Array [Array [Array [Array [Array [Boolean ,0xD_A_D0_A6],07_33],0XC_E1C],0b110110],0X1];__m:_){} }''',
                '''Class,_5__v6,{,$t,(,),{,},Var,$_nI,,,$0,,,e,,,eaR,,,$2a,:,Array,[,Float,,,832,],;,Constructor,(,__,,,R,,,__1,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0xDAD0A6,],,,0733,],,,0XCE1C,],,,0b110110,],,,0X1,],;,__m,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_1134(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:u{Constructor (G:Array [Array [Float ,06_0],64];_n_25:S9_56;H,e593:Float ){}Destructor (){} }Class i{w(){} }''',
                '''Class,_,:,u,{,Constructor,(,G,:,Array,[,Array,[,Float,,,060,],,,64,],;,_n_25,:,S9_56,;,H,,,e593,:,Float,),{,},Destructor,(,),{,},},Class,i,{,w,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1135(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C_0__8:a{}Class R{Constructor (){} }Class J_2__W{}Class _1:f5{z(J,h7,_:Boolean ){} }Class __Z{}Class h_:S{}''',
                '''Class,C_0__8,:,a,{,},Class,R,{,Constructor,(,),{,},},Class,J_2__W,{,},Class,_1,:,f5,{,z,(,J,,,h7,,,_,:,Boolean,),{,},},Class,__Z,{,},Class,h_,:,S,{,},<EOF>''',
                101
            )
        )

    def test_1136(self):
        self.assertTrue(
            TestLexer.test(
                '''Class a:r{$P(_:N;Fs:_;E,_X,_H:x_Kn_;m_4,o,h:__0__){} }Class u{Constructor (_Y___E:y;B,_,R8,__,_:Float ;dB_:Float ;k9_:Int ;_m7:Array [Boolean ,0B1]){} }''',
                '''Class,a,:,r,{,$P,(,_,:,N,;,Fs,:,_,;,E,,,_X,,,_H,:,x_Kn_,;,m_4,,,o,,,h,:,__0__,),{,},},Class,u,{,Constructor,(,_Y___E,:,y,;,B,,,_,,,R8,,,__,,,_,:,Float,;,dB_,:,Float,;,k9_,:,Int,;,_m7,:,Array,[,Boolean,,,0B1,],),{,},},<EOF>''',
                101
            )
        )

    def test_1137(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _800{}Class V{U(_4,R,___4:Array [Boolean ,9]){}Constructor (_9_08wL:Array [Array [Boolean ,0X2_1],2];_,__:String ;_,Yz:Boolean ;ffl_,_8_,_68_,r,C,o,M:e;W,NSJ,X1,_:Boolean ){} }''',
                '''Class,_800,{,},Class,V,{,U,(,_4,,,R,,,___4,:,Array,[,Boolean,,,9,],),{,},Constructor,(,_9_08wL,:,Array,[,Array,[,Boolean,,,0X21,],,,2,],;,_,,,__,:,String,;,_,,,Yz,:,Boolean,;,ffl_,,,_8_,,,_68_,,,r,,,C,,,o,,,M,:,e,;,W,,,NSJ,,,X1,,,_,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_1138(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Val $4:Int ;Constructor (_:_;W:Array [Float ,0B100]){Return ;} }Class p:e3{Val $3,_,$_M5_,$0t:Array [Int ,0X5C];}Class B4_{Var $x:v_;}''',
                '''Class,_,:,_,{,Val,$4,:,Int,;,Constructor,(,_,:,_,;,W,:,Array,[,Float,,,0B100,],),{,Return,;,},},Class,p,:,e3,{,Val,$3,,,_,,,$_M5_,,,$0t,:,Array,[,Int,,,0X5C,],;,},Class,B4_,{,Var,$x,:,v_,;,},<EOF>''',
                101
            )
        )

    def test_1139(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:x{Var Q,$_,$v:String ;Destructor (){} }Class _{}Class _0BXE:_{W41(z,X,_,_,Iz4,_3,m1_F_,_u5:_6_;C8_,G_7,X,J,_:Int ){} }Class y_{}''',
                '''Class,_,:,x,{,Var,Q,,,$_,,,$v,:,String,;,Destructor,(,),{,},},Class,_,{,},Class,_0BXE,:,_,{,W41,(,z,,,X,,,_,,,_,,,Iz4,,,_3,,,m1_F_,,,_u5,:,_6_,;,C8_,,,G_7,,,X,,,J,,,_,:,Int,),{,},},Class,y_,{,},<EOF>''',
                101
            )
        )

    def test_1140(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g{__(_,J,_2_,v:Float ;_:Array [Int ,0b10100];g_:Array [Float ,32];_7v:Array [Array [Boolean ,11],0b10100]){} }Class w{_(_ki_h,_:String ;_,_:Array [Array [Array [Float ,0b10100],5],0X2];j,f:Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,0b10100],0144],01],0144],0144],0144],0B1],32],32];_i,x:Int ){} }''',
                '''Class,g,{,__,(,_,,,J,,,_2_,,,v,:,Float,;,_,:,Array,[,Int,,,0b10100,],;,g_,:,Array,[,Float,,,32,],;,_7v,:,Array,[,Array,[,Boolean,,,11,],,,0b10100,],),{,},},Class,w,{,_,(,_ki_h,,,_,:,String,;,_,,,_,:,Array,[,Array,[,Array,[,Float,,,0b10100,],,,5,],,,0X2,],;,j,,,f,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0b10100,],,,0144,],,,01,],,,0144,],,,0144,],,,0144,],,,0B1,],,,32,],,,32,],;,_i,,,x,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_1141(self):
        self.assertTrue(
            TestLexer.test(
                '''Class fN{}Class __4:V{Var D,w:Array [Array [Boolean ,0X4C],0X4C];Constructor (){} }Class _E:____{}Class __{Var $_:Array [Boolean ,4];Var $Q2w1,$1,$_:Array [Array [Array [String ,0X7_CC],75],75];}''',
                '''Class,fN,{,},Class,__4,:,V,{,Var,D,,,w,:,Array,[,Array,[,Boolean,,,0X4C,],,,0X4C,],;,Constructor,(,),{,},},Class,_E,:,____,{,},Class,__,{,Var,$_,:,Array,[,Boolean,,,4,],;,Var,$Q2w1,,,$1,,,$_,:,Array,[,Array,[,Array,[,String,,,0X7CC,],,,75,],,,75,],;,},<EOF>''',
                101
            )
        )

    def test_1142(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Qd41{}Class _:__A{Val _,$0255,_5_,$4:Boolean ;Var $C:_;}Class _{}Class _:O_{Var W,H:Int ;Var $_:Array [Array [Float ,06_12],100];}''',
                '''Class,Qd41,{,},Class,_,:,__A,{,Val,_,,,$0255,,,_5_,,,$4,:,Boolean,;,Var,$C,:,_,;,},Class,_,{,},Class,_,:,O_,{,Var,W,,,H,:,Int,;,Var,$_,:,Array,[,Array,[,Float,,,0612,],,,100,],;,},<EOF>''',
                101
            )
        )

    def test_1143(self):
        self.assertTrue(
            TestLexer.test(
                '''Class v{Var _:Array [Array [Array [Int ,041],041],0b11011];$5(_z__8d,_,y:Float ;_2:V_;__,_,_:Array [Array [Array [Float ,65],0b1],0b11011];W,o:iYS){Break ;} }Class _:__{}''',
                '''Class,v,{,Var,_,:,Array,[,Array,[,Array,[,Int,,,041,],,,041,],,,0b11011,],;,$5,(,_z__8d,,,_,,,y,:,Float,;,_2,:,V_,;,__,,,_,,,_,:,Array,[,Array,[,Array,[,Float,,,65,],,,0b1,],,,0b11011,],;,W,,,o,:,iYS,),{,Break,;,},},Class,_,:,__,{,},<EOF>''',
                101
            )
        )

    def test_1144(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P_i{Constructor (i_,B:H2_){}Constructor (){}Var $5j,$_,$6:Float ;Destructor (){Var g,_9:Array [Array [Float ,4],0B10_1];Return ;} }Class __:K{}''',
                '''Class,P_i,{,Constructor,(,i_,,,B,:,H2_,),{,},Constructor,(,),{,},Var,$5j,,,$_,,,$6,:,Float,;,Destructor,(,),{,Var,g,,,_9,:,Array,[,Array,[,Float,,,4,],,,0B101,],;,Return,;,},},Class,__,:,K,{,},<EOF>''',
                101
            )
        )

    def test_1145(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Ytk:s34{}Class h_2_{}Class r_:_{$R(_,__21q:_;dc_:__;S_,_,Pbl,dx0,_,H0:Array [Float ,0xA]){qW::$_Q_LV();} }''',
                '''Class,Ytk,:,s34,{,},Class,h_2_,{,},Class,r_,:,_,{,$R,(,_,,,__21q,:,_,;,dc_,:,__,;,S_,,,_,,,Pbl,,,dx0,,,_,,,H0,:,Array,[,Float,,,0xA,],),{,qW,::,$_Q_LV,(,),;,},},<EOF>''',
                101
            )
        )

    def test_1146(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:_71{Constructor (_9_:Boolean ){}Var m__,$6k,$_l,_047:Float ;}Class X_9m{Var $53W,$8_V,$x:Boolean ;}Class h{_(_:_){} }''',
                '''Class,__,:,_71,{,Constructor,(,_9_,:,Boolean,),{,},Var,m__,,,$6k,,,$_l,,,_047,:,Float,;,},Class,X_9m,{,Var,$53W,,,$8_V,,,$x,:,Boolean,;,},Class,h,{,_,(,_,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_1147(self):
        self.assertTrue(
            TestLexer.test(
                '''Class c1_G_0{}Class __4hBS:g{Constructor (_S9,V_:A_;__:Boolean ;v:Array [Float ,0x58];_,_V69,_,HU,_I3k,_:Array [Array [Boolean ,0x58],93];_,W,H7:String ){Continue ;} }Class _{}''',
                '''Class,c1_G_0,{,},Class,__4hBS,:,g,{,Constructor,(,_S9,,,V_,:,A_,;,__,:,Boolean,;,v,:,Array,[,Float,,,0x58,],;,_,,,_V69,,,_,,,HU,,,_I3k,,,_,:,Array,[,Array,[,Boolean,,,0x58,],,,93,],;,_,,,W,,,H7,:,String,),{,Continue,;,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_1148(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J{}Class Z{Constructor (){Val _,G,_9:ET;}$Zi_n(_,Q:Array [Float ,23_8];_:Array [Array [Float ,0xB],0B1];_,__E_:Float ){} }''',
                '''Class,J,{,},Class,Z,{,Constructor,(,),{,Val,_,,,G,,,_9,:,ET,;,},$Zi_n,(,_,,,Q,:,Array,[,Float,,,238,],;,_,:,Array,[,Array,[,Float,,,0xB,],,,0B1,],;,_,,,__E_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_1149(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _1_j5{}Class b8{_(){}Var M,$___C,$A_b,__S:String ;Constructor (){}Constructor (){}Constructor (w,D0_:w_1){} }Class __9:s{Constructor (){Break ;} }Class g_:w{}Class X:_O{}''',
                '''Class,_1_j5,{,},Class,b8,{,_,(,),{,},Var,M,,,$___C,,,$A_b,,,__S,:,String,;,Constructor,(,),{,},Constructor,(,),{,},Constructor,(,w,,,D0_,:,w_1,),{,},},Class,__9,:,s,{,Constructor,(,),{,Break,;,},},Class,g_,:,w,{,},Class,X,:,_O,{,},<EOF>''',
                101
            )
        )

    def test_1150(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q{}Class g{Var $p:Boolean ;Var $_,_,h:_4;Constructor (V_,_1,__,Vd25_U3:Array [Array [Array [Array [Array [String ,0b1101],0XCE],05],0b1101],0B1010101];T:Array [String ,0b1101];_N:P_;i,W:__1_;__x_,W:Boolean ){} }''',
                '''Class,q,{,},Class,g,{,Var,$p,:,Boolean,;,Var,$_,,,_,,,h,:,_4,;,Constructor,(,V_,,,_1,,,__,,,Vd25_U3,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b1101,],,,0XCE,],,,05,],,,0b1101,],,,0B1010101,],;,T,:,Array,[,String,,,0b1101,],;,_N,:,P_,;,i,,,W,:,__1_,;,__x_,,,W,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_1151(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g{$B(_F:y9){}__(b5:_;__,_,__:Boolean ;D4:Array [Array [Array [Array [Int ,0b1],07],68],0b1];_:Boolean ){Break ;Return ;}Y(){}Var $1,$c_s,$W,$9:String ;}Class B8:_{}''',
                '''Class,g,{,$B,(,_F,:,y9,),{,},__,(,b5,:,_,;,__,,,_,,,__,:,Boolean,;,D4,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b1,],,,07,],,,68,],,,0b1,],;,_,:,Boolean,),{,Break,;,Return,;,},Y,(,),{,},Var,$1,,,$c_s,,,$W,,,$9,:,String,;,},Class,B8,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1152(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7:_40{O6(){} }Class _{Val $U:Array [Boolean ,0X38];}Class _:s{Var $_,nI:_;Val Q,o_:z;$34_(C0,_6:v_){} }Class _0p:__{Constructor (od,O:_;_:Int ;_,Y___:___z){} }''',
                '''Class,_7,:,_40,{,O6,(,),{,},},Class,_,{,Val,$U,:,Array,[,Boolean,,,0X38,],;,},Class,_,:,s,{,Var,$_,,,nI,:,_,;,Val,Q,,,o_,:,z,;,$34_,(,C0,,,_6,:,v_,),{,},},Class,_0p,:,__,{,Constructor,(,od,,,O,:,_,;,_,:,Int,;,_,,,Y___,:,___z,),{,},},<EOF>''',
                101
            )
        )

    def test_1153(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o_{Constructor (e,N_2u:Array [Array [Array [Array [Array [Int ,0B1_1_0],0b1],076],0b111],5];z5:Array [Array [Int ,26],0X5_8]){Continue ;} }Class p6_{}Class _1{}Class _:i{$s(_U,I_,ibD7:Array [Array [Float ,0B1],05]){p::$_T();} }''',
                '''Class,o_,{,Constructor,(,e,,,N_2u,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B110,],,,0b1,],,,076,],,,0b111,],,,5,],;,z5,:,Array,[,Array,[,Int,,,26,],,,0X58,],),{,Continue,;,},},Class,p6_,{,},Class,_1,{,},Class,_,:,i,{,$s,(,_U,,,I_,,,ibD7,:,Array,[,Array,[,Float,,,0B1,],,,05,],),{,p,::,$_T,(,),;,},},<EOF>''',
                101
            )
        )

    def test_1154(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_9{}Class KJ_:Y{}Class _633_{$P(m1:Array [Int ,0X8_7_6_A]){}Constructor (_:String ;_m_0,gM5,_,___:_){}U48(){Q5::$_H_();}Val Ue:String ;}''',
                '''Class,_,:,_9,{,},Class,KJ_,:,Y,{,},Class,_633_,{,$P,(,m1,:,Array,[,Int,,,0X876A,],),{,},Constructor,(,_,:,String,;,_m_0,,,gM5,,,_,,,___,:,_,),{,},U48,(,),{,Q5,::,$_H_,(,),;,},Val,Ue,:,String,;,},<EOF>''',
                101
            )
        )

    def test_1155(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{$mHu(eT_Qs_FFv8,J,_,_9R,Y:q;a9_0V:_J;r,X5j:String ;h,_Jw4:_e){}T(_:i9){Break ;}Constructor (){} }''',
                '''Class,__,{,$mHu,(,eT_Qs_FFv8,,,J,,,_,,,_9R,,,Y,:,q,;,a9_0V,:,_J,;,r,,,X5j,:,String,;,h,,,_Jw4,:,_e,),{,},T,(,_,:,i9,),{,Break,;,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1156(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _o:pX2_P_{Var g,$3_,$d,$__:Q_;Constructor (v590__:String ){ {} }}Class jwe_:A2_{}Class _54:_{Var R2K,_,k:_;}Class _{$_(_,I___,_:Array [Boolean ,0b101101]){Array ()._._4_().I5()._86_._();} }''',
                '''Class,_o,:,pX2_P_,{,Var,g,,,$3_,,,$d,,,$__,:,Q_,;,Constructor,(,v590__,:,String,),{,{,},},},Class,jwe_,:,A2_,{,},Class,_54,:,_,{,Var,R2K,,,_,,,k,:,_,;,},Class,_,{,$_,(,_,,,I___,,,_,:,Array,[,Boolean,,,0b101101,],),{,Array,(,),.,_,.,_4_,(,),.,I5,(,),.,_86_,.,_,(,),;,},},<EOF>''',
                101
            )
        )

    def test_1157(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _:M_{Destructor (){}Constructor (){}Constructor (Q:String ;_i,y,T:_w;w_:Array [Array [Float ,060],0x56]){} }Class _{}''',
                '''Class,_,{,},Class,_,:,M_,{,Destructor,(,),{,},Constructor,(,),{,},Constructor,(,Q,:,String,;,_i,,,y,,,T,:,_w,;,w_,:,Array,[,Array,[,Float,,,060,],,,0x56,],),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_1158(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9R{Destructor (){}Constructor (_h,_5,m:Array [Boolean ,012];_4,X,_S__:Boolean ;_:Array [Float ,0X47]){}Destructor (){} }''',
                '''Class,_9R,{,Destructor,(,),{,},Constructor,(,_h,,,_5,,,m,:,Array,[,Boolean,,,012,],;,_4,,,X,,,_S__,:,Boolean,;,_,:,Array,[,Float,,,0X47,],),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1159(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7:V{Val q:Array [Array [Array [Array [Array [Array [String ,9_6_6],0b10111],0X50],0b10111],1],0XB6];Destructor (){} }''',
                '''Class,_7,:,V,{,Val,q,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,966,],,,0b10111,],,,0X50,],,,0b10111,],,,1,],,,0XB6,],;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1160(self):
        self.assertTrue(
            TestLexer.test(
                '''Class x8:_{Var $9,$1y30:Array [Array [String ,8],0b1010000];}Class _:_8p{}Class __:_{Destructor (){Break ;}Constructor (){} }''',
                '''Class,x8,:,_,{,Var,$9,,,$1y30,:,Array,[,Array,[,String,,,8,],,,0b1010000,],;,},Class,_,:,_8p,{,},Class,__,:,_,{,Destructor,(,),{,Break,;,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1161(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:_4{Var $24,U,$N0p3,$7,$7_U,S,W_:Array [String ,0x3B];Var $_3_,$15,V:We_41;}Class P0:_{Destructor (){} }Class w_C{Constructor (q__:G;_:String ;F3,_,_G7:Array [Boolean ,0X4A]){}Destructor (){Continue ;} }''',
                '''Class,__,:,_4,{,Var,$24,,,U,,,$N0p3,,,$7,,,$7_U,,,S,,,W_,:,Array,[,String,,,0x3B,],;,Var,$_3_,,,$15,,,V,:,We_41,;,},Class,P0,:,_,{,Destructor,(,),{,},},Class,w_C,{,Constructor,(,q__,:,G,;,_,:,String,;,F3,,,_,,,_G7,:,Array,[,Boolean,,,0X4A,],),{,},Destructor,(,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_1162(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X:HR{}Class h_{}Class _0E_:_{Var _,_:Array [Array [Array [Float ,0b1_1],29],0xA_3];_B(){} }Class Oe:_e__{}''',
                '''Class,X,:,HR,{,},Class,h_,{,},Class,_0E_,:,_,{,Var,_,,,_,:,Array,[,Array,[,Array,[,Float,,,0b11,],,,29,],,,0xA3,],;,_B,(,),{,},},Class,Oe,:,_e__,{,},<EOF>''',
                101
            )
        )

    def test_1163(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _i{Var $2,J:Array [Array [Float ,0X7],0b1];Constructor (_b1v2___,_,_8:Array [Array [Array [String ,0B11],0X3],6];_:Array [Array [Array [String ,0B1],6],0140];_m,f,C_:String ){} }''',
                '''Class,_i,{,Var,$2,,,J,:,Array,[,Array,[,Float,,,0X7,],,,0b1,],;,Constructor,(,_b1v2___,,,_,,,_8,:,Array,[,Array,[,Array,[,String,,,0B11,],,,0X3,],,,6,],;,_,:,Array,[,Array,[,Array,[,String,,,0B1,],,,6,],,,0140,],;,_m,,,f,,,C_,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_1164(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_8A4{}Class oo2_j3_:_{$P6_j2(){}Val $I7,$_6_,$24_7_:Array [Array [Array [String ,0XA_D_F],06_06_0],04016];}''',
                '''Class,_,:,_8A4,{,},Class,oo2_j3_,:,_,{,$P6_j2,(,),{,},Val,$I7,,,$_6_,,,$24_7_,:,Array,[,Array,[,Array,[,String,,,0XADF,],,,06060,],,,04016,],;,},<EOF>''',
                101
            )
        )

    def test_1165(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class A{Constructor (){}Val e,$_:i_0D;Var $zs0:d5;Constructor (_:Float ;k,_h:Boolean ){} }Class __1:l_{}''',
                '''Class,_,:,_,{,},Class,A,{,Constructor,(,),{,},Val,e,,,$_,:,i_0D,;,Var,$zs0,:,d5,;,Constructor,(,_,:,Float,;,k,,,_h,:,Boolean,),{,},},Class,__1,:,l_,{,},<EOF>''',
                101
            )
        )

    def test_1166(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class kq_:_67{Constructor (){Continue ;{} }}Class ___93915o1:_R{}Class R9z73O{Var _3,$__C3,$0_,S:c__;}''',
                '''Class,_,:,_,{,},Class,kq_,:,_67,{,Constructor,(,),{,Continue,;,{,},},},Class,___93915o1,:,_R,{,},Class,R9z73O,{,Var,_3,,,$__C3,,,$0_,,,S,:,c__,;,},<EOF>''',
                101
            )
        )

    def test_1167(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Nd{Var $7,$1,__,j,__,$_,$_,ut__:Array [Int ,0x90_1];Val $6,$X,$v:Boolean ;Constructor (XK,A3,M:Float ;k,_,S:Boolean ){Continue ;Return ;} }''',
                '''Class,Nd,{,Var,$7,,,$1,,,__,,,j,,,__,,,$_,,,$_,,,ut__,:,Array,[,Int,,,0x901,],;,Val,$6,,,$X,,,$v,:,Boolean,;,Constructor,(,XK,,,A3,,,M,:,Float,;,k,,,_,,,S,:,Boolean,),{,Continue,;,Return,;,},},<EOF>''',
                101
            )
        )

    def test_1168(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{$73(Lk_,__,__s,W,_,p_,g,J,_,h0:Array [Array [Int ,50],51];D:Boolean ){} }Class _z5b_j{Destructor (){Val X,S_,v,Ze_,_:_44;} }''',
                '''Class,__,{,$73,(,Lk_,,,__,,,__s,,,W,,,_,,,p_,,,g,,,J,,,_,,,h0,:,Array,[,Array,[,Int,,,50,],,,51,],;,D,:,Boolean,),{,},},Class,_z5b_j,{,Destructor,(,),{,Val,X,,,S_,,,v,,,Ze_,,,_,:,_44,;,},},<EOF>''',
                101
            )
        )

    def test_1169(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{Val __,$_Eq_6_Z:___8;}Class L_O:sb{O__(_,A:Array [Array [Float ,4],037];_,_,_,D:Int ;M:Array [Array [Int ,0x50],8_1];Xs_:Boolean ;_0r_8E:i;_72:P;D,C:Array [Array [Array [Array [Float ,0B111100],24],0b101000],5_79];__,_7Of:Int ){} }''',
                '''Class,__,{,Val,__,,,$_Eq_6_Z,:,___8,;,},Class,L_O,:,sb,{,O__,(,_,,,A,:,Array,[,Array,[,Float,,,4,],,,037,],;,_,,,_,,,_,,,D,:,Int,;,M,:,Array,[,Array,[,Int,,,0x50,],,,81,],;,Xs_,:,Boolean,;,_0r_8E,:,i,;,_72,:,P,;,D,,,C,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B111100,],,,24,],,,0b101000,],,,579,],;,__,,,_7Of,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_1170(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _y86W{Val $W:Boolean ;}Class W:_{Var $j_0:j_BK;Var $_,$_,$_i_7P,$y,_,d,G:Array [Float ,0b100];}Class _:_{}''',
                '''Class,_y86W,{,Val,$W,:,Boolean,;,},Class,W,:,_,{,Var,$j_0,:,j_BK,;,Var,$_,,,$_,,,$_i_7P,,,$y,,,_,,,d,,,G,:,Array,[,Float,,,0b100,],;,},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1171(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:U{Var W,$_:Array [Array [Array [Array [String ,41],0B1],066],0B1_1];Val $3cSfM7,C1,$_,$93m84r,_,$0,$p,$fg_R,$4,$Z_51,$N:Array [Int ,01];Var $H,$697:Float ;Destructor (){}Constructor (_:Array [Float ,0x14]){} }Class B{}''',
                '''Class,_,:,U,{,Var,W,,,$_,:,Array,[,Array,[,Array,[,Array,[,String,,,41,],,,0B1,],,,066,],,,0B11,],;,Val,$3cSfM7,,,C1,,,$_,,,$93m84r,,,_,,,$0,,,$p,,,$fg_R,,,$4,,,$Z_51,,,$N,:,Array,[,Int,,,01,],;,Var,$H,,,$697,:,Float,;,Destructor,(,),{,},Constructor,(,_,:,Array,[,Float,,,0x14,],),{,},},Class,B,{,},<EOF>''',
                101
            )
        )

    def test_1172(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:Jxa_fd{}Class _:z{}Class A_{Var Nq__,_:Array [Array [Array [Int ,6],0x4C],0b1];Destructor (){ {}Continue ;} }Class _{}Class c{}Class L_{}''',
                '''Class,__,:,Jxa_fd,{,},Class,_,:,z,{,},Class,A_,{,Var,Nq__,,,_,:,Array,[,Array,[,Array,[,Int,,,6,],,,0x4C,],,,0b1,],;,Destructor,(,),{,{,},Continue,;,},},Class,_,{,},Class,c,{,},Class,L_,{,},<EOF>''',
                101
            )
        )

    def test_1173(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y{}Class j{Destructor (){} }Class u{Val $6fO3:E;$R5(f7:Array [Boolean ,0x4C]){}Val zx,_2,__:Array [Array [Boolean ,0B1],4];Destructor (){} }Class s{}''',
                '''Class,y,{,},Class,j,{,Destructor,(,),{,},},Class,u,{,Val,$6fO3,:,E,;,$R5,(,f7,:,Array,[,Boolean,,,0x4C,],),{,},Val,zx,,,_2,,,__,:,Array,[,Array,[,Boolean,,,0B1,],,,4,],;,Destructor,(,),{,},},Class,s,{,},<EOF>''',
                101
            )
        )

    def test_1174(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:h{}Class t_{Var $e:String ;d_(){}Val $8_:Array [Int ,0X6];Var e:String ;Val $o,$5_:Boolean ;Destructor (){}_I8(){} }''',
                '''Class,_,:,h,{,},Class,t_,{,Var,$e,:,String,;,d_,(,),{,},Val,$8_,:,Array,[,Int,,,0X6,],;,Var,e,:,String,;,Val,$o,,,$5_,:,Boolean,;,Destructor,(,),{,},_I8,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1175(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9{}Class T_O{Var C_8b8___:n;Constructor (){_O3v::$q_();}Constructor (_A3_:Array [Array [Array [String ,6_1],0413],81_9]){}Constructor (__A9__:Float ){} }''',
                '''Class,_9,{,},Class,T_O,{,Var,C_8b8___,:,n,;,Constructor,(,),{,_O3v,::,$q_,(,),;,},Constructor,(,_A3_,:,Array,[,Array,[,Array,[,String,,,61,],,,0413,],,,819,],),{,},Constructor,(,__A9__,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_1176(self):
        self.assertTrue(
            TestLexer.test(
                '''Class cS{}Class Z{}Class _n:_{q(hq4y5__x_:Int ;c,_3:Float ){Var Xhe_L7u8:Array [Boolean ,0b1001000];}Constructor (_:_){} }''',
                '''Class,cS,{,},Class,Z,{,},Class,_n,:,_,{,q,(,hq4y5__x_,:,Int,;,c,,,_3,:,Float,),{,Var,Xhe_L7u8,:,Array,[,Boolean,,,0b1001000,],;,},Constructor,(,_,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_1177(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{Constructor (){} }Class w__R90{Constructor (_54:Array [Array [Array [Float ,0B10_01],0xF],32];R8:Boolean ){} }Class Z_{}''',
                '''Class,__,{,Constructor,(,),{,},},Class,w__R90,{,Constructor,(,_54,:,Array,[,Array,[,Array,[,Float,,,0B1001,],,,0xF,],,,32,],;,R8,:,Boolean,),{,},},Class,Z_,{,},<EOF>''',
                101
            )
        )

    def test_1178(self):
        self.assertTrue(
            TestLexer.test(
                '''Class N{Constructor (){Continue ;} }Class h6:hOEfu_7{}Class _x{}Class _:_{}Class e{_4V(t:Array [Int ,020];_:G;_Vu4:Float ;__,j:_;o,z:String ;K:P;c0:Array [Int ,0X5];_:a){}$E(){} }''',
                '''Class,N,{,Constructor,(,),{,Continue,;,},},Class,h6,:,hOEfu_7,{,},Class,_x,{,},Class,_,:,_,{,},Class,e,{,_4V,(,t,:,Array,[,Int,,,020,],;,_,:,G,;,_Vu4,:,Float,;,__,,,j,:,_,;,o,,,z,:,String,;,K,:,P,;,c0,:,Array,[,Int,,,0X5,],;,_,:,a,),{,},$E,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1179(self):
        self.assertTrue(
            TestLexer.test(
                '''Class z_0:q{}Class _4q:_{Constructor (__:gF;Y,_OG:__;m,_F_:Array [Int ,0x2];_:Array [String ,95];_,_,_2v:Array [String ,0xD]){} }''',
                '''Class,z_0,:,q,{,},Class,_4q,:,_,{,Constructor,(,__,:,gF,;,Y,,,_OG,:,__,;,m,,,_F_,:,Array,[,Int,,,0x2,],;,_,:,Array,[,String,,,95,],;,_,,,_,,,_2v,:,Array,[,String,,,0xD,],),{,},},<EOF>''',
                101
            )
        )

    def test_1180(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Z:_{}Class m_nuF9:O8_{Val $_,$i:Array [Array [Array [Array [Array [Array [Int ,04],07],5_6_2],03_5_3_326],04],0B100110];}''',
                '''Class,Z,:,_,{,},Class,m_nuF9,:,O8_,{,Val,$_,,,$i,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,04,],,,07,],,,562,],,,0353326,],,,04,],,,0B100110,],;,},<EOF>''',
                101
            )
        )

    def test_1181(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Destructor (){Continue ;Continue ;o9_::$c2_._();}Val v,_GZ8_X30,$MK,$W:Array [Array [Boolean ,88],88];}''',
                '''Class,_,:,_,{,Destructor,(,),{,Continue,;,Continue,;,o9_,::,$c2_,.,_,(,),;,},Val,v,,,_GZ8_X30,,,$MK,,,$W,:,Array,[,Array,[,Boolean,,,88,],,,88,],;,},<EOF>''',
                101
            )
        )

    def test_1182(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:bC{PM9(){}__(){} }Class W:__6G{Var p4i__,$cb_,$N:Array [Array [Array [Array [Float ,0X2],0XB9],0x4D],3_5_1_7];}''',
                '''Class,_,:,bC,{,PM9,(,),{,},__,(,),{,},},Class,W,:,__6G,{,Var,p4i__,,,$cb_,,,$N,:,Array,[,Array,[,Array,[,Array,[,Float,,,0X2,],,,0XB9,],,,0x4D,],,,3517,],;,},<EOF>''',
                101
            )
        )

    def test_1183(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ____87{}Class D{Constructor (i,f1_aa,T:Int ;m,_1,B:Array [Int ,86];F:String ;s,_:Array [Array [Array [Array [Int ,0B1110],06],0X64],0B1]){}Destructor (){ {Break ;} }}''',
                '''Class,____87,{,},Class,D,{,Constructor,(,i,,,f1_aa,,,T,:,Int,;,m,,,_1,,,B,:,Array,[,Int,,,86,],;,F,:,String,;,s,,,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0B1110,],,,06,],,,0X64,],,,0B1,],),{,},Destructor,(,),{,{,Break,;,},},},<EOF>''',
                101
            )
        )

    def test_1184(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __0:_2_{$1(X,_____:Array [Array [Float ,0b1011101],0b1011101];o:_){}Constructor (d,_E,_,__:__t_w;_,_67,__,P:String ){} }''',
                '''Class,__0,:,_2_,{,$1,(,X,,,_____,:,Array,[,Array,[,Float,,,0b1011101,],,,0b1011101,],;,o,:,_,),{,},Constructor,(,d,,,_E,,,_,,,__,:,__t_w,;,_,,,_67,,,__,,,P,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_1185(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Hq:p{Var _:Array [Float ,0B1];}Class B_{Val $_,s:Array [String ,0b1010];Constructor (b:__;Z,h:_6;nz:Float ;x_c:Int ){}Var $__B_,$An,$4_,$Z4,SxsPfb__6:_;$_(_H,__:Int ;r_,j,_,N,_,h:Int ;Bf9y:___){Continue ;} }''',
                '''Class,Hq,:,p,{,Var,_,:,Array,[,Float,,,0B1,],;,},Class,B_,{,Val,$_,,,s,:,Array,[,String,,,0b1010,],;,Constructor,(,b,:,__,;,Z,,,h,:,_6,;,nz,:,Float,;,x_c,:,Int,),{,},Var,$__B_,,,$An,,,$4_,,,$Z4,,,SxsPfb__6,:,_,;,$_,(,_H,,,__,:,Int,;,r_,,,j,,,_,,,N,,,_,,,h,:,Int,;,Bf9y,:,___,),{,Continue,;,},},<EOF>''',
                101
            )
        )

    def test_1186(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class N{$5(__,w:Array [Array [String ,0b11101],026];dg3:_gy;b:Array [Array [Array [Int ,0x2],05_7_0],65];s,_:Array [Float ,65]){}Destructor (){Break ;}Val $__,$__:String ;}''',
                '''Class,__,{,},Class,N,{,$5,(,__,,,w,:,Array,[,Array,[,String,,,0b11101,],,,026,],;,dg3,:,_gy,;,b,:,Array,[,Array,[,Array,[,Int,,,0x2,],,,0570,],,,65,],;,s,,,_,:,Array,[,Float,,,65,],),{,},Destructor,(,),{,Break,;,},Val,$__,,,$__,:,String,;,},<EOF>''',
                101
            )
        )

    def test_1187(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Ty{Var $bq_h:Int ;Val I:Float ;Val $nv:Array [Array [Float ,7_95_28],0X14];$_(Pk,_,_2Q29_:Array [Int ,0X14]){} }''',
                '''Class,Ty,{,Var,$bq_h,:,Int,;,Val,I,:,Float,;,Val,$nv,:,Array,[,Array,[,Float,,,79528,],,,0X14,],;,$_,(,Pk,,,_,,,_2Q29_,:,Array,[,Int,,,0X14,],),{,},},<EOF>''',
                101
            )
        )

    def test_1188(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _q{Var $87,$d1_:_;Var _E,__d_q8,n,NcT_,_,R,qA:Array [Array [Boolean ,0x5D_4_F8],0b1001111];Var $6:Array [Int ,5];}''',
                '''Class,_q,{,Var,$87,,,$d1_,:,_,;,Var,_E,,,__d_q8,,,n,,,NcT_,,,_,,,R,,,qA,:,Array,[,Array,[,Boolean,,,0x5D4F8,],,,0b1001111,],;,Var,$6,:,Array,[,Int,,,5,],;,},<EOF>''',
                101
            )
        )

    def test_1189(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n{Constructor (){} }Class rne_:_{Destructor (){}Var I,$3_,Fv_:_J;Var $_7,K:i_J;Val $3_,g:Array [Float ,0B1];}''',
                '''Class,n,{,Constructor,(,),{,},},Class,rne_,:,_,{,Destructor,(,),{,},Var,I,,,$3_,,,Fv_,:,_J,;,Var,$_7,,,K,:,i_J,;,Val,$3_,,,g,:,Array,[,Float,,,0B1,],;,},<EOF>''',
                101
            )
        )

    def test_1190(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __X{}Class __:_{}Class C6_:_0{Val W,$g:d;Var Y_t:Array [Array [Array [Array [Array [Array [Int ,0xD],3_8],1],03],03],0X2];}''',
                '''Class,__X,{,},Class,__,:,_,{,},Class,C6_,:,_0,{,Val,W,,,$g,:,d,;,Var,Y_t,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0xD,],,,38,],,,1,],,,03,],,,03,],,,0X2,],;,},<EOF>''',
                101
            )
        )

    def test_1191(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _392_:ZL{}Class h{$__(_9MZ8_8:v;_:Array [Array [String ,04],0B100010];_d:Boolean ;MH,_M,P4t_7,o2_N03:Array [Array [Int ,633],18]){} }''',
                '''Class,_392_,:,ZL,{,},Class,h,{,$__,(,_9MZ8_8,:,v,;,_,:,Array,[,Array,[,String,,,04,],,,0B100010,],;,_d,:,Boolean,;,MH,,,_M,,,P4t_7,,,o2_N03,:,Array,[,Array,[,Int,,,633,],,,18,],),{,},},<EOF>''',
                101
            )
        )

    def test_1192(self):
        self.assertTrue(
            TestLexer.test(
                '''Class a_{}Class _{}Class _1X{Constructor (_,f_904:Array [Boolean ,0136];_:Boolean ){Continue ;Break ;Break ;{} }Destructor (){} }Class _c___B{}Class _:___{}''',
                '''Class,a_,{,},Class,_,{,},Class,_1X,{,Constructor,(,_,,,f_904,:,Array,[,Boolean,,,0136,],;,_,:,Boolean,),{,Continue,;,Break,;,Break,;,{,},},Destructor,(,),{,},},Class,_c___B,{,},Class,_,:,___,{,},<EOF>''',
                101
            )
        )

    def test_1193(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8g:V{Constructor (_729:Array [Array [Array [Array [Array [String ,0b1],0b1],0x3_2],3_8_63_3],02]){}Var _v,cc,$_:Array [Array [Array [Float ,0X1_C_1],042],0B1000000];}''',
                '''Class,_8g,:,V,{,Constructor,(,_729,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b1,],,,0b1,],,,0x32,],,,38633,],,,02,],),{,},Var,_v,,,cc,,,$_,:,Array,[,Array,[,Array,[,Float,,,0X1C1,],,,042,],,,0B1000000,],;,},<EOF>''',
                101
            )
        )

    def test_1194(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:U{}Class C:_{}Class H_52{}Class u_F{}Class k{Val $_1:Float ;Destructor (){} }Class _:t_{Constructor (){__::$H_();Continue ;Continue ;}Destructor (){Break ;} }''',
                '''Class,_,:,U,{,},Class,C,:,_,{,},Class,H_52,{,},Class,u_F,{,},Class,k,{,Val,$_1,:,Float,;,Destructor,(,),{,},},Class,_,:,t_,{,Constructor,(,),{,__,::,$H_,(,),;,Continue,;,Continue,;,},Destructor,(,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_1195(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{$_5(X,_,An,_8a3_088,__:_T_;dK65,_:Array [Array [Int ,0X4],0b10100];__e,KA:Float ){} }Class X:_{}Class H5{}''',
                '''Class,_,:,_,{,$_5,(,X,,,_,,,An,,,_8a3_088,,,__,:,_T_,;,dK65,,,_,:,Array,[,Array,[,Int,,,0X4,],,,0b10100,],;,__e,,,KA,:,Float,),{,},},Class,X,:,_,{,},Class,H5,{,},<EOF>''',
                101
            )
        )

    def test_1196(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _B:J_{Destructor (){Return ;}Constructor (k9F:String ;rLE_1:_4){} }Class HG:xC{Var Z:Array [Array [Int ,0b1],0b1_0];}''',
                '''Class,_B,:,J_,{,Destructor,(,),{,Return,;,},Constructor,(,k9F,:,String,;,rLE_1,:,_4,),{,},},Class,HG,:,xC,{,Var,Z,:,Array,[,Array,[,Int,,,0b1,],,,0b10,],;,},<EOF>''',
                101
            )
        )

    def test_1197(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ______:__{_(p3_2:Array [Array [Array [Array [Float ,49],02],7],2];M0,k__:Array [Boolean ,49]){} }Class u8{}''',
                '''Class,______,:,__,{,_,(,p3_2,:,Array,[,Array,[,Array,[,Array,[,Float,,,49,],,,02,],,,7,],,,2,],;,M0,,,k__,:,Array,[,Boolean,,,49,],),{,},},Class,u8,{,},<EOF>''',
                101
            )
        )

    def test_1198(self):
        self.assertTrue(
            TestLexer.test(
                '''Class S:_{Var $8:Array [Float ,0X25];F2r(){Continue ;Break ;Val h:Array [Array [Array [String ,0x1],2],0b1_1_0_1100];} }''',
                '''Class,S,:,_,{,Var,$8,:,Array,[,Float,,,0X25,],;,F2r,(,),{,Continue,;,Break,;,Val,h,:,Array,[,Array,[,Array,[,String,,,0x1,],,,2,],,,0b1101100,],;,},},<EOF>''',
                101
            )
        )

    def test_1199(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0:AVxv{}Class EI:O9___{Constructor (n__:W6C;b:Array [Array [Array [Float ,34],054_1],0X8]){}Val $fax,$_,$_0uD:Int ;Constructor (_b:Bj){}Destructor (){} }Class __4h:_{}''',
                '''Class,_0,:,AVxv,{,},Class,EI,:,O9___,{,Constructor,(,n__,:,W6C,;,b,:,Array,[,Array,[,Array,[,Float,,,34,],,,0541,],,,0X8,],),{,},Val,$fax,,,$_,,,$_0uD,:,Int,;,Constructor,(,_b,:,Bj,),{,},Destructor,(,),{,},},Class,__4h,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1200(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ld:W{}Class _W:_{}Class R:_{}Class Lfq:G{Var $94:Array [Array [Float ,23],0b10110];}Class _Y{Val $0,$RE,$_91339,$4:O;}''',
                '''Class,ld,:,W,{,},Class,_W,:,_,{,},Class,R,:,_,{,},Class,Lfq,:,G,{,Var,$94,:,Array,[,Array,[,Float,,,23,],,,0b10110,],;,},Class,_Y,{,Val,$0,,,$RE,,,$_91339,,,$4,:,O,;,},<EOF>''',
                101
            )
        )

    def test_1201(self):
        self.assertTrue(
            TestLexer.test(
                '''Class uu_{}Class N6e{R(F_5_,_e27:SO;S0:Float ;V,_,e:Int ;_9,_:Array [Array [Int ,0B111001],0x56];Zc:Array [Boolean ,051]){} }Class i:z{}Class c:u10{}''',
                '''Class,uu_,{,},Class,N6e,{,R,(,F_5_,,,_e27,:,SO,;,S0,:,Float,;,V,,,_,,,e,:,Int,;,_9,,,_,:,Array,[,Array,[,Int,,,0B111001,],,,0x56,],;,Zc,:,Array,[,Boolean,,,051,],),{,},},Class,i,:,z,{,},Class,c,:,u10,{,},<EOF>''',
                101
            )
        )

    def test_1202(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $6:Boolean ;$_(_:Array [Array [Boolean ,04],0b101000];_2r:Array [String ,014_75_2];I8_:__;n__0_K2:_){Val _:Array [Array [Array [Array [Array [Int ,052],052],37_2_8_7],28],0x42]=!_d_::$e.__0;{}Break ;} }''',
                '''Class,_,{,Val,$6,:,Boolean,;,$_,(,_,:,Array,[,Array,[,Boolean,,,04,],,,0b101000,],;,_2r,:,Array,[,String,,,014752,],;,I8_,:,__,;,n__0_K2,:,_,),{,Val,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,052,],,,052,],,,37287,],,,28,],,,0x42,],=,!,_d_,::,$e,.,__0,;,{,},Break,;,},},<EOF>''',
                101
            )
        )

    def test_1203(self):
        self.assertTrue(
            TestLexer.test(
                '''Class x37{Val $99:String ;}Class c:_U73{}Class _3:P{T0(){Break ;}Destructor (){} }Class T{Val _p7,_,_,G3__:Array [Array [Boolean ,0x2],0X4];Var $_,$cls:Int ;_1__(){} }''',
                '''Class,x37,{,Val,$99,:,String,;,},Class,c,:,_U73,{,},Class,_3,:,P,{,T0,(,),{,Break,;,},Destructor,(,),{,},},Class,T,{,Val,_p7,,,_,,,_,,,G3__,:,Array,[,Array,[,Boolean,,,0x2,],,,0X4,],;,Var,$_,,,$cls,:,Int,;,_1__,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1204(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Q{Constructor (_,Mh,Fz,_:Array [Array [Array [Boolean ,06],0x11],0X53]){}Var _m,_,$x,t,$_,$o,Va:Array [Array [Array [Array [Float ,0B101010],0b1],16],0b1];}Class _7_{}Class u:f_{}Class _A:s{}''',
                '''Class,Q,{,Constructor,(,_,,,Mh,,,Fz,,,_,:,Array,[,Array,[,Array,[,Boolean,,,06,],,,0x11,],,,0X53,],),{,},Var,_m,,,_,,,$x,,,t,,,$_,,,$o,,,Va,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B101010,],,,0b1,],,,16,],,,0b1,],;,},Class,_7_,{,},Class,u,:,f_,{,},Class,_A,:,s,{,},<EOF>''',
                101
            )
        )

    def test_1205(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T:n{}Class e{$XTS(IU__4n,_hB:_s;F_mn_:Y;_e,__E:Array [Array [Float ,7],0X60];_5:_){}$4(wJo_:String ){} }Class n7{}''',
                '''Class,T,:,n,{,},Class,e,{,$XTS,(,IU__4n,,,_hB,:,_s,;,F_mn_,:,Y,;,_e,,,__E,:,Array,[,Array,[,Float,,,7,],,,0X60,],;,_5,:,_,),{,},$4,(,wJo_,:,String,),{,},},Class,n7,{,},<EOF>''',
                101
            )
        )

    def test_1206(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val c:Array [Array [Array [Array [Array [String ,0x34],0B1],0b100100],0b100100],0X7];}Class __{}Class o:j__{}Class k1hi:t_{}''',
                '''Class,_,{,Val,c,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0x34,],,,0B1,],,,0b100100,],,,0b100100,],,,0X7,],;,},Class,__,{,},Class,o,:,j__,{,},Class,k1hi,:,t_,{,},<EOF>''',
                101
            )
        )

    def test_1207(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _u{Val _:Float ;}Class O__{}Class ry:xu3{Var $1:Array [Array [Array [Boolean ,72],13],0b11001];}Class s{Destructor (){} }''',
                '''Class,_u,{,Val,_,:,Float,;,},Class,O__,{,},Class,ry,:,xu3,{,Var,$1,:,Array,[,Array,[,Array,[,Boolean,,,72,],,,13,],,,0b11001,],;,},Class,s,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1208(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k_n{_(){Break ;{Return ;} }}Class p{Val $g,$w:S;Constructor (){Continue ;}Constructor (V,_:Float ){} }Class S_:P{}''',
                '''Class,k_n,{,_,(,),{,Break,;,{,Return,;,},},},Class,p,{,Val,$g,,,$w,:,S,;,Constructor,(,),{,Continue,;,},Constructor,(,V,,,_,:,Float,),{,},},Class,S_,:,P,{,},<EOF>''',
                101
            )
        )

    def test_1209(self):
        self.assertTrue(
            TestLexer.test(
                '''Class DE__lP:l4{Destructor (){}o(__5:S1;_,y:_8f;_,_,_:T6;L5:Boolean ;__:_16){} }Class F:p{Val _:Array [Boolean ,70];}''',
                '''Class,DE__lP,:,l4,{,Destructor,(,),{,},o,(,__5,:,S1,;,_,,,y,:,_8f,;,_,,,_,,,_,:,T6,;,L5,:,Boolean,;,__,:,_16,),{,},},Class,F,:,p,{,Val,_,:,Array,[,Boolean,,,70,],;,},<EOF>''',
                101
            )
        )

    def test_1210(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $0,Ca:Array [String ,02];}Class __j:_80_g{}Class Z:_x{Constructor (){}Val $4__,_,$5uk,$i__9,F_1,_2_:v_;}Class J:_0_R{}''',
                '''Class,_,{,Val,$0,,,Ca,:,Array,[,String,,,02,],;,},Class,__j,:,_80_g,{,},Class,Z,:,_x,{,Constructor,(,),{,},Val,$4__,,,_,,,$5uk,,,$i__9,,,F_1,,,_2_,:,v_,;,},Class,J,:,_0_R,{,},<EOF>''',
                101
            )
        )

    def test_1211(self):
        self.assertTrue(
            TestLexer.test(
                '''Class fAc_:_{}Class u:__{Destructor (){}Val Z_W,$I:_S;}Class j{}Class L__:F0{Var _T:Array [Boolean ,100];}Class f{Val $7:D;Destructor (){} }''',
                '''Class,fAc_,:,_,{,},Class,u,:,__,{,Destructor,(,),{,},Val,Z_W,,,$I,:,_S,;,},Class,j,{,},Class,L__,:,F0,{,Var,_T,:,Array,[,Boolean,,,100,],;,},Class,f,{,Val,$7,:,D,;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1212(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class _7_8:VU{}Class V_s_{}Class __:_T{}Class o__{Constructor (){}Constructor (){} }Class y:_{}Class D:_{}Class f{$U(T:Array [String ,88]){} }''',
                '''Class,_,:,_,{,},Class,_7_8,:,VU,{,},Class,V_s_,{,},Class,__,:,_T,{,},Class,o__,{,Constructor,(,),{,},Constructor,(,),{,},},Class,y,:,_,{,},Class,D,:,_,{,},Class,f,{,$U,(,T,:,Array,[,String,,,88,],),{,},},<EOF>''',
                101
            )
        )

    def test_1213(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _Fp:q___{Destructor (){}y2(){} }Class n:__0b{Var $81_,A:Int ;Var $8_:Int ;Val _k:Array [Array [Boolean ,2],0B11];}''',
                '''Class,_Fp,:,q___,{,Destructor,(,),{,},y2,(,),{,},},Class,n,:,__0b,{,Var,$81_,,,A,:,Int,;,Var,$8_,:,Int,;,Val,_k,:,Array,[,Array,[,Boolean,,,2,],,,0B11,],;,},<EOF>''',
                101
            )
        )

    def test_1214(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _PE{____V(_0H038U:Array [Array [Array [Boolean ,0171],5_2],0x9];tz9u:Array [Array [Float ,9],79];o:B9;t058:Array [Array [Int ,79],5_9]){}_(){Var bZ_:Array [Array [Array [Array [Array [Boolean ,0x5],04],0X9],79],06_66];}I(){}Val $_,$__8QgD:Array [Boolean ,0b11];}Class _J18{}''',
                '''Class,_PE,{,____V,(,_0H038U,:,Array,[,Array,[,Array,[,Boolean,,,0171,],,,52,],,,0x9,],;,tz9u,:,Array,[,Array,[,Float,,,9,],,,79,],;,o,:,B9,;,t058,:,Array,[,Array,[,Int,,,79,],,,59,],),{,},_,(,),{,Var,bZ_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x5,],,,04,],,,0X9,],,,79,],,,0666,],;,},I,(,),{,},Val,$_,,,$__8QgD,:,Array,[,Boolean,,,0b11,],;,},Class,_J18,{,},<EOF>''',
                101
            )
        )

    def test_1215(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Destructor (){Continue ;}$_(E_:Boolean ;_:String ;_:Array [Array [Array [Float ,4],077],0B1];_:pyMh;_,S_,Dpi_4,sw0,H,FA_:String ;_,_A__:Boolean ){Continue ;{}Continue ;} }''',
                '''Class,_,{,Destructor,(,),{,Continue,;,},$_,(,E_,:,Boolean,;,_,:,String,;,_,:,Array,[,Array,[,Array,[,Float,,,4,],,,077,],,,0B1,],;,_,:,pyMh,;,_,,,S_,,,Dpi_4,,,sw0,,,H,,,FA_,:,String,;,_,,,_A__,:,Boolean,),{,Continue,;,{,},Continue,;,},},<EOF>''',
                101
            )
        )

    def test_1216(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:n{}Class n4:_z{}Class U:_{_7(){} }Class E:c{}Class _7:h{Constructor (_,h:Array [Array [Boolean ,0x44],023]){}Val $G:_;}''',
                '''Class,_,:,n,{,},Class,n4,:,_z,{,},Class,U,:,_,{,_7,(,),{,},},Class,E,:,c,{,},Class,_7,:,h,{,Constructor,(,_,,,h,:,Array,[,Array,[,Boolean,,,0x44,],,,023,],),{,},Val,$G,:,_,;,},<EOF>''',
                101
            )
        )

    def test_1217(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _x{Var $j,$_,_:_5u_;Val $3,_:Array [Array [Array [Array [Array [Boolean ,0b11_1_1],031],0234_0],12],0B1];Destructor (){} }Class _:p{}Class T_:iS_7{}''',
                '''Class,_x,{,Var,$j,,,$_,,,_,:,_5u_,;,Val,$3,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1111,],,,031,],,,02340,],,,12,],,,0B1,],;,Destructor,(,),{,},},Class,_,:,p,{,},Class,T_,:,iS_7,{,},<EOF>''',
                101
            )
        )

    def test_1218(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _2_:_{}Class r_{Destructor (){}Constructor (_p:Int ;_:Array [Array [Float ,03_4],42];iD:Array [Boolean ,0x7];Z57S_,_Y:yO_){}$2(o,N,_,pk,I,_:Array [Array [String ,0b1],0x4A]){} }''',
                '''Class,_2_,:,_,{,},Class,r_,{,Destructor,(,),{,},Constructor,(,_p,:,Int,;,_,:,Array,[,Array,[,Float,,,034,],,,42,],;,iD,:,Array,[,Boolean,,,0x7,],;,Z57S_,,,_Y,:,yO_,),{,},$2,(,o,,,N,,,_,,,pk,,,I,,,_,:,Array,[,Array,[,String,,,0b1,],,,0x4A,],),{,},},<EOF>''',
                101
            )
        )

    def test_1219(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_a_4_{}Class q:D{Val C:String ;}Class _:_P_U{Constructor (_,_4__,N:Array [Array [Float ,0b10001],05]){} }Class _{}''',
                '''Class,_,:,_a_4_,{,},Class,q,:,D,{,Val,C,:,String,;,},Class,_,:,_P_U,{,Constructor,(,_,,,_4__,,,N,:,Array,[,Array,[,Float,,,0b10001,],,,05,],),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_1220(self):
        self.assertTrue(
            TestLexer.test(
                '''Class j:meE_{Constructor (_g8_8,q_:Array [Array [String ,0X2_9_95_FB],4];B:Array [Array [Array [Array [Array [Array [Array [Int ,83],83],0x31],07_5_1],0B111101],4],6_5]){Return ;}Destructor (){_::$x.W_3_.___.__.AQ()._97_();}Var $7,$I:Array [Array [Array [Array [Array [Int ,0x31],0x2A],0101],0101],0b1_111];}''',
                '''Class,j,:,meE_,{,Constructor,(,_g8_8,,,q_,:,Array,[,Array,[,String,,,0X2995FB,],,,4,],;,B,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,83,],,,83,],,,0x31,],,,0751,],,,0B111101,],,,4,],,,65,],),{,Return,;,},Destructor,(,),{,_,::,$x,.,W_3_,.,___,.,__,.,AQ,(,),.,_97_,(,),;,},Var,$7,,,$I,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x31,],,,0x2A,],,,0101,],,,0101,],,,0b1111,],;,},<EOF>''',
                101
            )
        )

    def test_1221(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y11:k_{Constructor (H3,_:Array [Boolean ,05];_990,L:String ;_40,O__:String ){}Var $Gd_,$_:Array [Float ,8_70];}''',
                '''Class,y11,:,k_,{,Constructor,(,H3,,,_,:,Array,[,Boolean,,,05,],;,_990,,,L,:,String,;,_40,,,O__,:,String,),{,},Var,$Gd_,,,$_,:,Array,[,Float,,,870,],;,},<EOF>''',
                101
            )
        )

    def test_1222(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _r1w_{Destructor (){}$gS9K(q:sg;_9,_Y_,__,Cv4_4:Array [Array [Array [String ,3],0XE7],0B1_1_0];__,_:Boolean ){}Constructor (){}Var $7_,$6:Float ;}Class S{Val $I24,$96772_:Array [Array [Array [Float ,036],036],0B101];}''',
                '''Class,_r1w_,{,Destructor,(,),{,},$gS9K,(,q,:,sg,;,_9,,,_Y_,,,__,,,Cv4_4,:,Array,[,Array,[,Array,[,String,,,3,],,,0XE7,],,,0B110,],;,__,,,_,:,Boolean,),{,},Constructor,(,),{,},Var,$7_,,,$6,:,Float,;,},Class,S,{,Val,$I24,,,$96772_,:,Array,[,Array,[,Array,[,Float,,,036,],,,036,],,,0B101,],;,},<EOF>''',
                101
            )
        )

    def test_1223(self):
        self.assertTrue(
            TestLexer.test(
                '''Class u{Constructor (){R::$x();Break ;}Var d:_;Constructor (T2_:String ){}Destructor (){}Val _,L8,_0_:b;Constructor (j:Int ;_,_:Array [Array [Array [Array [Array [Array [Array [Boolean ,0B100011],0X38],0b1],0XBCC3],87],8],075];q0_U0:Array [Array [Array [Array [Boolean ,075],0b1],0b10],01_1];_o:p3;_O:Int ){}Val __,S,$_m,$4,G:Boolean ;}''',
                '''Class,u,{,Constructor,(,),{,R,::,$x,(,),;,Break,;,},Var,d,:,_,;,Constructor,(,T2_,:,String,),{,},Destructor,(,),{,},Val,_,,,L8,,,_0_,:,b,;,Constructor,(,j,:,Int,;,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B100011,],,,0X38,],,,0b1,],,,0XBCC3,],,,87,],,,8,],,,075,],;,q0_U0,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,075,],,,0b1,],,,0b10,],,,011,],;,_o,:,p3,;,_O,:,Int,),{,},Val,__,,,S,,,$_m,,,$4,,,G,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_1224(self):
        self.assertTrue(
            TestLexer.test(
                '''Class M5O{}Class I{}Class _{Var $_,$F5,q_r,$__,H:Int ;Var $f:String ;Constructor (){}Destructor (){} }Class __{Constructor (_:Array [Array [Float ,035],0b1110]){} }Class _:_903M{}Class i_D{Constructor (K,_,_b:_3_){Continue ;Continue ;} }Class f__3{Constructor (){} }Class O_:_{}''',
                '''Class,M5O,{,},Class,I,{,},Class,_,{,Var,$_,,,$F5,,,q_r,,,$__,,,H,:,Int,;,Var,$f,:,String,;,Constructor,(,),{,},Destructor,(,),{,},},Class,__,{,Constructor,(,_,:,Array,[,Array,[,Float,,,035,],,,0b1110,],),{,},},Class,_,:,_903M,{,},Class,i_D,{,Constructor,(,K,,,_,,,_b,:,_3_,),{,Continue,;,Continue,;,},},Class,f__3,{,Constructor,(,),{,},},Class,O_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1225(self):
        self.assertTrue(
            TestLexer.test(
                '''Class q_O:CL{Constructor (g,E_,_59_,I,N__3X:Boolean ;_,eQ:_;__,_3_B0,H:Array [String ,1];nF5,kv,_,e4Kjg6_70:Int ){} }''',
                '''Class,q_O,:,CL,{,Constructor,(,g,,,E_,,,_59_,,,I,,,N__3X,:,Boolean,;,_,,,eQ,:,_,;,__,,,_3_B0,,,H,:,Array,[,String,,,1,],;,nF5,,,kv,,,_,,,e4Kjg6_70,:,Int,),{,},},<EOF>''',
                101
            )
        )

    def test_1226(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Constructor (V:Array [Array [Array [Array [Float ,0B1001111],0x5B],6],056];D:Array [Array [Array [Float ,017],0X25_C_8],0XE_A];_gw,K_3,_a,f,_O,_,_e5_:b0;kU,_:Array [Array [Float ,056],0x1];O,__,B,J_3:Array [Int ,0b1]){} }''',
                '''Class,_,:,_,{,Constructor,(,V,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B1001111,],,,0x5B,],,,6,],,,056,],;,D,:,Array,[,Array,[,Array,[,Float,,,017,],,,0X25C8,],,,0XEA,],;,_gw,,,K_3,,,_a,,,f,,,_O,,,_,,,_e5_,:,b0,;,kU,,,_,:,Array,[,Array,[,Float,,,056,],,,0x1,],;,O,,,__,,,B,,,J_3,:,Array,[,Int,,,0b1,],),{,},},<EOF>''',
                101
            )
        )

    def test_1227(self):
        self.assertTrue(
            TestLexer.test(
                '''Class D2:_7{$1_(){}Constructor (__rV11:Array [Array [Array [Float ,5],0b1100],0b100];_N,_:Array [Float ,0x51];l_,f,_3:Float ;F:String ){}Destructor (){} }''',
                '''Class,D2,:,_7,{,$1_,(,),{,},Constructor,(,__rV11,:,Array,[,Array,[,Array,[,Float,,,5,],,,0b1100,],,,0b100,],;,_N,,,_,:,Array,[,Float,,,0x51,],;,l_,,,f,,,_3,:,Float,;,F,:,String,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1228(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V:y{Val _,_:t__;Val _:W_01;$3pE(t,__qk:Float ;g_h,__0__Wa_,z:_;_1,_93_EYKam_5_1:Array [String ,0XD_7];m_S,_2_I,sn,_H2_,jML:Boolean ;__:Array [Float ,0B1000111]){ {}Break ;}Destructor (){}Destructor (){} }''',
                '''Class,V,:,y,{,Val,_,,,_,:,t__,;,Val,_,:,W_01,;,$3pE,(,t,,,__qk,:,Float,;,g_h,,,__0__Wa_,,,z,:,_,;,_1,,,_93_EYKam_5_1,:,Array,[,String,,,0XD7,],;,m_S,,,_2_I,,,sn,,,_H2_,,,jML,:,Boolean,;,__,:,Array,[,Float,,,0B1000111,],),{,{,},Break,;,},Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1229(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Constructor (A,__:_){Break ;}Destructor (){}Destructor (){} }Class _{$_4mOS(){ {} }Destructor (){}Constructor (){ {Break ;} }}''',
                '''Class,_,:,_,{,Constructor,(,A,,,__,:,_,),{,Break,;,},Destructor,(,),{,},Destructor,(,),{,},},Class,_,{,$_4mOS,(,),{,{,},},Destructor,(,),{,},Constructor,(,),{,{,Break,;,},},},<EOF>''',
                101
            )
        )

    def test_1230(self):
        self.assertTrue(
            TestLexer.test(
                '''Class c{}Class _:__p_8{Var __:_;Destructor (){} }Class _{Var $U_:Array [Array [Array [Array [Int ,0x7],0105],0xA],02];}''',
                '''Class,c,{,},Class,_,:,__p_8,{,Var,__,:,_,;,Destructor,(,),{,},},Class,_,{,Var,$U_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0x7,],,,0105,],,,0xA,],,,02,],;,},<EOF>''',
                101
            )
        )

    def test_1231(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _3p:_9_R4{Constructor (lS,_1q:Array [Float ,0B1001000];__,__0_:_kT){}Val $20,K,$_,$2j:Array [Int ,0B1001000];Val nuQ_f__y,$W,_:Int ;}''',
                '''Class,_3p,:,_9_R4,{,Constructor,(,lS,,,_1q,:,Array,[,Float,,,0B1001000,],;,__,,,__0_,:,_kT,),{,},Val,$20,,,K,,,$_,,,$2j,:,Array,[,Int,,,0B1001000,],;,Val,nuQ_f__y,,,$W,,,_,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_1232(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _3:C_0_{Var k:Float ;S_8_7(_:Float ;T__,__,_c_,A:Array [Array [Array [Int ,75],067],0B101001];D_,_H_:Array [Array [Boolean ,067],0x4D]){}Val $_1_h,u0,$_:Array [Array [String ,75],0b101100];}''',
                '''Class,_3,:,C_0_,{,Var,k,:,Float,;,S_8_7,(,_,:,Float,;,T__,,,__,,,_c_,,,A,:,Array,[,Array,[,Array,[,Int,,,75,],,,067,],,,0B101001,],;,D_,,,_H_,:,Array,[,Array,[,Boolean,,,067,],,,0x4D,],),{,},Val,$_1_h,,,u0,,,$_,:,Array,[,Array,[,String,,,75,],,,0b101100,],;,},<EOF>''',
                101
            )
        )

    def test_1233(self):
        self.assertTrue(
            TestLexer.test(
                '''Class a:Y{Destructor (){}$5m_j(c_:Array [Array [Float ,6],0B11]){Continue ;} }Class _:_{Var y0,$7_:Boolean ;Val _:Float ;}Class b:B{}''',
                '''Class,a,:,Y,{,Destructor,(,),{,},$5m_j,(,c_,:,Array,[,Array,[,Float,,,6,],,,0B11,],),{,Continue,;,},},Class,_,:,_,{,Var,y0,,,$7_,:,Boolean,;,Val,_,:,Float,;,},Class,b,:,B,{,},<EOF>''',
                101
            )
        )

    def test_1234(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class _{j_U8(){}Val $_Gm5_31f_8:Array [Boolean ,9];$_2(){} }Class J:_{Constructor (){} }Class __0:_4y__{}Class _{Val $_,v9:Array [Int ,0B110101];}''',
                '''Class,__,{,},Class,_,{,j_U8,(,),{,},Val,$_Gm5_31f_8,:,Array,[,Boolean,,,9,],;,$_2,(,),{,},},Class,J,:,_,{,Constructor,(,),{,},},Class,__0,:,_4y__,{,},Class,_,{,Val,$_,,,v9,:,Array,[,Int,,,0B110101,],;,},<EOF>''',
                101
            )
        )

    def test_1235(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{_(___J:Float ;hv,Kb:Array [String ,0x43];_,i,D:Array [String ,010];_T,_e,j3_6:_){} }Class L:_D{}Class _M2:_{}''',
                '''Class,_,{,_,(,___J,:,Float,;,hv,,,Kb,:,Array,[,String,,,0x43,],;,_,,,i,,,D,:,Array,[,String,,,010,],;,_T,,,_e,,,j3_6,:,_,),{,},},Class,L,:,_D,{,},Class,_M2,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1236(self):
        self.assertTrue(
            TestLexer.test(
                '''Class u:M9F{_(_:_Y_;N__2S:Array [Array [Float ,0b1],0x24]){}_(m:Array [Int ,0b10_11]){Continue ;Return ;}Val $91Y,$_,$w:Float ;}Class B:_{}''',
                '''Class,u,:,M9F,{,_,(,_,:,_Y_,;,N__2S,:,Array,[,Array,[,Float,,,0b1,],,,0x24,],),{,},_,(,m,:,Array,[,Int,,,0b1011,],),{,Continue,;,Return,;,},Val,$91Y,,,$_,,,$w,:,Float,;,},Class,B,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1237(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Destructor (){} }Class _{Val jG:Array [Array [Array [Array [Array [Array [Boolean ,067],0B1010010],0X35],5],067],0x4C];Var $d_L_,$1Y94,_a:Array [Float ,0b1000001];Constructor (_,h_:Int ){}Var $89:Boolean ;}''',
                '''Class,_,:,_,{,Destructor,(,),{,},},Class,_,{,Val,jG,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,067,],,,0B1010010,],,,0X35,],,,5,],,,067,],,,0x4C,],;,Var,$d_L_,,,$1Y94,,,_a,:,Array,[,Float,,,0b1000001,],;,Constructor,(,_,,,h_,:,Int,),{,},Var,$89,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_1238(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E{Destructor (){}Constructor (_,k:Boolean ;k:Boolean ;N1a4:Array [Array [Array [Array [Int ,0b1],80],045],0B101001]){} }''',
                '''Class,E,{,Destructor,(,),{,},Constructor,(,_,,,k,:,Boolean,;,k,:,Boolean,;,N1a4,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b1,],,,80,],,,045,],,,0B101001,],),{,},},<EOF>''',
                101
            )
        )

    def test_1239(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J4:_{t(y7_,z:Array [Array [Array [Array [Array [Array [Boolean ,0125],06],0x2A],05_7],1],0x2A];_d1q:Y2ZGD_;S_1:String ;_,j___6:v){} }''',
                '''Class,J4,:,_,{,t,(,y7_,,,z,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0125,],,,06,],,,0x2A,],,,057,],,,1,],,,0x2A,],;,_d1q,:,Y2ZGD_,;,S_1,:,String,;,_,,,j___6,:,v,),{,},},<EOF>''',
                101
            )
        )

    def test_1240(self):
        self.assertTrue(
            TestLexer.test(
                '''Class U:mh{Constructor (t_42m:Int ){Return ;}Destructor (){}Val $_Y_,$_,_Q,$8,O,T,$3,_:Array [Int ,90];}Class s{}''',
                '''Class,U,:,mh,{,Constructor,(,t_42m,:,Int,),{,Return,;,},Destructor,(,),{,},Val,$_Y_,,,$_,,,_Q,,,$8,,,O,,,T,,,$3,,,_,:,Array,[,Int,,,90,],;,},Class,s,{,},<EOF>''',
                101
            )
        )

    def test_1241(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:lN{Val _,wKI:_;V(r,_:Array [Int ,06_4_01_1]){Val _,_:Array [Array [Boolean ,5],0x36];} }Class _:__{}Class ___2{}Class _:_3_{}''',
                '''Class,_,:,lN,{,Val,_,,,wKI,:,_,;,V,(,r,,,_,:,Array,[,Int,,,064011,],),{,Val,_,,,_,:,Array,[,Array,[,Boolean,,,5,],,,0x36,],;,},},Class,_,:,__,{,},Class,___2,{,},Class,_,:,_3_,{,},<EOF>''',
                101
            )
        )

    def test_1242(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _78{}Class r{Val o,_cH,$_:Float ;}Class _{Var $LF_,$_:_;}Class m_O{Var $_,_,$4,Y_55:_;Destructor (){Var nv2__:String ;} }''',
                '''Class,_78,{,},Class,r,{,Val,o,,,_cH,,,$_,:,Float,;,},Class,_,{,Var,$LF_,,,$_,:,_,;,},Class,m_O,{,Var,$_,,,_,,,$4,,,Y_55,:,_,;,Destructor,(,),{,Var,nv2__,:,String,;,},},<EOF>''',
                101
            )
        )

    def test_1243(self):
        self.assertTrue(
            TestLexer.test(
                '''Class TI:__5{}Class z:_{Constructor (RT:Boolean ){Break ;} }Class JZ_{}Class r_6{}Class d5{Val _6Hx,__,z,_9_:Array [Array [Array [String ,89],0x3A_6],07_6];}''',
                '''Class,TI,:,__5,{,},Class,z,:,_,{,Constructor,(,RT,:,Boolean,),{,Break,;,},},Class,JZ_,{,},Class,r_6,{,},Class,d5,{,Val,_6Hx,,,__,,,z,,,_9_,:,Array,[,Array,[,Array,[,String,,,89,],,,0x3A6,],,,076,],;,},<EOF>''',
                101
            )
        )

    def test_1244(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (d,__4,__4_:Array [Array [String ,9],05_6_5];_4:b0;_pB:_){} }Class TK_4__:__3{Constructor (__M,V2,_:Boolean ){}Constructor (_kl,h,i:_;___O:__z){ {} }Destructor (){}Var $sj7,$__,$_,Q___,$5:O;}''',
                '''Class,_,{,Constructor,(,d,,,__4,,,__4_,:,Array,[,Array,[,String,,,9,],,,0565,],;,_4,:,b0,;,_pB,:,_,),{,},},Class,TK_4__,:,__3,{,Constructor,(,__M,,,V2,,,_,:,Boolean,),{,},Constructor,(,_kl,,,h,,,i,:,_,;,___O,:,__z,),{,{,},},Destructor,(,),{,},Var,$sj7,,,$__,,,$_,,,Q___,,,$5,:,O,;,},<EOF>''',
                101
            )
        )

    def test_1245(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _27:Cd8_{Constructor (){Return ;{} }Val $_,$2:Array [Boolean ,0B101_0_0];$c_(qN,c:Array [Array [Array [Int ,07],0B100001],0B100001]){}Constructor (){} }Class _L:_{}''',
                '''Class,_27,:,Cd8_,{,Constructor,(,),{,Return,;,{,},},Val,$_,,,$2,:,Array,[,Boolean,,,0B10100,],;,$c_,(,qN,,,c,:,Array,[,Array,[,Array,[,Int,,,07,],,,0B100001,],,,0B100001,],),{,},Constructor,(,),{,},},Class,_L,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1246(self):
        self.assertTrue(
            TestLexer.test(
                '''Class E{D_8(p:Array [Array [Boolean ,045],05];__l7,p,n,g:String ){_A5_::$b();} }Class _:e_{Var $_:g6;Constructor (_1,A:d_4){} }Class _{Val $a,N_:_748__x;Var $R,$_,$0:Float ;$3__(_Q:_){} }''',
                '''Class,E,{,D_8,(,p,:,Array,[,Array,[,Boolean,,,045,],,,05,],;,__l7,,,p,,,n,,,g,:,String,),{,_A5_,::,$b,(,),;,},},Class,_,:,e_,{,Var,$_,:,g6,;,Constructor,(,_1,,,A,:,d_4,),{,},},Class,_,{,Val,$a,,,N_,:,_748__x,;,Var,$R,,,$_,,,$0,:,Float,;,$3__,(,_Q,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_1247(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _u{Dc7(){} }Class _:_F_{Constructor (__:Float ;U,a:Boolean ;X,_,_6:a;_:Array [Float ,5_2]){}Val D9___s,Bag,T:Array [Array [Array [Array [String ,0b10],0X1_98],8],50];}''',
                '''Class,_u,{,Dc7,(,),{,},},Class,_,:,_F_,{,Constructor,(,__,:,Float,;,U,,,a,:,Boolean,;,X,,,_,,,_6,:,a,;,_,:,Array,[,Float,,,52,],),{,},Val,D9___s,,,Bag,,,T,:,Array,[,Array,[,Array,[,Array,[,String,,,0b10,],,,0X198,],,,8,],,,50,],;,},<EOF>''',
                101
            )
        )

    def test_1248(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8:d{Destructor (){} }Class _{}Class U{Val s71x__:Array [Array [String ,0b1100001],07];}Class __{Var $_O0m,_7l_:Boolean ;Val $i,p___c4:String ;}''',
                '''Class,_8,:,d,{,Destructor,(,),{,},},Class,_,{,},Class,U,{,Val,s71x__,:,Array,[,Array,[,String,,,0b1100001,],,,07,],;,},Class,__,{,Var,$_O0m,,,_7l_,:,Boolean,;,Val,$i,,,p___c4,:,String,;,},<EOF>''',
                101
            )
        )

    def test_1249(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o:___{}Class _W8:F_R3O_3{Constructor (_,__:Boolean ;_,H,__,_C_,_:Array [String ,011];B_:Float ){}Val $9:Float ;}Class G7_I:_Y{}Class ___v5x_{}''',
                '''Class,o,:,___,{,},Class,_W8,:,F_R3O_3,{,Constructor,(,_,,,__,:,Boolean,;,_,,,H,,,__,,,_C_,,,_,:,Array,[,String,,,011,],;,B_,:,Float,),{,},Val,$9,:,Float,;,},Class,G7_I,:,_Y,{,},Class,___v5x_,{,},<EOF>''',
                101
            )
        )

    def test_1250(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7:h__b{Destructor (){Var j__:Array [Int ,067];}Val _,a:_j;$_(Os2Z,_,_93_o:v940){Var U6:Array [Array [Int ,5_88],0X58];} }''',
                '''Class,_7,:,h__b,{,Destructor,(,),{,Var,j__,:,Array,[,Int,,,067,],;,},Val,_,,,a,:,_j,;,$_,(,Os2Z,,,_,,,_93_o,:,v940,),{,Var,U6,:,Array,[,Array,[,Int,,,588,],,,0X58,],;,},},<EOF>''',
                101
            )
        )

    def test_1251(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y{}Class m4:O{}Class M:_j_{}Class p:Mp04{$rl(t3p:_S;V:Array [Array [Boolean ,0X4A],023];u:_;C_,_,uH:_k;_784_8_d4__,__:k9;TwdY,_:_){}Destructor (){} }''',
                '''Class,y,{,},Class,m4,:,O,{,},Class,M,:,_j_,{,},Class,p,:,Mp04,{,$rl,(,t3p,:,_S,;,V,:,Array,[,Array,[,Boolean,,,0X4A,],,,023,],;,u,:,_,;,C_,,,_,,,uH,:,_k,;,_784_8_d4__,,,__,:,k9,;,TwdY,,,_,:,_,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1252(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_42{}Class __t_:_x97{}Class u:_J{}Class _{Constructor (){}Var G6,$_n:Array [Boolean ,0X1_41];Val _c_:Array [Boolean ,01];}''',
                '''Class,_,:,_42,{,},Class,__t_,:,_x97,{,},Class,u,:,_J,{,},Class,_,{,Constructor,(,),{,},Var,G6,,,$_n,:,Array,[,Boolean,,,0X141,],;,Val,_c_,:,Array,[,Boolean,,,01,],;,},<EOF>''',
                101
            )
        )

    def test_1253(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_X{_(_,C,iV:Array [Array [Array [Array [Array [Boolean ,99],877_43_6_11],0xBD_6],033],0X5F]){}Var $__x,_6:Array [Int ,0b1_0];}''',
                '''Class,_,:,_X,{,_,(,_,,,C,,,iV,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,99,],,,87743611,],,,0xBD6,],,,033,],,,0X5F,],),{,},Var,$__x,,,_6,:,Array,[,Int,,,0b10,],;,},<EOF>''',
                101
            )
        )

    def test_1254(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _91:__{Constructor (){ {} }}Class _P{}Class _9__V:t{$5j3n(R_:Boolean ;_,_2a,m,N2:Array [String ,0x2E]){} }''',
                '''Class,_91,:,__,{,Constructor,(,),{,{,},},},Class,_P,{,},Class,_9__V,:,t,{,$5j3n,(,R_,:,Boolean,;,_,,,_2a,,,m,,,N2,:,Array,[,String,,,0x2E,],),{,},},<EOF>''',
                101
            )
        )

    def test_1255(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___P:_dN5{Destructor (){}Val _:Array [Array [Array [Array [Array [Array [Int ,06],0122],0b11],64],64],0XFC];}''',
                '''Class,___P,:,_dN5,{,Destructor,(,),{,},Val,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,06,],,,0122,],,,0b11,],,,64,],,,64,],,,0XFC,],;,},<EOF>''',
                101
            )
        )

    def test_1256(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var $S,_BL8_2,______V,S3:Array [Float ,0b100010];Var $9O:Array [Array [Array [Array [Array [Int ,011],011],0B111110],0x55],0X1];}''',
                '''Class,_,{,Var,$S,,,_BL8_2,,,______V,,,S3,:,Array,[,Float,,,0b100010,],;,Var,$9O,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,011,],,,011,],,,0B111110,],,,0x55,],,,0X1,],;,},<EOF>''',
                101
            )
        )

    def test_1257(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class g:Wa57_{Constructor (){Continue ;}Destructor (){}$_(__:Int ;__:u5;_:Float ;_:Array [Array [Array [Array [Int ,014],0x8_1],014],050];bC,s,L6:Float ){} }Class S_:XV{Val G,_,$_q,f:Tz;}''',
                '''Class,_,{,},Class,g,:,Wa57_,{,Constructor,(,),{,Continue,;,},Destructor,(,),{,},$_,(,__,:,Int,;,__,:,u5,;,_,:,Float,;,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,014,],,,0x81,],,,014,],,,050,],;,bC,,,s,,,L6,:,Float,),{,},},Class,S_,:,XV,{,Val,G,,,_,,,$_q,,,f,:,Tz,;,},<EOF>''',
                101
            )
        )

    def test_1258(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X{$4_5_(_:Array [Boolean ,017];_14,_,x:Float ){}L(u_i1,X,aA_1:Array [Array [Array [Array [Array [String ,0b1001011],04],0X54],1_0],0B100_1]){Return ;Break ;Continue ;}Constructor (){} }''',
                '''Class,X,{,$4_5_,(,_,:,Array,[,Boolean,,,017,],;,_14,,,_,,,x,:,Float,),{,},L,(,u_i1,,,X,,,aA_1,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b1001011,],,,04,],,,0X54,],,,10,],,,0B1001,],),{,Return,;,Break,;,Continue,;,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1259(self):
        self.assertTrue(
            TestLexer.test(
                '''Class U4_:j_0{__2_3S_31L(_:Float ){Break ;}Constructor (_9e7_:Array [Array [Array [Array [Float ,7481],2],0x49],88];_,_:Int ;_,V,_w__:Array [Int ,0140]){} }''',
                '''Class,U4_,:,j_0,{,__2_3S_31L,(,_,:,Float,),{,Break,;,},Constructor,(,_9e7_,:,Array,[,Array,[,Array,[,Array,[,Float,,,7481,],,,2,],,,0x49,],,,88,],;,_,,,_,:,Int,;,_,,,V,,,_w__,:,Array,[,Int,,,0140,],),{,},},<EOF>''',
                101
            )
        )

    def test_1260(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:Q__81{}Class H{Val $_,vXE:_;}Class mg{}Class k{Var w:Array [Float ,0X12];Var $_VN7:Int ;}Class _6{Var _,$0_,$0,$E,$_9,_:Vjh;}''',
                '''Class,__,:,Q__81,{,},Class,H,{,Val,$_,,,vXE,:,_,;,},Class,mg,{,},Class,k,{,Var,w,:,Array,[,Float,,,0X12,],;,Var,$_VN7,:,Int,;,},Class,_6,{,Var,_,,,$0_,,,$0,,,$E,,,$_9,,,_,:,Vjh,;,},<EOF>''',
                101
            )
        )

    def test_1261(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Y_{}Class R:_Q{Constructor (F:Array [Array [Array [Array [Float ,67],050],07],0B110100]){} }Class _1{_(F:s_){} }''',
                '''Class,Y_,{,},Class,R,:,_Q,{,Constructor,(,F,:,Array,[,Array,[,Array,[,Array,[,Float,,,67,],,,050,],,,07,],,,0B110100,],),{,},},Class,_1,{,_,(,F,:,s_,),{,},},<EOF>''',
                101
            )
        )

    def test_1262(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J{}Class __{Constructor (){Continue ;}Val F:Array [Array [String ,0X28],046];Constructor (o,e,___,U9,J:_2){} }''',
                '''Class,J,{,},Class,__,{,Constructor,(,),{,Continue,;,},Val,F,:,Array,[,Array,[,String,,,0X28,],,,046,],;,Constructor,(,o,,,e,,,___,,,U9,,,J,:,_2,),{,},},<EOF>''',
                101
            )
        )

    def test_1263(self):
        self.assertTrue(
            TestLexer.test(
                '''Class O_{$h(O2_,_,V7:Boolean ;d9_R,C:_;nT:Array [Int ,0B1_1_00];AU,z,_75:_;S,Pi_,Y:String ;_,v1,_,f,s,__,_w5,_:_;a:Int ;s_a:Float ;MX:Array [Array [Float ,032],0b10011]){}Destructor (){} }Class _Op:Y{}''',
                '''Class,O_,{,$h,(,O2_,,,_,,,V7,:,Boolean,;,d9_R,,,C,:,_,;,nT,:,Array,[,Int,,,0B1100,],;,AU,,,z,,,_75,:,_,;,S,,,Pi_,,,Y,:,String,;,_,,,v1,,,_,,,f,,,s,,,__,,,_w5,,,_,:,_,;,a,:,Int,;,s_a,:,Float,;,MX,:,Array,[,Array,[,Float,,,032,],,,0b10011,],),{,},Destructor,(,),{,},},Class,_Op,:,Y,{,},<EOF>''',
                101
            )
        )

    def test_1264(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{}Class _{Val _l,$8:Array [Array [Array [Float ,8],0x43],1];}Class U1q7:N{Val $7:Array [Array [Array [Array [Int ,80],0b10111],80],0105];}''',
                '''Class,__,{,},Class,_,{,Val,_l,,,$8,:,Array,[,Array,[,Array,[,Float,,,8,],,,0x43,],,,1,],;,},Class,U1q7,:,N,{,Val,$7,:,Array,[,Array,[,Array,[,Array,[,Int,,,80,],,,0b10111,],,,80,],,,0105,],;,},<EOF>''',
                101
            )
        )

    def test_1265(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:f{Constructor (_:Boolean ;_:Array [Array [Array [Int ,01_1],01_5],04];k,V7_,e:Array [Int ,76_48]){Return ;} }''',
                '''Class,_,:,f,{,Constructor,(,_,:,Boolean,;,_,:,Array,[,Array,[,Array,[,Int,,,011,],,,015,],,,04,],;,k,,,V7_,,,e,:,Array,[,Int,,,7648,],),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_1266(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class ey6{Val $G:_;}Class _9_70n9{}Class m_:k_0K{Destructor (){} }Class _H{Constructor (){} }Class __:dh{}''',
                '''Class,_,:,_,{,},Class,ey6,{,Val,$G,:,_,;,},Class,_9_70n9,{,},Class,m_,:,k_0K,{,Destructor,(,),{,},},Class,_H,{,Constructor,(,),{,},},Class,__,:,dh,{,},<EOF>''',
                101
            )
        )

    def test_1267(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_7{}Class __58:_124{}Class X7429{Constructor (B:String ;_1C:_3){}Destructor (){}Destructor (){}Constructor (_2z:___69){} }Class _:BbW{}''',
                '''Class,_,:,_7,{,},Class,__58,:,_124,{,},Class,X7429,{,Constructor,(,B,:,String,;,_1C,:,_3,),{,},Destructor,(,),{,},Destructor,(,),{,},Constructor,(,_2z,:,___69,),{,},},Class,_,:,BbW,{,},<EOF>''',
                101
            )
        )

    def test_1268(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t_:Q{Var J__W_:Float ;Constructor (WZh_:Array [Array [Float ,023],0B1111];_:String ;q0:Boolean ){} }Class _1:Cb{}Class _3{}''',
                '''Class,t_,:,Q,{,Var,J__W_,:,Float,;,Constructor,(,WZh_,:,Array,[,Array,[,Float,,,023,],,,0B1111,],;,_,:,String,;,q0,:,Boolean,),{,},},Class,_1,:,Cb,{,},Class,_3,{,},<EOF>''',
                101
            )
        )

    def test_1269(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P{Constructor (H:Float ;ZE:String ){} }Class ___y{$_06L(__y:String ;j7:Array [Int ,047];_:Array [Array [Array [Array [Array [Array [Float ,0x6A],0b1010000],94],0XDA7],0xD],94]){} }''',
                '''Class,P,{,Constructor,(,H,:,Float,;,ZE,:,String,),{,},},Class,___y,{,$_06L,(,__y,:,String,;,j7,:,Array,[,Int,,,047,],;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x6A,],,,0b1010000,],,,94,],,,0XDA7,],,,0xD,],,,94,],),{,},},<EOF>''',
                101
            )
        )

    def test_1270(self):
        self.assertTrue(
            TestLexer.test(
                '''Class i9_46{}Class _:O4{}Class m2{wsO9(_,_:Int ;_:Array [Array [Array [Int ,0b1_11_0],04],72];_:Array [Int ,0X1]){} }Class Ib913{}''',
                '''Class,i9_46,{,},Class,_,:,O4,{,},Class,m2,{,wsO9,(,_,,,_,:,Int,;,_,:,Array,[,Array,[,Array,[,Int,,,0b1110,],,,04,],,,72,],;,_,:,Array,[,Int,,,0X1,],),{,},},Class,Ib913,{,},<EOF>''',
                101
            )
        )

    def test_1271(self):
        self.assertTrue(
            TestLexer.test(
                '''Class G7:n{Constructor (F:Array [Array [Float ,0B10],0x2D];x:b7_;_8l,P:Array [Array [Boolean ,586],89_8];q,z_w3:Array [Array [Array [Array [Float ,6_8],0XA],0133],0B111_0]){}Val $_N:r;}''',
                '''Class,G7,:,n,{,Constructor,(,F,:,Array,[,Array,[,Float,,,0B10,],,,0x2D,],;,x,:,b7_,;,_8l,,,P,:,Array,[,Array,[,Boolean,,,586,],,,898,],;,q,,,z_w3,:,Array,[,Array,[,Array,[,Array,[,Float,,,68,],,,0XA,],,,0133,],,,0B1110,],),{,},Val,$_N,:,r,;,},<EOF>''',
                101
            )
        )

    def test_1272(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7_I_{}Class C{}Class f:_{}Class _9{}Class L{Constructor (_:Array [Array [Boolean ,0b1],0B10];u:Int ;_85p,C_:_){} }''',
                '''Class,_7_I_,{,},Class,C,{,},Class,f,:,_,{,},Class,_9,{,},Class,L,{,Constructor,(,_,:,Array,[,Array,[,Boolean,,,0b1,],,,0B10,],;,u,:,Int,;,_85p,,,C_,:,_,),{,},},<EOF>''',
                101
            )
        )

    def test_1273(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class WQ{Var $0,_6_x,$X_,$__92B9:oB;Val $8:Array [String ,05_6];Constructor (S0v_,_6_,_CZh_7,Sn:b_3;u:Boolean ;g,_,_5_,_78_,m,p_:String ){}Destructor (){} }''',
                '''Class,_,:,_,{,},Class,WQ,{,Var,$0,,,_6_x,,,$X_,,,$__92B9,:,oB,;,Val,$8,:,Array,[,String,,,056,],;,Constructor,(,S0v_,,,_6_,,,_CZh_7,,,Sn,:,b_3,;,u,:,Boolean,;,g,,,_,,,_5_,,,_78_,,,m,,,p_,:,String,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1274(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_3y,_:_5;A:_;_l,B,l,o:_){ {}Var j1,Mi,x,m1m:Array [Array [Array [Boolean ,469],07],01];} }''',
                '''Class,_,{,Constructor,(,_3y,,,_,:,_5,;,A,:,_,;,_l,,,B,,,l,,,o,:,_,),{,{,},Var,j1,,,Mi,,,x,,,m1m,:,Array,[,Array,[,Array,[,Boolean,,,469,],,,07,],,,01,],;,},},<EOF>''',
                101
            )
        )

    def test_1275(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Q{Var $SXq:_0;Var $0a,$02927,m7:String ;D3_G(D:_9xjHg_N34_){Var l:Array [Array [Array [Array [Array [Int ,1],0b1_0],0XF4],42],0XC];} }Class m:_{}Class _K:__73{_(__:nRQ7I){} }Class C:B{}Class __1E{Val _:_0;}Class _:k_{}''',
                '''Class,Q,{,Var,$SXq,:,_0,;,Var,$0a,,,$02927,,,m7,:,String,;,D3_G,(,D,:,_9xjHg_N34_,),{,Var,l,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,1,],,,0b10,],,,0XF4,],,,42,],,,0XC,],;,},},Class,m,:,_,{,},Class,_K,:,__73,{,_,(,__,:,nRQ7I,),{,},},Class,C,:,B,{,},Class,__1E,{,Val,_,:,_0,;,},Class,_,:,k_,{,},<EOF>''',
                101
            )
        )

    def test_1276(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:B{Val $C:Float ;}Class _:_l{Constructor (F,b,_,_s,v,_4o:Float ;_2,_:Array [Array [Array [Array [String ,0B1011010],0b1],0B10],0B1011010]){} }''',
                '''Class,_,:,B,{,Val,$C,:,Float,;,},Class,_,:,_l,{,Constructor,(,F,,,b,,,_,,,_s,,,v,,,_4o,:,Float,;,_2,,,_,:,Array,[,Array,[,Array,[,Array,[,String,,,0B1011010,],,,0b1,],,,0B10,],,,0B1011010,],),{,},},<EOF>''',
                101
            )
        )

    def test_1277(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __28H_8{Val AF4,_,$1,Y:Array [Array [Array [Array [Array [Boolean ,176],02],0X8],44],0x46];Destructor (){} }Class pu4z_{}Class _9:_{Var $_:_Q8;}''',
                '''Class,__28H_8,{,Val,AF4,,,_,,,$1,,,Y,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,176,],,,02,],,,0X8,],,,44,],,,0x46,],;,Destructor,(,),{,},},Class,pu4z_,{,},Class,_9,:,_,{,Var,$_,:,_Q8,;,},<EOF>''',
                101
            )
        )

    def test_1278(self):
        self.assertTrue(
            TestLexer.test(
                '''Class N{}Class N0b:_{Val Y,_j,B:Float ;}Class _{}Class _1n:M{Constructor (_,u4:D;_8_A,_,_,D,_7,_:Boolean ){} }''',
                '''Class,N,{,},Class,N0b,:,_,{,Val,Y,,,_j,,,B,:,Float,;,},Class,_,{,},Class,_1n,:,M,{,Constructor,(,_,,,u4,:,D,;,_8_A,,,_,,,_,,,D,,,_7,,,_,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_1279(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Y:_{}Class W:A{Constructor (_66_Z9,__,__0,W0zk:Int ;_3:Array [Int ,0x44_C_0];__,h2,_:Array [Array [Array [Array [Int ,0105],0XA46A],0105],0x51]){} }''',
                '''Class,Y,:,_,{,},Class,W,:,A,{,Constructor,(,_66_Z9,,,__,,,__0,,,W0zk,:,Int,;,_3,:,Array,[,Int,,,0x44C0,],;,__,,,h2,,,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0105,],,,0XA46A,],,,0105,],,,0x51,],),{,},},<EOF>''',
                101
            )
        )

    def test_1280(self):
        self.assertTrue(
            TestLexer.test(
                '''Class pG:s{Constructor (J_:Float ;_,O4,_8,E:Float ;eR_:Array [Array [Int ,0x84_A],90];Sr:P_EGB;sJ,_,_,K_:_7){} }''',
                '''Class,pG,:,s,{,Constructor,(,J_,:,Float,;,_,,,O4,,,_8,,,E,:,Float,;,eR_,:,Array,[,Array,[,Int,,,0x84A,],,,90,],;,Sr,:,P_EGB,;,sJ,,,_,,,_,,,K_,:,_7,),{,},},<EOF>''',
                101
            )
        )

    def test_1281(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Ym{Destructor (){Continue ;}Constructor (){}Constructor (_i2N:Array [Array [String ,03],0xF_4C]){00.H._P_=!----New _d();} }Class _X{}''',
                '''Class,Ym,{,Destructor,(,),{,Continue,;,},Constructor,(,),{,},Constructor,(,_i2N,:,Array,[,Array,[,String,,,03,],,,0xF4C,],),{,00,.,H,.,_P_,=,!,-,-,-,-,New,_d,(,),;,},},Class,_X,{,},<EOF>''',
                101
            )
        )

    def test_1282(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Constructor (){}Val __:lO;}Class N:_Q9_{Constructor (_:Array [Array [Array [Int ,0x1C],0B1],0b11_1];_3:Boolean ;_5u,Nw8_,_E4,___:String ;v,g:pl){}p(_nP,_6,_:Boolean ;VL__:Int ;_:_){} }Class P{}''',
                '''Class,_,:,_,{,Constructor,(,),{,},Val,__,:,lO,;,},Class,N,:,_Q9_,{,Constructor,(,_,:,Array,[,Array,[,Array,[,Int,,,0x1C,],,,0B1,],,,0b111,],;,_3,:,Boolean,;,_5u,,,Nw8_,,,_E4,,,___,:,String,;,v,,,g,:,pl,),{,},p,(,_nP,,,_6,,,_,:,Boolean,;,VL__,:,Int,;,_,:,_,),{,},},Class,P,{,},<EOF>''',
                101
            )
        )

    def test_1283(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:sY{Var $0a:__;Destructor (){} }Class _{}Class J:_2_{$_2p(){} }Class _7:_{}Class d{Destructor (){Return ;HI_::$8();} }Class s{}Class Eo6__0:_P{Destructor (){} }''',
                '''Class,_,:,sY,{,Var,$0a,:,__,;,Destructor,(,),{,},},Class,_,{,},Class,J,:,_2_,{,$_2p,(,),{,},},Class,_7,:,_,{,},Class,d,{,Destructor,(,),{,Return,;,HI_,::,$8,(,),;,},},Class,s,{,},Class,Eo6__0,:,_P,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1284(self):
        self.assertTrue(
            TestLexer.test(
                '''Class x:_4O1{}Class x_7:f{Constructor (){}Var $__5,$7:Array [Float ,0B1_0_1_0];Constructor (q__,_2,h:Array [Int ,0b1];yM,__,b,_:Int ){}Constructor (M_:Array [Boolean ,0B1011011]){}Constructor (G:__Jm1_9;J_R:Array [Int ,6];u:Boolean ){}Var $_s:N;}Class __:c{}''',
                '''Class,x,:,_4O1,{,},Class,x_7,:,f,{,Constructor,(,),{,},Var,$__5,,,$7,:,Array,[,Float,,,0B1010,],;,Constructor,(,q__,,,_2,,,h,:,Array,[,Int,,,0b1,],;,yM,,,__,,,b,,,_,:,Int,),{,},Constructor,(,M_,:,Array,[,Boolean,,,0B1011011,],),{,},Constructor,(,G,:,__Jm1_9,;,J_R,:,Array,[,Int,,,6,],;,u,:,Boolean,),{,},Var,$_s,:,N,;,},Class,__,:,c,{,},<EOF>''',
                101
            )
        )

    def test_1285(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Destructor (){}Constructor (__:String ;_,_h,_:Array [Float ,0X4];_r040,nQ:j;_N8,U7,z8__,__:String ;_:Float ){} }''',
                '''Class,_,{,Destructor,(,),{,},Constructor,(,__,:,String,;,_,,,_h,,,_,:,Array,[,Float,,,0X4,],;,_r040,,,nQ,:,j,;,_N8,,,U7,,,z8__,,,__,:,String,;,_,:,Float,),{,},},<EOF>''',
                101
            )
        )

    def test_1286(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X3{}Class __:_S7{Val $_,_:Array [Array [Boolean ,0125],1];Var $1_,_:Array [Float ,04];$6(W6,b0:Boolean ;_,_:Array [String ,0B10000];_5B_Zo___t,o:Boolean ;_BH:Array [Array [Array [Boolean ,0125],0X4_7A_1],0x28]){} }''',
                '''Class,X3,{,},Class,__,:,_S7,{,Val,$_,,,_,:,Array,[,Array,[,Boolean,,,0125,],,,1,],;,Var,$1_,,,_,:,Array,[,Float,,,04,],;,$6,(,W6,,,b0,:,Boolean,;,_,,,_,:,Array,[,String,,,0B10000,],;,_5B_Zo___t,,,o,:,Boolean,;,_BH,:,Array,[,Array,[,Array,[,Boolean,,,0125,],,,0X47A1,],,,0x28,],),{,},},<EOF>''',
                101
            )
        )

    def test_1287(self):
        self.assertTrue(
            TestLexer.test(
                '''Class K:f4{}Class V{Val $77:Int ;}Class P{Val _,$3:Array [Array [Array [Array [Float ,12],0B10101],0B1],12];_c_5_(h,K:String ;c:Int ;yz,m_:___;gT2b,__E_6,v_,S2,_,_2p,_:r){} }Class U_BX__o__{Var $__,ik_85_:Array [Float ,0B10101_0];}Class _:A3{}Class _{}Class M6{}Class _N:__{}''',
                '''Class,K,:,f4,{,},Class,V,{,Val,$77,:,Int,;,},Class,P,{,Val,_,,,$3,:,Array,[,Array,[,Array,[,Array,[,Float,,,12,],,,0B10101,],,,0B1,],,,12,],;,_c_5_,(,h,,,K,:,String,;,c,:,Int,;,yz,,,m_,:,___,;,gT2b,,,__E_6,,,v_,,,S2,,,_,,,_2p,,,_,:,r,),{,},},Class,U_BX__o__,{,Var,$__,,,ik_85_,:,Array,[,Float,,,0B101010,],;,},Class,_,:,A3,{,},Class,_,{,},Class,M6,{,},Class,_N,:,__,{,},<EOF>''',
                101
            )
        )

    def test_1288(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $77,__36,_:_;Destructor (){} }Class IY{$_0F(){}$_(hw,n3,__,_,j,O,_,_,__S,__:Boolean ;_:Boolean ;b_K,_:Array [Float ,0XA]){}Destructor (){_k::$d.q.T()._();} }Class a:Va{}''',
                '''Class,_,{,Val,$77,,,__36,,,_,:,_,;,Destructor,(,),{,},},Class,IY,{,$_0F,(,),{,},$_,(,hw,,,n3,,,__,,,_,,,j,,,O,,,_,,,_,,,__S,,,__,:,Boolean,;,_,:,Boolean,;,b_K,,,_,:,Array,[,Float,,,0XA,],),{,},Destructor,(,),{,_k,::,$d,.,q,.,T,(,),.,_,(,),;,},},Class,a,:,Va,{,},<EOF>''',
                101
            )
        )

    def test_1289(self):
        self.assertTrue(
            TestLexer.test(
                '''Class kC_:uce{Constructor (_O,_,_Te:Boolean ;_k:Q__;_:Int ;__549_,z1,b:ff;_,Y,gh_z_y_6_,_k:String ){} }Class n{}Class _4_Q_S_{}''',
                '''Class,kC_,:,uce,{,Constructor,(,_O,,,_,,,_Te,:,Boolean,;,_k,:,Q__,;,_,:,Int,;,__549_,,,z1,,,b,:,ff,;,_,,,Y,,,gh_z_y_6_,,,_k,:,String,),{,},},Class,n,{,},Class,_4_Q_S_,{,},<EOF>''',
                101
            )
        )

    def test_1290(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _t{Var $_,$5dR:_;}Class _z7{Var W_i___7,j,$_,p__3,$7,b38:_;}Class _9rB{$Z_(_,__Q:F;_,_d:Float ;___:_;_,_,_8:z_;_,_,K:Array [String ,0b1001011];D:Array [Float ,0130];_:_;_:_wQ;_,V,_6,_3,G8:Array [Boolean ,0130];e:_){}$L6(){Val _,_:Int ;}_(){} }''',
                '''Class,_t,{,Var,$_,,,$5dR,:,_,;,},Class,_z7,{,Var,W_i___7,,,j,,,$_,,,p__3,,,$7,,,b38,:,_,;,},Class,_9rB,{,$Z_,(,_,,,__Q,:,F,;,_,,,_d,:,Float,;,___,:,_,;,_,,,_,,,_8,:,z_,;,_,,,_,,,K,:,Array,[,String,,,0b1001011,],;,D,:,Array,[,Float,,,0130,],;,_,:,_,;,_,:,_wQ,;,_,,,V,,,_6,,,_3,,,G8,:,Array,[,Boolean,,,0130,],;,e,:,_,),{,},$L6,(,),{,Val,_,,,_,:,Int,;,},_,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1291(self):
        self.assertTrue(
            TestLexer.test(
                '''Class BF{$1N__(_,_:Array [Array [Array [Array [Float ,044],24],04_6_5_1],0b1];_T__:_;_:String ){} }Class I9__82:T{}''',
                '''Class,BF,{,$1N__,(,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,044,],,,24,],,,04651,],,,0b1,],;,_T__,:,_,;,_,:,String,),{,},},Class,I9__82,:,T,{,},<EOF>''',
                101
            )
        )

    def test_1292(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _c:_{}Class _{Constructor (){} }Class __:_M{Constructor (t,_,yA___9,_,Ys:String ;_,Ps3_Z2,_,W,ua,I:Int ){Return ;} }''',
                '''Class,_c,:,_,{,},Class,_,{,Constructor,(,),{,},},Class,__,:,_M,{,Constructor,(,t,,,_,,,yA___9,,,_,,,Ys,:,String,;,_,,,Ps3_Z2,,,_,,,W,,,ua,,,I,:,Int,),{,Return,;,},},<EOF>''',
                101
            )
        )

    def test_1293(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:Q64{A(_:vV_2;_XN,_,_,e,k_,R,g_8,_,_e_:Array [Int ,0B100100]){}Var _:Array [Array [Float ,06],0X1];}Class _{}''',
                '''Class,_,:,Q64,{,A,(,_,:,vV_2,;,_XN,,,_,,,_,,,e,,,k_,,,R,,,g_8,,,_,,,_e_,:,Array,[,Int,,,0B100100,],),{,},Var,_,:,Array,[,Array,[,Float,,,06,],,,0X1,],;,},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_1294(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X5:E{Var $_5:Array [Float ,0x43];Var _R:_;Constructor (_9:Array [Array [Array [Array [Array [String ,0b11111],42],21],21],0X5D]){} }''',
                '''Class,X5,:,E,{,Var,$_5,:,Array,[,Float,,,0x43,],;,Var,_R,:,_,;,Constructor,(,_9,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b11111,],,,42,],,,21,],,,21,],,,0X5D,],),{,},},<EOF>''',
                101
            )
        )

    def test_1295(self):
        self.assertTrue(
            TestLexer.test(
                '''Class v{}Class _x78_:_{}Class I_Q__03cbwI:_f_{Var $_B,$6,_4n:Float ;Val W,$__:g;}Class G:U{Val $0C:P;}Class YpA:__8{}Class _:_4{}''',
                '''Class,v,{,},Class,_x78_,:,_,{,},Class,I_Q__03cbwI,:,_f_,{,Var,$_B,,,$6,,,_4n,:,Float,;,Val,W,,,$__,:,g,;,},Class,G,:,U,{,Val,$0C,:,P,;,},Class,YpA,:,__8,{,},Class,_,:,_4,{,},<EOF>''',
                101
            )
        )

    def test_1296(self):
        self.assertTrue(
            TestLexer.test(
                '''Class z:f{}Class _:Q3{Destructor (){}$O(){}$_f(_1,_,D:String ;_:String ;_3j,__G:_K31T;_:KL;g:_){}Constructor (){} }''',
                '''Class,z,:,f,{,},Class,_,:,Q3,{,Destructor,(,),{,},$O,(,),{,},$_f,(,_1,,,_,,,D,:,String,;,_,:,String,;,_3j,,,__G,:,_K31T,;,_,:,KL,;,g,:,_,),{,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1297(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _V_{Constructor (_,_g_,___,B:_h;r__:__;_7:Array [Float ,0x5A];_,Y,_:j){}Var _,_____z,$0_:_;Val $_,$_A7,__,_:_z;Constructor (){} }Class J5Q{$y6(J,M4:Array [Array [Boolean ,06],0x5A]){} }''',
                '''Class,_V_,{,Constructor,(,_,,,_g_,,,___,,,B,:,_h,;,r__,:,__,;,_7,:,Array,[,Float,,,0x5A,],;,_,,,Y,,,_,:,j,),{,},Var,_,,,_____z,,,$0_,:,_,;,Val,$_,,,$_A7,,,__,,,_,:,_z,;,Constructor,(,),{,},},Class,J5Q,{,$y6,(,J,,,M4,:,Array,[,Array,[,Boolean,,,06,],,,0x5A,],),{,},},<EOF>''',
                101
            )
        )

    def test_1298(self):
        self.assertTrue(
            TestLexer.test(
                '''Class F7:_{Destructor (){Val ___:D;_::$_f7();}Var $_j_,N__m:y;}Class _:__9{}Class W_:_v4D_2_{Destructor (){ {} }Constructor (){} }''',
                '''Class,F7,:,_,{,Destructor,(,),{,Val,___,:,D,;,_,::,$_f7,(,),;,},Var,$_j_,,,N__m,:,y,;,},Class,_,:,__9,{,},Class,W_,:,_v4D_2_,{,Destructor,(,),{,{,},},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1299(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m:_{Var $_J,$_:Array [Array [Int ,052],0b1010101];Val $h5,$4n8:Array [Array [Array [Array [Array [Array [Array [Float ,015],2],0X1_F],0x9],0B11011],49],05];Destructor (){} }''',
                '''Class,m,:,_,{,Var,$_J,,,$_,:,Array,[,Array,[,Int,,,052,],,,0b1010101,],;,Val,$h5,,,$4n8,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,015,],,,2,],,,0X1F,],,,0x9,],,,0B11011,],,,49,],,,05,],;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1300(self):
        self.assertTrue(
            TestLexer.test(
                '''Class fT:_{}Class kU2yee{$__(_,g_X:_8_R_;g,y:Array [Float ,0X2C];_6__,__:Array [Array [Array [Array [Int ,2],0b1],0B1],62];_,O,r:String ){} }''',
                '''Class,fT,:,_,{,},Class,kU2yee,{,$__,(,_,,,g_X,:,_8_R_,;,g,,,y,:,Array,[,Float,,,0X2C,],;,_6__,,,__,:,Array,[,Array,[,Array,[,Array,[,Int,,,2,],,,0b1,],,,0B1,],,,62,],;,_,,,O,,,r,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_1301(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_9{Val _,td,$_Kn,e4:Array [Array [Boolean ,0b1000000],0b1000000];}Class _:r{$_(O,P,_,P3:U;x5I:String ){Var W0:Array [Array [Array [Int ,027],027],0b1000000];}Var $b4,$5,$_:q;}''',
                '''Class,_,:,_9,{,Val,_,,,td,,,$_Kn,,,e4,:,Array,[,Array,[,Boolean,,,0b1000000,],,,0b1000000,],;,},Class,_,:,r,{,$_,(,O,,,P,,,_,,,P3,:,U,;,x5I,:,String,),{,Var,W0,:,Array,[,Array,[,Array,[,Int,,,027,],,,027,],,,0b1000000,],;,},Var,$b4,,,$5,,,$_,:,q,;,},<EOF>''',
                101
            )
        )

    def test_1302(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _b5_:z{Val $__:Int ;bU(){Break ;} }Class t:f_7{Constructor (U4,C:Boolean ;m,Z1,Bi,___,_,d_w:_;___,gU,D,W,_3,I64ii:Array [Array [Array [Array [String ,0x53],023],35],0x53]){Break ;} }''',
                '''Class,_b5_,:,z,{,Val,$__,:,Int,;,bU,(,),{,Break,;,},},Class,t,:,f_7,{,Constructor,(,U4,,,C,:,Boolean,;,m,,,Z1,,,Bi,,,___,,,_,,,d_w,:,_,;,___,,,gU,,,D,,,W,,,_3,,,I64ii,:,Array,[,Array,[,Array,[,Array,[,String,,,0x53,],,,023,],,,35,],,,0x53,],),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_1303(self):
        self.assertTrue(
            TestLexer.test(
                '''Class t__eOK{}Class Q{Constructor (){} }Class R7{}Class P6:_{}Class _7:W{W(__5_7_:_B;F__X,_vL1,_z_____,Oq:Array [Float ,3];U:String ){} }''',
                '''Class,t__eOK,{,},Class,Q,{,Constructor,(,),{,},},Class,R7,{,},Class,P6,:,_,{,},Class,_7,:,W,{,W,(,__5_7_,:,_B,;,F__X,,,_vL1,,,_z_____,,,Oq,:,Array,[,Float,,,3,],;,U,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_1304(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{$d(p89G3,x_,_,_,R:Array [String ,032];_:Array [Array [Boolean ,40],0X4]){}Var _,$Z:Array [Float ,65];}Class _:_{}Class R{}''',
                '''Class,_,{,$d,(,p89G3,,,x_,,,_,,,_,,,R,:,Array,[,String,,,032,],;,_,:,Array,[,Array,[,Boolean,,,40,],,,0X4,],),{,},Var,_,,,$Z,:,Array,[,Float,,,65,],;,},Class,_,:,_,{,},Class,R,{,},<EOF>''',
                101
            )
        )

    def test_1305(self):
        self.assertTrue(
            TestLexer.test(
                '''Class a:U{$qp(_,Ie,Qax_:Array [Array [Array [Boolean ,28],02],0b1];_u:ew8;K4A05,_:__){Var _,O,b,__z,_:Boolean ;} }''',
                '''Class,a,:,U,{,$qp,(,_,,,Ie,,,Qax_,:,Array,[,Array,[,Array,[,Boolean,,,28,],,,02,],,,0b1,],;,_u,:,ew8,;,K4A05,,,_,:,__,),{,Var,_,,,O,,,b,,,__z,,,_,:,Boolean,;,},},<EOF>''',
                101
            )
        )

    def test_1306(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _v:_{Var $_,$7,$R:Array [Array [Array [Array [Array [String ,0xE2],0B10000],0B1],0B111_1],07_3];Var $_:V_;Val $8___,$_:Boolean ;}Class _{Destructor (){Continue ;{} }}Class G:n57{}''',
                '''Class,_v,:,_,{,Var,$_,,,$7,,,$R,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0xE2,],,,0B10000,],,,0B1,],,,0B1111,],,,073,],;,Var,$_,:,V_,;,Val,$8___,,,$_,:,Boolean,;,},Class,_,{,Destructor,(,),{,Continue,;,{,},},},Class,G,:,n57,{,},<EOF>''',
                101
            )
        )

    def test_1307(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7_:_Wm4A{Destructor (){} }Class U:Y_1{$1_(_3,_:Int ){}Constructor (){} }Class _0{Destructor (){Continue ;}Val T_Q5q:Array [Float ,0XC7_00];Constructor (){} }Class S:_{Val _,b5:Array [Array [Int ,0X26],07];}Class _0:v1{}''',
                '''Class,_7_,:,_Wm4A,{,Destructor,(,),{,},},Class,U,:,Y_1,{,$1_,(,_3,,,_,:,Int,),{,},Constructor,(,),{,},},Class,_0,{,Destructor,(,),{,Continue,;,},Val,T_Q5q,:,Array,[,Float,,,0XC700,],;,Constructor,(,),{,},},Class,S,:,_,{,Val,_,,,b5,:,Array,[,Array,[,Int,,,0X26,],,,07,],;,},Class,_0,:,v1,{,},<EOF>''',
                101
            )
        )

    def test_1308(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:k{}Class C:_{__I(Y,_,D,V,A_7,Y,M,_:Array [Float ,044_11];_,Y4_5,_,Z,Y_:S;_,Mj:Array [Array [Boolean ,28],057];Sn,_,r,_:String ;_,_,_,d89,U,__:Boolean ;n:Array [Float ,0b1]){} }''',
                '''Class,_,:,k,{,},Class,C,:,_,{,__I,(,Y,,,_,,,D,,,V,,,A_7,,,Y,,,M,,,_,:,Array,[,Float,,,04411,],;,_,,,Y4_5,,,_,,,Z,,,Y_,:,S,;,_,,,Mj,:,Array,[,Array,[,Boolean,,,28,],,,057,],;,Sn,,,_,,,r,,,_,:,String,;,_,,,_,,,_,,,d89,,,U,,,__,:,Boolean,;,n,:,Array,[,Float,,,0b1,],),{,},},<EOF>''',
                101
            )
        )

    def test_1309(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __5_:_x{Var $3V,M,$92,$_:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0x33],056],0x33],047],06],056],60],5_2_3_3_89];}''',
                '''Class,__5_,:,_x,{,Var,$3V,,,M,,,$92,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x33,],,,056,],,,0x33,],,,047,],,,06,],,,056,],,,60,],,,523389,],;,},<EOF>''',
                101
            )
        )

    def test_1310(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V7_Fy{}Class g{Constructor (_,_:Boolean ;_,_R:Array [Array [Array [Boolean ,0B1],04],0xD]){}$Y6(){} }Class I{Destructor (){} }Class _:P1{}''',
                '''Class,V7_Fy,{,},Class,g,{,Constructor,(,_,,,_,:,Boolean,;,_,,,_R,:,Array,[,Array,[,Array,[,Boolean,,,0B1,],,,04,],,,0xD,],),{,},$Y6,(,),{,},},Class,I,{,Destructor,(,),{,},},Class,_,:,P1,{,},<EOF>''',
                101
            )
        )

    def test_1311(self):
        self.assertTrue(
            TestLexer.test(
                '''Class L{$_16(J,_:Array [String ,013]){Continue ;Break ;} }Class h4{}Class _5_{Destructor (){Val __:Q;{Continue ;} }}''',
                '''Class,L,{,$_16,(,J,,,_,:,Array,[,String,,,013,],),{,Continue,;,Break,;,},},Class,h4,{,},Class,_5_,{,Destructor,(,),{,Val,__,:,Q,;,{,Continue,;,},},},<EOF>''',
                101
            )
        )

    def test_1312(self):
        self.assertTrue(
            TestLexer.test(
                '''Class qo{}Class n15:_{Destructor (){}Constructor (M_:S_;__41,_,S,_6:Array [Array [Boolean ,902],42]){Break ;} }''',
                '''Class,qo,{,},Class,n15,:,_,{,Destructor,(,),{,},Constructor,(,M_,:,S_,;,__41,,,_,,,S,,,_6,:,Array,[,Array,[,Boolean,,,902,],,,42,],),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_1313(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __{$886V3(a:Array [Array [Float ,0x5A],031]){}Var C:__;Constructor (rqP4v,_9,_Sg,w_:Array [Array [Int ,0B10010],0B101]){}Constructor (){} }Class h{}Class n:i{}''',
                '''Class,__,{,$886V3,(,a,:,Array,[,Array,[,Float,,,0x5A,],,,031,],),{,},Var,C,:,__,;,Constructor,(,rqP4v,,,_9,,,_Sg,,,w_,:,Array,[,Array,[,Int,,,0B10010,],,,0B101,],),{,},Constructor,(,),{,},},Class,h,{,},Class,n,:,i,{,},<EOF>''',
                101
            )
        )

    def test_1314(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___u{Destructor (){} }Class _{Var $M4,$P4914,_89D:Array [Array [Array [Array [Boolean ,0X5],0137],01_2],0XC59];}Class _:_{}''',
                '''Class,___u,{,Destructor,(,),{,},},Class,_,{,Var,$M4,,,$P4914,,,_89D,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X5,],,,0137,],,,012,],,,0XC59,],;,},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1315(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:F_{}Class _:F2{}Class _x{Val $01,k9,yx,$v__15:Array [Array [String ,0xB],0b100001];Val $A:Boolean ;Var $_,__,d_20:Boolean ;Var $7,$hx,$4,$cth:Int ;}''',
                '''Class,_,:,F_,{,},Class,_,:,F2,{,},Class,_x,{,Val,$01,,,k9,,,yx,,,$v__15,:,Array,[,Array,[,String,,,0xB,],,,0b100001,],;,Val,$A,:,Boolean,;,Var,$_,,,__,,,d_20,:,Boolean,;,Var,$7,,,$hx,,,$4,,,$cth,:,Int,;,},<EOF>''',
                101
            )
        )

    def test_1316(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{__(V_,H_nG6,_r:Array [Array [Array [Array [Int ,0b1100000],0B1_1000_00010_0],0X2_6_6_D7_E],0143];W,g,_:e;Y4nk,_5___:Array [Boolean ,04]){}D(){} }''',
                '''Class,_,{,__,(,V_,,,H_nG6,,,_r,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b1100000,],,,0B11000000100,],,,0X266D7E,],,,0143,],;,W,,,g,,,_,:,e,;,Y4nk,,,_5___,:,Array,[,Boolean,,,04,],),{,},D,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1317(self):
        self.assertTrue(
            TestLexer.test(
                '''Class F:L{Constructor (){} }Class _:_{}Class T6{Var $979:Array [Boolean ,037];Val $_,$v2,$9:Array [Array [Array [Int ,037],0xD2_E_4],0xE_1];Val $v:_3__6;}''',
                '''Class,F,:,L,{,Constructor,(,),{,},},Class,_,:,_,{,},Class,T6,{,Var,$979,:,Array,[,Boolean,,,037,],;,Val,$_,,,$v2,,,$9,:,Array,[,Array,[,Array,[,Int,,,037,],,,0xD2E4,],,,0xE1,],;,Val,$v,:,_3__6,;,},<EOF>''',
                101
            )
        )

    def test_1318(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:C9{Constructor (){}Constructor (c,n___,___6Ui9:Boolean ){} }Class _3:_{Val $w:YK59;}Class _:k{Var $p,_3,$4_:Array [Array [Array [Array [String ,0x59],0140],0xA_0FF],0XC_C_D_1];}''',
                '''Class,_,:,C9,{,Constructor,(,),{,},Constructor,(,c,,,n___,,,___6Ui9,:,Boolean,),{,},},Class,_3,:,_,{,Val,$w,:,YK59,;,},Class,_,:,k,{,Var,$p,,,_3,,,$4_,:,Array,[,Array,[,Array,[,Array,[,String,,,0x59,],,,0140,],,,0xA0FF,],,,0XCCD1,],;,},<EOF>''',
                101
            )
        )

    def test_1319(self):
        self.assertTrue(
            TestLexer.test(
                '''Class b:AJ3_{_(ZomN8,UB,b3D_D:Int ){}Var $0_:Array [Array [Array [Float ,7],0xF],0B1001];}Class _g:S{}Class n:g{}Class ___:_{}''',
                '''Class,b,:,AJ3_,{,_,(,ZomN8,,,UB,,,b3D_D,:,Int,),{,},Var,$0_,:,Array,[,Array,[,Array,[,Float,,,7,],,,0xF,],,,0B1001,],;,},Class,_g,:,S,{,},Class,n,:,g,{,},Class,___,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1320(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{$l(r5:Float ;_:Float ;F:String ){}_(W:Array [Array [Array [String ,03_52],0b1010110],0x41];Sv,C__Pu,__:Array [Array [Float ,0B1011010],16];o,I,A_,f:_6;_N,_U6v,_u:o;L:Array [Array [String ,16],0b1_0_0_0];_38:Array [Boolean ,0B11]){Break ;} }''',
                '''Class,_,{,$l,(,r5,:,Float,;,_,:,Float,;,F,:,String,),{,},_,(,W,:,Array,[,Array,[,Array,[,String,,,0352,],,,0b1010110,],,,0x41,],;,Sv,,,C__Pu,,,__,:,Array,[,Array,[,Float,,,0B1011010,],,,16,],;,o,,,I,,,A_,,,f,:,_6,;,_N,,,_U6v,,,_u,:,o,;,L,:,Array,[,Array,[,String,,,16,],,,0b1000,],;,_38,:,Array,[,Boolean,,,0B11,],),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_1321(self):
        self.assertTrue(
            TestLexer.test(
                '''Class p_:___{}Class F{Constructor (__,_:Array [Array [String ,0X44],0B1];_,_,__,zG5:l_E;_6:e;TG,A_y4,K:Array [Boolean ,137_7]){} }''',
                '''Class,p_,:,___,{,},Class,F,{,Constructor,(,__,,,_,:,Array,[,Array,[,String,,,0X44,],,,0B1,],;,_,,,_,,,__,,,zG5,:,l_E,;,_6,:,e,;,TG,,,A_y4,,,K,:,Array,[,Boolean,,,1377,],),{,},},<EOF>''',
                101
            )
        )

    def test_1322(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0{Constructor (_:E;uB3__,_1:Array [String ,0X5];_4,q8,s,_b,__,FV5,_6_,V:Array [Float ,42]){} }Class U{}''',
                '''Class,_0,{,Constructor,(,_,:,E,;,uB3__,,,_1,:,Array,[,String,,,0X5,],;,_4,,,q8,,,s,,,_b,,,__,,,FV5,,,_6_,,,V,:,Array,[,Float,,,42,],),{,},},Class,U,{,},<EOF>''',
                101
            )
        )

    def test_1323(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _l5:dF15Bz{}Class s_{}Class N:_{vm(s,c,_,b:Array [String ,0X4E]){Continue ;}Val $K:_6;}Class _:Cg3A{}Class B{}''',
                '''Class,_l5,:,dF15Bz,{,},Class,s_,{,},Class,N,:,_,{,vm,(,s,,,c,,,_,,,b,:,Array,[,String,,,0X4E,],),{,Continue,;,},Val,$K,:,_6,;,},Class,_,:,Cg3A,{,},Class,B,{,},<EOF>''',
                101
            )
        )

    def test_1324(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _z_{Val _:Array [Array [Array [Int ,0X73],14],49];}Class H{}Class h_G_8:__{}Class _:t_bZ{}Class K_58_:__o{}''',
                '''Class,_z_,{,Val,_,:,Array,[,Array,[,Array,[,Int,,,0X73,],,,14,],,,49,],;,},Class,H,{,},Class,h_G_8,:,__,{,},Class,_,:,t_bZ,{,},Class,K_58_,:,__o,{,},<EOF>''',
                101
            )
        )

    def test_1325(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:___{Var $h,_,i6:Boolean ;Destructor (){} }Class _89__:zu_u5{}Class _0___{}Class ka{}Class _L______g0n{u(){} }''',
                '''Class,__,:,___,{,Var,$h,,,_,,,i6,:,Boolean,;,Destructor,(,),{,},},Class,_89__,:,zu_u5,{,},Class,_0___,{,},Class,ka,{,},Class,_L______g0n,{,u,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1326(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V4H{Constructor (hU:Array [Int ,0116];__2_,Mu43_WfC:Array [Array [Array [Array [Array [Int ,95],0116],95],05],0631_4];_,_u_8q:String ;X,e_,F4,_4I,_,_,a,_:Array [Array [String ,07_3],04]){} }''',
                '''Class,V4H,{,Constructor,(,hU,:,Array,[,Int,,,0116,],;,__2_,,,Mu43_WfC,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,95,],,,0116,],,,95,],,,05,],,,06314,],;,_,,,_u_8q,:,String,;,X,,,e_,,,F4,,,_4I,,,_,,,_,,,a,,,_,:,Array,[,Array,[,String,,,073,],,,04,],),{,},},<EOF>''',
                101
            )
        )

    def test_1327(self):
        self.assertTrue(
            TestLexer.test(
                '''Class qZa:_053{Val _1_,$__2:_;Constructor (E,I2J,_:Array [Array [Int ,047],0b1_01];K61:W;_,__8,_:Array [Array [Float ,067],0b10110]){} }''',
                '''Class,qZa,:,_053,{,Val,_1_,,,$__2,:,_,;,Constructor,(,E,,,I2J,,,_,:,Array,[,Array,[,Int,,,047,],,,0b101,],;,K61,:,W,;,_,,,__8,,,_,:,Array,[,Array,[,Float,,,067,],,,0b10110,],),{,},},<EOF>''',
                101
            )
        )

    def test_1328(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _4:_{$IQ(_,M_l,_:_){}aeW2(){} }Class _:z{Destructor (){}_Gw(_8,_,f_,_,k:_){}$K(){ {Continue ;Continue ;Continue ;} }Destructor (){} }Class _:__0U{}''',
                '''Class,_4,:,_,{,$IQ,(,_,,,M_l,,,_,:,_,),{,},aeW2,(,),{,},},Class,_,:,z,{,Destructor,(,),{,},_Gw,(,_8,,,_,,,f_,,,_,,,k,:,_,),{,},$K,(,),{,{,Continue,;,Continue,;,Continue,;,},},Destructor,(,),{,},},Class,_,:,__0U,{,},<EOF>''',
                101
            )
        )

    def test_1329(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _Y:_L{Var $_:Array [Array [String ,0B1_0],0b110];Val _g:Float ;Var $R:Array [Array [Array [Array [Int ,0xC2],0X2],9],053];}''',
                '''Class,_Y,:,_L,{,Var,$_,:,Array,[,Array,[,String,,,0B10,],,,0b110,],;,Val,_g,:,Float,;,Var,$R,:,Array,[,Array,[,Array,[,Array,[,Int,,,0xC2,],,,0X2,],,,9,],,,053,],;,},<EOF>''',
                101
            )
        )

    def test_1330(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Cd:Kq{$2(__,e1q7,Ig_,_9,_6I,u,b:Array [Float ,0b1_0_1_0];_,__:_;_:Float ;_:__5x;WU6,__,QK2b:Array [Float ,0b1000000];_7,cIt_,_:Array [Int ,0xB96_CAE];_,z,f_:String ){} }''',
                '''Class,Cd,:,Kq,{,$2,(,__,,,e1q7,,,Ig_,,,_9,,,_6I,,,u,,,b,:,Array,[,Float,,,0b1010,],;,_,,,__,:,_,;,_,:,Float,;,_,:,__5x,;,WU6,,,__,,,QK2b,:,Array,[,Float,,,0b1000000,],;,_7,,,cIt_,,,_,:,Array,[,Int,,,0xB96CAE,],;,_,,,z,,,f_,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_1331(self):
        self.assertTrue(
            TestLexer.test(
                '''Class V__:__{X(_,f_4,_:Array [Array [Array [Array [Float ,0b1_1_0_1],0X5A],0xE],0B1_1]){}Var $1:Float ;}Class _6{}Class _4{}Class m:ne{}Class Y__a{}Class C015Y:__N{$_(){}Var _,$_:Array [Boolean ,0B110011];}''',
                '''Class,V__,:,__,{,X,(,_,,,f_4,,,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0b1101,],,,0X5A,],,,0xE,],,,0B11,],),{,},Var,$1,:,Float,;,},Class,_6,{,},Class,_4,{,},Class,m,:,ne,{,},Class,Y__a,{,},Class,C015Y,:,__N,{,$_,(,),{,},Var,_,,,$_,:,Array,[,Boolean,,,0B110011,],;,},<EOF>''',
                101
            )
        )

    def test_1332(self):
        self.assertTrue(
            TestLexer.test(
                '''Class unU4___{}Class Q_3__:c{}Class _{}Class u_:_{}Class _026:_{Val $381__:Array [Array [Array [Boolean ,0b1011101],0b1],0b1];}Class z_{Destructor (){ {Val _BDf,VV1,_:i;} }Constructor (_:Array [Array [String ,76],01_2]){} }''',
                '''Class,unU4___,{,},Class,Q_3__,:,c,{,},Class,_,{,},Class,u_,:,_,{,},Class,_026,:,_,{,Val,$381__,:,Array,[,Array,[,Array,[,Boolean,,,0b1011101,],,,0b1,],,,0b1,],;,},Class,z_,{,Destructor,(,),{,{,Val,_BDf,,,VV1,,,_,:,i,;,},},Constructor,(,_,:,Array,[,Array,[,String,,,76,],,,012,],),{,},},<EOF>''',
                101
            )
        )

    def test_1333(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:Z{Constructor (i_,A,_:s;__,_,k_6:Array [String ,95]){} }Class pG6{Val l_,V,$54_:J;Var $k,A,h,$_7,$_,p:Array [Array [Array [Boolean ,02],02],0b10101];}''',
                '''Class,__,:,Z,{,Constructor,(,i_,,,A,,,_,:,s,;,__,,,_,,,k_6,:,Array,[,String,,,95,],),{,},},Class,pG6,{,Val,l_,,,V,,,$54_,:,J,;,Var,$k,,,A,,,h,,,$_7,,,$_,,,p,:,Array,[,Array,[,Array,[,Boolean,,,02,],,,02,],,,0b10101,],;,},<EOF>''',
                101
            )
        )

    def test_1334(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Hg13F{_68(_3:_N_h__;__0__,sO,f,H:Array [Array [Int ,0b1],03_7_1];_z:String ;w_:Array [Array [Array [Int ,0x5_501],0x56],5_3];_:String ;G_:__;a_7:v){} }''',
                '''Class,Hg13F,{,_68,(,_3,:,_N_h__,;,__0__,,,sO,,,f,,,H,:,Array,[,Array,[,Int,,,0b1,],,,0371,],;,_z,:,String,;,w_,:,Array,[,Array,[,Array,[,Int,,,0x5501,],,,0x56,],,,53,],;,_,:,String,;,G_,:,__,;,a_7,:,v,),{,},},<EOF>''',
                101
            )
        )

    def test_1335(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _bS_{Val X,w3:Array [Array [Array [Int ,0B1],66],0b100001];Destructor (){Var N0:Int ;_::$163();} }Class __{}Class q3:x{}''',
                '''Class,_bS_,{,Val,X,,,w3,:,Array,[,Array,[,Array,[,Int,,,0B1,],,,66,],,,0b100001,],;,Destructor,(,),{,Var,N0,:,Int,;,_,::,$163,(,),;,},},Class,__,{,},Class,q3,:,x,{,},<EOF>''',
                101
            )
        )

    def test_1336(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __0:m{I3(_,Y_M5,_ZrYnE_:Array [Float ,0x4];_Z,TR:Array [Array [Boolean ,010],0xAF]){}Val $r:_;}Class _{}Class N_:R{}''',
                '''Class,__0,:,m,{,I3,(,_,,,Y_M5,,,_ZrYnE_,:,Array,[,Float,,,0x4,],;,_Z,,,TR,:,Array,[,Array,[,Boolean,,,010,],,,0xAF,],),{,},Val,$r,:,_,;,},Class,_,{,},Class,N_,:,R,{,},<EOF>''',
                101
            )
        )

    def test_1337(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T9_:k{}Class _:_{}Class _3_:__{Var $_,f,Xn7B_,$___02c,$n:Boolean ;}Class g:D{Destructor (){}$hzq(){} }Class C7{Constructor (){} }Class Y357{}Class B{}Class q_I{Destructor (){}Constructor (){} }''',
                '''Class,T9_,:,k,{,},Class,_,:,_,{,},Class,_3_,:,__,{,Var,$_,,,f,,,Xn7B_,,,$___02c,,,$n,:,Boolean,;,},Class,g,:,D,{,Destructor,(,),{,},$hzq,(,),{,},},Class,C7,{,Constructor,(,),{,},},Class,Y357,{,},Class,B,{,},Class,q_I,{,Destructor,(,),{,},Constructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1338(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var _O,__2K__:Float ;p(_09,q,_1,__wG:Array [Array [Int ,12],0XC]){} }Class _:n{Val $j9G:Array [Array [Int ,0x7_B],06];Val $32_,$hK,_L__H:R;}Class _{PG(_:Int ;Y_:Array [Int ,0x7]){}Val __oE:Float ;}''',
                '''Class,_,{,Var,_O,,,__2K__,:,Float,;,p,(,_09,,,q,,,_1,,,__wG,:,Array,[,Array,[,Int,,,12,],,,0XC,],),{,},},Class,_,:,n,{,Val,$j9G,:,Array,[,Array,[,Int,,,0x7B,],,,06,],;,Val,$32_,,,$hK,,,_L__H,:,R,;,},Class,_,{,PG,(,_,:,Int,;,Y_,:,Array,[,Int,,,0x7,],),{,},Val,__oE,:,Float,;,},<EOF>''',
                101
            )
        )

    def test_1339(self):
        self.assertTrue(
            TestLexer.test(
                '''Class n:z{}Class dy5:_{Constructor (E,_2,uD:Array [Array [Array [Array [Array [Float ,0b1],03],0b110110],0B111000],0b1]){} }Class c{Var _,E:p__;}''',
                '''Class,n,:,z,{,},Class,dy5,:,_,{,Constructor,(,E,,,_2,,,uD,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1,],,,03,],,,0b110110,],,,0B111000,],,,0b1,],),{,},},Class,c,{,Var,_,,,E,:,p__,;,},<EOF>''',
                101
            )
        )

    def test_1340(self):
        self.assertTrue(
            TestLexer.test(
                '''Class iG5{Var _u,__:Array [Array [String ,0X12],0X8_2_0_9];Destructor (){}c8(){} }Class V{Var $_,$D_,$_,$____:__a;}Class j0_3{}Class L{Val M_,q:__;Constructor (){}Constructor (){Continue ;Break ;} }Class N:k_v{}''',
                '''Class,iG5,{,Var,_u,,,__,:,Array,[,Array,[,String,,,0X12,],,,0X8209,],;,Destructor,(,),{,},c8,(,),{,},},Class,V,{,Var,$_,,,$D_,,,$_,,,$____,:,__a,;,},Class,j0_3,{,},Class,L,{,Val,M_,,,q,:,__,;,Constructor,(,),{,},Constructor,(,),{,Continue,;,Break,;,},},Class,N,:,k_v,{,},<EOF>''',
                101
            )
        )

    def test_1341(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _g5{Var PB7U7s,d76,$2h6c4,x9qzC:Array [Array [String ,50],0B11111];}Class __28:R1o{Constructor (){}$_(_x:Float ;s,k:Array [String ,0b1]){} }''',
                '''Class,_g5,{,Var,PB7U7s,,,d76,,,$2h6c4,,,x9qzC,:,Array,[,Array,[,String,,,50,],,,0B11111,],;,},Class,__28,:,R1o,{,Constructor,(,),{,},$_,(,_x,:,Float,;,s,,,k,:,Array,[,String,,,0b1,],),{,},},<EOF>''',
                101
            )
        )

    def test_1342(self):
        self.assertTrue(
            TestLexer.test(
                '''Class c:_{Destructor (){} }Class pu:_{Val sh,$_,E,_1_7,$_0,P7,_:Array [String ,0X64];}Class __6{}Class _:R{}Class _5_:_{Var _,$1:Array [Array [Array [Boolean ,3],01],015_6];}''',
                '''Class,c,:,_,{,Destructor,(,),{,},},Class,pu,:,_,{,Val,sh,,,$_,,,E,,,_1_7,,,$_0,,,P7,,,_,:,Array,[,String,,,0X64,],;,},Class,__6,{,},Class,_,:,R,{,},Class,_5_,:,_,{,Var,_,,,$1,:,Array,[,Array,[,Array,[,Boolean,,,3,],,,01,],,,0156,],;,},<EOF>''',
                101
            )
        )

    def test_1343(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:h__{Val I_v_A6h9:Array [Int ,0133];_(){Continue ;}Var ___,_:Array [Array [Array [Array [Boolean ,0xB],0XD],07_2],0133];Destructor (){} }Class w9:k7{}''',
                '''Class,_,:,h__,{,Val,I_v_A6h9,:,Array,[,Int,,,0133,],;,_,(,),{,Continue,;,},Var,___,,,_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0xB,],,,0XD,],,,072,],,,0133,],;,Destructor,(,),{,},},Class,w9,:,k7,{,},<EOF>''',
                101
            )
        )

    def test_1344(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C:_{}Class _:L{Var __,$8_2_,_v,nk:_6;g_C_(){}$Os(){}Var $i_:Array [Array [Array [Array [String ,0B1],0x19],86],33_3_1];}''',
                '''Class,C,:,_,{,},Class,_,:,L,{,Var,__,,,$8_2_,,,_v,,,nk,:,_6,;,g_C_,(,),{,},$Os,(,),{,},Var,$i_,:,Array,[,Array,[,Array,[,Array,[,String,,,0B1,],,,0x19,],,,86,],,,3331,],;,},<EOF>''',
                101
            )
        )

    def test_1345(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val $0,H6,__:Array [String ,055];Constructor (_:Int ){Val _:String ;}Val z_:String ;i(_,_:_){} }Class _:_{}''',
                '''Class,_,{,Val,$0,,,H6,,,__,:,Array,[,String,,,055,],;,Constructor,(,_,:,Int,),{,Val,_,:,String,;,},Val,z_,:,String,;,i,(,_,,,_,:,_,),{,},},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1346(self):
        self.assertTrue(
            TestLexer.test(
                '''Class tS_:j{}Class _8_:_0{Constructor (_X__Y_,_,o6jY:Array [Array [Array [Float ,02],0b1],0X2C];d_1,a,_90n,_:String ;_0,Q:Int ;J0e:u;___A:Int ;_W:g){}Destructor (){} }''',
                '''Class,tS_,:,j,{,},Class,_8_,:,_0,{,Constructor,(,_X__Y_,,,_,,,o6jY,:,Array,[,Array,[,Array,[,Float,,,02,],,,0b1,],,,0X2C,],;,d_1,,,a,,,_90n,,,_,:,String,;,_0,,,Q,:,Int,;,J0e,:,u,;,___A,:,Int,;,_W,:,g,),{,},Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1347(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:t{}Class HU___{$_(W:Array [Array [Float ,3],0X9];_3:_3;M,_:String ;w:Int ;_,K:Array [Array [Array [Array [Int ,0x23],0b1],0b1_10_10],0X8]){Break ;}Var _,___,_c:b;}''',
                '''Class,_,:,t,{,},Class,HU___,{,$_,(,W,:,Array,[,Array,[,Float,,,3,],,,0X9,],;,_3,:,_3,;,M,,,_,:,String,;,w,:,Int,;,_,,,K,:,Array,[,Array,[,Array,[,Array,[,Int,,,0x23,],,,0b1,],,,0b11010,],,,0X8,],),{,Break,;,},Var,_,,,___,,,_c,:,b,;,},<EOF>''',
                101
            )
        )

    def test_1348(self):
        self.assertTrue(
            TestLexer.test(
                '''Class p7:__{Var $I_1p,$vB_,R:Array [Array [Array [Array [Array [Array [String ,64],0B1000111],0X51],13],0b1],05];}Class _4:b{}''',
                '''Class,p7,:,__,{,Var,$I_1p,,,$vB_,,,R,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,64,],,,0B1000111,],,,0X51,],,,13,],,,0b1,],,,05,],;,},Class,_4,:,b,{,},<EOF>''',
                101
            )
        )

    def test_1349(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:___r_H0_{Val $_,v,_8:u;}Class _{Constructor (_,__2,N6,_:Array [Array [String ,0x4],67];_,__s7_:Int ;_,_:E;u1,_:Array [Array [Float ,03],0136]){} }''',
                '''Class,_,:,___r_H0_,{,Val,$_,,,v,,,_8,:,u,;,},Class,_,{,Constructor,(,_,,,__2,,,N6,,,_,:,Array,[,Array,[,String,,,0x4,],,,67,],;,_,,,__s7_,:,Int,;,_,,,_,:,E,;,u1,,,_,:,Array,[,Array,[,Float,,,03,],,,0136,],),{,},},<EOF>''',
                101
            )
        )

    def test_1350(self):
        self.assertTrue(
            TestLexer.test(
                '''Class H:L_{Val K:Int ;Constructor (_,V:_;b:ZA;_:B;L,_,S_:Array [Array [Array [Boolean ,8_3],0b1],0x38]){}Val $l3a,$6__:_;}Class y{tR__j(){}Val $7,_7,$9:_;}''',
                '''Class,H,:,L_,{,Val,K,:,Int,;,Constructor,(,_,,,V,:,_,;,b,:,ZA,;,_,:,B,;,L,,,_,,,S_,:,Array,[,Array,[,Array,[,Boolean,,,83,],,,0b1,],,,0x38,],),{,},Val,$l3a,,,$6__,:,_,;,},Class,y,{,tR__j,(,),{,},Val,$7,,,_7,,,$9,:,_,;,},<EOF>''',
                101
            )
        )

    def test_1351(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _1{}Class _:J{Val $_:_;Constructor (_33:Array [String ,0x3D];_:Boolean ){Return ;}Constructor (m___:Boolean ;K:Array [Array [Array [Array [Boolean ,0x3],82_0_8],910_5],0142];__C_IG:Array [Array [Array [Array [Array [Array [String ,0B1],0b1_0_0],0B11111],0142],0b1_0_1_0],0x3D]){} }Class _{}''',
                '''Class,_1,{,},Class,_,:,J,{,Val,$_,:,_,;,Constructor,(,_33,:,Array,[,String,,,0x3D,],;,_,:,Boolean,),{,Return,;,},Constructor,(,m___,:,Boolean,;,K,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x3,],,,8208,],,,9105,],,,0142,],;,__C_IG,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B1,],,,0b100,],,,0B11111,],,,0142,],,,0b1010,],,,0x3D,],),{,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_1352(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _K3__:J_{Val $4_:Int ;}Class S5_:TX{Var ___:Int ;$TH(_,K_:Float ){ {Var z_5,t_:Array [Array [Array [String ,84],0x60],0B11];}_IT::$W73.V()._28().K._();Break ;Val a_,_C,nG_:T9F;} }''',
                '''Class,_K3__,:,J_,{,Val,$4_,:,Int,;,},Class,S5_,:,TX,{,Var,___,:,Int,;,$TH,(,_,,,K_,:,Float,),{,{,Var,z_5,,,t_,:,Array,[,Array,[,Array,[,String,,,84,],,,0x60,],,,0B11,],;,},_IT,::,$W73,.,V,(,),.,_28,(,),.,K,.,_,(,),;,Break,;,Val,a_,,,_C,,,nG_,:,T9F,;,},},<EOF>''',
                101
            )
        )

    def test_1353(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _58:_{Destructor (){} }Class _:P5{Constructor (p6,_,U:x;_:_;_BG:Array [Float ,0B1_1_1_1];m_8_,_,__1r:Boolean ){} }''',
                '''Class,_58,:,_,{,Destructor,(,),{,},},Class,_,:,P5,{,Constructor,(,p6,,,_,,,U,:,x,;,_,:,_,;,_BG,:,Array,[,Float,,,0B1111,],;,m_8_,,,_,,,__1r,:,Boolean,),{,},},<EOF>''',
                101
            )
        )

    def test_1354(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _z{}Class U:_Y{_(f:Array [Array [Array [Boolean ,0x5A],0X17],0x5A];_,g,_W_,c_,H:Array [Array [Array [Array [Boolean ,024],0b1],04],0b1]){} }Class _{}Class G:v_{}''',
                '''Class,_z,{,},Class,U,:,_Y,{,_,(,f,:,Array,[,Array,[,Array,[,Boolean,,,0x5A,],,,0X17,],,,0x5A,],;,_,,,g,,,_W_,,,c_,,,H,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,024,],,,0b1,],,,04,],,,0b1,],),{,},},Class,_,{,},Class,G,:,v_,{,},<EOF>''',
                101
            )
        )

    def test_1355(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __L9:h_3{Var sq,_2,X,An0__4,_,$_:Array [Array [Float ,060],27_4];Constructor (_,o3_6Mc,_R8:Array [Array [Int ,060],51]){Break ;} }Class _Z_4:_0__Y{}Class A{}''',
                '''Class,__L9,:,h_3,{,Var,sq,,,_2,,,X,,,An0__4,,,_,,,$_,:,Array,[,Array,[,Float,,,060,],,,274,],;,Constructor,(,_,,,o3_6Mc,,,_R8,:,Array,[,Array,[,Int,,,060,],,,51,],),{,Break,;,},},Class,_Z_4,:,_0__Y,{,},Class,A,{,},<EOF>''',
                101
            )
        )

    def test_1356(self):
        self.assertTrue(
            TestLexer.test(
                '''Class eY2L{}Class _{}Class v{Val _,$_z:Array [Array [Array [Array [Array [Array [Array [Int ,054_4_6_0],07_00],52],0B1],0x13],012],04];}''',
                '''Class,eY2L,{,},Class,_,{,},Class,v,{,Val,_,,,$_z,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,054460,],,,0700,],,,52,],,,0B1,],,,0x13,],,,012,],,,04,],;,},<EOF>''',
                101
            )
        )

    def test_1357(self):
        self.assertTrue(
            TestLexer.test(
                '''Class u{Constructor (_:Array [Array [Float ,013],0xB_3_3];_y4,Wky_7,_:Array [Array [Array [String ,053_636],01],0xD];d:String ;v:Array [Boolean ,0x7D_1C]){}Val _1____g,$_:_;}''',
                '''Class,u,{,Constructor,(,_,:,Array,[,Array,[,Float,,,013,],,,0xB33,],;,_y4,,,Wky_7,,,_,:,Array,[,Array,[,Array,[,String,,,053636,],,,01,],,,0xD,],;,d,:,String,;,v,:,Array,[,Boolean,,,0x7D1C,],),{,},Val,_1____g,,,$_,:,_,;,},<EOF>''',
                101
            )
        )

    def test_1358(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class __{}Class _:m{Constructor (H2g_cY:String ){Continue ;}Var $0,M,ZvQ_,$__9_,$__,$t,$A_U:___;Destructor (){} }''',
                '''Class,_,:,_,{,},Class,__,{,},Class,_,:,m,{,Constructor,(,H2g_cY,:,String,),{,Continue,;,},Var,$0,,,M,,,ZvQ_,,,$__9_,,,$__,,,$t,,,$A_U,:,___,;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1359(self):
        self.assertTrue(
            TestLexer.test(
                '''Class G:u{Constructor (f:Array [Array [Array [String ,0X2],0X1A],0b110111]){}Constructor (_:Boolean ;_V,_62_1:_){}Val $_,_4:Boolean ;Constructor (T_eK:String ){} }Class _:_{}''',
                '''Class,G,:,u,{,Constructor,(,f,:,Array,[,Array,[,Array,[,String,,,0X2,],,,0X1A,],,,0b110111,],),{,},Constructor,(,_,:,Boolean,;,_V,,,_62_1,:,_,),{,},Val,$_,,,_4,:,Boolean,;,Constructor,(,T_eK,:,String,),{,},},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1360(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Val t:Int ;}Class m__{Constructor (){Var __,_M__,b476,_v:Boolean ;}Var r,b,$U4__:U3;}Class __:jx_{Destructor (){} }''',
                '''Class,_,{,Val,t,:,Int,;,},Class,m__,{,Constructor,(,),{,Var,__,,,_M__,,,b476,,,_v,:,Boolean,;,},Var,r,,,b,,,$U4__,:,U3,;,},Class,__,:,jx_,{,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1361(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k__Pi:_8{Destructor (){}Constructor (E3:A;g:Array [Boolean ,3]){} }Class m4u7L:c_MW{}Class e:O{}Class t9{}Class b{}''',
                '''Class,k__Pi,:,_8,{,Destructor,(,),{,},Constructor,(,E3,:,A,;,g,:,Array,[,Boolean,,,3,],),{,},},Class,m4u7L,:,c_MW,{,},Class,e,:,O,{,},Class,t9,{,},Class,b,{,},<EOF>''',
                101
            )
        )

    def test_1362(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _T{}Class _q7_{G(O,x,_,__:Array [Array [Array [Array [Array [Array [Boolean ,66],66],0x9_5],02_0_27_2],0b100110],66]){} }''',
                '''Class,_T,{,},Class,_q7_,{,G,(,O,,,x,,,_,,,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,66,],,,66,],,,0x95,],,,020272,],,,0b100110,],,,66,],),{,},},<EOF>''',
                101
            )
        )

    def test_1363(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X:G1{Destructor (){Continue ;}Destructor (){}Destructor (){}Val $_:D;Constructor (){}$m3(X,_:Boolean ){}Destructor (){ {} }}''',
                '''Class,X,:,G1,{,Destructor,(,),{,Continue,;,},Destructor,(,),{,},Destructor,(,),{,},Val,$_,:,D,;,Constructor,(,),{,},$m3,(,X,,,_,:,Boolean,),{,},Destructor,(,),{,{,},},},<EOF>''',
                101
            )
        )

    def test_1364(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w{}Class z9v{}Class K:_{_H(){}Constructor (){Var _:Array [Array [Array [Array [Boolean ,0X2B],0x4B],047],06];}Constructor (B,__,_7__:Array [Boolean ,0X45_0]){} }''',
                '''Class,w,{,},Class,z9v,{,},Class,K,:,_,{,_H,(,),{,},Constructor,(,),{,Var,_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X2B,],,,0x4B,],,,047,],,,06,],;,},Constructor,(,B,,,__,,,_7__,:,Array,[,Boolean,,,0X450,],),{,},},<EOF>''',
                101
            )
        )

    def test_1365(self):
        self.assertTrue(
            TestLexer.test(
                '''Class s{Var $8:l;Constructor (k,y:Array [Array [Float ,045],0b1111];_:Int ;_2:j;v1:Array [Boolean ,045];_,I_,J,o5,W7_,n4,Mpm,_pF:Array [Int ,045]){}Wm(M__,o:f_;_:Array [Array [Boolean ,045],0x31]){}Destructor (){} }Class _0:_{Constructor (Y1zB:g;_,o5:I;_:Boolean ;qV_,a_:B){} }''',
                '''Class,s,{,Var,$8,:,l,;,Constructor,(,k,,,y,:,Array,[,Array,[,Float,,,045,],,,0b1111,],;,_,:,Int,;,_2,:,j,;,v1,:,Array,[,Boolean,,,045,],;,_,,,I_,,,J,,,o5,,,W7_,,,n4,,,Mpm,,,_pF,:,Array,[,Int,,,045,],),{,},Wm,(,M__,,,o,:,f_,;,_,:,Array,[,Array,[,Boolean,,,045,],,,0x31,],),{,},Destructor,(,),{,},},Class,_0,:,_,{,Constructor,(,Y1zB,:,g,;,_,,,o5,:,I,;,_,:,Boolean,;,qV_,,,a_,:,B,),{,},},<EOF>''',
                101
            )
        )

    def test_1366(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Y{$4c(_P:Boolean ){} }Class __1_s{}Class _7:_4qe6{Constructor (){Var __:Int ;} }Class _:_{Var $989,__,S7S_:Boolean ;}''',
                '''Class,Y,{,$4c,(,_P,:,Boolean,),{,},},Class,__1_s,{,},Class,_7,:,_4qe6,{,Constructor,(,),{,Var,__,:,Int,;,},},Class,_,:,_,{,Var,$989,,,__,,,S7S_,:,Boolean,;,},<EOF>''',
                101
            )
        )

    def test_1367(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class N_{$_a(I,_,_64J,kl,B7,D:r6F7_;ii:_;Vx,_:Boolean ;P2h,Jd3_:Array [Boolean ,92];u:Boolean ){Break ;Continue ;} }Class _{}''',
                '''Class,_,{,},Class,N_,{,$_a,(,I,,,_,,,_64J,,,kl,,,B7,,,D,:,r6F7_,;,ii,:,_,;,Vx,,,_,:,Boolean,;,P2h,,,Jd3_,:,Array,[,Boolean,,,92,],;,u,:,Boolean,),{,Break,;,Continue,;,},},Class,_,{,},<EOF>''',
                101
            )
        )

    def test_1368(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _j{Constructor (L,_,g__:Array [Array [Int ,0X2],0X37];g3:Array [Array [Array [Boolean ,0x1C],062],062];w:Array [Boolean ,03_7];E2:String ){} }''',
                '''Class,_j,{,Constructor,(,L,,,_,,,g__,:,Array,[,Array,[,Int,,,0X2,],,,0X37,],;,g3,:,Array,[,Array,[,Array,[,Boolean,,,0x1C,],,,062,],,,062,],;,w,:,Array,[,Boolean,,,037,],;,E2,:,String,),{,},},<EOF>''',
                101
            )
        )

    def test_1369(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k_:w6{Constructor (){Val _5:String ;}Var CF5rBpe:_;}Class V_Me{__(Z2,B,_T,h_:Array [Array [Int ,0133],0xD]){} }''',
                '''Class,k_,:,w6,{,Constructor,(,),{,Val,_5,:,String,;,},Var,CF5rBpe,:,_,;,},Class,V_Me,{,__,(,Z2,,,B,,,_T,,,h_,:,Array,[,Array,[,Int,,,0133,],,,0xD,],),{,},},<EOF>''',
                101
            )
        )

    def test_1370(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_U{Val Z:n;Val _,$_9v8:Array [Array [Array [Array [Array [Float ,0b1],0b11],053],053],0b1];}Class F:z{Val $3_p2_:Int ;$W58(_,_n7:Boolean ;_9_:Array [Array [String ,28],9]){} }''',
                '''Class,_,:,_U,{,Val,Z,:,n,;,Val,_,,,$_9v8,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1,],,,0b11,],,,053,],,,053,],,,0b1,],;,},Class,F,:,z,{,Val,$3_p2_,:,Int,;,$W58,(,_,,,_n7,:,Boolean,;,_9_,:,Array,[,Array,[,String,,,28,],,,9,],),{,},},<EOF>''',
                101
            )
        )

    def test_1371(self):
        self.assertTrue(
            TestLexer.test(
                '''Class dm{}Class _{}Class _l82{Var z,$1,$_:Array [Boolean ,0x55];Constructor (d:V){}Val $_r_:hL;}Class n{}Class _:_{}''',
                '''Class,dm,{,},Class,_,{,},Class,_l82,{,Var,z,,,$1,,,$_,:,Array,[,Boolean,,,0x55,],;,Constructor,(,d,:,V,),{,},Val,$_r_,:,hL,;,},Class,n,{,},Class,_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1372(self):
        self.assertTrue(
            TestLexer.test(
                '''Class M_:G{Zp36(_4,_G_,_7R,_,J,_:_33_;_7,n,_:String ){}Constructor (kL_,_Z,_,n_,Y,_,O,o3:String ;J,_,__,Z,q_,Pj1:Int ;M,x_:Array [String ,03]){} }Class _:t{}''',
                '''Class,M_,:,G,{,Zp36,(,_4,,,_G_,,,_7R,,,_,,,J,,,_,:,_33_,;,_7,,,n,,,_,:,String,),{,},Constructor,(,kL_,,,_Z,,,_,,,n_,,,Y,,,_,,,O,,,o3,:,String,;,J,,,_,,,__,,,Z,,,q_,,,Pj1,:,Int,;,M,,,x_,:,Array,[,String,,,03,],),{,},},Class,_,:,t,{,},<EOF>''',
                101
            )
        )

    def test_1373(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var $5_3__9:U;}Class AU__{Constructor (){Break ;}Constructor (){Continue ;} }Class _r:U{G7(u,Qp:_N3){} }Class _7:_1_{Destructor (){Continue ;} }Class _7_0H9_p7_8:z{}Class __{}''',
                '''Class,_,{,Var,$5_3__9,:,U,;,},Class,AU__,{,Constructor,(,),{,Break,;,},Constructor,(,),{,Continue,;,},},Class,_r,:,U,{,G7,(,u,,,Qp,:,_N3,),{,},},Class,_7,:,_1_,{,Destructor,(,),{,Continue,;,},},Class,_7_0H9_p7_8,:,z,{,},Class,__,{,},<EOF>''',
                101
            )
        )

    def test_1374(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class _:P{Constructor (_,__u58_:Float ;H_:D5;b,A_:Array [Int ,0b10];_EV,A_,__R:_2__){} }Class _S{Destructor (){}Val $__:String ;Constructor (){Break ;} }''',
                '''Class,_,:,_,{,},Class,_,:,P,{,Constructor,(,_,,,__u58_,:,Float,;,H_,:,D5,;,b,,,A_,:,Array,[,Int,,,0b10,],;,_EV,,,A_,,,__R,:,_2__,),{,},},Class,_S,{,Destructor,(,),{,},Val,$__,:,String,;,Constructor,(,),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_1375(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Zy5W_:_8V_{Constructor (Z0_:String ;Hu,_G,E_:String ;N,n,_f,B,__,_G,D:String ;__:Array [Array [Float ,7],045]){} }''',
                '''Class,Zy5W_,:,_8V_,{,Constructor,(,Z0_,:,String,;,Hu,,,_G,,,E_,:,String,;,N,,,n,,,_f,,,B,,,__,,,_G,,,D,:,String,;,__,:,Array,[,Array,[,Float,,,7,],,,045,],),{,},},<EOF>''',
                101
            )
        )

    def test_1376(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_79s{}Class _Kg7:_{Var g3:Array [Array [Int ,0x9],5];Destructor (){} }Class BS:_s___{Var $4r:String ;}Class n{Val _:String ;}''',
                '''Class,_,:,_79s,{,},Class,_Kg7,:,_,{,Var,g3,:,Array,[,Array,[,Int,,,0x9,],,,5,],;,Destructor,(,),{,},},Class,BS,:,_s___,{,Var,$4r,:,String,;,},Class,n,{,Val,_,:,String,;,},<EOF>''',
                101
            )
        )

    def test_1377(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _0{Constructor (__:Array [Array [Array [Array [Array [Boolean ,21],0x41],21],5],016_4]){}$w(q_:Array [Array [Int ,0B11],01];_,uj:Array [Boolean ,013]){} }''',
                '''Class,_0,{,Constructor,(,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,21,],,,0x41,],,,21,],,,5,],,,0164,],),{,},$w,(,q_,:,Array,[,Array,[,Int,,,0B11,],,,01,],;,_,,,uj,:,Array,[,Boolean,,,013,],),{,},},<EOF>''',
                101
            )
        )

    def test_1378(self):
        self.assertTrue(
            TestLexer.test(
                '''Class w{Constructor (_,v_:_){} }Class _:O{Constructor (_M:Int ;_:Array [Boolean ,0x49];P:Array [Array [Float ,75],0x4B];_,_30,__0:RLW){}Destructor (){} }Class __6y{}''',
                '''Class,w,{,Constructor,(,_,,,v_,:,_,),{,},},Class,_,:,O,{,Constructor,(,_M,:,Int,;,_,:,Array,[,Boolean,,,0x49,],;,P,:,Array,[,Array,[,Float,,,75,],,,0x4B,],;,_,,,_30,,,__0,:,RLW,),{,},Destructor,(,),{,},},Class,__6y,{,},<EOF>''',
                101
            )
        )

    def test_1379(self):
        self.assertTrue(
            TestLexer.test(
                '''Class x:__{}Class _7:F{Constructor (T:Array [Array [Array [Array [Array [String ,0X44],0x8],0B1],5],0B1];_:Boolean ){}Var S68t_s_:Boolean ;Destructor (){} }''',
                '''Class,x,:,__,{,},Class,_7,:,F,{,Constructor,(,T,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X44,],,,0x8,],,,0B1,],,,5,],,,0B1,],;,_,:,Boolean,),{,},Var,S68t_s_,:,Boolean,;,Destructor,(,),{,},},<EOF>''',
                101
            )
        )

    def test_1380(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _xi_5:_M{$_(_8,_:Int ;_5:Array [Int ,0X2];W__,k5_P,mc_5,d,_I,_,_,_,_7_:Array [Array [Array [String ,0X4],338_8],0x15]){}Var oo:Array [Float ,55];}''',
                '''Class,_xi_5,:,_M,{,$_,(,_8,,,_,:,Int,;,_5,:,Array,[,Int,,,0X2,],;,W__,,,k5_P,,,mc_5,,,d,,,_I,,,_,,,_,,,_,,,_7_,:,Array,[,Array,[,Array,[,String,,,0X4,],,,3388,],,,0x15,],),{,},Var,oo,:,Array,[,Float,,,55,],;,},<EOF>''',
                101
            )
        )

    def test_1381(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k:_z{Val $03,$W,$B:_;}Class _60r{}Class A_:i{Constructor (){}Constructor (_:Array [String ,0X63];_,p:G4;___5_x:Boolean ){} }Class __M{Val $__:Float ;}Class b_7_:_{}''',
                '''Class,k,:,_z,{,Val,$03,,,$W,,,$B,:,_,;,},Class,_60r,{,},Class,A_,:,i,{,Constructor,(,),{,},Constructor,(,_,:,Array,[,String,,,0X63,],;,_,,,p,:,G4,;,___5_x,:,Boolean,),{,},},Class,__M,{,Val,$__,:,Float,;,},Class,b_7_,:,_,{,},<EOF>''',
                101
            )
        )

    def test_1382(self):
        self.assertTrue(
            TestLexer.test(
                '''Class i:_8371{$0(_72_4m:_9;tk,_,K:Array [Boolean ,0B1_1];__3,_S:Array [Array [Boolean ,05],87];_,Q:String ){}$7(l7_:Array [Array [Array [Array [Boolean ,87],07_5],0b111101],041_6];q:l;__,D,_7:E;A:Array [Array [Array [Array [Float ,87],05],8],02]){Break ;} }''',
                '''Class,i,:,_8371,{,$0,(,_72_4m,:,_9,;,tk,,,_,,,K,:,Array,[,Boolean,,,0B11,],;,__3,,,_S,:,Array,[,Array,[,Boolean,,,05,],,,87,],;,_,,,Q,:,String,),{,},$7,(,l7_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,87,],,,075,],,,0b111101,],,,0416,],;,q,:,l,;,__,,,D,,,_7,:,E,;,A,:,Array,[,Array,[,Array,[,Array,[,Float,,,87,],,,05,],,,8,],,,02,],),{,Break,;,},},<EOF>''',
                101
            )
        )

    def test_1383(self):
        self.assertTrue(
            TestLexer.test(
                '''Class h:L_{}Class _{Val d:N9_;}Class Z:U8R_6{$1___(_l_2:Int ){}Val $R:String ;Val $_:Array [Float ,0x6_9C_0_B];}Class R:_R_{}Class _65{}''',
                '''Class,h,:,L_,{,},Class,_,{,Val,d,:,N9_,;,},Class,Z,:,U8R_6,{,$1___,(,_l_2,:,Int,),{,},Val,$R,:,String,;,Val,$_,:,Array,[,Float,,,0x69C0B,],;,},Class,R,:,_R_,{,},Class,_65,{,},<EOF>''',
                101
            )
        )

    def test_1384(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m_7_w:_{Destructor (){}Val M7,___4,_,$i:Array [Float ,0B101110];}Class x:_zi{}Class k3__{Val _36:Array [Float ,0b101000];Constructor (_4i_:Array [Array [Array [String ,2],0b1],0X4C];_,__:Boolean ;P:Array [Array [Array [Int ,4],0136],0136]){} }''',
                '''Class,m_7_w,:,_,{,Destructor,(,),{,},Val,M7,,,___4,,,_,,,$i,:,Array,[,Float,,,0B101110,],;,},Class,x,:,_zi,{,},Class,k3__,{,Val,_36,:,Array,[,Float,,,0b101000,],;,Constructor,(,_4i_,:,Array,[,Array,[,Array,[,String,,,2,],,,0b1,],,,0X4C,],;,_,,,__,:,Boolean,;,P,:,Array,[,Array,[,Array,[,Int,,,4,],,,0136,],,,0136,],),{,},},<EOF>''',
                101
            )
        )

    def test_1385(self):
        self.assertTrue(
            TestLexer.test(
                '''Class F9_2_3_{Constructor (H,h_,U6k,_,I,_9:Array [Array [Array [Float ,0b1],3],0b1];__,oP_1,B4H,I_,Y:Array [Boolean ,33];_3,e1_6:N){} }''',
                '''Class,F9_2_3_,{,Constructor,(,H,,,h_,,,U6k,,,_,,,I,,,_9,:,Array,[,Array,[,Array,[,Float,,,0b1,],,,3,],,,0b1,],;,__,,,oP_1,,,B4H,,,I_,,,Y,:,Array,[,Boolean,,,33,],;,_3,,,e1_6,:,N,),{,},},<EOF>''',
                101
            )
        )
