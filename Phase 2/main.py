from lexer import JLexer
from parserfile import JParser
from symbolTable import SymTable

# Read source code from file
def filereader(filename):
    with open (filename) as f:
        data = f.read()
    return data

# main
if __name__ == "__main__":
    # create symbol table
    mySymbolTable = SymTable()
    # create lexer
    lexer = JLexer()
    # create parser
    parser = JParser(mySymbolTable)

    # read file test.txt
    text = filereader("test.txt")
    # get tokens
    symt = lexer.tokenize(text)
    # parse tokens to result
    result = parser.parse(symt)
    # print tokens
    print(JLexer.tokens)
    # print results 
    print("Critical---------------------")
    for item in result:
        print(item)
    print("Critical---------------------")

    # print updated symbol table
    print('Symbol Table =>', mySymbolTable.symbols)
    
