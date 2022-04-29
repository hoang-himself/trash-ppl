# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u0279\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\7\2~\n\2\f\2\16\2\u0081\13\2\3")
        buf.write("\2\5\2\u0084\n\2\3\2\7\2\u0087\n\2\f\2\16\2\u008a\13\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0092\n\3\3\3\3\3\7\3\u0096")
        buf.write("\n\3\f\3\16\3\u0099\13\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u00a1")
        buf.write("\n\4\f\4\16\4\u00a4\13\4\3\4\5\4\u00a7\n\4\3\4\7\4\u00aa")
        buf.write("\n\4\f\4\16\4\u00ad\13\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u00b5")
        buf.write("\n\5\3\6\3\6\3\6\5\6\u00ba\n\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\5\t\u00d0\n\t\3\n\3\n\3\n\7\n\u00d5\n\n\f\n\16\n\u00d8")
        buf.write("\13\n\3\13\3\13\3\13\5\13\u00dd\n\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\5\f\u00e5\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00fb\n\17\3\20\3\20\3\20\7\20\u0100\n")
        buf.write("\20\f\20\16\20\u0103\13\20\3\20\3\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\5\21\u0110\n\21\3\22\3\22")
        buf.write("\3\22\5\22\u0115\n\22\3\22\3\22\3\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\24\3\24\3\24\7\24\u0122\n\24\f\24\16\24\u0125")
        buf.write("\13\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\7\26\u012e\n")
        buf.write("\26\f\26\16\26\u0131\13\26\3\27\3\27\3\27\3\27\3\27\5")
        buf.write("\27\u0138\n\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\7\32")
        buf.write("\u0141\n\32\f\32\16\32\u0144\13\32\3\33\3\33\3\33\7\33")
        buf.write("\u0149\n\33\f\33\16\33\u014c\13\33\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u015e\n\35\3\36\3\36\3\36\7\36\u0163\n\36\f")
        buf.write("\36\16\36\u0166\13\36\3\37\3\37\3\37\3\37\3\37\5\37\u016d")
        buf.write("\n\37\3 \3 \3 \3 \3 \5 \u0174\n \3!\3!\3!\3!\3!\3!\7!")
        buf.write("\u017c\n!\f!\16!\u017f\13!\3\"\3\"\3\"\3\"\3\"\3\"\7\"")
        buf.write("\u0187\n\"\f\"\16\"\u018a\13\"\3#\3#\3#\3#\3#\3#\7#\u0192")
        buf.write("\n#\f#\16#\u0195\13#\3$\3$\3$\5$\u019a\n$\3%\3%\3%\5%")
        buf.write("\u019f\n%\3&\3&\3&\3&\3&\3&\3&\3&\7&\u01a9\n&\f&\16&\u01ac")
        buf.write("\13&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01b6\n\'\3\'")
        buf.write("\5\'\u01b9\n\'\7\'\u01bb\n\'\f\'\16\'\u01be\13\'\3(\3")
        buf.write("(\3(\3(\3(\5(\u01c5\n(\3(\5(\u01c8\n(\3(\5(\u01cb\n(\3")
        buf.write(")\3)\3)\3)\5)\u01d1\n)\3)\3)\5)\u01d5\n)\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\5*\u01df\n*\3+\3+\3+\3+\5+\u01e5\n+\3+\3+\3")
        buf.write(",\3,\3,\3,\3,\3-\3-\3.\3.\5.\u01f2\n.\3/\3/\3/\7/\u01f7")
        buf.write("\n/\f/\16/\u01fa\13/\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\7\60\u0204\n\60\f\60\16\60\u0207\13\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u0211\n\61\3\61\5")
        buf.write("\61\u0214\n\61\7\61\u0216\n\61\f\61\16\61\u0219\13\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u0223\n")
        buf.write("\62\3\62\5\62\u0226\n\62\7\62\u0228\n\62\f\62\16\62\u022b")
        buf.write("\13\62\3\63\3\63\3\64\3\64\7\64\u0231\n\64\f\64\16\64")
        buf.write("\u0234\13\64\3\64\5\64\u0237\n\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\38\38\38\38\38\38\38\38\39\39\39\39\39\59\u0255\n9\3")
        buf.write(":\3:\3:\3;\3;\3;\3<\3<\5<\u025f\n<\3<\3<\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\5=\u026e\n=\3>\3>\7>\u0272\n>\f>\16")
        buf.write(">\u0275\13>\3>\3>\3>\2\n@BDJL^`b?\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprtvxz\2\13\3\2\7\b\3\2$%\3\2\35 \3\2\21")
        buf.write("\22\3\2AB\4\2\65\66=@\3\2\63\64\3\289\3\2:<\2\u028d\2")
        buf.write("\177\3\2\2\2\4\u008d\3\2\2\2\6\u009c\3\2\2\2\b\u00b4\3")
        buf.write("\2\2\2\n\u00b6\3\2\2\2\f\u00bd\3\2\2\2\16\u00c1\3\2\2")
        buf.write("\2\20\u00cf\3\2\2\2\22\u00d1\3\2\2\2\24\u00d9\3\2\2\2")
        buf.write("\26\u00e1\3\2\2\2\30\u00e8\3\2\2\2\32\u00ec\3\2\2\2\34")
        buf.write("\u00fa\3\2\2\2\36\u00fc\3\2\2\2 \u010f\3\2\2\2\"\u0111")
        buf.write("\3\2\2\2$\u0119\3\2\2\2&\u011e\3\2\2\2(\u0126\3\2\2\2")
        buf.write("*\u012a\3\2\2\2,\u0137\3\2\2\2.\u0139\3\2\2\2\60\u013b")
        buf.write("\3\2\2\2\62\u013d\3\2\2\2\64\u0145\3\2\2\2\66\u014d\3")
        buf.write("\2\2\28\u015d\3\2\2\2:\u015f\3\2\2\2<\u016c\3\2\2\2>\u0173")
        buf.write("\3\2\2\2@\u0175\3\2\2\2B\u0180\3\2\2\2D\u018b\3\2\2\2")
        buf.write("F\u0199\3\2\2\2H\u019e\3\2\2\2J\u01a0\3\2\2\2L\u01ad\3")
        buf.write("\2\2\2N\u01ca\3\2\2\2P\u01d4\3\2\2\2R\u01de\3\2\2\2T\u01e0")
        buf.write("\3\2\2\2V\u01e8\3\2\2\2X\u01ed\3\2\2\2Z\u01f1\3\2\2\2")
        buf.write("\\\u01f3\3\2\2\2^\u01fb\3\2\2\2`\u0208\3\2\2\2b\u021a")
        buf.write("\3\2\2\2d\u022c\3\2\2\2f\u022e\3\2\2\2h\u0238\3\2\2\2")
        buf.write("j\u023e\3\2\2\2l\u0244\3\2\2\2n\u0247\3\2\2\2p\u024f\3")
        buf.write("\2\2\2r\u0256\3\2\2\2t\u0259\3\2\2\2v\u025c\3\2\2\2x\u026d")
        buf.write("\3\2\2\2z\u026f\3\2\2\2|~\5\4\3\2}|\3\2\2\2~\u0081\3\2")
        buf.write("\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0083\3\2\2")
        buf.write("\2\u0081\177\3\2\2\2\u0082\u0084\5\6\4\2\u0083\u0082\3")
        buf.write("\2\2\2\u0083\u0084\3\2\2\2\u0084\u0088\3\2\2\2\u0085\u0087")
        buf.write("\5\4\3\2\u0086\u0085\3\2\2\2\u0087\u008a\3\2\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008b\3\2\2\2")
        buf.write("\u008a\u0088\3\2\2\2\u008b\u008c\7\2\2\3\u008c\3\3\2\2")
        buf.write("\2\u008d\u008e\7\5\2\2\u008e\u0091\7%\2\2\u008f\u0090")
        buf.write("\7*\2\2\u0090\u0092\7%\2\2\u0091\u008f\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0097\7\60\2\2\u0094")
        buf.write("\u0096\5\b\5\2\u0095\u0094\3\2\2\2\u0096\u0099\3\2\2\2")
        buf.write("\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009a\3")
        buf.write("\2\2\2\u0099\u0097\3\2\2\2\u009a\u009b\7\61\2\2\u009b")
        buf.write("\5\3\2\2\2\u009c\u009d\7\5\2\2\u009d\u009e\7\3\2\2\u009e")
        buf.write("\u00a2\7\60\2\2\u009f\u00a1\5\b\5\2\u00a0\u009f\3\2\2")
        buf.write("\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5")
        buf.write("\u00a7\5\36\20\2\u00a6\u00a5\3\2\2\2\u00a6\u00a7\3\2\2")
        buf.write("\2\u00a7\u00ab\3\2\2\2\u00a8\u00aa\5\b\5\2\u00a9\u00a8")
        buf.write("\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab")
        buf.write("\u00ac\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00ab\3\2\2\2")
        buf.write("\u00ae\u00af\7\61\2\2\u00af\7\3\2\2\2\u00b0\u00b5\5\n")
        buf.write("\6\2\u00b1\u00b5\5\24\13\2\u00b2\u00b5\5\"\22\2\u00b3")
        buf.write("\u00b5\5$\23\2\u00b4\u00b0\3\2\2\2\u00b4\u00b1\3\2\2\2")
        buf.write("\u00b4\u00b2\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5\t\3\2\2")
        buf.write("\2\u00b6\u00b9\t\2\2\2\u00b7\u00ba\5\f\7\2\u00b8\u00ba")
        buf.write("\5\16\b\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00bb\u00bc\7)\2\2\u00bc\13\3\2\2\2\u00bd")
        buf.write("\u00be\5\22\n\2\u00be\u00bf\7*\2\2\u00bf\u00c0\58\35\2")
        buf.write("\u00c0\r\3\2\2\2\u00c1\u00c2\t\3\2\2\u00c2\u00c3\5\20")
        buf.write("\t\2\u00c3\u00c4\5<\37\2\u00c4\17\3\2\2\2\u00c5\u00c6")
        buf.write("\7(\2\2\u00c6\u00c7\t\3\2\2\u00c7\u00c8\5\20\t\2\u00c8")
        buf.write("\u00c9\5<\37\2\u00c9\u00ca\7(\2\2\u00ca\u00d0\3\2\2\2")
        buf.write("\u00cb\u00cc\7*\2\2\u00cc\u00cd\58\35\2\u00cd\u00ce\7")
        buf.write("\67\2\2\u00ce\u00d0\3\2\2\2\u00cf\u00c5\3\2\2\2\u00cf")
        buf.write("\u00cb\3\2\2\2\u00d0\21\3\2\2\2\u00d1\u00d6\t\3\2\2\u00d2")
        buf.write("\u00d3\7(\2\2\u00d3\u00d5\t\3\2\2\u00d4\u00d2\3\2\2\2")
        buf.write("\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3")
        buf.write("\2\2\2\u00d7\23\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00da")
        buf.write("\t\3\2\2\u00da\u00dc\7,\2\2\u00db\u00dd\5&\24\2\u00dc")
        buf.write("\u00db\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\3\2\2\2")
        buf.write("\u00de\u00df\7-\2\2\u00df\u00e0\5z>\2\u00e0\25\3\2\2\2")
        buf.write("\u00e1\u00e4\t\2\2\2\u00e2\u00e5\5\30\r\2\u00e3\u00e5")
        buf.write("\5\32\16\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5")
        buf.write("\u00e6\3\2\2\2\u00e6\u00e7\7)\2\2\u00e7\27\3\2\2\2\u00e8")
        buf.write("\u00e9\5\64\33\2\u00e9\u00ea\7*\2\2\u00ea\u00eb\58\35")
        buf.write("\2\u00eb\31\3\2\2\2\u00ec\u00ed\7%\2\2\u00ed\u00ee\5\34")
        buf.write("\17\2\u00ee\u00ef\5<\37\2\u00ef\33\3\2\2\2\u00f0\u00f1")
        buf.write("\7(\2\2\u00f1\u00f2\7%\2\2\u00f2\u00f3\5\34\17\2\u00f3")
        buf.write("\u00f4\5<\37\2\u00f4\u00f5\7(\2\2\u00f5\u00fb\3\2\2\2")
        buf.write("\u00f6\u00f7\7*\2\2\u00f7\u00f8\58\35\2\u00f8\u00f9\7")
        buf.write("\67\2\2\u00f9\u00fb\3\2\2\2\u00fa\u00f0\3\2\2\2\u00fa")
        buf.write("\u00f6\3\2\2\2\u00fb\35\3\2\2\2\u00fc\u00fd\7\4\2\2\u00fd")
        buf.write("\u0101\7\60\2\2\u00fe\u0100\5 \21\2\u00ff\u00fe\3\2\2")
        buf.write("\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102")
        buf.write("\3\2\2\2\u0102\u0104\3\2\2\2\u0103\u0101\3\2\2\2\u0104")
        buf.write("\u0105\7\61\2\2\u0105\37\3\2\2\2\u0106\u0110\5\26\f\2")
        buf.write("\u0107\u0110\5V,\2\u0108\u0110\5r:\2\u0109\u0110\5t;\2")
        buf.write("\u010a\u0110\5f\64\2\u010b\u0110\5n8\2\u010c\u010d\5<")
        buf.write("\37\2\u010d\u010e\7)\2\2\u010e\u0110\3\2\2\2\u010f\u0106")
        buf.write("\3\2\2\2\u010f\u0107\3\2\2\2\u010f\u0108\3\2\2\2\u010f")
        buf.write("\u0109\3\2\2\2\u010f\u010a\3\2\2\2\u010f\u010b\3\2\2\2")
        buf.write("\u010f\u010c\3\2\2\2\u0110!\3\2\2\2\u0111\u0112\7\31\2")
        buf.write("\2\u0112\u0114\7,\2\2\u0113\u0115\5&\24\2\u0114\u0113")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write("\u0117\7-\2\2\u0117\u0118\5z>\2\u0118#\3\2\2\2\u0119\u011a")
        buf.write("\7\32\2\2\u011a\u011b\7,\2\2\u011b\u011c\7-\2\2\u011c")
        buf.write("\u011d\5z>\2\u011d%\3\2\2\2\u011e\u0123\5(\25\2\u011f")
        buf.write("\u0120\7)\2\2\u0120\u0122\5(\25\2\u0121\u011f\3\2\2\2")
        buf.write("\u0122\u0125\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0124\3")
        buf.write("\2\2\2\u0124\'\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u0127")
        buf.write("\5\64\33\2\u0127\u0128\7*\2\2\u0128\u0129\58\35\2\u0129")
        buf.write(")\3\2\2\2\u012a\u012f\5,\27\2\u012b\u012c\7(\2\2\u012c")
        buf.write("\u012e\5,\27\2\u012d\u012b\3\2\2\2\u012e\u0131\3\2\2\2")
        buf.write("\u012f\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130+\3\2\2")
        buf.write("\2\u0131\u012f\3\2\2\2\u0132\u0138\5.\30\2\u0133\u0138")
        buf.write("\7!\2\2\u0134\u0138\7\"\2\2\u0135\u0138\5\60\31\2\u0136")
        buf.write("\u0138\5\66\34\2\u0137\u0132\3\2\2\2\u0137\u0133\3\2\2")
        buf.write("\2\u0137\u0134\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0136")
        buf.write("\3\2\2\2\u0138-\3\2\2\2\u0139\u013a\t\4\2\2\u013a/\3\2")
        buf.write("\2\2\u013b\u013c\t\5\2\2\u013c\61\3\2\2\2\u013d\u0142")
        buf.write("\7$\2\2\u013e\u013f\7(\2\2\u013f\u0141\7$\2\2\u0140\u013e")
        buf.write("\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140\3\2\2\2\u0142")
        buf.write("\u0143\3\2\2\2\u0143\63\3\2\2\2\u0144\u0142\3\2\2\2\u0145")
        buf.write("\u014a\7%\2\2\u0146\u0147\7(\2\2\u0147\u0149\7%\2\2\u0148")
        buf.write("\u0146\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2")
        buf.write("\u014a\u014b\3\2\2\2\u014b\65\3\2\2\2\u014c\u014a\3\2")
        buf.write("\2\2\u014d\u014e\7,\2\2\u014e\u014f\5*\26\2\u014f\u0150")
        buf.write("\7-\2\2\u0150\67\3\2\2\2\u0151\u015e\7\25\2\2\u0152\u015e")
        buf.write("\7\26\2\2\u0153\u015e\7\27\2\2\u0154\u015e\7\24\2\2\u0155")
        buf.write("\u0156\7\30\2\2\u0156\u0157\7.\2\2\u0157\u0158\58\35\2")
        buf.write("\u0158\u0159\7(\2\2\u0159\u015a\5.\30\2\u015a\u015b\7")
        buf.write("/\2\2\u015b\u015e\3\2\2\2\u015c\u015e\7%\2\2\u015d\u0151")
        buf.write("\3\2\2\2\u015d\u0152\3\2\2\2\u015d\u0153\3\2\2\2\u015d")
        buf.write("\u0154\3\2\2\2\u015d\u0155\3\2\2\2\u015d\u015c\3\2\2\2")
        buf.write("\u015e9\3\2\2\2\u015f\u0164\5<\37\2\u0160\u0161\7(\2\2")
        buf.write("\u0161\u0163\5<\37\2\u0162\u0160\3\2\2\2\u0163\u0166\3")
        buf.write("\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165;")
        buf.write("\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0168\5> \2\u0168\u0169")
        buf.write("\t\6\2\2\u0169\u016a\5> \2\u016a\u016d\3\2\2\2\u016b\u016d")
        buf.write("\5> \2\u016c\u0167\3\2\2\2\u016c\u016b\3\2\2\2\u016d=")
        buf.write("\3\2\2\2\u016e\u016f\5@!\2\u016f\u0170\t\7\2\2\u0170\u0171")
        buf.write("\5@!\2\u0171\u0174\3\2\2\2\u0172\u0174\5@!\2\u0173\u016e")
        buf.write("\3\2\2\2\u0173\u0172\3\2\2\2\u0174?\3\2\2\2\u0175\u0176")
        buf.write("\b!\1\2\u0176\u0177\5B\"\2\u0177\u017d\3\2\2\2\u0178\u0179")
        buf.write("\f\4\2\2\u0179\u017a\t\b\2\2\u017a\u017c\5B\"\2\u017b")
        buf.write("\u0178\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2")
        buf.write("\u017d\u017e\3\2\2\2\u017eA\3\2\2\2\u017f\u017d\3\2\2")
        buf.write("\2\u0180\u0181\b\"\1\2\u0181\u0182\5D#\2\u0182\u0188\3")
        buf.write("\2\2\2\u0183\u0184\f\4\2\2\u0184\u0185\t\t\2\2\u0185\u0187")
        buf.write("\5D#\2\u0186\u0183\3\2\2\2\u0187\u018a\3\2\2\2\u0188\u0186")
        buf.write("\3\2\2\2\u0188\u0189\3\2\2\2\u0189C\3\2\2\2\u018a\u0188")
        buf.write("\3\2\2\2\u018b\u018c\b#\1\2\u018c\u018d\5F$\2\u018d\u0193")
        buf.write("\3\2\2\2\u018e\u018f\f\4\2\2\u018f\u0190\t\n\2\2\u0190")
        buf.write("\u0192\5F$\2\u0191\u018e\3\2\2\2\u0192\u0195\3\2\2\2\u0193")
        buf.write("\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194E\3\2\2\2\u0195")
        buf.write("\u0193\3\2\2\2\u0196\u0197\7\62\2\2\u0197\u019a\5F$\2")
        buf.write("\u0198\u019a\5H%\2\u0199\u0196\3\2\2\2\u0199\u0198\3\2")
        buf.write("\2\2\u019aG\3\2\2\2\u019b\u019c\79\2\2\u019c\u019f\5H")
        buf.write("%\2\u019d\u019f\5J&\2\u019e\u019b\3\2\2\2\u019e\u019d")
        buf.write("\3\2\2\2\u019fI\3\2\2\2\u01a0\u01a1\b&\1\2\u01a1\u01a2")
        buf.write("\5L\'\2\u01a2\u01aa\3\2\2\2\u01a3\u01a4\f\4\2\2\u01a4")
        buf.write("\u01a5\7.\2\2\u01a5\u01a6\5<\37\2\u01a6\u01a7\7/\2\2\u01a7")
        buf.write("\u01a9\3\2\2\2\u01a8\u01a3\3\2\2\2\u01a9\u01ac\3\2\2\2")
        buf.write("\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01abK\3\2\2")
        buf.write("\2\u01ac\u01aa\3\2\2\2\u01ad\u01ae\b\'\1\2\u01ae\u01af")
        buf.write("\5N(\2\u01af\u01bc\3\2\2\2\u01b0\u01b1\f\4\2\2\u01b1\u01b2")
        buf.write("\7&\2\2\u01b2\u01b8\7%\2\2\u01b3\u01b5\7,\2\2\u01b4\u01b6")
        buf.write("\5:\36\2\u01b5\u01b4\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6")
        buf.write("\u01b7\3\2\2\2\u01b7\u01b9\7-\2\2\u01b8\u01b3\3\2\2\2")
        buf.write("\u01b8\u01b9\3\2\2\2\u01b9\u01bb\3\2\2\2\u01ba\u01b0\3")
        buf.write("\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd")
        buf.write("\3\2\2\2\u01bdM\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c0")
        buf.write("\5P)\2\u01c0\u01c1\7+\2\2\u01c1\u01c7\7$\2\2\u01c2\u01c4")
        buf.write("\7,\2\2\u01c3\u01c5\5:\36\2\u01c4\u01c3\3\2\2\2\u01c4")
        buf.write("\u01c5\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c8\7-\2\2")
        buf.write("\u01c7\u01c2\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01cb\3")
        buf.write("\2\2\2\u01c9\u01cb\5P)\2\u01ca\u01bf\3\2\2\2\u01ca\u01c9")
        buf.write("\3\2\2\2\u01cbO\3\2\2\2\u01cc\u01cd\7\33\2\2\u01cd\u01ce")
        buf.write("\7%\2\2\u01ce\u01d0\7,\2\2\u01cf\u01d1\5:\36\2\u01d0\u01cf")
        buf.write("\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2")
        buf.write("\u01d5\7-\2\2\u01d3\u01d5\5R*\2\u01d4\u01cc\3\2\2\2\u01d4")
        buf.write("\u01d3\3\2\2\2\u01d5Q\3\2\2\2\u01d6\u01d7\7,\2\2\u01d7")
        buf.write("\u01d8\5<\37\2\u01d8\u01d9\7-\2\2\u01d9\u01df\3\2\2\2")
        buf.write("\u01da\u01df\5,\27\2\u01db\u01df\7%\2\2\u01dc\u01df\7")
        buf.write("\6\2\2\u01dd\u01df\7\23\2\2\u01de\u01d6\3\2\2\2\u01de")
        buf.write("\u01da\3\2\2\2\u01de\u01db\3\2\2\2\u01de\u01dc\3\2\2\2")
        buf.write("\u01de\u01dd\3\2\2\2\u01dfS\3\2\2\2\u01e0\u01e1\7\33\2")
        buf.write("\2\u01e1\u01e2\7%\2\2\u01e2\u01e4\7,\2\2\u01e3\u01e5\5")
        buf.write(":\36\2\u01e4\u01e3\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e6")
        buf.write("\3\2\2\2\u01e6\u01e7\7-\2\2\u01e7U\3\2\2\2\u01e8\u01e9")
        buf.write("\5X-\2\u01e9\u01ea\7\67\2\2\u01ea\u01eb\5Z.\2\u01eb\u01ec")
        buf.write("\7)\2\2\u01ecW\3\2\2\2\u01ed\u01ee\5^\60\2\u01eeY\3\2")
        buf.write("\2\2\u01ef\u01f2\5V,\2\u01f0\u01f2\5<\37\2\u01f1\u01ef")
        buf.write("\3\2\2\2\u01f1\u01f0\3\2\2\2\u01f2[\3\2\2\2\u01f3\u01f8")
        buf.write("\5^\60\2\u01f4\u01f5\7(\2\2\u01f5\u01f7\5^\60\2\u01f6")
        buf.write("\u01f4\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8\u01f6\3\2\2\2")
        buf.write("\u01f8\u01f9\3\2\2\2\u01f9]\3\2\2\2\u01fa\u01f8\3\2\2")
        buf.write("\2\u01fb\u01fc\b\60\1\2\u01fc\u01fd\5`\61\2\u01fd\u0205")
        buf.write("\3\2\2\2\u01fe\u01ff\f\4\2\2\u01ff\u0200\7.\2\2\u0200")
        buf.write("\u0201\5^\60\2\u0201\u0202\7/\2\2\u0202\u0204\3\2\2\2")
        buf.write("\u0203\u01fe\3\2\2\2\u0204\u0207\3\2\2\2\u0205\u0203\3")
        buf.write("\2\2\2\u0205\u0206\3\2\2\2\u0206_\3\2\2\2\u0207\u0205")
        buf.write("\3\2\2\2\u0208\u0209\b\61\1\2\u0209\u020a\5b\62\2\u020a")
        buf.write("\u0217\3\2\2\2\u020b\u020c\f\4\2\2\u020c\u020d\7&\2\2")
        buf.write("\u020d\u0213\7%\2\2\u020e\u0210\7,\2\2\u020f\u0211\5\\")
        buf.write("/\2\u0210\u020f\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0212")
        buf.write("\3\2\2\2\u0212\u0214\7-\2\2\u0213\u020e\3\2\2\2\u0213")
        buf.write("\u0214\3\2\2\2\u0214\u0216\3\2\2\2\u0215\u020b\3\2\2\2")
        buf.write("\u0216\u0219\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218\3")
        buf.write("\2\2\2\u0218a\3\2\2\2\u0219\u0217\3\2\2\2\u021a\u021b")
        buf.write("\b\62\1\2\u021b\u021c\5d\63\2\u021c\u0229\3\2\2\2\u021d")
        buf.write("\u021e\f\4\2\2\u021e\u021f\7+\2\2\u021f\u0225\7$\2\2\u0220")
        buf.write("\u0222\7,\2\2\u0221\u0223\5\\/\2\u0222\u0221\3\2\2\2\u0222")
        buf.write("\u0223\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u0226\7-\2\2")
        buf.write("\u0225\u0220\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0228\3")
        buf.write("\2\2\2\u0227\u021d\3\2\2\2\u0228\u022b\3\2\2\2\u0229\u0227")
        buf.write("\3\2\2\2\u0229\u022a\3\2\2\2\u022ac\3\2\2\2\u022b\u0229")
        buf.write("\3\2\2\2\u022c\u022d\7%\2\2\u022de\3\2\2\2\u022e\u0232")
        buf.write("\5h\65\2\u022f\u0231\5j\66\2\u0230\u022f\3\2\2\2\u0231")
        buf.write("\u0234\3\2\2\2\u0232\u0230\3\2\2\2\u0232\u0233\3\2\2\2")
        buf.write("\u0233\u0236\3\2\2\2\u0234\u0232\3\2\2\2\u0235\u0237\5")
        buf.write("l\67\2\u0236\u0235\3\2\2\2\u0236\u0237\3\2\2\2\u0237g")
        buf.write("\3\2\2\2\u0238\u0239\7\t\2\2\u0239\u023a\7,\2\2\u023a")
        buf.write("\u023b\5<\37\2\u023b\u023c\7-\2\2\u023c\u023d\5z>\2\u023d")
        buf.write("i\3\2\2\2\u023e\u023f\7\n\2\2\u023f\u0240\7,\2\2\u0240")
        buf.write("\u0241\5<\37\2\u0241\u0242\7-\2\2\u0242\u0243\5z>\2\u0243")
        buf.write("k\3\2\2\2\u0244\u0245\7\13\2\2\u0245\u0246\5z>\2\u0246")
        buf.write("m\3\2\2\2\u0247\u0248\7\17\2\2\u0248\u0249\7,\2\2\u0249")
        buf.write("\u024a\7%\2\2\u024a\u024b\7\20\2\2\u024b\u024c\5p9\2\u024c")
        buf.write("\u024d\7-\2\2\u024d\u024e\5z>\2\u024eo\3\2\2\2\u024f\u0250")
        buf.write("\5<\37\2\u0250\u0251\7\'\2\2\u0251\u0254\5<\37\2\u0252")
        buf.write("\u0253\7\34\2\2\u0253\u0255\5<\37\2\u0254\u0252\3\2\2")
        buf.write("\2\u0254\u0255\3\2\2\2\u0255q\3\2\2\2\u0256\u0257\7\f")
        buf.write("\2\2\u0257\u0258\7)\2\2\u0258s\3\2\2\2\u0259\u025a\7\r")
        buf.write("\2\2\u025a\u025b\7)\2\2\u025bu\3\2\2\2\u025c\u025e\7\16")
        buf.write("\2\2\u025d\u025f\5<\37\2\u025e\u025d\3\2\2\2\u025e\u025f")
        buf.write("\3\2\2\2\u025f\u0260\3\2\2\2\u0260\u0261\7)\2\2\u0261")
        buf.write("w\3\2\2\2\u0262\u026e\5z>\2\u0263\u026e\5\26\f\2\u0264")
        buf.write("\u026e\5V,\2\u0265\u026e\5r:\2\u0266\u026e\5t;\2\u0267")
        buf.write("\u026e\5v<\2\u0268\u026e\5f\64\2\u0269\u026e\5n8\2\u026a")
        buf.write("\u026b\5<\37\2\u026b\u026c\7)\2\2\u026c\u026e\3\2\2\2")
        buf.write("\u026d\u0262\3\2\2\2\u026d\u0263\3\2\2\2\u026d\u0264\3")
        buf.write("\2\2\2\u026d\u0265\3\2\2\2\u026d\u0266\3\2\2\2\u026d\u0267")
        buf.write("\3\2\2\2\u026d\u0268\3\2\2\2\u026d\u0269\3\2\2\2\u026d")
        buf.write("\u026a\3\2\2\2\u026ey\3\2\2\2\u026f\u0273\7\60\2\2\u0270")
        buf.write("\u0272\5x=\2\u0271\u0270\3\2\2\2\u0272\u0275\3\2\2\2\u0273")
        buf.write("\u0271\3\2\2\2\u0273\u0274\3\2\2\2\u0274\u0276\3\2\2\2")
        buf.write("\u0275\u0273\3\2\2\2\u0276\u0277\7\61\2\2\u0277{\3\2\2")
        buf.write("\2<\177\u0083\u0088\u0091\u0097\u00a2\u00a6\u00ab\u00b4")
        buf.write("\u00b9\u00cf\u00d6\u00dc\u00e4\u00fa\u0101\u010f\u0114")
        buf.write("\u0123\u012f\u0137\u0142\u014a\u015d\u0164\u016c\u0173")
        buf.write("\u017d\u0188\u0193\u0199\u019e\u01aa\u01b5\u01b8\u01bc")
        buf.write("\u01c4\u01c7\u01ca\u01d0\u01d4\u01de\u01e4\u01f1\u01f8")
        buf.write("\u0205\u0210\u0213\u0217\u0222\u0225\u0229\u0232\u0236")
        buf.write("\u0254\u025e\u026d\u0273")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Program'", "<INVALID>", "'Class'", "'Self'", 
                     "'Val'", "'Var'", "'If'", "'Elseif'", "'Else'", "'Break'", 
                     "'Continue'", "'Return'", "'Foreach'", "'In'", "'True'", 
                     "'False'", "'Null'", "'String'", "'Int'", "'Float'", 
                     "'Boolean'", "'Array'", "'Constructor'", "'Destructor'", 
                     "'New'", "'By'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'.'", "'..'", "','", "';'", 
                     "':'", "'::'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'!'", "'&&'", "'||'", "'=='", "'!='", "'='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'>'", "'>='", "'<'", "'<='", 
                     "'+.'", "'==.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "MAIN", "CLASS", "SELF", 
                      "VAL", "VAR", "IF", "ELSEIF", "ELSE", "BREAK", "CONTINUE", 
                      "RETURN", "FOREACH", "IN", "TRUE", "FALSE", "NULL", 
                      "STRING", "INTEGER", "FLOAT", "BOOLEAN", "ARRAY", 
                      "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "DEC_LITERAL", 
                      "HEX_LITERAL", "OCTAL_LITERAL", "BINARY_LITERAL", 
                      "FLOAT_LITERAL", "STRING_LITERAL", "BLOCK_COMMENT", 
                      "STATIC_ID_NAME", "ID_NAME", "DOT", "DOT2", "COMMA", 
                      "SEMICOLON", "COLON", "COLON2", "LP", "RP", "LSB", 
                      "RSB", "LCB", "RCB", "LOG_NEGATE", "LOG_AND", "LOG_OR", 
                      "LOG_EQ", "LOG_NEQ", "EQ", "PLUS", "MINUS", "ASTERISK", 
                      "F_SLASH", "PERCENT", "GT", "GEQ", "LT", "LEQ", "STR_CONCAT", 
                      "STR_EQ", "WS", "ERROR_TOKEN", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_entry_class = 2
    RULE_class_mem_decl = 3
    RULE_attr_decl = 4
    RULE_attr_decl_wo_asg = 5
    RULE_attr_decl_w_asg = 6
    RULE_attr_decl_rep = 7
    RULE_attr_name_list = 8
    RULE_method_decl = 9
    RULE_method_local_decl = 10
    RULE_method_local_decl_wo_asg = 11
    RULE_method_local_decl_w_asg = 12
    RULE_method_local_decl_rep = 13
    RULE_entry_method = 14
    RULE_stmt_wo_return = 15
    RULE_cons_method = 16
    RULE_des_method = 17
    RULE_param_list = 18
    RULE_param = 19
    RULE_literal_list = 20
    RULE_literal = 21
    RULE_int_literal = 22
    RULE_boolean_literal = 23
    RULE_static_idname_list = 24
    RULE_idname_list = 25
    RULE_array_literal = 26
    RULE_any_type = 27
    RULE_expr_list = 28
    RULE_expr = 29
    RULE_expr1 = 30
    RULE_expr2 = 31
    RULE_expr3 = 32
    RULE_expr4 = 33
    RULE_expr5 = 34
    RULE_expr6 = 35
    RULE_expr7 = 36
    RULE_expr8 = 37
    RULE_expr9 = 38
    RULE_expr10 = 39
    RULE_operand = 40
    RULE_new_object_expr = 41
    RULE_assign_stmt = 42
    RULE_assign_lhs = 43
    RULE_assign_rhs = 44
    RULE_assign_lhs_sub_expr_list = 45
    RULE_assign_lhs_sub_expr = 46
    RULE_assign_lhs_sub_expr1 = 47
    RULE_assign_lhs_sub_expr2 = 48
    RULE_assign_lhs_sub_expr3 = 49
    RULE_flow_stmt = 50
    RULE_if_stmt = 51
    RULE_elseif_stmt = 52
    RULE_else_stmt = 53
    RULE_for_stmt = 54
    RULE_for_range = 55
    RULE_break_stmt = 56
    RULE_continue_stmt = 57
    RULE_return_stmt = 58
    RULE_stmt = 59
    RULE_block_stmt = 60

    ruleNames =  [ "program", "class_decl", "entry_class", "class_mem_decl", 
                   "attr_decl", "attr_decl_wo_asg", "attr_decl_w_asg", "attr_decl_rep", 
                   "attr_name_list", "method_decl", "method_local_decl", 
                   "method_local_decl_wo_asg", "method_local_decl_w_asg", 
                   "method_local_decl_rep", "entry_method", "stmt_wo_return", 
                   "cons_method", "des_method", "param_list", "param", "literal_list", 
                   "literal", "int_literal", "boolean_literal", "static_idname_list", 
                   "idname_list", "array_literal", "any_type", "expr_list", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "expr9", "expr10", "operand", 
                   "new_object_expr", "assign_stmt", "assign_lhs", "assign_rhs", 
                   "assign_lhs_sub_expr_list", "assign_lhs_sub_expr", "assign_lhs_sub_expr1", 
                   "assign_lhs_sub_expr2", "assign_lhs_sub_expr3", "flow_stmt", 
                   "if_stmt", "elseif_stmt", "else_stmt", "for_stmt", "for_range", 
                   "break_stmt", "continue_stmt", "return_stmt", "stmt", 
                   "block_stmt" ]

    EOF = Token.EOF
    T__0=1
    MAIN=2
    CLASS=3
    SELF=4
    VAL=5
    VAR=6
    IF=7
    ELSEIF=8
    ELSE=9
    BREAK=10
    CONTINUE=11
    RETURN=12
    FOREACH=13
    IN=14
    TRUE=15
    FALSE=16
    NULL=17
    STRING=18
    INTEGER=19
    FLOAT=20
    BOOLEAN=21
    ARRAY=22
    CONSTRUCTOR=23
    DESTRUCTOR=24
    NEW=25
    BY=26
    DEC_LITERAL=27
    HEX_LITERAL=28
    OCTAL_LITERAL=29
    BINARY_LITERAL=30
    FLOAT_LITERAL=31
    STRING_LITERAL=32
    BLOCK_COMMENT=33
    STATIC_ID_NAME=34
    ID_NAME=35
    DOT=36
    DOT2=37
    COMMA=38
    SEMICOLON=39
    COLON=40
    COLON2=41
    LP=42
    RP=43
    LSB=44
    RSB=45
    LCB=46
    RCB=47
    LOG_NEGATE=48
    LOG_AND=49
    LOG_OR=50
    LOG_EQ=51
    LOG_NEQ=52
    EQ=53
    PLUS=54
    MINUS=55
    ASTERISK=56
    F_SLASH=57
    PERCENT=58
    GT=59
    GEQ=60
    LT=61
    LEQ=62
    STR_CONCAT=63
    STR_EQ=64
    WS=65
    ERROR_TOKEN=66
    UNCLOSE_STRING=67
    ILLEGAL_ESCAPE=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declContext,i)


        def entry_class(self):
            return self.getTypedRuleContext(D96Parser.Entry_classContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 122
                    self.class_decl() 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 128
                self.entry_class()


            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CLASS:
                self.state = 131
                self.class_decl()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 137
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID_NAME)
            else:
                return self.getToken(D96Parser.ID_NAME, i)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def class_mem_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_mem_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_mem_declContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(D96Parser.CLASS)
            self.state = 140
            self.match(D96Parser.ID_NAME)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 141
                self.match(D96Parser.COLON)
                self.state = 142
                self.match(D96Parser.ID_NAME)


            self.state = 145
            self.match(D96Parser.LCB)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.STATIC_ID_NAME) | (1 << D96Parser.ID_NAME))) != 0):
                self.state = 146
                self.class_mem_decl()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Entry_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def class_mem_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_mem_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_mem_declContext,i)


        def entry_method(self):
            return self.getTypedRuleContext(D96Parser.Entry_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_entry_class

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntry_class" ):
                return visitor.visitEntry_class(self)
            else:
                return visitor.visitChildren(self)




    def entry_class(self):

        localctx = D96Parser.Entry_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_entry_class)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(D96Parser.CLASS)
            self.state = 155
            self.match(D96Parser.T__0)
            self.state = 156
            self.match(D96Parser.LCB)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 157
                    self.class_mem_decl() 
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.MAIN:
                self.state = 163
                self.entry_method()


            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.STATIC_ID_NAME) | (1 << D96Parser.ID_NAME))) != 0):
                self.state = 166
                self.class_mem_decl()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 172
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_mem_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_decl(self):
            return self.getTypedRuleContext(D96Parser.Attr_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(D96Parser.Method_declContext,0)


        def cons_method(self):
            return self.getTypedRuleContext(D96Parser.Cons_methodContext,0)


        def des_method(self):
            return self.getTypedRuleContext(D96Parser.Des_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_mem_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_mem_decl" ):
                return visitor.visitClass_mem_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_mem_decl(self):

        localctx = D96Parser.Class_mem_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_mem_decl)
        try:
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.attr_decl()
                pass
            elif token in [D96Parser.STATIC_ID_NAME, D96Parser.ID_NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.method_decl()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.cons_method()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
                self.des_method()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def attr_decl_wo_asg(self):
            return self.getTypedRuleContext(D96Parser.Attr_decl_wo_asgContext,0)


        def attr_decl_w_asg(self):
            return self.getTypedRuleContext(D96Parser.Attr_decl_w_asgContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl" ):
                return visitor.visitAttr_decl(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl(self):

        localctx = D96Parser.Attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attr_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 181
                self.attr_decl_wo_asg()
                pass

            elif la_ == 2:
                self.state = 182
                self.attr_decl_w_asg()
                pass


            self.state = 185
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_wo_asgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_name_list(self):
            return self.getTypedRuleContext(D96Parser.Attr_name_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def any_type(self):
            return self.getTypedRuleContext(D96Parser.Any_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr_decl_wo_asg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_wo_asg" ):
                return visitor.visitAttr_decl_wo_asg(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_wo_asg(self):

        localctx = D96Parser.Attr_decl_wo_asgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attr_decl_wo_asg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.attr_name_list()
            self.state = 188
            self.match(D96Parser.COLON)
            self.state = 189
            self.any_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_w_asgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_decl_rep(self):
            return self.getTypedRuleContext(D96Parser.Attr_decl_repContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def ID_NAME(self):
            return self.getToken(D96Parser.ID_NAME, 0)

        def STATIC_ID_NAME(self):
            return self.getToken(D96Parser.STATIC_ID_NAME, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_decl_w_asg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_w_asg" ):
                return visitor.visitAttr_decl_w_asg(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_w_asg(self):

        localctx = D96Parser.Attr_decl_w_asgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attr_decl_w_asg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            _la = self._input.LA(1)
            if not(_la==D96Parser.STATIC_ID_NAME or _la==D96Parser.ID_NAME):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 192
            self.attr_decl_rep()
            self.state = 193
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_repContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def attr_decl_rep(self):
            return self.getTypedRuleContext(D96Parser.Attr_decl_repContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def ID_NAME(self):
            return self.getToken(D96Parser.ID_NAME, 0)

        def STATIC_ID_NAME(self):
            return self.getToken(D96Parser.STATIC_ID_NAME, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def any_type(self):
            return self.getTypedRuleContext(D96Parser.Any_typeContext,0)


        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_decl_rep

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_rep" ):
                return visitor.visitAttr_decl_rep(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_rep(self):

        localctx = D96Parser.Attr_decl_repContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attr_decl_rep)
        self._la = 0 # Token type
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(D96Parser.COMMA)
                self.state = 196
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC_ID_NAME or _la==D96Parser.ID_NAME):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 197
                self.attr_decl_rep()
                self.state = 198
                self.expr()
                self.state = 199
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(D96Parser.COLON)
                self.state = 202
                self.any_type()
                self.state = 203
                self.match(D96Parser.EQ)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_name_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID_NAME)
            else:
                return self.getToken(D96Parser.ID_NAME, i)

        def STATIC_ID_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.STATIC_ID_NAME)
            else:
                return self.getToken(D96Parser.STATIC_ID_NAME, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_name_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_name_list" ):
                return visitor.visitAttr_name_list(self)
            else:
                return visitor.visitChildren(self)




    def attr_name_list(self):

        localctx = D96Parser.Attr_name_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attr_name_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            _la = self._input.LA(1)
            if not(_la==D96Parser.STATIC_ID_NAME or _la==D96Parser.ID_NAME):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 208
                self.match(D96Parser.COMMA)
                self.state = 209
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC_ID_NAME or _la==D96Parser.ID_NAME):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def ID_NAME(self):
            return self.getToken(D96Parser.ID_NAME, 0)

        def STATIC_ID_NAME(self):
            return self.getToken(D96Parser.STATIC_ID_NAME, 0)

        def param_list(self):
            return self.getTypedRuleContext(D96Parser.Param_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = D96Parser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            _la = self._input.LA(1)
            if not(_la==D96Parser.STATIC_ID_NAME or _la==D96Parser.ID_NAME):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 216
            self.match(D96Parser.LP)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID_NAME:
                self.state = 217
                self.param_list()


            self.state = 220
            self.match(D96Parser.RP)
            self.state = 221
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_local_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def method_local_decl_wo_asg(self):
            return self.getTypedRuleContext(D96Parser.Method_local_decl_wo_asgContext,0)


        def method_local_decl_w_asg(self):
            return self.getTypedRuleContext(D96Parser.Method_local_decl_w_asgContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_local_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_local_decl" ):
                return visitor.visitMethod_local_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_local_decl(self):

        localctx = D96Parser.Method_local_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_method_local_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 224
                self.method_local_decl_wo_asg()
                pass

            elif la_ == 2:
                self.state = 225
                self.method_local_decl_w_asg()
                pass


            self.state = 228
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_local_decl_wo_asgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idname_list(self):
            return self.getTypedRuleContext(D96Parser.Idname_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def any_type(self):
            return self.getTypedRuleContext(D96Parser.Any_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_local_decl_wo_asg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_local_decl_wo_asg" ):
                return visitor.visitMethod_local_decl_wo_asg(self)
            else:
                return visitor.visitChildren(self)




    def method_local_decl_wo_asg(self):

        localctx = D96Parser.Method_local_decl_wo_asgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_method_local_decl_wo_asg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.idname_list()
            self.state = 231
            self.match(D96Parser.COLON)
            self.state = 232
            self.any_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_local_decl_w_asgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_NAME(self):
            return self.getToken(D96Parser.ID_NAME, 0)

        def method_local_decl_rep(self):
            return self.getTypedRuleContext(D96Parser.Method_local_decl_repContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_local_decl_w_asg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_local_decl_w_asg" ):
                return visitor.visitMethod_local_decl_w_asg(self)
            else:
                return visitor.visitChildren(self)




    def method_local_decl_w_asg(self):

        localctx = D96Parser.Method_local_decl_w_asgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method_local_decl_w_asg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(D96Parser.ID_NAME)
            self.state = 235
            self.method_local_decl_rep()
            self.state = 236
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_local_decl_repContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def ID_NAME(self):
            return self.getToken(D96Parser.ID_NAME, 0)

        def method_local_decl_rep(self):
            return self.getTypedRuleContext(D96Parser.Method_local_decl_repContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def any_type(self):
            return self.getTypedRuleContext(D96Parser.Any_typeContext,0)


        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_local_decl_rep

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_local_decl_rep" ):
                return visitor.visitMethod_local_decl_rep(self)
            else:
                return visitor.visitChildren(self)




    def method_local_decl_rep(self):

        localctx = D96Parser.Method_local_decl_repContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_method_local_decl_rep)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(D96Parser.COMMA)
                self.state = 239
                self.match(D96Parser.ID_NAME)
                self.state = 240
                self.method_local_decl_rep()
                self.state = 241
                self.expr()
                self.state = 242
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(D96Parser.COLON)
                self.state = 245
                self.any_type()
                self.state = 246
                self.match(D96Parser.EQ)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Entry_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(D96Parser.MAIN, 0)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def stmt_wo_return(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Stmt_wo_returnContext)
            else:
                return self.getTypedRuleContext(D96Parser.Stmt_wo_returnContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_entry_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntry_method" ):
                return visitor.visitEntry_method(self)
            else:
                return visitor.visitChildren(self)




    def entry_method(self):

        localctx = D96Parser.Entry_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_entry_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(D96Parser.MAIN)
            self.state = 251
            self.match(D96Parser.LCB)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.IF) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.FOREACH) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.DEC_LITERAL) | (1 << D96Parser.HEX_LITERAL) | (1 << D96Parser.OCTAL_LITERAL) | (1 << D96Parser.BINARY_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID_NAME) | (1 << D96Parser.LP) | (1 << D96Parser.LOG_NEGATE) | (1 << D96Parser.MINUS))) != 0):
                self.state = 252
                self.stmt_wo_return()
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 258
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_wo_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_local_decl(self):
            return self.getTypedRuleContext(D96Parser.Method_local_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmtContext,0)


        def flow_stmt(self):
            return self.getTypedRuleContext(D96Parser.Flow_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(D96Parser.For_stmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_wo_return

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_wo_return" ):
                return visitor.visitStmt_wo_return(self)
            else:
                return visitor.visitChildren(self)




    def stmt_wo_return(self):

        localctx = D96Parser.Stmt_wo_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmt_wo_return)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.method_local_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
                self.break_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 263
                self.continue_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 264
                self.flow_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 265
                self.for_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 266
                self.expr()
                self.state = 267
                self.match(D96Parser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cons_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def param_list(self):
            return self.getTypedRuleContext(D96Parser.Param_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_cons_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCons_method" ):
                return visitor.visitCons_method(self)
            else:
                return visitor.visitChildren(self)




    def cons_method(self):

        localctx = D96Parser.Cons_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_cons_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 272
            self.match(D96Parser.LP)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID_NAME:
                self.state = 273
                self.param_list()


            self.state = 276
            self.match(D96Parser.RP)
            self.state = 277
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Des_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_des_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDes_method" ):
                return visitor.visitDes_method(self)
            else:
                return visitor.visitChildren(self)




    def des_method(self):

        localctx = D96Parser.Des_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_des_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(D96Parser.DESTRUCTOR)
            self.state = 280
            self.match(D96Parser.LP)
            self.state = 281
            self.match(D96Parser.RP)
            self.state = 282
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ParamContext)
            else:
                return self.getTypedRuleContext(D96Parser.ParamContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMICOLON)
            else:
                return self.getToken(D96Parser.SEMICOLON, i)

        def getRuleIndex(self):
            return D96Parser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = D96Parser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.param()
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMICOLON:
                self.state = 285
                self.match(D96Parser.SEMICOLON)
                self.state = 286
                self.param()
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idname_list(self):
            return self.getTypedRuleContext(D96Parser.Idname_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def any_type(self):
            return self.getTypedRuleContext(D96Parser.Any_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = D96Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.idname_list()
            self.state = 293
            self.match(D96Parser.COLON)
            self.state = 294
            self.any_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.LiteralContext)
            else:
                return self.getTypedRuleContext(D96Parser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_literal_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_list" ):
                return visitor.visitLiteral_list(self)
            else:
                return visitor.visitChildren(self)




    def literal_list(self):

        localctx = D96Parser.Literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_literal_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.literal()
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 297
                self.match(D96Parser.COMMA)
                self.state = 298
                self.literal()
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_literal(self):
            return self.getTypedRuleContext(D96Parser.Int_literalContext,0)


        def FLOAT_LITERAL(self):
            return self.getToken(D96Parser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def boolean_literal(self):
            return self.getTypedRuleContext(D96Parser.Boolean_literalContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(D96Parser.Array_literalContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_literal)
        try:
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DEC_LITERAL, D96Parser.HEX_LITERAL, D96Parser.OCTAL_LITERAL, D96Parser.BINARY_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.int_literal()
                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.match(D96Parser.FLOAT_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 306
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 307
                self.boolean_literal()
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 308
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC_LITERAL(self):
            return self.getToken(D96Parser.DEC_LITERAL, 0)

        def HEX_LITERAL(self):
            return self.getToken(D96Parser.HEX_LITERAL, 0)

        def OCTAL_LITERAL(self):
            return self.getToken(D96Parser.OCTAL_LITERAL, 0)

        def BINARY_LITERAL(self):
            return self.getToken(D96Parser.BINARY_LITERAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_int_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_literal" ):
                return visitor.visitInt_literal(self)
            else:
                return visitor.visitChildren(self)




    def int_literal(self):

        localctx = D96Parser.Int_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_int_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.DEC_LITERAL) | (1 << D96Parser.HEX_LITERAL) | (1 << D96Parser.OCTAL_LITERAL) | (1 << D96Parser.BINARY_LITERAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_boolean_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_literal" ):
                return visitor.visitBoolean_literal(self)
            else:
                return visitor.visitChildren(self)




    def boolean_literal(self):

        localctx = D96Parser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            _la = self._input.LA(1)
            if not(_la==D96Parser.TRUE or _la==D96Parser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_idname_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC_ID_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.STATIC_ID_NAME)
            else:
                return self.getToken(D96Parser.STATIC_ID_NAME, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_static_idname_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_idname_list" ):
                return visitor.visitStatic_idname_list(self)
            else:
                return visitor.visitChildren(self)




    def static_idname_list(self):

        localctx = D96Parser.Static_idname_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_static_idname_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(D96Parser.STATIC_ID_NAME)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 316
                self.match(D96Parser.COMMA)
                self.state = 317
                self.match(D96Parser.STATIC_ID_NAME)
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idname_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID_NAME)
            else:
                return self.getToken(D96Parser.ID_NAME, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_idname_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdname_list" ):
                return visitor.visitIdname_list(self)
            else:
                return visitor.visitChildren(self)




    def idname_list(self):

        localctx = D96Parser.Idname_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_idname_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(D96Parser.ID_NAME)
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 324
                self.match(D96Parser.COMMA)
                self.state = 325
                self.match(D96Parser.ID_NAME)
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def literal_list(self):
            return self.getTypedRuleContext(D96Parser.Literal_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = D96Parser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(D96Parser.LP)
            self.state = 332
            self.literal_list()
            self.state = 333
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Any_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(D96Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def any_type(self):
            return self.getTypedRuleContext(D96Parser.Any_typeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def int_literal(self):
            return self.getTypedRuleContext(D96Parser.Int_literalContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def ID_NAME(self):
            return self.getToken(D96Parser.ID_NAME, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_any_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAny_type" ):
                return visitor.visitAny_type(self)
            else:
                return visitor.visitChildren(self)




    def any_type(self):

        localctx = D96Parser.Any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_any_type)
        try:
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.match(D96Parser.INTEGER)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 337
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 338
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 339
                self.match(D96Parser.ARRAY)
                self.state = 340
                self.match(D96Parser.LSB)
                self.state = 341
                self.any_type()
                self.state = 342
                self.match(D96Parser.COMMA)
                self.state = 343
                self.int_literal()
                self.state = 344
                self.match(D96Parser.RSB)
                pass
            elif token in [D96Parser.ID_NAME]:
                self.enterOuterAlt(localctx, 6)
                self.state = 346
                self.match(D96Parser.ID_NAME)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.expr()
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 350
                self.match(D96Parser.COMMA)
                self.state = 351
                self.expr()
                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr1Context,i)


        def STR_CONCAT(self):
            return self.getToken(D96Parser.STR_CONCAT, 0)

        def STR_EQ(self):
            return self.getToken(D96Parser.STR_EQ, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.expr1()
                self.state = 358
                _la = self._input.LA(1)
                if not(_la==D96Parser.STR_CONCAT or _la==D96Parser.STR_EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 359
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr2Context,i)


        def LOG_EQ(self):
            return self.getToken(D96Parser.LOG_EQ, 0)

        def LOG_NEQ(self):
            return self.getToken(D96Parser.LOG_NEQ, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def LEQ(self):
            return self.getToken(D96Parser.LEQ, 0)

        def GEQ(self):
            return self.getToken(D96Parser.GEQ, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.expr2(0)
                self.state = 365
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LOG_EQ) | (1 << D96Parser.LOG_NEQ) | (1 << D96Parser.GT) | (1 << D96Parser.GEQ) | (1 << D96Parser.LT) | (1 << D96Parser.LEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 366
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(D96Parser.Expr2Context,0)


        def LOG_AND(self):
            return self.getToken(D96Parser.LOG_AND, 0)

        def LOG_OR(self):
            return self.getToken(D96Parser.LOG_OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 374
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 375
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.LOG_AND or _la==D96Parser.LOG_OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 376
                    self.expr3(0) 
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def PLUS(self):
            return self.getToken(D96Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 390
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 385
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 386
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.PLUS or _la==D96Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 387
                    self.expr4(0) 
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def ASTERISK(self):
            return self.getToken(D96Parser.ASTERISK, 0)

        def F_SLASH(self):
            return self.getToken(D96Parser.F_SLASH, 0)

        def PERCENT(self):
            return self.getToken(D96Parser.PERCENT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 401
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 396
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 397
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ASTERISK) | (1 << D96Parser.F_SLASH) | (1 << D96Parser.PERCENT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 398
                    self.expr5() 
                self.state = 403
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOG_NEGATE(self):
            return self.getToken(D96Parser.LOG_NEGATE, 0)

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr5)
        try:
            self.state = 407
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LOG_NEGATE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.match(D96Parser.LOG_NEGATE)
                self.state = 405
                self.expr5()
                pass
            elif token in [D96Parser.SELF, D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL, D96Parser.NEW, D96Parser.DEC_LITERAL, D96Parser.HEX_LITERAL, D96Parser.OCTAL_LITERAL, D96Parser.BINARY_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ID_NAME, D96Parser.LP, D96Parser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr6)
        try:
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.match(D96Parser.MINUS)
                self.state = 410
                self.expr6()
                pass
            elif token in [D96Parser.SELF, D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL, D96Parser.NEW, D96Parser.DEC_LITERAL, D96Parser.HEX_LITERAL, D96Parser.OCTAL_LITERAL, D96Parser.BINARY_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ID_NAME, D96Parser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.expr7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 424
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 417
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 418
                    self.match(D96Parser.LSB)
                    self.state = 419
                    self.expr()
                    self.state = 420
                    self.match(D96Parser.RSB) 
                self.state = 426
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID_NAME(self):
            return self.getToken(D96Parser.ID_NAME, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 442
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 430
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 431
                    self.match(D96Parser.DOT)
                    self.state = 432
                    self.match(D96Parser.ID_NAME)
                    self.state = 438
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        self.state = 433
                        self.match(D96Parser.LP)
                        self.state = 435
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.DEC_LITERAL) | (1 << D96Parser.HEX_LITERAL) | (1 << D96Parser.OCTAL_LITERAL) | (1 << D96Parser.BINARY_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID_NAME) | (1 << D96Parser.LP) | (1 << D96Parser.LOG_NEGATE) | (1 << D96Parser.MINUS))) != 0):
                            self.state = 434
                            self.expr_list()


                        self.state = 437
                        self.match(D96Parser.RP)

             
                self.state = 444
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def COLON2(self):
            return self.getToken(D96Parser.COLON2, 0)

        def STATIC_ID_NAME(self):
            return self.getToken(D96Parser.STATIC_ID_NAME, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr9)
        self._la = 0 # Token type
        try:
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.expr10()
                self.state = 446
                self.match(D96Parser.COLON2)
                self.state = 447
                self.match(D96Parser.STATIC_ID_NAME)
                self.state = 453
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 448
                    self.match(D96Parser.LP)
                    self.state = 450
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.DEC_LITERAL) | (1 << D96Parser.HEX_LITERAL) | (1 << D96Parser.OCTAL_LITERAL) | (1 << D96Parser.BINARY_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID_NAME) | (1 << D96Parser.LP) | (1 << D96Parser.LOG_NEGATE) | (1 << D96Parser.MINUS))) != 0):
                        self.state = 449
                        self.expr_list()


                    self.state = 452
                    self.match(D96Parser.RP)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 455
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID_NAME(self):
            return self.getToken(D96Parser.ID_NAME, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def operand(self):
            return self.getTypedRuleContext(D96Parser.OperandContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.state = 466
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.match(D96Parser.NEW)
                self.state = 459
                self.match(D96Parser.ID_NAME)
                self.state = 460
                self.match(D96Parser.LP)
                self.state = 462
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.DEC_LITERAL) | (1 << D96Parser.HEX_LITERAL) | (1 << D96Parser.OCTAL_LITERAL) | (1 << D96Parser.BINARY_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID_NAME) | (1 << D96Parser.LP) | (1 << D96Parser.LOG_NEGATE) | (1 << D96Parser.MINUS))) != 0):
                    self.state = 461
                    self.expr_list()


                self.state = 464
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.SELF, D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL, D96Parser.DEC_LITERAL, D96Parser.HEX_LITERAL, D96Parser.OCTAL_LITERAL, D96Parser.BINARY_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ID_NAME, D96Parser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def ID_NAME(self):
            return self.getToken(D96Parser.ID_NAME, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = D96Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_operand)
        try:
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                self.match(D96Parser.LP)
                self.state = 469
                self.expr()
                self.state = 470
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 473
                self.match(D96Parser.ID_NAME)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 474
                self.match(D96Parser.SELF)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 475
                self.match(D96Parser.NULL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class New_object_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID_NAME(self):
            return self.getToken(D96Parser.ID_NAME, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_new_object_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNew_object_expr" ):
                return visitor.visitNew_object_expr(self)
            else:
                return visitor.visitChildren(self)




    def new_object_expr(self):

        localctx = D96Parser.New_object_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_new_object_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(D96Parser.NEW)
            self.state = 479
            self.match(D96Parser.ID_NAME)
            self.state = 480
            self.match(D96Parser.LP)
            self.state = 482
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.DEC_LITERAL) | (1 << D96Parser.HEX_LITERAL) | (1 << D96Parser.OCTAL_LITERAL) | (1 << D96Parser.BINARY_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID_NAME) | (1 << D96Parser.LP) | (1 << D96Parser.LOG_NEGATE) | (1 << D96Parser.MINUS))) != 0):
                self.state = 481
                self.expr_list()


            self.state = 484
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhsContext,0)


        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def assign_rhs(self):
            return self.getTypedRuleContext(D96Parser.Assign_rhsContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.assign_lhs()
            self.state = 487
            self.match(D96Parser.EQ)
            self.state = 488
            self.assign_rhs()
            self.state = 489
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs_sub_expr(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhs_sub_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs" ):
                return visitor.visitAssign_lhs(self)
            else:
                return visitor.visitChildren(self)




    def assign_lhs(self):

        localctx = D96Parser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_assign_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.assign_lhs_sub_expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_rhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_rhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_rhs" ):
                return visitor.visitAssign_rhs(self)
            else:
                return visitor.visitChildren(self)




    def assign_rhs(self):

        localctx = D96Parser.Assign_rhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_assign_rhs)
        try:
            self.state = 495
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 494
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lhs_sub_expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs_sub_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Assign_lhs_sub_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.Assign_lhs_sub_exprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs_sub_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs_sub_expr_list" ):
                return visitor.visitAssign_lhs_sub_expr_list(self)
            else:
                return visitor.visitChildren(self)




    def assign_lhs_sub_expr_list(self):

        localctx = D96Parser.Assign_lhs_sub_expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_assign_lhs_sub_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.assign_lhs_sub_expr(0)
            self.state = 502
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 498
                self.match(D96Parser.COMMA)
                self.state = 499
                self.assign_lhs_sub_expr(0)
                self.state = 504
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lhs_sub_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs_sub_expr1(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhs_sub_expr1Context,0)


        def assign_lhs_sub_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Assign_lhs_sub_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.Assign_lhs_sub_exprContext,i)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs_sub_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs_sub_expr" ):
                return visitor.visitAssign_lhs_sub_expr(self)
            else:
                return visitor.visitChildren(self)



    def assign_lhs_sub_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Assign_lhs_sub_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_assign_lhs_sub_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.assign_lhs_sub_expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 515
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Assign_lhs_sub_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assign_lhs_sub_expr)
                    self.state = 508
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 509
                    self.match(D96Parser.LSB)
                    self.state = 510
                    self.assign_lhs_sub_expr(0)
                    self.state = 511
                    self.match(D96Parser.RSB) 
                self.state = 517
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Assign_lhs_sub_expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs_sub_expr2(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhs_sub_expr2Context,0)


        def assign_lhs_sub_expr1(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhs_sub_expr1Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID_NAME(self):
            return self.getToken(D96Parser.ID_NAME, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def assign_lhs_sub_expr_list(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhs_sub_expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs_sub_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs_sub_expr1" ):
                return visitor.visitAssign_lhs_sub_expr1(self)
            else:
                return visitor.visitChildren(self)



    def assign_lhs_sub_expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Assign_lhs_sub_expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_assign_lhs_sub_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.assign_lhs_sub_expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 533
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Assign_lhs_sub_expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assign_lhs_sub_expr1)
                    self.state = 521
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 522
                    self.match(D96Parser.DOT)
                    self.state = 523
                    self.match(D96Parser.ID_NAME)
                    self.state = 529
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        self.state = 524
                        self.match(D96Parser.LP)
                        self.state = 526
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==D96Parser.ID_NAME:
                            self.state = 525
                            self.assign_lhs_sub_expr_list()


                        self.state = 528
                        self.match(D96Parser.RP)

             
                self.state = 535
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Assign_lhs_sub_expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs_sub_expr3(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhs_sub_expr3Context,0)


        def assign_lhs_sub_expr2(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhs_sub_expr2Context,0)


        def COLON2(self):
            return self.getToken(D96Parser.COLON2, 0)

        def STATIC_ID_NAME(self):
            return self.getToken(D96Parser.STATIC_ID_NAME, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def assign_lhs_sub_expr_list(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhs_sub_expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs_sub_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs_sub_expr2" ):
                return visitor.visitAssign_lhs_sub_expr2(self)
            else:
                return visitor.visitChildren(self)



    def assign_lhs_sub_expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Assign_lhs_sub_expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_assign_lhs_sub_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.assign_lhs_sub_expr3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 551
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Assign_lhs_sub_expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assign_lhs_sub_expr2)
                    self.state = 539
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 540
                    self.match(D96Parser.COLON2)
                    self.state = 541
                    self.match(D96Parser.STATIC_ID_NAME)
                    self.state = 547
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                    if la_ == 1:
                        self.state = 542
                        self.match(D96Parser.LP)
                        self.state = 544
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==D96Parser.ID_NAME:
                            self.state = 543
                            self.assign_lhs_sub_expr_list()


                        self.state = 546
                        self.match(D96Parser.RP)

             
                self.state = 553
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Assign_lhs_sub_expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_NAME(self):
            return self.getToken(D96Parser.ID_NAME, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs_sub_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs_sub_expr3" ):
                return visitor.visitAssign_lhs_sub_expr3(self)
            else:
                return visitor.visitChildren(self)




    def assign_lhs_sub_expr3(self):

        localctx = D96Parser.Assign_lhs_sub_expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_assign_lhs_sub_expr3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.match(D96Parser.ID_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Flow_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def elseif_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Elseif_stmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.Elseif_stmtContext,i)


        def else_stmt(self):
            return self.getTypedRuleContext(D96Parser.Else_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_flow_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlow_stmt" ):
                return visitor.visitFlow_stmt(self)
            else:
                return visitor.visitChildren(self)




    def flow_stmt(self):

        localctx = D96Parser.Flow_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_flow_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.if_stmt()
            self.state = 560
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 557
                self.elseif_stmt()
                self.state = 562
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 564
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 563
                self.else_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self.match(D96Parser.IF)
            self.state = 567
            self.match(D96Parser.LP)
            self.state = 568
            self.expr()
            self.state = 569
            self.match(D96Parser.RP)
            self.state = 570
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt" ):
                return visitor.visitElseif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt(self):

        localctx = D96Parser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.match(D96Parser.ELSEIF)
            self.state = 573
            self.match(D96Parser.LP)
            self.state = 574
            self.expr()
            self.state = 575
            self.match(D96Parser.RP)
            self.state = 576
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = D96Parser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
            self.match(D96Parser.ELSE)
            self.state = 579
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def ID_NAME(self):
            return self.getToken(D96Parser.ID_NAME, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def for_range(self):
            return self.getTypedRuleContext(D96Parser.For_rangeContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = D96Parser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(D96Parser.FOREACH)
            self.state = 582
            self.match(D96Parser.LP)
            self.state = 583
            self.match(D96Parser.ID_NAME)
            self.state = 584
            self.match(D96Parser.IN)
            self.state = 585
            self.for_range()
            self.state = 586
            self.match(D96Parser.RP)
            self.state = 587
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def DOT2(self):
            return self.getToken(D96Parser.DOT2, 0)

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_range

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_range" ):
                return visitor.visitFor_range(self)
            else:
                return visitor.visitChildren(self)




    def for_range(self):

        localctx = D96Parser.For_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_for_range)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self.expr()
            self.state = 590
            self.match(D96Parser.DOT2)
            self.state = 591
            self.expr()
            self.state = 594
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 592
                self.match(D96Parser.BY)
                self.state = 593
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.match(D96Parser.BREAK)
            self.state = 597
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = D96Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self.match(D96Parser.CONTINUE)
            self.state = 600
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.match(D96Parser.RETURN)
            self.state = 604
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.DEC_LITERAL) | (1 << D96Parser.HEX_LITERAL) | (1 << D96Parser.OCTAL_LITERAL) | (1 << D96Parser.BINARY_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID_NAME) | (1 << D96Parser.LP) | (1 << D96Parser.LOG_NEGATE) | (1 << D96Parser.MINUS))) != 0):
                self.state = 603
                self.expr()


            self.state = 606
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def method_local_decl(self):
            return self.getTypedRuleContext(D96Parser.Method_local_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def flow_stmt(self):
            return self.getTypedRuleContext(D96Parser.Flow_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(D96Parser.For_stmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_stmt)
        try:
            self.state = 619
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 608
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 609
                self.method_local_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 610
                self.assign_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 611
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 612
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 613
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 614
                self.flow_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 615
                self.for_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 616
                self.expr()
                self.state = 617
                self.match(D96Parser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self.match(D96Parser.LCB)
            self.state = 625
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.IF) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.RETURN) | (1 << D96Parser.FOREACH) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.DEC_LITERAL) | (1 << D96Parser.HEX_LITERAL) | (1 << D96Parser.OCTAL_LITERAL) | (1 << D96Parser.BINARY_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID_NAME) | (1 << D96Parser.LP) | (1 << D96Parser.LCB) | (1 << D96Parser.LOG_NEGATE) | (1 << D96Parser.MINUS))) != 0):
                self.state = 622
                self.stmt()
                self.state = 627
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 628
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[31] = self.expr2_sempred
        self._predicates[32] = self.expr3_sempred
        self._predicates[33] = self.expr4_sempred
        self._predicates[36] = self.expr7_sempred
        self._predicates[37] = self.expr8_sempred
        self._predicates[46] = self.assign_lhs_sub_expr_sempred
        self._predicates[47] = self.assign_lhs_sub_expr1_sempred
        self._predicates[48] = self.assign_lhs_sub_expr2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def assign_lhs_sub_expr_sempred(self, localctx:Assign_lhs_sub_exprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def assign_lhs_sub_expr1_sempred(self, localctx:Assign_lhs_sub_expr1Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def assign_lhs_sub_expr2_sempred(self, localctx:Assign_lhs_sub_expr2Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         




