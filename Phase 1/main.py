from lexer import JLexer

def readfile(filename):
    with open (filename) as f:
        data = f.read()
    return data


if __name__ == "__main__":


    lexer = JLexer()

    DATA_TYPES = ["CHAR", "STRING", "INT", "DOUBLE", "FLOATNUM", "LONG", "SHORT", "BOOLEAN"]

    LITERALS_LIST = ["CHAR_LIT", "STRING_LIT", "INTEGER", "FLOAT", "FALSE","TRUE"]

    inpNum = input("enter your file number : ")
    text = readfile("inputs/"+inpNum+".txt")

    tokens = lexer.tokenize(text) 
    

    
        


