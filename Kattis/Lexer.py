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
            #skip whitespace
            c = self.__get_next_char()
            while c.isspace():
                c = self.__get_next_char()
            Token = tok(self.__column - 1, None, '')

            if c == '"':
                Token.category = tok.STRING

                #Consume all the charcaters
                c = self.__get_next_char()

                if c == '"':
                    c = self.__get_next_char()

                else: 
                    while True:
                        Token.lexeme += c
                        c = self.__get_next_char()

                        if c == '':
                            raise SyntaxError('Mismatched quotes')
                        if c == '"':
                            c = self.__get_next_char()
                            break
            elif c.isdigit():
                Token.category = tok.UNSIGNEDINT
                found_point = False
                while True:
                    Token.lexeme += c
                    c = self.__get_next_char()
                    if not c.isdigit():
                        if c == '.':
                            if not found_point:
                                found_point = True
                                Token.category = tok.UNSIGNEDFLOAT
                            else:
                                break
                        else:
                            break
            elif c.isalpha():
                while True:
                    Token.lexeme += c
                    c = self.__get_next_char()
                    if not ((c.isalpha()or c.isdigit()) or c == '_' or c == '$'):
                        break
                Token.lexeme = Token.lexeme.upper()
                if Token.lexeme in tok.keywords:
                    Token.category = tok.keywords[Token.lexeme]

                else: 
                    Token.category = tok.NAME
                
                if Token.lexeme == 'REM':
                    while c != '':
                        Token.lexeme += c
                        c = self.__get_next_char()
            elif c in tok.Symbol:
                save = c
                c = self.__get_next_char()
                twochar = save + c
                if twochar in tok.Symbol:
                    Token.category = tok.Symbol[twochar]
                    Token.lexeme = twochar
                    c = self.__get_next_char()
                else:
                    Token.category = tok.Symbol[save]
            elif c != '':
                raise SyntaxError('Syntax Error')
            tokenlt.append(Token)
        return tokenlt

    def __get_next_char(self):
        if self.__column < len(self.__stmt):
            next_char = self.__stmt[self.__column]
            self.__column = self.__column + 1
            return next_char
        else:
            return ''

if __name__ == "__main__":
    import doctest
    doctest.testmod()