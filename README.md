<!-- ABOUT THE PROJECT -->
## About The Project
In this project, we have 2 phases. The first phase is related to lexical analysis. The second phase is related to parser analysis. In the following, we will give explanations for each phase separately.

## Phase 1
In this phase, we will have lexical analysis. In such a way that the user selects a text file and we analyze it lexically in Java language. The output of the file is also printed as a symbol table .

Now let's go to the description of the code: We define the tokens that are in the Java language and also put the patterns that are supposed to recognize the tokens. For example, the comment or new line identification pattern.

new line :
``` 
@_(r'\n+')
    def ignore_enter(self, t): # filter newlines
        self.lineno += t.value.count('\n')
```

or multiline comments
```
ignore_multiline_comments = r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'
```


In the main file, the contents of the file are also read:
```
text = readfile("inputs/"+inpNum+".txt")
```


Then the contents of the file goes to the lexical analysis class and returns the tokens.
```
tokens = lexer.tokenize(text) 
```


Then, to generate the symbol table, we need to check the tokens before and after, what type they are and what their value is, and if not, the value is set as undefined.

```
DATA_TYPES = ["CHAR", "STRING", "INT", "DOUBLE", "FLOATNUM", "LONG", "SHORT", "BOOLEAN"]

LITERALS_LIST = ["CHAR_LIT", "STRING_LIT", "INTEGER", "FLOAT", "FALSE","TRUE"]
.
.
.
current_token_type = "undefined"
```


And finally, the symbol table is printed.

    for k, v in result.items():
	    print(k+" : ",v)
	    
	    
## Phase 2
In the second phase, we have parser analysis, which is the next step after lexical analysis.

```
symt = lexer.tokenize(text)
```

As in the first phase, we perform lexical analysis and then send the tokens we have recognized to the parser class.
```
result = parser.parse(symt)
```
In the parser class, we define precedence.
```
precedence = 
(('nonassoc', EQUAL, LEQUAL, GEQUAL, NEQUAL, GREATERT, LESST), 
('left', PLUS, MINUS), 
('left', TIMES, DIVIDE),)
```


Then we define the existing grammars. For example, the :
```
@_("statements")
    def block(self, p):
     
      	return p.statements
```

At the end, we put a function for error detection.
```
def error(self, token):
        print(
            f'SYNTAX ERROR near character "{token.value}" at line {token.lineno}')	   
```

After the analysis process, the Pars tree output is printed for us.

And at the end, the symbol table is printed again for us.

```
print('Symbol Table =>', mySymbolTable.symbols) 
```



### Built With

* [python](https://www.python.org/)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This project has no Prerequisites

### Installation


1. Clone the repo
   ```sh
    https://github.com/Mahdeei/compiler_1401
   ```

<p align="right">(<a href="#top">back to top</a>)</p>





<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

mahdi khatib - [@symaach](https://instagram.com/symaach) - khmahdee@gmail.com

Project Link: [https://github.com/Mahdeei/compiler_1401](https://github.com/Mahdeei/compiler_1401)

<p align="right">(<a href="#top">back to top</a>)</p>



