import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_block_comment(self):
        input = r'''
##
    Block of comment
##
 '''
        expect = r'<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 100))

    def test_lowercase_id(self):
        input = r'abc'
        expect = r'abc,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 101))

    def test_mixed_alphabet_id(self):
        input = r'aCBbdc'
        expect = r'aCBbdc,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 102))

    def test_mixed_alphanummeric_id(self):
        input = r'aAsVN3'
        expect = r'aAsVN3,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 103))

    def test_keyword_1(self):
        input = r'Break Continue If Elseif Else'
        expect = r'Break,Continue,If,Elseif,Else,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 111))

    def test_keyword_2(self):
        input = r'Foreach True False Array In'
        expect = r'Foreach,True,False,Array,In,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 112))

    def test_keyword_3(self):
        input = r'Int Float Boolean String Return'
        expect = r'Int,Float,Boolean,String,Return,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 113))

    def test_keyword_4(self):
        input = r'Null Class Val Var'
        expect = r'Null,Class,Val,Var,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 114))

    def test_keyword_5(self):
        input = r'Constructor Destructor New By'
        expect = r'Constructor,Destructor,New,By,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 115))

    def test_keyword_6(self):
        input = r'Val Var By'
        expect = r'Val,Var,By,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 116))

    def test_operator_1(self):
        input = r'+ - * / %'
        expect = r'+,-,*,/,%,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 121))

    def test_operator_2(self):
        input = r'! && || == ='
        expect = r'!,&&,||,==,=,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 122))

    def test_operator_3(self):
        input = r'!= > <= > >='
        expect = r'!=,>,<=,>,>=,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 123))

    def test_operator_4(self):
        input = r'==. +. . :: New'
        expect = r'==.,+.,.,::,New,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 124))

    def test_separator(self):
        input = r'( ) [ ] . , ; { }'
        expect = r'(,),[,],.,,,;,{,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 130))

    def test_decimal_int(self):
        input = r'123123'
        expect = r'123123,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 131))

    def test_binary_int(self):
        input = r'0b00000001'
        expect = r'0b00000001,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 132))

    def test_hex_int(self):
        input = r'0X_DEA_DBEE_F'
        expect = r'0XDEADBEEF,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 133))

    def test_octal_int(self):
        input = r'001234567'
        expect = r'001234567,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 134))

    def test_decimal_int_underscore(self):
        input = r'123_123'
        expect = r'123123,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 135))

    def test_float_int(self):
        input = r'1.234'
        expect = r'1.234,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 136))

    def test_float_int_exp(self):
        input = r'1.2e3'
        expect = r'1.2e3,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 137))

    def test_int_exp(self):
        input = r'7E-10'
        expect = r'7E-10,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 138))

    def test_float_int_underscore(self):
        input = r'1_234.567'
        expect = r'1234.567,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 139))

    def test_fucking_abomination_float(self):
        input = r'123_4.5_6E+7_8'
        expect = r'1234.56E+78,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 140))

    def test_truthy(self):
        input = r'True'
        expect = r'True,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 141))

    def test_falsy(self):
        input = r'False'
        expect = r'False,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 142))

    def test_good_string(self):
        input = r'"This is my string"'
        expect = r'This is my string,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 151))

    def test_unclose_string(self):
        input = r'"There are many like it, but this one is mine'
        expect = r'Unclosed String: There are many like it, but this one is mine'
        self.assertTrue(TestLexer.test(input, expect, 152))

    def string_with_tab(self):
        input = r'This is a string containing tab \t'
        expect = r'This,is,a,string,containing,tab,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 153))

    def string_with_quote(self):
        input = r'''"He asked me: '"Where is John'""'''
        expect = r''
        self.assertTrue(TestLexer.test(input, expect, 154))

    def test_wrong_term_string(self):
        input = r'''
"The missile knows where it it at all times'
'''
        expect = r'Unclosed String: The missile knows where it it at all times'
        self.assertTrue(TestLexer.test(input, expect, 155))

    def test_edge_illegal_escape(self):
        input = r'"abc\"'
        expect = r'Illegal Escape In String: abc\"'
        self.assertTrue(TestLexer.test(input, expect, 156))

    def test_flat_int_array(self):
        input = r'Array(1,  5, 7  ,12)'
        expect = r'Array,(,1,,,5,,,7,,,12,),<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 161))

    def test_flat_string_array(self):
        input = r'Array("Murica", "fuck yeah")'
        expect = r'Array,(,Murica,,,fuck yeah,),<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 162))

    def test_pyramid_mixed_array(self):
        input = r'''
Array (
    Array("Volvo", "22", "18"),
    Array("Saab", "5", "2"),
    Array("Land Rover", "17", "15")
)
'''
        expect = r'Array,(,Array,(,Volvo,,,22,,,18,),,,Array,(,Saab,,,5,,,2,),,,Array,(,Land Rover,,,17,,,15,),),<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 163))

    def test_extra_string(self):
        input = r'''
"abc\\h"
'''
        expect = r'abc\\h,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 170))

    def test_external_1(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class U{_34K(_,BC,_:Array [Array [Float ,0B1],0x25];_K,_,_7Dj__,t,U:Array [String ,0B1010101]){}Val _:String ;}Class n:__{Var s,$_:Array [String ,05];Val e_5J:i2W5_;Var O,$_,$g8G_,N8x,_I:Array [Array [Boolean ,0x25],8];}''',
                '''Class,_,{,},Class,U,{,_34K,(,_,,,BC,,,_,:,Array,[,Array,[,Float,,,0B1,],,,0x25,],;,_K,,,_,,,_7Dj__,,,t,,,U,:,Array,[,String,,,0B1010101,],),{,},Val,_,:,String,;,},Class,n,:,__,{,Var,s,,,$_,:,Array,[,String,,,05,],;,Val,e_5J,:,i2W5_,;,Var,O,,,$_,,,$g8G_,,,N8x,,,_I,:,Array,[,Array,[,Boolean,,,0x25,],,,8,],;,},<EOF>''',
                301
            )
        )

    def test_external_2(self):
        self.assertTrue(
            TestLexer.test(
                '''Class W_:___{Val $1:__;}Class v_{Constructor (ww:__;Y:E;MIQ:Array [Array [Array [Int ,0142],0X2C],0XFD];N:Array [Int ,02_7]){}_4P(){}Val $_9:Boolean ;$76(_,C,W:Q;g7_325:Float ;__,SS3_4,F:Array [String ,0x1F];_pc,VP,_8:Array [Array [Array [Float ,0142],56],0142];a:Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,0B1],0X7B],45_1],0b100_0],0X2C],1],03],0142],0B1]){Break ;} }Class _{}Class _:M{}''',
                '''Class,W_,:,___,{,Val,$1,:,__,;,},Class,v_,{,Constructor,(,ww,:,__,;,Y,:,E,;,MIQ,:,Array,[,Array,[,Array,[,Int,,,0142,],,,0X2C,],,,0XFD,],;,N,:,Array,[,Int,,,027,],),{,},_4P,(,),{,},Val,$_9,:,Boolean,;,$76,(,_,,,C,,,W,:,Q,;,g7_325,:,Float,;,__,,,SS3_4,,,F,:,Array,[,String,,,0x1F,],;,_pc,,,VP,,,_8,:,Array,[,Array,[,Array,[,Float,,,0142,],,,56,],,,0142,],;,a,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B1,],,,0X7B,],,,451,],,,0b1000,],,,0X2C,],,,1,],,,03,],,,0142,],,,0B1,],),{,Break,;,},},Class,_,{,},Class,_,:,M,{,},<EOF>''',
                302
            )
        )

    def test_external_3(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l_:_9m6{$f(_m_:Int ){ {Continue ;} }}Class _:_{Constructor (){} }Class F:i_{Destructor (){}Val _,$F7:_;Constructor (_3:y;_s,_,M,_:L){Continue ;} }''',
                '''Class,l_,:,_9m6,{,$f,(,_m_,:,Int,),{,{,Continue,;,},},},Class,_,:,_,{,Constructor,(,),{,},},Class,F,:,i_,{,Destructor,(,),{,},Val,_,,,$F7,:,_,;,Constructor,(,_3,:,y,;,_s,,,_,,,M,,,_,:,L,),{,Continue,;,},},<EOF>''',
                303
            )
        )

    def test_external_4(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:C{J3_(__,Xc____2:Array [Array [Array [Array [Array [Array [Boolean ,0xD_A_CD],0x2],0b111_1],0X48],0X6B_6],68]){} }''',
                '''Class,_,:,C,{,J3_,(,__,,,Xc____2,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0xDACD,],,,0x2,],,,0b1111,],,,0X48,],,,0X6B6,],,,68,],),{,},},<EOF>''',
                304
            )
        )

    def test_external_5(self):
        self.assertTrue(
            TestLexer.test(
                '''Class C:x7X_{Var $65:Array [Array [Array [Array [Array [Boolean ,0b1],03],74],0X1F],07_6];}Class w:__9{Constructor (r:Array [Array [Array [Int ,74],012],02_3_3_3];C3C___Z:Float ){}Var _g,$z:Boolean ;Val A:Float ;}''',
                '''Class,C,:,x7X_,{,Var,$65,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1,],,,03,],,,74,],,,0X1F,],,,076,],;,},Class,w,:,__9,{,Constructor,(,r,:,Array,[,Array,[,Array,[,Int,,,74,],,,012,],,,02333,],;,C3C___Z,:,Float,),{,},Var,_g,,,$z,:,Boolean,;,Val,A,:,Float,;,},<EOF>''',
                305
            )
        )

    def test_external_6(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (C,M0w:Array [Array [Array [String ,01],0X6_6],0617];_,_,_v:Int ){} }Class D:T{Val $nD5:_;}''',
                '''Class,_,{,Constructor,(,C,,,M0w,:,Array,[,Array,[,Array,[,String,,,01,],,,0X66,],,,0617,],;,_,,,_,,,_v,:,Int,),{,},},Class,D,:,T,{,Val,$nD5,:,_,;,},<EOF>''',
                306
            )
        )

    def test_external_7(self):
        self.assertTrue(
            TestLexer.test(
                '''Class o{}Class _w0:N{Constructor (){} }Class _:Gn8V_{Destructor (){Continue ;_::$S();}_4s61b(){Break ;Continue ;} }''',
                '''Class,o,{,},Class,_w0,:,N,{,Constructor,(,),{,},},Class,_,:,Gn8V_,{,Destructor,(,),{,Continue,;,_,::,$S,(,),;,},_4s61b,(,),{,Break,;,Continue,;,},},<EOF>''',
                307
            )
        )

    def test_external_8(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P5_{}Class __:_7_2{$T(_:Array [Array [Array [Boolean ,016],016],0b1]){}Constructor (_:t){}Val $____,f34W0i,f166:Array [Array [Boolean ,0b1],0B11];}''',
                '''Class,P5_,{,},Class,__,:,_7_2,{,$T,(,_,:,Array,[,Array,[,Array,[,Boolean,,,016,],,,016,],,,0b1,],),{,},Constructor,(,_,:,t,),{,},Val,$____,,,f34W0i,,,f166,:,Array,[,Array,[,Boolean,,,0b1,],,,0B11,],;,},<EOF>''',
                308
            )
        )

    def test_external_9(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class b1:_{Val $_:_;}Class N7_{Constructor (){}Destructor (){} }Class F_{}Class ____:A{_uq(){}_(_:Boolean ){ {}Break ;} }Class _C2__:Z_8{Val $i,_30:Boolean ;}''',
                '''Class,_,{,},Class,b1,:,_,{,Val,$_,:,_,;,},Class,N7_,{,Constructor,(,),{,},Destructor,(,),{,},},Class,F_,{,},Class,____,:,A,{,_uq,(,),{,},_,(,_,:,Boolean,),{,{,},Break,;,},},Class,_C2__,:,Z_8,{,Val,$i,,,_30,:,Boolean,;,},<EOF>''',
                309
            )
        )

    def test_external_10(self):
        self.assertTrue(
            TestLexer.test(
                '''Class A58y:__9{Constructor (_0_d9:_;_,m:Array [Array [Array [Array [Boolean ,0xB],04],05_704_0_2],0B110];r,__:Float ;K_:e){}Val __81J:_;}''',
                '''Class,A58y,:,__9,{,Constructor,(,_0_d9,:,_,;,_,,,m,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0xB,],,,04,],,,0570402,],,,0B110,],;,r,,,__,:,Float,;,K_,:,e,),{,},Val,__81J,:,_,;,},<EOF>''',
                310
            )
        )

    def test_external_11(self):
        self.assertTrue(
            TestLexer.test(
                '''Class W:f_b{Var $_,$tu_:_;$53_(h,j:String ){Continue ;_v::$6().b1.m__P.h5.ZotqY();_jS2::$_KI7._o._B._();} }Class _:jM7q{}''',
                '''Class,W,:,f_b,{,Var,$_,,,$tu_,:,_,;,$53_,(,h,,,j,:,String,),{,Continue,;,_v,::,$6,(,),.,b1,.,m__P,.,h5,.,ZotqY,(,),;,_jS2,::,$_KI7,.,_o,.,_B,.,_,(,),;,},},Class,_,:,jM7q,{,},<EOF>''',
                311
            )
        )

    def test_external_12(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _8:_K{$_(_3,F:_;_:Int ){}Var _:__2=!g::$y_W4k_2.__G_._();Val $9:Float ;Var $3_:Array [Array [Array [Boolean ,0x1A],0X6D_7],77];$__(){} }Class _{Constructor (D_6a,UN_v_Nl92e4_4G:Int ;z:Int ){ {} }}''',
                '''Class,_8,:,_K,{,$_,(,_3,,,F,:,_,;,_,:,Int,),{,},Var,_,:,__2,=,!,g,::,$y_W4k_2,.,__G_,.,_,(,),;,Val,$9,:,Float,;,Var,$3_,:,Array,[,Array,[,Array,[,Boolean,,,0x1A,],,,0X6D7,],,,77,],;,$__,(,),{,},},Class,_,{,Constructor,(,D_6a,,,UN_v_Nl92e4_4G,:,Int,;,z,:,Int,),{,{,},},},<EOF>''',
                312
            )
        )

    def test_external_13(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:Y{I(J,g38,_f:Array [Array [Boolean ,053],8_5];D,u:Boolean ;e,_:GVX;_1w,Q4_,_H,i1,_,_8hm:Boolean ){} }''',
                '''Class,_,:,Y,{,I,(,J,,,g38,,,_f,:,Array,[,Array,[,Boolean,,,053,],,,85,],;,D,,,u,:,Boolean,;,e,,,_,:,GVX,;,_1w,,,Q4_,,,_H,,,i1,,,_,,,_8hm,:,Boolean,),{,},},<EOF>''',
                313
            )
        )

    def test_external_14(self):
        self.assertTrue(
            TestLexer.test(
                '''Class X{}Class _:R_{Constructor (s:Array [Array [Array [Array [Array [Int ,02],60],7],60],0115];_6:Float ){Return ;} }Class Y2y:k{}''',
                '''Class,X,{,},Class,_,:,R_,{,Constructor,(,s,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,02,],,,60,],,,7,],,,60,],,,0115,],;,_6,:,Float,),{,Return,;,},},Class,Y2y,:,k,{,},<EOF>''',
                314
            )
        )

    def test_external_15(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{}Class _:i2{Val $30:Xu;}Class _{Destructor (){d::$_w__();} }Class M{Var qH0,_,$5:Array [Array [Array [Array [Array [Array [Int ,012],40],0xA],83_2],4],0b111_10];}''',
                '''Class,_,{,},Class,_,:,i2,{,Val,$30,:,Xu,;,},Class,_,{,Destructor,(,),{,d,::,$_w__,(,),;,},},Class,M,{,Var,qH0,,,_,,,$5,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,012,],,,40,],,,0xA,],,,832,],,,4,],,,0b11110,],;,},<EOF>''',
                315
            )
        )

    def test_external_16(self):
        self.assertTrue(
            TestLexer.test(
                '''Class hO{Val $3_:Float ;Val $_E,$_,$1Y:kSa;$_(qd__,_i:Array [String ,52]){}Val C_J__,$isN_,_:Array [String ,0b11111];}''',
                '''Class,hO,{,Val,$3_,:,Float,;,Val,$_E,,,$_,,,$1Y,:,kSa,;,$_,(,qd__,,,_i,:,Array,[,String,,,52,],),{,},Val,C_J__,,,$isN_,,,_,:,Array,[,String,,,0b11111,],;,},<EOF>''',
                316
            )
        )

    def test_external_17(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:rs__{Constructor (L:Array [Boolean ,020_20];_,__,_:Array [Array [Array [Array [Array [Int ,0x5],57],6_823],0B1_0],0xC];_k:f){}Var Y:N;j(_:Array [Array [Array [Array [Array [Array [Array [Boolean ,027],0b10],0b100000],07],2_2],0xD1],0x53]){}Destructor (){} }Class __{}''',
                '''Class,_,:,rs__,{,Constructor,(,L,:,Array,[,Boolean,,,02020,],;,_,,,__,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x5,],,,57,],,,6823,],,,0B10,],,,0xC,],;,_k,:,f,),{,},Var,Y,:,N,;,j,(,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,027,],,,0b10,],,,0b100000,],,,07,],,,22,],,,0xD1,],,,0x53,],),{,},Destructor,(,),{,},},Class,__,{,},<EOF>''',
                317
            )
        )

    def test_external_18(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ur:e{Destructor (){Break ;}Destructor (){}Var $E,o0:Array [Array [Array [String ,02],0b111100],04];Val __:Boolean ;}''',
                '''Class,ur,:,e,{,Destructor,(,),{,Break,;,},Destructor,(,),{,},Var,$E,,,o0,:,Array,[,Array,[,Array,[,String,,,02,],,,0b111100,],,,04,],;,Val,__,:,Boolean,;,},<EOF>''',
                318
            )
        )

    def test_external_19(self):
        self.assertTrue(
            TestLexer.test(
                '''Class T:r24xr__r1c{$n(_o:Array [Array [Array [Array [Int ,0xE_C0],0b111001],0b1],05];D,F:N;_:String ;o:D){}Constructor (_:Boolean ){} }Class y3{Var $rp_,_,$r,$r,g38:Array [Float ,34];}''',
                '''Class,T,:,r24xr__r1c,{,$n,(,_o,:,Array,[,Array,[,Array,[,Array,[,Int,,,0xEC0,],,,0b111001,],,,0b1,],,,05,],;,D,,,F,:,N,;,_,:,String,;,o,:,D,),{,},Constructor,(,_,:,Boolean,),{,},},Class,y3,{,Var,$rp_,,,_,,,$r,,,$r,,,g38,:,Array,[,Float,,,34,],;,},<EOF>''',
                319
            )
        )

    def test_external_20(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___{}Class B__{}Class _{Var __M_,s:_;_(Y_U,_,_,_:dPG;Sr:Array [Array [Array [Array [Array [Array [Int ,3],01],84],0B11],0X1],02];_:Float ){} }Class _:oAi{}Class _{Val $C:Int ;}''',
                '''Class,___,{,},Class,B__,{,},Class,_,{,Var,__M_,,,s,:,_,;,_,(,Y_U,,,_,,,_,,,_,:,dPG,;,Sr,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,3,],,,01,],,,84,],,,0B11,],,,0X1,],,,02,],;,_,:,Float,),{,},},Class,_,:,oAi,{,},Class,_,{,Val,$C,:,Int,;,},<EOF>''',
                320
            )
        )

    def test_external_21(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __:u_{Var _:Array [Array [Array [Array [Array [Array [Array [String ,27],0B100100],05],0b10111],0b10111],037],0B100100];_(_2:Int ;cw5,_3,_,MG:String ){}Var $_,g01__S:Array [Int ,76];}''',
                '''Class,__,:,u_,{,Var,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,27,],,,0B100100,],,,05,],,,0b10111,],,,0b10111,],,,037,],,,0B100100,],;,_,(,_2,:,Int,;,cw5,,,_3,,,_,,,MG,:,String,),{,},Var,$_,,,g01__S,:,Array,[,Int,,,76,],;,},<EOF>''',
                321
            )
        )

    def test_external_22(self):
        self.assertTrue(
            TestLexer.test(
                '''Class N{_(U_W:_;_:p7){ {} }Var _:Float ;Val $_M_jw7,$I_7,$__,_4:Array [Int ,0b1_00];Var $_,$_,$9:Array [Boolean ,07];}''',
                '''Class,N,{,_,(,U_W,:,_,;,_,:,p7,),{,{,},},Var,_,:,Float,;,Val,$_M_jw7,,,$I_7,,,$__,,,_4,:,Array,[,Int,,,0b100,],;,Var,$_,,,$_,,,$9,:,Array,[,Boolean,,,07,],;,},<EOF>''',
                322
            )
        )

    def test_external_23(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J{}Class __{_0(z,_8,X5:r;_3F:T_4Vp;i,_:Boolean ){}Constructor (_,_,_U,__:Int ;PS_,pF1,__:Y;Q,_79_,_W9,R_,_0_2_:Int ){}$c4(_,j_5,B:Array [Array [Float ,39],0B1010010];_:n;_9__,_2k,_SX3:String ){Return ;} }''',
                '''Class,J,{,},Class,__,{,_0,(,z,,,_8,,,X5,:,r,;,_3F,:,T_4Vp,;,i,,,_,:,Boolean,),{,},Constructor,(,_,,,_,,,_U,,,__,:,Int,;,PS_,,,pF1,,,__,:,Y,;,Q,,,_79_,,,_W9,,,R_,,,_0_2_,:,Int,),{,},$c4,(,_,,,j_5,,,B,:,Array,[,Array,[,Float,,,39,],,,0B1010010,],;,_,:,n,;,_9__,,,_2k,,,_SX3,:,String,),{,Return,;,},},<EOF>''',
                323
            )
        )

    def test_external_24(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Val $E_,w1,Sv:Array [Array [Array [Array [Array [String ,88_4_1_2],07],4_8],043],0X6];Constructor (X__:Float ;M,____J1,_,_,cu,__3__,_:String ){Break ;} }''',
                '''Class,_,:,_,{,Val,$E_,,,w1,,,Sv,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,88412,],,,07,],,,48,],,,043,],,,0X6,],;,Constructor,(,X__,:,Float,;,M,,,____J1,,,_,,,_,,,cu,,,__3__,,,_,:,String,),{,Break,;,},},<EOF>''',
                324
            )
        )

    def test_external_25(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _1_0_:q{Constructor (_,Og,_:Array [Array [Float ,0x3_4],0B10101];d_,__:__;_,_7_,k,_,_,p1:Array [Float ,0x46];x:Array [Boolean ,0B1_101_0];_:j16){Continue ;} }Class ___1{}''',
                '''Class,_1_0_,:,q,{,Constructor,(,_,,,Og,,,_,:,Array,[,Array,[,Float,,,0x34,],,,0B10101,],;,d_,,,__,:,__,;,_,,,_7_,,,k,,,_,,,_,,,p1,:,Array,[,Float,,,0x46,],;,x,:,Array,[,Boolean,,,0B11010,],;,_,:,j16,),{,Continue,;,},},Class,___1,{,},<EOF>''',
                325
            )
        )

    def test_external_26(self):
        self.assertTrue(
            TestLexer.test(
                '''Class x:_{Constructor (__,o7M__A43,_,_:Int ;_:Array [Array [Array [Int ,33_5],64],0B1_0_11_1_1];F8A_E,s,__:__;__:String ;_,G:String ){}$_4_(){} }''',
                '''Class,x,:,_,{,Constructor,(,__,,,o7M__A43,,,_,,,_,:,Int,;,_,:,Array,[,Array,[,Array,[,Int,,,335,],,,64,],,,0B101111,],;,F8A_E,,,s,,,__,:,__,;,__,:,String,;,_,,,G,:,String,),{,},$_4_,(,),{,},},<EOF>''',
                326
            )
        )

    def test_external_27(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __2v273{Destructor (){}Destructor (){} }Class __{Destructor (){}$y(_:Array [Int ,2]){Break ;Var r5:Array [Array [Array [Array [String ,021],2],0X7],0x19];} }''',
                '''Class,__2v273,{,Destructor,(,),{,},Destructor,(,),{,},},Class,__,{,Destructor,(,),{,},$y,(,_,:,Array,[,Int,,,2,],),{,Break,;,Var,r5,:,Array,[,Array,[,Array,[,Array,[,String,,,021,],,,2,],,,0X7,],,,0x19,],;,},},<EOF>''',
                327
            )
        )

    def test_external_28(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _rc4{Constructor (cR,F_:Array [Int ,81];N,_0,_J,_,__0_Bz,_:Array [Array [Array [Array [Array [Boolean ,0b11],9],0b1010000],0b10_1],07];t,J_:a_;_x_,_9:q;_:p){kd::$A2();} }''',
                '''Class,_rc4,{,Constructor,(,cR,,,F_,:,Array,[,Int,,,81,],;,N,,,_0,,,_J,,,_,,,__0_Bz,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b11,],,,9,],,,0b1010000,],,,0b101,],,,07,],;,t,,,J_,:,a_,;,_x_,,,_9,:,q,;,_,:,p,),{,kd,::,$A2,(,),;,},},<EOF>''',
                328
            )
        )

    def test_external_29(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{Val $_,J:Array [Array [Array [Array [Boolean ,0B110001],2],0x7E],0b100];Var __,$23x,_,b:Array [Array [Array [Boolean ,0B1],0x45],0X34];}Class K:l{Val $_,$_4:a7_9_95O;}''',
                '''Class,_,:,_,{,Val,$_,,,J,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B110001,],,,2,],,,0x7E,],,,0b100,],;,Var,__,,,$23x,,,_,,,b,:,Array,[,Array,[,Array,[,Boolean,,,0B1,],,,0x45,],,,0X34,],;,},Class,K,:,l,{,Val,$_,,,$_4,:,a7_9_95O,;,},<EOF>''',
                329
            )
        )

    def test_external_30(self):
        self.assertTrue(
            TestLexer.test(
                '''Class P8{Constructor (N,_9:Array [String ,82];_Y:Array [Array [Boolean ,0X9],0X7]){}Constructor (_Ej__:Int ;s,U,_1n,_:Array [String ,45];c:Array [Array [Float ,0B111110],075];_h:Int ){Val D,__,N__Q_,J,g2,z_p_7:s;} }''',
                '''Class,P8,{,Constructor,(,N,,,_9,:,Array,[,String,,,82,],;,_Y,:,Array,[,Array,[,Boolean,,,0X9,],,,0X7,],),{,},Constructor,(,_Ej__,:,Int,;,s,,,U,,,_1n,,,_,:,Array,[,String,,,45,],;,c,:,Array,[,Array,[,Float,,,0B111110,],,,075,],;,_h,:,Int,),{,Val,D,,,__,,,N__Q_,,,J,,,g2,,,z_p_7,:,s,;,},},<EOF>''',
                330
            )
        )

    def test_external_31(self):
        self.assertTrue(
            TestLexer.test(
                '''Class J9_6C4_{}Class __:_{}Class n_S:p_I{}Class y2_ht__{Var $_:Float ;$8(V,v_0p_2:String ){Return ;Continue ;} }''',
                '''Class,J9_6C4_,{,},Class,__,:,_,{,},Class,n_S,:,p_I,{,},Class,y2_ht__,{,Var,$_,:,Float,;,$8,(,V,,,v_0p_2,:,String,),{,Return,;,Continue,;,},},<EOF>''',
                331
            )
        )

    def test_external_32(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___:_{$0(){Break ;} }Class _4UH:hQ{Var Jut:Array [String ,0X35];Val _,$_M_5,$t:_;}Class N:P9{}Class N:_69{Constructor (){Break ;} }''',
                '''Class,___,:,_,{,$0,(,),{,Break,;,},},Class,_4UH,:,hQ,{,Var,Jut,:,Array,[,String,,,0X35,],;,Val,_,,,$_M_5,,,$t,:,_,;,},Class,N,:,P9,{,},Class,N,:,_69,{,Constructor,(,),{,Break,;,},},<EOF>''',
                332
            )
        )

    def test_external_33(self):
        self.assertTrue(
            TestLexer.test(
                '''Class k0I_:J2{Wl9(P:Array [Array [Int ,026],0x2D];__,_4:_8){} }Class _L_:_y{}Class u{Val _,x:Array [Boolean ,06_40];Val _31_,_,$_0:String ;}''',
                '''Class,k0I_,:,J2,{,Wl9,(,P,:,Array,[,Array,[,Int,,,026,],,,0x2D,],;,__,,,_4,:,_8,),{,},},Class,_L_,:,_y,{,},Class,u,{,Val,_,,,x,:,Array,[,Boolean,,,0640,],;,Val,_31_,,,_,,,$_0,:,String,;,},<EOF>''',
                333
            )
        )

    def test_external_34(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Q:_0{__0(_:Array [Int ,0X8];__,_,_,_8:Array [Array [Float ,0xA_7_E7],0b11101];o_K:v_){}Val $5:Array [Array [String ,0x23],0b1];}''',
                '''Class,Q,:,_0,{,__0,(,_,:,Array,[,Int,,,0X8,],;,__,,,_,,,_,,,_8,:,Array,[,Array,[,Float,,,0xA7E7,],,,0b11101,],;,o_K,:,v_,),{,},Val,$5,:,Array,[,Array,[,String,,,0x23,],,,0b1,],;,},<EOF>''',
                334
            )
        )

    def test_external_35(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:q{Val $_O:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,02],0X6],2],77],0113],0113],0113],0113],0X6],0B1011000],03_20_6];}''',
                '''Class,_,:,q,{,Val,$_O,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,02,],,,0X6,],,,2,],,,77,],,,0113,],,,0113,],,,0113,],,,0113,],,,0X6,],,,0B1011000,],,,03206,],;,},<EOF>''',
                335
            )
        )

    def test_external_36(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___4:_{Val Q_Q:Array [String ,5];}Class _:_{}Class oZ__{}Class _{}Class p:_{}Class k{Var $_:Array [Array [Int ,0X7_F],0131];Destructor (){} }''',
                '''Class,___4,:,_,{,Val,Q_Q,:,Array,[,String,,,5,],;,},Class,_,:,_,{,},Class,oZ__,{,},Class,_,{,},Class,p,:,_,{,},Class,k,{,Var,$_,:,Array,[,Array,[,Int,,,0X7F,],,,0131,],;,Destructor,(,),{,},},<EOF>''',
                336
            )
        )

    def test_external_37(self):
        self.assertTrue(
            TestLexer.test(
                '''Class m{Destructor (){} }Class __:_{_J(_,Q,__:Float ;T:m47){}Constructor (y,_:String ;HSW:Float ){Break ;} }Class _k{}Class UO3{Destructor (){} }Class I:Gu0{$S(P,v__1R:Float ){Continue ;} }''',
                '''Class,m,{,Destructor,(,),{,},},Class,__,:,_,{,_J,(,_,,,Q,,,__,:,Float,;,T,:,m47,),{,},Constructor,(,y,,,_,:,String,;,HSW,:,Float,),{,Break,;,},},Class,_k,{,},Class,UO3,{,Destructor,(,),{,},},Class,I,:,Gu0,{,$S,(,P,,,v__1R,:,Float,),{,Continue,;,},},<EOF>''',
                337
            )
        )

    def test_external_38(self):
        self.assertTrue(
            TestLexer.test(
                '''Class p{Constructor (Ra_,OQ_:Array [Array [Array [Array [Array [Array [Array [Int ,0X36],57],0B1011110],0b110101],57],0X36],0B1]){} }Class w_X9_NPlc:V{Constructor (_,_U45,Z7l:Array [Array [Array [Array [Array [Int ,66_0_5],0B1011110],0b110101],0xF],07];_:Float ){} }''',
                '''Class,p,{,Constructor,(,Ra_,,,OQ_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0X36,],,,57,],,,0B1011110,],,,0b110101,],,,57,],,,0X36,],,,0B1,],),{,},},Class,w_X9_NPlc,:,V,{,Constructor,(,_,,,_U45,,,Z7l,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,6605,],,,0B1011110,],,,0b110101,],,,0xF,],,,07,],;,_,:,Float,),{,},},<EOF>''',
                338
            )
        )

    def test_external_39(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __s_{Var $s0_3980,$_v_7:Array [Array [Array [Array [Array [Array [Float ,0B10_01],1],0XA],0X3],010],0354];}Class _3:dU{}Class kTF:_1_{}''',
                '''Class,__s_,{,Var,$s0_3980,,,$_v_7,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B1001,],,,1,],,,0XA,],,,0X3,],,,010,],,,0354,],;,},Class,_3,:,dU,{,},Class,kTF,:,_1_,{,},<EOF>''',
                339
            )
        )

    def test_external_40(self):
        self.assertTrue(
            TestLexer.test(
                '''Class FQ_n0:_kN{}Class _iq:_{Val $_,L,r,$_,_:String ;}Class _:__b{}Class zO__{Constructor (z,y_:Array [Array [Array [Float ,0x22],36],06_0];_I,_Zo:Array [Array [Array [String ,01],0x22],04]){} }''',
                '''Class,FQ_n0,:,_kN,{,},Class,_iq,:,_,{,Val,$_,,,L,,,r,,,$_,,,_,:,String,;,},Class,_,:,__b,{,},Class,zO__,{,Constructor,(,z,,,y_,:,Array,[,Array,[,Array,[,Float,,,0x22,],,,36,],,,060,],;,_I,,,_Zo,:,Array,[,Array,[,Array,[,String,,,01,],,,0x22,],,,04,],),{,},},<EOF>''',
                340
            )
        )

    def test_external_41(self):
        self.assertTrue(
            TestLexer.test(
                '''Class S_:n8X{Var $s5C:_;Var _,$4__74,$4w,___2,$_:Array [Float ,0X9];Constructor (_,a,Z3,C:___2__Za;_,_,Wc_a1:String ;L4:Float ;_:Iq__1){} }Class P:_3{Var M_7,$b:h;}''',
                '''Class,S_,:,n8X,{,Var,$s5C,:,_,;,Var,_,,,$4__74,,,$4w,,,___2,,,$_,:,Array,[,Float,,,0X9,],;,Constructor,(,_,,,a,,,Z3,,,C,:,___2__Za,;,_,,,_,,,Wc_a1,:,String,;,L4,:,Float,;,_,:,Iq__1,),{,},},Class,P,:,_3,{,Var,M_7,,,$b,:,h,;,},<EOF>''',
                341
            )
        )

    def test_external_42(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _o:_{$z__(){}Destructor (){}Destructor (){Continue ;} }Class V{$WQj(O:Array [String ,054];_8,__0:b_C;y_:_E_53;K:Boolean ){} }''',
                '''Class,_o,:,_,{,$z__,(,),{,},Destructor,(,),{,},Destructor,(,),{,Continue,;,},},Class,V,{,$WQj,(,O,:,Array,[,String,,,054,],;,_8,,,__0,:,b_C,;,y_,:,_E_53,;,K,:,Boolean,),{,},},<EOF>''',
                342
            )
        )

    def test_external_43(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Constructor (_,k0t,qNs:Array [Array [Array [Float ,0B100110],5],04_2];U,b,_60EuU:e4;_,L4__C_1:String ){} }''',
                '''Class,_,{,Constructor,(,_,,,k0t,,,qNs,:,Array,[,Array,[,Array,[,Float,,,0B100110,],,,5,],,,042,],;,U,,,b,,,_60EuU,:,e4,;,_,,,L4__C_1,:,String,),{,},},<EOF>''',
                343
            )
        )

    def test_external_44(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{$8(_L__F,_P,_,_:Array [Array [String ,0112],54]){ {} }}Class ___:E{Destructor (){} }Class N:Jd4_{}Class fDE{}Class FW7:_4{}''',
                '''Class,_,:,_,{,$8,(,_L__F,,,_P,,,_,,,_,:,Array,[,Array,[,String,,,0112,],,,54,],),{,{,},},},Class,___,:,E,{,Destructor,(,),{,},},Class,N,:,Jd4_,{,},Class,fDE,{,},Class,FW7,:,_4,{,},<EOF>''',
                344
            )
        )

    def test_external_45(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_M_{}Class _H{$4_(D:Array [Array [Array [Int ,58],03_6_3],04]){Break ;} }Class _rdG2{Destructor (){ {}{_::$2();} }}Class Z0:x94{}''',
                '''Class,_,:,_M_,{,},Class,_H,{,$4_,(,D,:,Array,[,Array,[,Array,[,Int,,,58,],,,0363,],,,04,],),{,Break,;,},},Class,_rdG2,{,Destructor,(,),{,{,},{,_,::,$2,(,),;,},},},Class,Z0,:,x94,{,},<EOF>''',
                345
            )
        )

    def test_external_46(self):
        self.assertTrue(
            TestLexer.test(
                '''Class lkO{Destructor (){}$__t(__H:Array [Array [Int ,0124],03];Y,_5,j:String ;d:Float ){}Constructor (){}Var J,_:r;}''',
                '''Class,lkO,{,Destructor,(,),{,},$__t,(,__H,:,Array,[,Array,[,Int,,,0124,],,,03,],;,Y,,,_5,,,j,:,String,;,d,:,Float,),{,},Constructor,(,),{,},Var,J,,,_,:,r,;,},<EOF>''',
                346
            )
        )

    def test_external_47(self):
        self.assertTrue(
            TestLexer.test(
                '''Class kn:_B{$_(Y,__:Array [Array [Array [Float ,0101],0b101001],1_0_51];_o8:Array [Boolean ,01];j8_,e,K:_;_,MW,R:jv_){} }''',
                '''Class,kn,:,_B,{,$_,(,Y,,,__,:,Array,[,Array,[,Array,[,Float,,,0101,],,,0b101001,],,,1051,],;,_o8,:,Array,[,Boolean,,,01,],;,j8_,,,e,,,K,:,_,;,_,,,MW,,,R,:,jv_,),{,},},<EOF>''',
                347
            )
        )

    def test_external_48(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __R:M{Var $_:String ;Destructor (){}$_0(r,r_:Array [Float ,0x57];K___m_:Float ;O,_,E,_q:Array [Int ,0B1_00_0101];I,__,_,_,g2,g_:Boolean ;Y:W8;u,_,r:Int ;_S,_9:Boolean ){}Var __,$_,sN,$VG_K,$__,$2,$0__R:_8;}Class z0:X{}''',
                '''Class,__R,:,M,{,Var,$_,:,String,;,Destructor,(,),{,},$_0,(,r,,,r_,:,Array,[,Float,,,0x57,],;,K___m_,:,Float,;,O,,,_,,,E,,,_q,:,Array,[,Int,,,0B1000101,],;,I,,,__,,,_,,,_,,,g2,,,g_,:,Boolean,;,Y,:,W8,;,u,,,_,,,r,:,Int,;,_S,,,_9,:,Boolean,),{,},Var,__,,,$_,,,sN,,,$VG_K,,,$__,,,$2,,,$0__R,:,_8,;,},Class,z0,:,X,{,},<EOF>''',
                348
            )
        )

    def test_external_49(self):
        self.assertTrue(
            TestLexer.test(
                '''Class rK{Var Q,$_M_a0P,$_49,_3U,M,_7b:Array [Array [Int ,051],0xE_4];M_(){}_(l:String ;P,_,_7_,_,__4:Array [Array [Boolean ,0xC],0b1011100]){} }''',
                '''Class,rK,{,Var,Q,,,$_M_a0P,,,$_49,,,_3U,,,M,,,_7b,:,Array,[,Array,[,Int,,,051,],,,0xE4,],;,M_,(,),{,},_,(,l,:,String,;,P,,,_,,,_7_,,,_,,,__4,:,Array,[,Array,[,Boolean,,,0xC,],,,0b1011100,],),{,},},<EOF>''',
                349
            )
        )

    def test_external_50(self):
        self.assertTrue(
            TestLexer.test(
                '''Class Tz:__{}Class T{}Class _{Val $s,$K_W,q_:T;Var $C:j;Destructor (){} }Class S{}Class C:F{}Class _{Val $7:String ;Val _,C,G_,$q:Array [Array [Int ,94],0b1001011];Var $R,w:Array [Array [Array [Array [Boolean ,5],0x4],025],0X9];Val a:Float ;}''',
                '''Class,Tz,:,__,{,},Class,T,{,},Class,_,{,Val,$s,,,$K_W,,,q_,:,T,;,Var,$C,:,j,;,Destructor,(,),{,},},Class,S,{,},Class,C,:,F,{,},Class,_,{,Val,$7,:,String,;,Val,_,,,C,,,G_,,,$q,:,Array,[,Array,[,Int,,,94,],,,0b1001011,],;,Var,$R,,,w,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,5,],,,0x4,],,,025,],,,0X9,],;,Val,a,:,Float,;,},<EOF>''',
                350
            )
        )

    def test_external_51(self):
        self.assertTrue(
            TestLexer.test(
                '''Class K8:_{Destructor (){ {} }$T(a7,b,f,_8___,B,_a,_9:Array [String ,04];s_:_4;_s,_v:Array [Array [Int ,0X5_8],0B1];j:Array [Array [Boolean ,0B1001],0101];Q,_O5:vl;v,_,__7:_){} }''',
                '''Class,K8,:,_,{,Destructor,(,),{,{,},},$T,(,a7,,,b,,,f,,,_8___,,,B,,,_a,,,_9,:,Array,[,String,,,04,],;,s_,:,_4,;,_s,,,_v,:,Array,[,Array,[,Int,,,0X58,],,,0B1,],;,j,:,Array,[,Array,[,Boolean,,,0B1001,],,,0101,],;,Q,,,_O5,:,vl,;,v,,,_,,,__7,:,_,),{,},},<EOF>''',
                351
            )
        )

    def test_external_52(self):
        self.assertTrue(
            TestLexer.test(
                '''Class l___U{Constructor (F_G_V_,_:Float ;K:Array [String ,0x35]){}Destructor (){_::$_8()._N();{} }}Class _:_{}''',
                '''Class,l___U,{,Constructor,(,F_G_V_,,,_,:,Float,;,K,:,Array,[,String,,,0x35,],),{,},Destructor,(,),{,_,::,$_8,(,),.,_N,(,),;,{,},},},Class,_,:,_,{,},<EOF>''',
                352
            )
        )

    def test_external_53(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:_{}Class uq_4:_0_{Val b:Array [Array [Array [Array [Array [Float ,0112],0b1_1_1],93],0X4],0112];Var _6:Array [Array [Int ,0112],0x22];}''',
                '''Class,_,:,_,{,},Class,uq_4,:,_0_,{,Val,b,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0112,],,,0b111,],,,93,],,,0X4,],,,0112,],;,Var,_6,:,Array,[,Array,[,Int,,,0112,],,,0x22,],;,},<EOF>''',
                353
            )
        )

    def test_external_54(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _7{}Class Y__6_:Q{Constructor (){}Constructor (){} }Class _:p{m(_p:Float ;__:k64;H:Array [Boolean ,0X57]){}Var Q:Q8;Destructor (){}Val $_:Array [Array [Float ,0X57],0X57];}''',
                '''Class,_7,{,},Class,Y__6_,:,Q,{,Constructor,(,),{,},Constructor,(,),{,},},Class,_,:,p,{,m,(,_p,:,Float,;,__,:,k64,;,H,:,Array,[,Boolean,,,0X57,],),{,},Var,Q,:,Q8,;,Destructor,(,),{,},Val,$_,:,Array,[,Array,[,Float,,,0X57,],,,0X57,],;,},<EOF>''',
                354
            )
        )

    def test_external_55(self):
        self.assertTrue(
            TestLexer.test(
                '''Class __2:u{}Class B{}Class l_:S{Destructor (){ {} }Var _9:__a_114_;Constructor (_,_g5,t2,_:Float ;__h:_;C,_:_;__X_1,M8:Array [Array [Array [Int ,0B1_1],0x26],0B1];x,_,I3:Array [Array [Int ,0XD],5];__KAl_,y:String ){} }''',
                '''Class,__2,:,u,{,},Class,B,{,},Class,l_,:,S,{,Destructor,(,),{,{,},},Var,_9,:,__a_114_,;,Constructor,(,_,,,_g5,,,t2,,,_,:,Float,;,__h,:,_,;,C,,,_,:,_,;,__X_1,,,M8,:,Array,[,Array,[,Array,[,Int,,,0B11,],,,0x26,],,,0B1,],;,x,,,_,,,I3,:,Array,[,Array,[,Int,,,0XD,],,,5,],;,__KAl_,,,y,:,String,),{,},},<EOF>''',
                355
            )
        )

    def test_external_56(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _9y6a_:_D{}Class q_:w6q{}Class _{$___(){} }Class __{c(){} }Class _0_O:xH{}Class _C{Val $_7,___,_59,O:gg;}Class d_2{Destructor (){Continue ;} }Class ___{n4_4_E(){} }''',
                '''Class,_9y6a_,:,_D,{,},Class,q_,:,w6q,{,},Class,_,{,$___,(,),{,},},Class,__,{,c,(,),{,},},Class,_0_O,:,xH,{,},Class,_C,{,Val,$_7,,,___,,,_59,,,O,:,gg,;,},Class,d_2,{,Destructor,(,),{,Continue,;,},},Class,___,{,n4_4_E,(,),{,},},<EOF>''',
                356
            )
        )

    def test_external_57(self):
        self.assertTrue(
            TestLexer.test(
                '''Class v:__{}Class __:A_{Constructor (_t:Float ;_:Array [Array [Float ,0b1_0],0b1];MY__MA,P,cb2_42:Array [Array [Int ,0X1],5]){} }''',
                '''Class,v,:,__,{,},Class,__,:,A_,{,Constructor,(,_t,:,Float,;,_,:,Array,[,Array,[,Float,,,0b10,],,,0b1,],;,MY__MA,,,P,,,cb2_42,:,Array,[,Array,[,Int,,,0X1,],,,5,],),{,},},<EOF>''',
                357
            )
        )

    def test_external_58(self):
        self.assertTrue(
            TestLexer.test(
                '''Class g:_{}Class _q2:_k_{}Class _:_{_(O:___wt;MGY_,H8:Array [Float ,0x38];_,K_:Array [Array [Float ,04_5_3],01];W6t_Bl:Array [Array [Array [Array [String ,28],28],0B1],04_25];Z4_8,_7_:Boolean ){}Var _,_:B;}''',
                '''Class,g,:,_,{,},Class,_q2,:,_k_,{,},Class,_,:,_,{,_,(,O,:,___wt,;,MGY_,,,H8,:,Array,[,Float,,,0x38,],;,_,,,K_,:,Array,[,Array,[,Float,,,0453,],,,01,],;,W6t_Bl,:,Array,[,Array,[,Array,[,Array,[,String,,,28,],,,28,],,,0B1,],,,0425,],;,Z4_8,,,_7_,:,Boolean,),{,},Var,_,,,_,:,B,;,},<EOF>''',
                358
            )
        )

    def test_external_59(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _:i_7b_3_{Val $_:Float ;Constructor (L:_;_3_L:Array [Array [Array [Int ,8],48],6_3]){} }Class x{}Class ___1_{}''',
                '''Class,_,:,i_7b_3_,{,Val,$_,:,Float,;,Constructor,(,L,:,_,;,_3_L,:,Array,[,Array,[,Array,[,Int,,,8,],,,48,],,,63,],),{,},},Class,x,{,},Class,___1_,{,},<EOF>''',
                359
            )
        )

    def test_external_60(self):
        self.assertTrue(
            TestLexer.test(
                '''Class y2_5_47C:_{Constructor (){}Val $19,_11_:Array [Boolean ,076];Val $d5K_,$6,hXj5355_,$_0_8:x_;Var $_h52P__4,$oj_,$_:ss;Var K,$O,_z_,$3,$e,E,$C,_,to:__2;}Class _7:_u{}Class mH:s5096{}''',
                '''Class,y2_5_47C,:,_,{,Constructor,(,),{,},Val,$19,,,_11_,:,Array,[,Boolean,,,076,],;,Val,$d5K_,,,$6,,,hXj5355_,,,$_0_8,:,x_,;,Var,$_h52P__4,,,$oj_,,,$_,:,ss,;,Var,K,,,$O,,,_z_,,,$3,,,$e,,,E,,,$C,,,_,,,to,:,__2,;,},Class,_7,:,_u,{,},Class,mH,:,s5096,{,},<EOF>''',
                360
            )
        )

    def test_external_61(self):
        self.assertTrue(
            TestLexer.test(
                '''Class WsR1{Val _,$_UU_,O,$V:Array [Int ,01];$W(_Q,_O__39m,k:String ){}m9__(){}Constructor (_:String ){}Val __HX2_1,o,$iM4R:SE;}''',
                '''Class,WsR1,{,Val,_,,,$_UU_,,,O,,,$V,:,Array,[,Int,,,01,],;,$W,(,_Q,,,_O__39m,,,k,:,String,),{,},m9__,(,),{,},Constructor,(,_,:,String,),{,},Val,__HX2_1,,,o,,,$iM4R,:,SE,;,},<EOF>''',
                361
            )
        )

    def test_external_62(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _6:W{Var $L:Array [Array [Float ,0x5E],0117];}Class E0{Val $6J:P;Destructor (){}Val $d:IF5;Constructor (){Return ;} }Class __pr:q_{}Class l:C{}''',
                '''Class,_6,:,W,{,Var,$L,:,Array,[,Array,[,Float,,,0x5E,],,,0117,],;,},Class,E0,{,Val,$6J,:,P,;,Destructor,(,),{,},Val,$d,:,IF5,;,Constructor,(,),{,Return,;,},},Class,__pr,:,q_,{,},Class,l,:,C,{,},<EOF>''',
                362
            )
        )

    def test_external_63(self):
        self.assertTrue(
            TestLexer.test(
                '''Class ___04:_fU{}Class _kc:_{Var $9,$__,yz:Array [Array [Array [Array [Array [Array [Array [Array [String ,02],04_3],5_1],0b1],076],0B1_1],0XD],0X56];}''',
                '''Class,___04,:,_fU,{,},Class,_kc,:,_,{,Var,$9,,,$__,,,yz,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,02,],,,043,],,,51,],,,0b1,],,,076,],,,0B11,],,,0XD,],,,0X56,],;,},<EOF>''',
                363
            )
        )

    def test_external_64(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _Q9_{Var $6,G:Boolean ;}Class t:C90_{Destructor (){} }Class _:_10_{Var _,$_1,_f36E_8HI_:B_;}Class k__S_1_1{}''',
                '''Class,_Q9_,{,Var,$6,,,G,:,Boolean,;,},Class,t,:,C90_,{,Destructor,(,),{,},},Class,_,:,_10_,{,Var,_,,,$_1,,,_f36E_8HI_,:,B_,;,},Class,k__S_1_1,{,},<EOF>''',
                364
            )
        )

    def test_external_65(self):
        self.assertTrue(
            TestLexer.test(
                '''Class _{Var __6,m:Array [Array [Array [Array [Boolean ,5],0B1110],4_5],03_6_33];}Class O:_{Val __C_:Array [Boolean ,0b111010];}''',
                '''Class,_,{,Var,__6,,,m,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,5,],,,0B1110,],,,45,],,,03633,],;,},Class,O,:,_,{,Val,__C_,:,Array,[,Boolean,,,0b111010,],;,},<EOF>''',
                365
            )
        )
