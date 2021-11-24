# this is a class for the token words they can use
class Token:
    LET = 0 #let statements
    PRINT = 1 #Print statements
    PRINTLN = 2 # Print line statements to add onto a line
    IF = 3 #if statements
    THEN = 4 # then statements
    PLUS = 5 #addition statements
    MINUS = 6 #subtraction statements
    TIMES = 7 #multiplication statements
    DIVIDE = 8 #division statements
    NEWLINE = 9 #end of a line
    UNSIGNEDINT = 10 #Integer
    NAME = 11 # none keyword identifier
    EXIT = 12 # end program. Most likely not needed for kattis
    GREATER = 13 #greater >
    LESSER = 14 #less <
    STEP = 15 #step 
    GOTO = 16 #jump to line
    NOTEQUAL = 17 # not equal 
    LESSEQUAL = 18 # <=
    GREATEREQUAL = 19 #>=
    STRING = 20 #String value
    EQUAL = 21 # =
    AND = 22 # logical and
    OR = 23 # Logical or
    NOT = 24 # Logical Negation
    ASSIGNOP = 25 # = 
    LEFTPAREN = 26 # (
    RIGHTPAREN = 27 # )
    COMMA = 28 # ,
    ELSE = 29 #else 
    FOR = 30 #for loop
    #INT = 30 #INT FUNCTION

    #Symbol assignments
    Symbol = {'=': ASSIGNOP, '(': LEFTPAREN, ')': RIGHTPAREN,
              '+': PLUS, '-': MINUS, '*': TIMES, '/': DIVIDE,
              '\n': NEWLINE, '<': LESSER,'>': GREATER,'<>': NOTEQUAL,
              '<=': LESSEQUAL, '>=': GREATEREQUAL, ',': COMMA,
              '!=': NOTEQUAL}

    #Displayable names for different Tokens
    callnm = ['LET','PRINT','PRINTLN','IF','THEN','PLUS','MINUS','TIMES',
              'DIVIDE','NEWLINE','UNSIGNEDINT','NAME','EXIT','GREATER',
              'LESSER','STEP','GOTO','NOTEQUAL','LESSEQUAL','GREATEREQUAL',
              'STRING','EQUAL','AND','OR','NOT','ASSIGNOP','LEFTPAREN',
              'RIGHTPAREN','COMMA', 'ELSE', 'FOR']

    #Disctionary of BASIC needed words
    keywords = {'LET': LET, 'PRINT' : PRINT, 'PRINTLN': PRINTLN,
                'IF': IF, 'THEN': THEN, 'EXIT' : EXIT,'STEP': STEP,
                'GOTO': GOTO,'ELSE': ELSE, 'FOR': FOR}
    
    #functions to be used 
    #funcs = {}
    #^^^ not needed for this kattis problem

    def __init__(self, column, category, lexeme):
        self.column = column #column that the token starts on
        self.category = category # category that the token is in
        self.lexeme = lexeme #Token in string form

    def nice_print(self):
        print('Column:', self.column,'Category: ', self.callnm[self.category],
        'Lexeme: ',self.lexeme)

    def print_lex(self):
        print(self.lexeme, end = ' ')
#NICE
