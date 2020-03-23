from collections import defaultdict


class Number(object):
    def __init__(self):
        self.vars = []
        self.scales = []

    @property
    def size(self):
        return len(self.scales)

    def multiply_n(self, n):
        for i in range(self.size):
            self.scales[i] *= n

    def multiply_token(self, s):
        for i in range(self.size):
            self.vars[i][s] += 1

    def add_n(self, n):
        for i in range(self.size):
            if len(self.vars[i]) == 0:
                self.scales[i] += n
                break
        self.vars.append(defaultdict(int))
        self.scales.append(n)

    def get_key(self, var):
        return '*'.join(sorted(['*'.join([k] * var[k]) for k in var]))

    def add_number(self, num):
        key2idx = {self.get_key(var): i for i, var in enumerate(self.vars)}
        keys1 = [self.get_key(var) for var in num.vars]
        for i, key in enumerate(keys1):
            if key in key2idx:
                self.scales[key2idx[key]] += num.scales[i]
            else:
                self.vars.append(num.vars[i])
                self.scales.append(num.scales[i])

    def multiply_number(self, num):
        new_var = []
        new_scales = []
        new_keys = dict()
        for i, var1 in enumerate(self.vars):
            for j, var2 in enumerate(num.vars):
                cnt = defaultdict(int)
                for k in var1:
                    cnt[k] += var1[k]
                for k in var2:
                    cnt[k] += var2[k]
                key = self.get_key(cnt)

                if key in new_keys:
                    new_scales[new_keys[key]] += self.scales[i] * num.scales[j]
                else:
                    new_var.append(cnt)
                    new_scales.append(self.scales[i] * num.scales[j])
                    new_keys[self.get_key(cnt)] = len(new_scales) - 1
        self.vars = new_var
        self.scales = new_scales


class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        operators = {'(', ')', '*', '+', '-'}
        word2val = dict()
        for i, var in enumerate(evalvars):
            word2val[var] = evalints[i]

        expression = expression.replace(' ', '')
        expression = '(' + expression + ')'

        # extract tokens
        N = len(expression)

        i = 0
        tokens = []
        while i < N:
            if expression[i] in operators:
                tokens.append(expression[i])
                i += 1
                continue

            j = i + 1
            while j < N and expression[j] != ' ' and expression[j] not in operators:
                j += 1

            tokens.append(expression[i:j])
            i = j

        # do operations
        ops = []
        stk = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == '(':
                ops.append('(')
            elif token == '+' or token == '-':
                while ops and ops[-1] != '(':
                    n = stk.pop()
                    if ops[-1] == '*':
                        stk[-1].multiply_number(n)
                    elif ops[-1] == '+':
                        stk[-1].add_number(n)
                    else:
                        n.multiply_n(-1)
                        stk[-1].add_number(n)
                    ops.pop()
                ops.append(token)
            elif token == '*':
                if ops and ops[-1] == '*':
                    n = stk.pop()
                    stk[-1].multiply_number(n)
                    ops.pop()
                ops.append(token)
            elif token == ')':
                while ops[-1] != '(':
                    n = stk.pop()
                    if ops[-1] == '*':
                        stk[-1].multiply_number(n)
                    elif ops[-1] == '+':
                        stk[-1].add_number(n)
                    elif ops[-1] == '-':
                        n.multiply_n(-1)
                        stk[-1].add_number(n)
                    ops.pop()
                ops.pop()
            else:
                n = Number()
                if token.isdigit():
                    n.add_n(int(token))
                elif token in word2val:
                    n.add_n(word2val[token])
                else:
                    n.add_n(1)
                    n.multiply_token(token)
                stk.append(n)
            i += 1

        res = stk[0]
        keys = [(-sum(var.values()), res.get_key(var)) for var in res.vars]
        idxs = sorted(list(range(len(keys))), key=lambda i: keys[i])
        ans = []
        for idx in idxs:
            scale = res.scales[idx]
            if scale == 0:
                continue

            if keys[idx][0] == 0:
                ans.append(str(scale))
            else:
                ans.append('%d*%s' % (scale, keys[idx][1]))
        return ans