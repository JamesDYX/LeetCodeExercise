class Solution:
    def calculate(self, s: str) -> int:
        number_stack = []
        operator_stack = []

        def pop_operator():
            operator = operator_stack.pop()
            num2 = number_stack.pop()
            num1 = number_stack[-1]
            if operator == '+':
                number_stack[-1] = num1 + num2
            elif operator == '-':
                number_stack[-1] = num1 - num2
            elif operator == '*':
                number_stack[-1] = num1 * num2
            elif operator == '/':
                number_stack[-1] = int(num1/num2)

        index = 0
        while index < len(s):
            ch = s[index]
            if ch.isdigit():
                start = index
                while index < len(s) and s[index].isdigit():
                    index += 1
                number_stack.append(int(s[start:index]))
                continue
            elif ch == '(':
                operator_stack.append(ch)
            elif ch == '+' or ch == '-':
                while operator_stack and operator_stack[-1] != '(':
                    pop_operator()
                operator_stack.append(ch)
            elif ch == '*' or ch == '/':
                while operator_stack and (operator_stack[-1] == '*' or operator_stack[-1] == '/'):
                    pop_operator()
                operator_stack.append(ch)
            elif ch == ')':
                while operator_stack[-1] != '(':
                    pop_operator()
                operator_stack.pop()
            index += 1

        while operator_stack:
            pop_operator()

        return number_stack[0]


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        "1 + 1",
        " 2-1 + 2 ",
        "(1+(4+5+2)-3)+(6+8)",
        "2-(5-6)",
        "3+2*2",
        "3+2*2/(4+ 1)",
        "1*2-3/4+5*6-7*8+9/10",
    ]

    for test_case in test_cases:
        print(solution.calculate(test_case))