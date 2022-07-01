from sly import Lexer

class JLexer(Lexer): 

    tokens = {
        LBRACE, RBRACE, COL, SEMI,
        FOR, WHILE, IF, ELSE, SWITCH, CASE, BREAK,CHAR,STRING,
        STRING_LIT, CHAR_LIT, BOOLEAN, FLOATNUM, AND, OR, NOT,
        GREATERT, LESST, ASSIGN, PLUSPLUS, MINUSMINUS, PLUS,
        VOID, MAIN, DEFAULT, CONTINUE, RETURN, INTEGER,
        MINUS, DIVIDE, TIMES, MOD, LPAREN, RPAREN,
        TYPE, ID, EQUAL, LEQUAL, GEQUAL, NEQUAL,TRUE,FALSE,INT,DOUBLE
    }





    @_(r'-?\d+\.\d+')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    @_(r'-?\d+')
    def INTEGER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def ignore_enter(self, t): 
        self.lineno += t.value.count('\n')

    def find_column(self, text, token):
        last_cr = text.rfind('\n', 0, token.index)
        if last_cr < 0:
            last_cr = 0
        column = (token.index - last_cr) + 1
        return column

    def error(self, t):
        print(f'ERROR! Line {self.lineno}: Bad Character {t.value[0]}')
        self.index += 1
