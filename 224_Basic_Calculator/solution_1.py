class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        index = 0
        while index < len(s):
            if s[index] == ' ':
                index += 1
                continue
            elif s[index] == '+' or s[index] == '-' or s[index] == '(':
                stack.append(s[index])
                index += 1
                continue
            elif s[index] == ')':
                number = stack.pop()
                stack.pop()
                index += 1
            else:
                number = 0
                while index < len(s) and s[index].isdigit():
                    number = number * 10 + int(s[index])
                    index += 1

            if not stack or stack[-1] == '(':
                stack.append(number)
                continue
            operator = stack.pop()
            number1 = stack[-1]
            if operator == '+':
                stack[-1] = number1 + number
            else:
                stack[-1] = number1 - number

        return stack[0]


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        "1 + 1",
        " 2-1 + 2 ",
        "(1+(4+5+2)-3)+(6+8)",
        "2-(5-6)",
    ]

    for test_case in test_cases:
        print(solution.calculate(test_case))

