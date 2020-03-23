class Solution:
    def calculate(self, s: str) -> int:
        stack = [1, 1]  # a ( and a +
        result = 0
        index = 0
        while index < len(s):
            if s[index] == ' ':
                index += 1
            elif s[index] == '(' or s[index] == '+':
                stack.append(stack[-1])
                index += 1
            elif s[index] == '-':
                stack.append(-stack[-1])
                index += 1
            elif s[index] == ')':
                stack.pop()
                index += 1
            else:
                start = index
                while index < len(s) and s[index].isdigit():
                    index += 1
                number = int(s[start:index])
                result += stack.pop() * number
        return result


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
