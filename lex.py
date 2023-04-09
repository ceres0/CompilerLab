class Lex(object):
    def __init__(self, tranDict, accept):
        self.tranDict = tranDict
        self.state = 0 # InitState
        self.accept = accept
        
    def Transfer(self, inch): # inch: input char

