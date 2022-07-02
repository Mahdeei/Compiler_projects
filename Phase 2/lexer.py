from sly import Lexer


class JLexer(Lexer): 
    tokens = {
        LBRACE, RBRACE, COL, SEMI,
        FOR, WHILE, IF, ELSE, SWITCH, CASE, BREAK,
        STRING, CHAR, BOOLEAN, FLOAT, AND, OR, NOT,
        GREATERT, LESST, ASSIGN, PLUSPLUS, MINUSMINUS, PLUS,
        VOID, MAIN, DEFAULT, CONTINUE, RETURN, INTEGER,
        MINUS, DIVIDE, TIMES, MOD, LPAREN, RPAREN,
        TYPE, ID, EQUAL, LEQUAL, GEQUAL, NEQUAL,
    }

    ignore = '[ \t]'
    ignore_comments = r'\/\/.*'
    ignore_multiline_comments = r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'

    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACE = r'{'
    RBRACE = r'}'
    SEMI = r';'
    COL = r':'
    PLUSPLUS = r'\+\+'
    MINUSMINUS = r'\-\-'
    PLUS = r'\+'
    MINUS = r'\-'
    DIVIDE = r'\/'
    TIMES = r'\*'
    MOD = r'\%'
    EQUAL = r'\=\='
    NEQUAL = r'\!\='
    GEQUAL = r'>='
    LEQUAL = r'<='
    GREATERT = r'>'
    LESST = r'<'
    ASSIGN = r'\='
    AND = r'\&\&'
    OR = r'\|\|'
    NOT = r'\!(?!\W)'

    CHAR = r'\'(.?|\\.)\''
    STRING = r'(\".*\")'

    @_(r'-?\d+\.\d+')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    @_(r'-?\d+')
    def INTEGER(self, t):
        t.value = int(t.value)
        return t

    ID = r'[a-zA-Z_]+[a-zA-Z0-9_]*'

    ID['int'] = TYPE
    ID['long'] = TYPE
    ID['float'] = TYPE
    ID['double'] = TYPE
    ID['char'] = TYPE
    ID['String'] = TYPE
    ID['boolean'] = TYPE
    ID['true'] = BOOLEAN
    ID['false'] = BOOLEAN
    ID['for'] = FOR
    ID['while'] = WHILE
    ID['break'] = BREAK
    ID['continue'] = CONTINUE
    ID['if'] = IF
    ID['else'] = ELSE
    ID['switch'] = SWITCH
    ID['case'] = CASE
    ID['default'] = DEFAULT
    ID['void'] = VOID
    ID['main'] = MAIN
    ID['return'] = RETURN

    @_(r'\n+')
    def ignore_enter(self, t): # filter newlines
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
