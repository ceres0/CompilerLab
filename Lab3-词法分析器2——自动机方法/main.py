from lex import Lex
from config import Config

if __name__ == '__main__':
    cf = Config()
    lex = Lex(cf.tranDicts, [6])
    print('dict = ', cf.dict)
    print('r =', cf.regular)
    while True:
        print('Please choose:\n\t(1) Standard input\n\t(2) File input')
        ch = input('> ')
        if ch == '1':
            instr = input('> ')
            break
        elif ch == '2':
            fileDir = input('File: ')
            with open(fileDir, encoding='utf-8') as f:
                instr = f.read()
            break
        else:
            print('Error!')
    instrs = ''.join(instr.split()).split(';')
    # print(instrs)
    for str in instrs:
        lex.Recongnize(str)

