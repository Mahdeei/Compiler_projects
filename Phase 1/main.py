from lexer import JLexer


# function braye khondan file
def readfile(filename):
    with open (filename) as f:
        data = f.read()
    return data

# main 
if __name__ == "__main__":

    # lexer misazim 
    lexer = JLexer()

    # inja data type haye khodemon ro moshakhas mikonim
    DATA_TYPES = ["CHAR", "STRING", "INT", "DOUBLE", "FLOATNUM", "LONG", "SHORT", "BOOLEAN"]

    # inja list litteral haye khodemon ro moshakhas mikonim
    LITERALS_LIST = ["CHAR_LIT", "STRING_LIT", "INTEGER", "FLOAT", "FALSE","TRUE"]

    # shomare file mored nazar braye test kardan az file input
    inpNum = input("enter your file number : ")
    # file ro mikhonim
    text = readfile("inputs/"+inpNum+".txt")

    # token haro migirim
    tokens = lexer.tokenize(text) 
    
    result = dict() #dictionary misazim 
    arr = [] # yek array braye rikhtan token ha dar oon

    # token haro dar array mirizim
    for token in tokens:
        arr.append(token)
        print(token)

    # dar in qesmat mikhahim symbol table ro besazim 
    for index,token in enumerate(arr):
        if token.type == "ID" or token.type == "MAIN": # shenasaei mikonim identfier haro ya main ro  
            
            current_token_type = "undefined" # baraye set kardan type avalin bar undefind mizarim 
            if token.value in result.keys(): # agar dar kelid haye ma vojod dasht :
                if "type" in result[token.value]: # if type ash az qabl vojod dasht
                    current_token_type = result[token.value]["type"] # meqdar type ro hamon qabli mizarim

            if index > 0 and (not (token.value in result.keys())): #agar index > 0 bod va dar kelidha mojod nabod
                last_token = arr[index - 1] # token index qabli ro migirim
                
                if last_token.type in DATA_TYPES: # agar barabar ba data type ha bod 
                    
                    current_token_type = last_token.type #meqdarash ro update mikonim 

            current_token_value = "undefined"  # baraye set kardan value avalin bar undefind mizarim 
            if token.value in result.keys(): # agar dar kelid haye ma vojod dasht :
                if "value" in result[token.value]: # if value ash az qabl vojod dasht
                    current_token_value = result[token.value]["value"] # meqdar value ro hamon qabli mizarim

            if index < len(arr) - 2: # dar sorati ke 2 token qabltar bod :
                next_token = arr[index + 1] # token badi ro migirm va check mikonim
                
                if next_token.type == "ASSIGN": # agar = assign(=) bod 
                    
                    val_token = arr[index + 2] # token badi ro daryaft mikonim 
                    
                    if val_token.type in LITERALS_LIST: # agar barabar ba list litteral ha bod 
                        
                        current_token_value = val_token.value # update mikonim meqdarash ro

            # dar akhar result ro ba kelid hale hazer , maqadir id,name,type,value update mikonim 
            result[token.value] = {
                "id": arr.index(token) + 1,
                "name": token.value,
                "type": current_token_type,
                "value": current_token_value
            }

    print("\nsymbols : ")
    # print mikonim symbol table ro be sorat joda joda
    for k, v in result.items():
	    print(k+" : ",v)


    #finish


    
        


