from Token import Token as tok

class Lexer:
    def __init__(self):
        self.column = 0 #column number
        self.__stmt = ''
    
    def tokenize(self, stmt):
        self.__stmt = stmt
        self.__column = 0

        #list of tokens to be taken from statement
        tokenlt = []

        #Process every character in string
        c = self.__get_next_char()
        while c!= '':
            