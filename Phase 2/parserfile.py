from sly import Parser
from lexer import JLexer


class JParser(Parser): 
    def __init__(self, symbolTable):
        super().__init__()
        self.symbolTable = symbolTable

    debugfile = 'output.txt'
    tokens = JLexer.tokens
    precedence = (('nonassoc', EQUAL, LEQUAL, GEQUAL, NEQUAL, GREATERT, LESST), ('left', PLUS, MINUS), ('left', TIMES, DIVIDE),)

    @_("statements")
    def block(self, p):
        print('#1#', self.symstack, '\n')
        return p.statements

    @_("")
    def block(self, p):
        print('#2#', self.symstack, '\n')
        return []

    @_('statement')
    def statements(self, p):
        print('#3#', self.symstack, '\n')
        return [p.statement]

    @_('statements statement')
    def statements(self, p):
        print('#4#', self.symstack, '\n')
        p.statements.append(p.statement)
        return p.statements

    @_('var_declaration')
    def statement(self, p):
        print('#5#', self.symstack, '\n')
        return p.var_declaration

    @_('main_declaration')
    def statement(self, p):
        print('#6#', self.symstack, '\n')
        return p.main_declaration

    @_('assign_statement')
    def statement(self, p):
        print('#7#', self.symstack, '\n')
        return p.assign_statement

    @_('if_statement')
    def statement(self, p):
        print('#8#', self.symstack, '\n')
        return p.if_statement

    @_('while_statement')
    def statement(self, p):
        print('#9#', self.symstack, '\n')
        return p.while_statement

    @_('for_statement')
    def statement(self, p):
        print('#10#', self.symstack, '\n')
        return p.for_statement

    @_('switch_statement')
    def statement(self, p):
        print('#11#', self.symstack, '\n')
        return p.switch_statement

    @_('return_statement')
    def statement(self, p):
        print('#12#', self.symstack, '\n')
        return p.return_statement

    @_('break_statement')
    def statement(self, p):
        print('#13#', self.symstack, '\n')
        return p.break_statement

    @_('continue_statement')
    def statement(self, p):
        print('#14#', self.symstack, '\n')
        return p.continue_statement

    @_('plusplus_statement')
    def statement(self, p):
        print('#15#', self.symstack, '\n')
        return p.plusplus_statement

    @_('minusminus_statement')
    def statement(self, p):
        print('#16#', self.symstack, '\n')
        return p.minusminus_statement
    
    @_('plusplus_expr SEMI')
    def plusplus_statement(self, p):
        print('#17#', self.symstack, '\n')
        return p.plusplus_expr

    @_('minusminus_expr SEMI')
    def minusminus_statement(self, p):
        print('#18#', self.symstack, '\n')
        return p.minusminus_expr

    @_('CONTINUE SEMI')
    def continue_statement(self, p):
        print('#19#', self.symstack, '\n')
        return ('continue', )

    @_('BREAK SEMI')
    def break_statement(self, p):
        print('#20#', self.symstack, '\n')
        return ('break', )

    @_('RETURN expr SEMI')
    def return_statement(self, p):
        print('#21#', self.symstack, '\n')
        return ('return', p.expr)

    @_('RETURN SEMI')
    def return_statement(self, p):
        print('#22#', self.symstack, '\n')
        return ('return', )

    @_('IF LPAREN expr RPAREN LBRACE block RBRACE else_statement')
    def if_statement(self, p):
        print('#23#', self.symstack, '\n')
        return ('if', p.expr, ('branch', p.block), p.else_statement)

    @_('ELSE LPAREN expr RPAREN LBRACE block RBRACE else_statement')
    def else_statement(self, p):
        print('#24#', self.symstack, '\n')
        return ('else if', p.expr, ('branch', p.block), p.else_statement)

    @_('ELSE LBRACE block RBRACE')
    def else_statement(self, p):
        print('#25#', self.symstack, '\n')
        return ('else', ('branch', p.block))

    @_('')
    def else_statement(self, p):
        print('#26#', self.symstack, '\n')
        return []

    @_('WHILE LPAREN expr RPAREN LBRACE block RBRACE')
    def while_statement(self, p):
        print('#27#', self.symstack, '\n')
        return ('while_loop', ('while_loop_setup', p.expr), p.block)

    @_('FOR LPAREN var_declaration SEMI expr SEMI assign_statement RPAREN LBRACE block RBRACE')
    def for_statement(self, p):
        print('#28#', self.symstack, '\n')
        return ('for_loop', ('for_loop_setup', p.var_declaration, p.logical_expr, p.assignment_expr), p.block)

    @_('SWITCH LPAREN ID RPAREN LBRACE switch_block RBRACE')
    def switch_statement(self, p):
        print('#29#', self.symstack, '\n')
        return ('switch_statement', p.ID, p.switch_block)

    @_('CASE literal COL block switch_block')
    def switch_block(self, p):
        print('#30#', self.symstack, '\n')
        return ('switch_case', p.block, p.switch_block)

    @_('DEFAULT COL block')
    def switch_block(self, p):
        print('#31#', self.symstack, '\n')
        return ('switch_default', p.block)

    @_('block')
    def switch_block(self, p):
        print('#32#', self.symstack, '\n')
        return p.block

    @_("")
    def switch_block(self, p):
        print('#33#', self.symstack, '\n')
        return []

    @_('TYPE ID ASSIGN expr SEMI')
    def var_declaration(self, p):
        print('#34#', self.symstack, '\n')
        if (p.TYPE != p.expr[0]):
            return f'ERROR: Value does not match the type at line {p.lineno}'
        for token in self.symstack:
            if token.type == "ID":
                if self.symbolTable.search(token) == False:
                    self.symbolTable.insert(token)
                else:
                    print(
                        f'ERROR: Variable already defined at line {p.lineno}')

        return ('var_declaration', p.ID, p.expr)

    @_('TYPE ID SEMI')
    def var_declaration(self, p):
        print('#35#', self.symstack, '\n')
        for token in self.symstack:
            if token.type == "ID":
                if self.symbolTable.search(token) == False:
                    self.symbolTable.insert(token)
                else:
                    print(f'ERROR: Variable already defined at line{p.lineno}')

        return ('var_declaration', p.ID)

    @_('VOID MAIN LPAREN RPAREN LBRACE block RBRACE')
    def main_declaration(self, p):
        print('#36#', self.symstack, '\n')
        for token in self.symstack:
            if token.type == "MAIN":
                if self.symbolTable.search(token) == False:
                    self.symbolTable.insert(token)
                else:
                    print(
                        f'ERROR: Variable already defined at line {p.lineno}')

        return ('main_declaration', p.ID)

    @_('ID ASSIGN expr SEMI')
    def assign_statement(self, p):
        print('#37#', self.symstack, '\n')
        for token in self.symstack:
            if token.type == "ID":
                if self.symbolTable.search(token) == False:
                    print(f'ERROR: Variable is not defined at line {p.lineno}')

        return ('var_assignment', p.ID, p.expr)

    @_('expr PLUS expr',
        'expr MINUS expr',
        'expr TIMES expr',
        'expr DIVIDE expr',
        'expr MOD expr',
        'expr LESST expr',
        'expr LEQUAL expr',
        'expr GREATERT expr',
        'expr GEQUAL expr',
        'expr EQUAL expr',
        'expr NEQUAL expr',
        'expr AND expr',
        'expr OR expr')
    def expr(self, p):
        print('#38#', self.symstack, '\n')
        return (p[1], p.expr0, p.expr1)

    @_('NOT expr')
    def expr(self, p):
        print('#39#', self.symstack, '\n')
        return ('not', p.expr)

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        print('#40#', self.symstack, '\n')
        return p.expr

    @_('plusplus_expr',
       'minusminus_expr')
    def expr(self, p):
        print('#41#', self.symstack, '\n')
        return p[0]

    @_('ID PLUSPLUS')
    def plusplus_expr(self, p):
        print('#42#', self.symstack, '\n')
        return ('post_plusplus', p.ID)

    @_('PLUSPLUS ID')
    def plusplus_expr(self, p):
        print('#42#', self.symstack, '\n')
        return ('pre_plusplus', p.ID)

    @_('ID MINUSMINUS')
    def minusminus_expr(self, p):
        print('#43#', self.symstack, '\n')
        return ('post_minusminus', p.ID)

    @_('MINUSMINUS ID')
    def minusminus_expr(self, p):
        print('#44#', self.symstack, '\n')
        return ('pre_minusminus', p.ID)

    @_('ID')
    def expr(self, p):
        print('#45#', self.symstack, '\n')
        return p.ID

    @_('literal')
    def expr(self, p):
        print('#46#', self.symstack, '\n')
        return p.literal

    @_('INTEGER')
    def literal(self, p):
        print('#47#', self.symstack, '\n')
        return ('int', p.INTEGER)

    @_('FLOAT')
    def literal(self, p):
        print('#48#', self.symstack, '\n')
        return ('float', p.FLOAT)

    @_('CHAR')
    def literal(self, p):
        print('#49#', self.symstack, '\n')
        return ('char', p.CHAR)

    @_('STRING')
    def literal(self, p):
        print('#50#', self.symstack, '\n')
        return ('String', p.STRING)

    @_('BOOLEAN')
    def literal(self, p):
        print('#51#', self.symstack, '\n')
        return ('boolean', p.BOOLEAN)

    def error(self, token):
        print(
            f'SYNTAX ERROR near character "{token.value}" at line {token.lineno}')
