import re


def is_identifier(s):
    # 标识符由字母、数字和下划线组成，且以字母或下划线开头
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', s) is not None


def is_integer(s):
    # 整数由数字组成，可以带有正负号和小数点
    return re.match(r'^[-+]?\d+(\.\d+)?$', s) is not None


class PredParser:
    def __init__(self, grammar, first, follow, terms):
        self.grammar = grammar

        self.first = first
        self.follow = follow
        self.terms = terms
        self.pred_table = {}

    def generate_pred_table(self):
        for nonterminal in self.grammar.keys():
            for terminal in self.first[nonterminal]:
                if terminal != 'epsilon':
                    for prod in self.grammar[nonterminal]:
                        if prod[0] == terminal or prod[0] in self.grammar.keys():
                            self.pred_table[(nonterminal, terminal)] = prod
            if 'epsilon' in self.first[nonterminal]:
                for terminal in self.follow[nonterminal]:
                    self.pred_table[(nonterminal, terminal)
                                    ] = self.grammar[nonterminal]

    def parse(self, input_str):
        stack = ['$', 'S']
        while stack[-1] == '$' and input_str == '':
            top = stack[-1]
            term = self.get_term(input_str)
            if top == term:
                stack.pop()
                input_str = input_str[1:]
            elif top in self.grammar.keys():
                try:
                    input_str = input_str[len(term):]
                    print(top, '->', self.pred_table[(top, term)])
                    prod = self.pred_table[(top, term)]
                    stack.pop()
                    if prod[0] != 'epsilon':
                        stack.extend(reversed(prod))
                    print(stack)
                except KeyError:
                    print('Error: invalid token')
                    break
            else:
                print('Error: invalid symbol')
                break

    def get_term(self, str):
        term = ''
        while len(str) > 0 and str[0] == ' ':
            str = str[1:]
        for c in str:
            if c in self.term or c == ' ':
                break
            else:
                term += c
        if term == '' and str[0] != ' ':
            term = str[0]
        elif is_identifier(term):
            term = 'id'
        elif is_integer(term):
            term = 'num'
        return term


# 示例用法
grammar = {
    'S': [['E']],
    'E': [['T', '+', 'E'], ['T', '-', 'E'], ['T']],
    'T': [['F', '*', 'T'], ['F', '/', 'T'], ['F']],
    'F': [['(', 'E', ')'], ['id']]
}

first = {
    'S': {'id', '('},
    'E': {'id', '(', '+', '-'},
    'T': {'id', '(', '*', '/'},
    'F': {'id', '('}
}

follow = {
    'S': {'$', ')'},
    'E': {'$', ')'},
    'T': {'+', '-', '$', ')'},
    'F': {'*', '/', '+', '-', '$', ')'}
}

terms = {'+', '-', '*', '/', '(', ')', 'id', '$'}

parser = PredParser(grammar, first, follow, terms)
parser.generate_pred_table()
print(parser.pred_table)
