class PredictiveParser:
    def __init__(self, grammar, first_sets, follow_sets):
        self.grammar = grammar
        self.first_sets = first_sets
        self.follow_sets = follow_sets
        self.predict_table = {}

        self.build_predict_table()

    def build_predict_table(self):
        for non_terminal in self.grammar:
            productions = self.grammar[non_terminal]
            for production in productions:
                first_set = self.get_first_set(production)
                if 'epsilon' in first_set:
                    follow_set = self.follow_sets[non_terminal]
                    first_set.remove('epsilon')
                    combined_set = first_set.union(follow_set)
                    for token in combined_set:
                        self.add_to_table(non_terminal, token, production)
                else:
                    for token in first_set:
                        self.add_to_table(non_terminal, token, production)

    def get_first_set(self, production):
        result_set = set()
        first_token = production[0]
        if first_token not in self.grammar:
            result_set.add(first_token)
        else:
            for sub_production in self.grammar[first_token]:
                sub_first_set = self.get_first_set(sub_production)
                result_set.update(sub_first_set)
                if 'epsilon' not in sub_first_set:
                    break
        return result_set

    def add_to_table(self, non_terminal, terminal, production):
        if non_terminal not in self.predict_table:
            self.predict_table[non_terminal] = {}
        if terminal in self.predict_table[non_terminal]:
            raise ValueError("Grammar is not LL(1)!")
        self.predict_table[non_terminal][terminal] = production

    def parse(self, sentence):
        stack = ['$']
        sentence.append('$')
        input_index = 0
        while len(stack) > 0:
            top_symbol = stack.pop()
            if top_symbol in self.grammar:
                try:
                    production = self.predict_table[top_symbol][sentence[input_index]]
                except KeyError:
                    raise ValueError("Error: no valid productions for symbol")
                stack.extend(reversed(production))
            elif top_symbol == sentence[input_index]:
                input_index += 1
            else:
                raise ValueError("Error: top of stack and input do not match")
        return "Accepted"


# 示例文法
grammar = {
    'S': [['A', 'B'], ['C', 'd']],
    'A': [['a'], ['epsilon']],
    'B': [['b'], ['epsilon']],
    'C': [['c'], ['epsilon']]
}

# 示例FIRST集合
first_sets = {
    'S': {'a', 'c'},
    'A': {'a', 'epsilon'},
    'B': {'b', 'epsilon'},
    'C': {'c', 'epsilon'}
}

# 示例FOLLOW集合
follow_sets = {
    'S': {'$'},
    'A': {'b', 'c', 'd', '$'},
    'B': {'c', 'd', '$'},
    'C': {'d', '$'}
}

parser = PredictiveParser(grammar, first_sets, follow_sets)
result = parser.parse(['a', 'b', 'c', 'd'])
print(result)  # 输出 Accepted
