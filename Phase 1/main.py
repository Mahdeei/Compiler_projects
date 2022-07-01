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
    
    result = dict() 
    arr = [] 

    for token in tokens:
        arr.append(token)

    for index,token in enumerate(arr):
        if token.type == "ID" or token.type == "MAIN": 
            
            current_token_type = "undefined" 
            if token.value in result.keys(): 
                if "type" in result[token.value]: 
                    current_token_type = result[token.value]["type"] 

            if index > 0 and (not (token.value in result.keys())): 
                last_token = arr[index - 1]
                
                if last_token.type in DATA_TYPES:
                    
                    current_token_type = last_token.type 

            current_token_value = "undefined" 
            if token.value in result.keys(): 
                if "value" in result[token.value]: 
                    current_token_value = result[token.value]["value"] 

            if index < len(arr) - 2: 
                next_token = arr[index + 1] 
                
                if next_token.type == "ASSIGN":
                    
                    val_token = arr[index + 2] 
                    
                    if val_token.type in LITERALS_LIST:
                        
                        current_token_value = val_token.value 

            result[token.value] = {
                "id": arr.index(token) + 1,
                "name": token.value,
                "type": current_token_type,
                "value": current_token_value
            }

    print("\nsymbols : ")
    for k, v in result.items():
	    print(k+" : ",v)


    
        


