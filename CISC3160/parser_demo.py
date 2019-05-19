from tokenizer_demo import Tokenizer

class Parser:
    # open the file and tokenize the strings
    def __init__(self, filename):
        self.file = open (filename)
        self.token = Tokenizer(self.file.read())
        self.currentToken = {}
        self.symbolTable = {}
        self.program()
        self.print_table()

    # read the next token 
    def readToken(self):
        self.currentToken = self.token.next_token()

    # check if current token is equal to expected token
    def match(self, expectedToken):
        if self.currentToken['type'] != expectedToken:
            print ('error')
            raise Exception('Syntax Error: ', self.currentToken['type'] ,' not equal to ', expectedToken)

    #program
    def program(self):
        while True:
            self.assignment()
            if self.currentToken['type'] == 'EOF':
                break

    #assignment
    def assignment(self):
        self.readToken()
        if self.currentToken['type'] == 'Id':
            variable = self.currentToken['token']
            self.readToken()
            self.match('=')
            exp = self.exp()
            self.match(';')
            self.symbolTable[variable] = exp
            return

    #expression
    def exp(self):
        term = self.term()
        return term + self.exp_left()
    #eliminate left recursion
    def exp_left(self):
        if self.currentToken['type'] == '+':
            term = self.term()
            return term + self.exp_left()
        elif self.currentToken['type'] == '-':
            term = self.term()
            return (-1 * term) + self.exp_left()
        else:
            return 0
    
    #terms
    def term(self):
        factor = self.factor()
        return factor * self.term_left()
    #eliminate left recursion
    def term_left(self):
        self.readToken()
        if self.current_token['type'] == '*':
            factor = self.factor()
            return factor * self.term_left()
        else:
            return 1

    

    #Print out the Symbol Table
    def print_table(self):
        for eachitem in self.symbolTable.items():
           print('%s = %d' % (eachitem[0],eachitem[1]))
           self.file.close()

    
