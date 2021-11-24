class JumpSig:
    SIMPLE_JUMP = 0
    LOOP_BEGIN = 1
    LOOP_REPEAT = 2
    LOOP_SKIP = 3
    RETURN = 4
    EXECUTE = 5

    def __init__(self, ftarget=None, ftype=SIMPLE_JUMP, floop_var=None):
        if ftype not in [self.GOSUB, self.SIMPLE_JUMP, self.LOOP_BEGIN,
                         self.LOOP_REPEAT, self.RETURN,
                         self.LOOP_SKIP, self.STOP, self.EXECUTE]:
            raise TypeError('Invalid Jump sig type provided: ' + str(ftype))
        if ftarget == None and \
            ftype in [self.SIMPLE_JUMP, self.LOOP_SKIP]:
            raise TypeError("Invalid jump target provided: " + str(ftarget))
        
        if ftarget != None and \
            ftype in [self.RETURN, self.LOOP_BEGIN, self.LOOP_REPEAT,
                self.STOP, self.EXECUTE]:
                raise TypeError("Target wrongly Provided " + str(ftype))
        
        self.ftype = ftype
        self.ftarget = ftarget
        self.floop_var = floop_var