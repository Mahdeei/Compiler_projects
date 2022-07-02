class SymTable:
    def __init__(self):
        self.symbols = {}

    def insert(self, token):
        self.symbols[token.value] = {'type':token.type, 'lineNumber':token.lineno, 'index':token.index}
    
    def search(self, token):
        if token.value in self.symbols.keys():
            print('yes')
            return True
        print('no')
        return False