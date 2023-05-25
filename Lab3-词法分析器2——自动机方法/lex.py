class Lex(object):
    def __init__(self, tranDicts, accepts):
        self.tranDicts = tranDicts
        self.state = 0 # InitState
        self.accepts = accepts
        
    def Transfer(self, inch): # inch: input char
        self.state = self.tranDicts[self.state][inch] if inch in self.tranDicts[self.state] else -1
        if self.state in self.accepts:
            return True
        return False

    def Reset(self):
        self.state = 0

    def Recongnize(self, instr): # instr: input str
        len1 = len(instr)
        flag = True
        for i in range(len1):
            flag = self.Transfer(instr[i])
            if self.state == -1:
                break
        print(instr, 'yes' if flag else 'no')
        self.Reset()

if __name__ == '__main__':
    dicts = []
    dict1 = {'a': 0, 'b': 1}
    dicts.append(dict1)
    dicts.append(dict1)
    # print(dicts[0])
    # print(len(dicts))
    lex = Lex(dicts,[1])
    while True:
        str = input('> ')
        if str == 'q':
            break
        lex.Recongnize(str)
