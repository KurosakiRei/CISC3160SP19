from tokenizer_demo import Tokenizer

class Parser:
        # open the file and tokenize the string
    def __init__(self, filename):
        self.file = open (filename)
        self.token = Tokenizer(self.file.read())
        self.current_token = {}
        self.symbol_table = {}
        self.program()
        self.print_table()

    
