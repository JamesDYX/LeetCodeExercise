import functools


class Solution:
    """
    expr := [+|-] term {(+|-) term}
    term := factor {* factor}
    factor := variable | '(' expr ')' | integer
    """
    def basicCalculatorIV(self, expression: str, evalvars: list, evalints: list) -> list:
        eval_pair = {}
        for key, value in zip(evalvars, evalints):
            eval_pair[key] = value

        def expr(start_index) -> (list, int):
            # expr := [+|-] term {(+|-) term}
            neg = False
            while start_index < len(expression) and expression[start_index] == ' ':
                start_index += 1
            if expression[start_index] == '+':
                start_index += 1
            elif expression[start_index] == '-':
                neg = True
                start_index += 1
            while start_index < len(expression) and expression[start_index] == ' ':
                start_index += 1
            result, start_index = term(start_index)
            if neg:
                result = multiply_expr(result, [(-1, [])])
            while True:
                while start_index < len(expression) and expression[start_index] == ' ':
                    start_index += 1
                if start_index == len(expression):
                    break
                if expression[start_index] == '+':
                    neg = False
                elif expression[start_index] == '-':
                    neg = True
                else:
                    break
                start_index += 1
                while expression[start_index] == ' ':
                    start_index += 1
                temp_result, start_index = term(start_index)
                if neg:
                    temp_result = multiply_expr(temp_result, [(-1, [])])
                result += temp_result
            return simplifier(result), start_index

        def term(start_index) -> (list, int):
            # term := factor {* factor}
            result, start_index = factor(start_index)
            while True:
                while start_index < len(expression) and expression[start_index] == ' ':
                    start_index += 1
                if start_index == len(expression) or expression[start_index] != '*':
                    break
                start_index += 1
                while expression[start_index] == ' ':
                    start_index += 1
                temp_result, start_index = factor(start_index)
                result = simplifier(multiply_expr(result, temp_result))
            return result, start_index

        def factor(start_index) -> (list, int):
            # factor := variable | '(' expr ')' | integer
            if expression[start_index] == '(':
                result, start_index = expr(start_index+1)
                return result, start_index + 1
            elif expression[start_index].isdigit():
                begin = start_index
                start_index += 1
                while start_index < len(expression) and expression[start_index].isdigit():
                    start_index += 1
                result = [(int(expression[begin: start_index]), [])]
                return result, start_index
            else:
                begin = start_index
                start_index += 1
                while start_index < len(expression) and expression[start_index].isalpha():
                    start_index += 1
                var = expression[begin:start_index]
                if var in eval_pair:
                    return [(eval_pair[var], [])], start_index
                return [(1, [var])], start_index

        def simplifier(expression: list) -> list:
            result = []
            expr_index_pair = {}
            for coe, var in expression:
                encode = ''
                for v in var:
                    encode += ' '+v
                if encode in expr_index_pair:
                    id = expr_index_pair[encode]
                    coe += result[id][0]
                    result[id] = (coe, var)
                else:
                    id = len(result)
                    result.append((coe, var))
                    expr_index_pair[encode] = id
            index = 0
            while index < len(result):
                if result[index][0] == 0:
                    result.pop(index)
                else:
                    index += 1
            return result

        def multiply_expr(expression1: list, expression2: list) -> list:
            result = []
            for coe_1, var_1 in expression1:
                for coe_2, var_2 in expression2:
                    coe = coe_1 * coe_2
                    if not var_1 or not var_2:
                        var = var_1 if var_1 else var_2
                        result.append((coe, var))
                    else:
                        var = var_1 + var_2
                        var.sort()
                        result.append((coe, var))
            return result

        def cmp(term1: tuple, term2: tuple) -> int:
            var1 = term1[1]
            var2 = term2[1]
            if len(var1) > len(var2):
                return -1
            elif len(var1) < len(var2):
                return 1
            elif var1 < var2:
                return -1
            else:
                return 1

        result, _ = expr(0)
        result = sorted(result, key=functools.cmp_to_key(cmp))
        output = []
        for coe, var in result:
            s = coe.__str__()
            for v in var:
                s += ('*'+v)
            output.append(s)
        return output


if __name__ == '__main__':
    solution = Solution()
    huge_test = ("(9 * ((5 - 1 - f) + 11 * (12 * d - p) + (y - ac) + (bk * 8 + 6 * cg * r)) + cl) * o * ((cf * bp + p - 7) + (b + bq - bk) - 2) + bk",
                 ["d", "g", "h", "j", "l", "o", "s", "u", "v", "w", "af", "ag", "ah", "ak", "at", "au", "av", "aw", "az", "bc", "be", "bg", "bj", "bm", "bn", "bq", "br", "bs", "bt", "bu", "bv", "bw", "bx", "by", "bz", "ca", "cd", "ce", "cf", "ch", "ci", "ck", "cq", "cr", "cs", "cu", "cv"],
                 [3, 6, 7, 9, 11, 1, 5, 7, 8, 9, 10, 11, 12, 2, 11, 12, 0, 1, 4, 12, 1, 3, 6, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 5, 6, 7, 9, 10, 12, 5, 6, 7, 9, 10])
    test_cases = [
        ("e + 8 - a + 5", ["e"], [1]),
        ("e - 8 + temperature - pressure", ["e", "temperature"], [1, 12]),
        ("(e + 8) * (e - 8)", [], []),
        ("7 - 7", [], []),
        ("a * b * c + b * a * c * 4", [], []),
        ("((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))", [], []),
        huge_test
    ]

    expected = ["54*b*cg*r","-54*bk*cg*r","378*bp*cg*r","54*cg*p*r","-9*ac*b","9*ac*bk","-63*ac*bp","-9*ac*p","72*b*bk","1*b*cl","-9*b*f","-99*b*p","9*b*y","-72*bk*bk","504*bk*bp","-1*bk*cl","9*bk*f","171*bk*p","-9*bk*y","7*bp*cl","-63*bp*f","-693*bp*p","63*bp*y","-486*cg*r","1*cl*p","-9*f*p","-99*p*p","9*p*y","81*ac","3600*b","-4247*bk","25200*bp","-9*cl","81*f","4491*p","-81*y","-32400"]
    for expression, evalvars, evalints in test_cases:
        print(solution.basicCalculatorIV(expression, evalvars, evalints))
