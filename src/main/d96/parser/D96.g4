grammar D96;

// 1952255

@lexer::header {
from lexererr import *
}

options {
  language = Python3;
}

// Program structures

program
  : class_decl* entry_class? class_decl* EOF
  ;

class_decl
  : CLASS ID_NAME (COLON ID_NAME)? LCB class_mem_decl* RCB
  ; // no multiple inheritance

// class_decl
//   : CLASS ID_NAME (COLON ID_NAME)? LCB class_mem_decl* des_method? class_mem_decl* RCB
//   ; // no multiple inheritance

entry_class
  : CLASS 'Program' LCB class_mem_decl* entry_method? class_mem_decl* RCB
  ;

class_mem_decl
  : attr_decl
  | method_decl
  | cons_method
  | des_method
  ;

// class_mem_decl
//   : attr_decl
//   | method_decl
//   | cons_method
//   ;

attr_decl
  : (VAL | VAR) (attr_decl_wo_asg | attr_decl_w_asg) SEMICOLON
  ;
attr_decl_wo_asg
  : attr_name_list COLON any_type
  ;
attr_decl_w_asg
  : (ID_NAME | STATIC_ID_NAME) attr_decl_rep expr
  ;
attr_decl_rep
  : COMMA (ID_NAME | STATIC_ID_NAME) attr_decl_rep expr COMMA
  | COLON any_type EQ
  ;
attr_name_list
  : (ID_NAME | STATIC_ID_NAME) (COMMA (ID_NAME | STATIC_ID_NAME))*
  ;

method_decl
  : (ID_NAME | STATIC_ID_NAME) LP param_list? RP block_stmt
  ;

method_local_decl
  : (VAL | VAR) (method_local_decl_wo_asg | method_local_decl_w_asg) SEMICOLON
  ;
method_local_decl_wo_asg
  : idname_list COLON any_type
  ;
method_local_decl_w_asg
  : ID_NAME method_local_decl_rep expr
  ;
method_local_decl_rep
  : COMMA ID_NAME method_local_decl_rep expr COMMA
  | COLON any_type EQ
  ;

entry_method
  : MAIN LCB stmt_wo_return* RCB
  ;
MAIN: 'main' LP RP; // If it's stupid but it works, it's not stupid
stmt_wo_return
  : method_local_decl
  | assign_stmt
  | break_stmt | continue_stmt
  | flow_stmt
  | for_stmt
  | expr SEMICOLON
  ;

cons_method
  : CONSTRUCTOR LP param_list? RP block_stmt
  ;

des_method
  : DESTRUCTOR LP RP block_stmt
  ;

param_list
  : param (SEMICOLON param)*
  ;

param
  : idname_list COLON any_type
  ;

// Lexical structures

CLASS: 'Class';
SELF: 'Self';
VAL: 'Val';
VAR: 'Var';

IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
BREAK: 'Break';
CONTINUE: 'Continue';
RETURN: 'Return';

FOREACH: 'Foreach';
IN: 'In';

TRUE: 'True';
FALSE: 'False';
NULL: 'Null';

STRING: 'String';
INTEGER: 'Int';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
ARRAY: 'Array';

CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';

literal_list
  : literal (COMMA literal)*
  ;

literal
  : int_literal
  | FLOAT_LITERAL
  | STRING_LITERAL
  | boolean_literal
  | array_literal
  ;

int_literal
  : DEC_LITERAL
  | HEX_LITERAL
  | OCTAL_LITERAL
  | BINARY_LITERAL
  ;
// DEC_LITERAL: SIGN? [0-9] [_0-9]* {self.text = self.text.replace("_", "")}; // Dec
DEC_LITERAL: ('0' | [1-9] [_0-9]*) {self.text = self.text.replace("_", "")}; // Dec
HEX_LITERAL: '0' X '_'? [0-9A-F] [_0-9A-F]* {self.text = self.text.replace("_", "")}; // Hex
OCTAL_LITERAL: '0' '_'? [0-7] [_0-7]* {self.text = self.text.replace("_", "")}; // Oct
BINARY_LITERAL: '0' B '_'? [0-1] [_0-1]* {self.text = self.text.replace("_", "")}; // Bin

FLOAT_LITERAL
  : FLOAT_INT_LITERAL FLOAT_DEC_LITERAL {self.text = self.text.replace("_", "")}
  | (FLOAT_INT_LITERAL | FLOAT_DEC_LITERAL) FLOAT_EXP_LITERAL {self.text = self.text.replace("_", "")}
  | FLOAT_INT_LITERAL FLOAT_DEC_LITERAL FLOAT_EXP_LITERAL {self.text = self.text.replace("_", "")}
  ; // TODO Test '1. .100'
fragment FLOAT_INT_LITERAL: '0' | [1-9] [_0-9]*;
fragment FLOAT_DEC_LITERAL: DOT ([0-9] [_0-9]*)?;
fragment FLOAT_EXP_LITERAL: E SIGN? [0-9] [_0-9]*;

boolean_literal
  : TRUE
  | FALSE
  ;

STRING_LITERAL: '"' SUB_STRING* '"' {self.text = self.text[1:-1]}; // Quotes are not part of the string

BLOCK_COMMENT: HASHTAG2 .*? HASHTAG2 -> skip;

STATIC_ID_NAME: '$' [_0-9A-Za-z]+;
ID_NAME: [_A-Za-z] [_0-9A-Za-z]*;
static_idname_list: STATIC_ID_NAME (COMMA STATIC_ID_NAME)*;
idname_list: ID_NAME (COMMA ID_NAME)*;

fragment ESC_SEQ: '\\' [bfrnt'\\] | '\'"';
fragment SIGN: [+-];
fragment SUB_STRING: ~[\b\f\r\n\t'"\\] | ESC_SEQ;

array_literal
  : LP literal_list RP
  ;

// Types and values

any_type
  : INTEGER
  | FLOAT
  | BOOLEAN
  | STRING
  | ARRAY LSB any_type COMMA int_literal RSB
  | ID_NAME
  ;

// Expressions

expr_list: expr (COMMA expr)*;

expr
  : expr1 (STR_CONCAT | STR_EQ) expr1
  | expr1
  ;
expr1
  : expr2 (LOG_EQ | LOG_NEQ | LT | GT | LEQ | GEQ) expr2
  | expr2
  ;
expr2
  : expr2 (LOG_AND | LOG_OR) expr3
  | expr3
  ;
expr3
  : expr3 (PLUS | MINUS) expr4
  | expr4
  ;
expr4
  : expr4 (ASTERISK | F_SLASH | PERCENT) expr5
  | expr5
  ;
expr5
  : LOG_NEGATE expr5
  | expr6
  ;
expr6
  : MINUS expr6
  | expr7
  ;
expr7
  : expr7 LSB expr RSB
  | expr8
  ;
expr8
  : expr8 DOT ID_NAME (LP expr_list? RP)?
  | expr9
  ;
expr9
  : expr10 COLON2 STATIC_ID_NAME (LP expr_list? RP)?
  | expr10
  ;
expr10
  : NEW ID_NAME LP expr_list? RP
  | operand
  ;

operand
  : LP expr RP
  | literal
  | ID_NAME
  | SELF
  | NULL
  ;

new_object_expr
  : NEW ID_NAME LP expr_list? RP
  ;

// Assignment

assign_stmt
  : assign_lhs EQ assign_rhs SEMICOLON
  ;
assign_lhs
  : assign_lhs_sub_expr
  ;
assign_rhs
  : assign_stmt
  | expr
  ;
assign_lhs_sub_expr_list: assign_lhs_sub_expr (COMMA assign_lhs_sub_expr)*;
assign_lhs_sub_expr
  : assign_lhs_sub_expr LSB assign_lhs_sub_expr RSB
  | assign_lhs_sub_expr1
  ;
assign_lhs_sub_expr1
  : assign_lhs_sub_expr1 DOT ID_NAME (LP assign_lhs_sub_expr_list? RP)?
  | assign_lhs_sub_expr2
  ;
assign_lhs_sub_expr2
  : assign_lhs_sub_expr2 COLON2 STATIC_ID_NAME (LP assign_lhs_sub_expr_list? RP)?
  | assign_lhs_sub_expr3
  ;
assign_lhs_sub_expr3: ID_NAME;

// Flow

flow_stmt
  : if_stmt elseif_stmt* else_stmt?
  ;

if_stmt
  : IF LP expr RP block_stmt
  ;

elseif_stmt
  : ELSEIF LP expr RP block_stmt
  ;

else_stmt
  : ELSE block_stmt
  ;

// Loop

for_stmt
  : FOREACH LP ID_NAME IN for_range RP block_stmt
  ;
for_range
  : expr DOT2 expr (BY expr)?
  ;

// Jump

break_stmt
  : BREAK SEMICOLON
  ;

continue_stmt
  : CONTINUE SEMICOLON
  ;

return_stmt
  : RETURN expr? SEMICOLON
  ;

// Block

stmt
  : block_stmt
  | method_local_decl
  | assign_stmt
  | break_stmt | continue_stmt | return_stmt
  | flow_stmt
  | for_stmt
  | expr SEMICOLON
  ;

block_stmt
  : LCB stmt* RCB
  ;

// Scopes

DOT: '.';
DOT2: '..';
COMMA: ',';
SEMICOLON: ';';
COLON: ':';
COLON2: '::';
LP: '(';
RP: ')';
LSB: '[';
RSB: ']';
LCB: '{';
RCB: '}';
fragment HASHTAG2: '##';

LOG_NEGATE: '!';
LOG_AND: '&&';
LOG_OR: '||';
LOG_EQ: '==';
LOG_NEQ: '!=';

EQ: '=';
PLUS: '+';
MINUS: '-';
ASTERISK: '*';
F_SLASH: '/';
PERCENT: '%';

GT: '>';
GEQ: '>=';
LT: '<';
LEQ: '<=';

STR_CONCAT: '+.';
STR_EQ: '==.';

fragment A: [Aa];
fragment B: [Bb];
fragment C: [Cc];
fragment D: [Dd];
fragment E: [Ee];
fragment F: [Ff];
fragment G: [Gg];
fragment H: [Hh];
fragment I: [Ii];
fragment J: [Jj];
fragment K: [Kk];
fragment L: [Ll];
fragment M: [Mm];
fragment N: [Nn];
fragment O: [Oo];
fragment P: [Pp];
fragment Q: [Qq];
fragment R: [Rr];
fragment S: [Ss];
fragment T: [Tt];
fragment U: [Uu];
fragment V: [Vv];
fragment W: [Ww];
fragment X: [Xx];
fragment Y: [Yy];
fragment Z: [Zz];

WS: [ \t\r\n]+ -> skip;

ERROR_TOKEN: . {raise ErrorToken(self.text)};
UNCLOSE_STRING
  :'"' SUB_STRING* ([\b\f\r\n\t'\\] | EOF)
  {
    tmp = str(self.text)
    illegal = ['\b', '\f', '\r', '\n', '\t', '\'', '\\']
    if tmp[-1] in illegal:
      raise UncloseString(tmp[1:-1])
    else:
      raise UncloseString(tmp[1:])
  }
  ;
ILLEGAL_ESCAPE
  : '"' SUB_STRING* '\\' ~[bfrnt'\\]
  {
    y = str(self.text)
    raise IllegalEscape(y[1:])
  }
  ;
