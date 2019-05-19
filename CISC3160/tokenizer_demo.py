import re #for using regular expression 

class Tokenizer:

    #dictionaries the token types
    signs = { 'Id': re.compile(r'[a-zA-Z_]([a-zA-Z_]|[0-9])*'),
              'Lit': re.compile(r'0|[1-9][0-9]*'),
              '=': re.compile('\='),
              ';': re.compile('\;'),
              '+': re.compile('\+'),
              '-': re.compile('\-'),
              '*': re.compile('\*'),
              '(': re.compile('\('),
              ')': re.compile('\)'),
              }
    def __init__(self, string):
        #removing whitespace 
        self.string = ''.join(list(filter(lambda x: x != ' ',string)))
        self.currentPosition = 0
        self.endPoint = len(self.string)

    # In order to read the next vaild token 
    # and then return the token and its type
    def next_token(self):
        if self.currentPosition < self.endPoint:
            #check if the string contained '.'
            if self.string.find('.') != -1:
                print('error')
                raise Exception('ERROR: unrecognized character', self.text[match.start():match.end()])
            for pattern in self.signs:
                match = self.signs[pattern].match(self.string, self.currentPosition)
                if match:
                        self.currentPosition = match.end()
                        return {'token': self.string[match.start():match.end()], 'type': pattern} 
                    #return the string and its type
        else:
            #return the 'EOF' when it touch the end of file
            return {'token': '', 'type': 'EOF'}
