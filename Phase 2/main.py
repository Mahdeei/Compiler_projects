import sys
from lexer import JLexer
from parserfile import JParser
from symbolTable import SymTable

def filereader(filename):
    with open (filename) as f:
        data = f.read()
    return data

if __name__ == "__main__":
    mySymbolTable = SymTable()
    lexer = JLexer()
    parser = JParser(mySymbolTable)

    list_of_tokens = []


    text = filereader("test.txt")
    symt = lexer.tokenize(text)
    result = parser.parse(symt)

    print(JLexer.tokens)

    print("Critical---------------------")
    for item in result:
        print(item)
    print("Critical---------------------")


    print('Symbol Table =>', mySymbolTable.symbols)
    
