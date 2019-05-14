import re #for using regular expression 

class Tokenizer:

    signs = { 'Id': re.compile(r'[a-zA-Z_]([a-zA-Z_]|[0-9])*'),
              'Lit': re.compile(r'0|[1-9][0-9]*'),
              'Dot': re.compile('.'),
              '=': re.compile(r'='),
              ';': re.compile(r';'),
              '+': re.compile(r'\+'),
              '-': re.compile(r'-'),
              '*': re.compile(r'\*'),
              '(': re.compile(r'\('),
              ')': re.compile(r'\)'),
              }
    def __init__(self, string):
        #removing whitespace 
        self.string = ''.join(list(filter(lambda x: x != ' ',string)))
        self.currentPosition = 0
        self.endPoint = len(self.string)

    # read the next vaild token 
    # then return the token and its type
    def next_token(self):
        if self.currentPosition < self.endPoint:
            if self.string[self.currentPosition].find('.') != -1:
                return {'token': '', 'type': 'error'} 
            if self.string[self.currentPosition].isalnum():
                return {'token': self.string[self.currentPosition], 'type': 'Id'}
            if self.string[self.currentPosition].isalpha():
                return {'token': self.string[self.currentPosition], 'type': 'Lit'}
            for sign in self.signs:
                match = self.signs[sign] == self.string[self.currentPosition]
                if match:
                        return {'token': self.string[self.currentPosition], 'type': sign} 
        else:
            #return the 'EOF' when it touch the end
            return {'token': '', 'type': 'EOF'}
