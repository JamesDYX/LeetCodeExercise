class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif not stack:
                return False
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
        return not stack


if __name__ == '__main__':
    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "]",
    ]

    solution = Solution()
    for test_case in test_cases:
        print(solution.isValid(test_case))
