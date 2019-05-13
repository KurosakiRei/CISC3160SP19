

class Tokenizer:

    signs = ['=',';','+','-','*','(',')']
    def __init__(self, string):
        #removing whitespace 
        self.string = ''.join(list(filter(lambda x: x != ' ',string)))
        self.endPoint = len(self.string)
        self.currentPosition = 0

    # read the next token that starts from currentPosition and return the token and its type
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
