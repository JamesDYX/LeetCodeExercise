class Solution:
    def generateParenthesis(self, n: int) -> list:
        if not n:
            return [""]
        solution_set = [[""]]
        for counter in range(1, n+1):
            temp_set = []
            for left_n in range(counter):
                right_n = counter-left_n-1
                for string_1 in solution_set[left_n]:
                    for string_2 in solution_set[right_n]:
                        temp_set.append(string_1+'('+string_2+')')
            if counter == n:
                return temp_set
            solution_set.append(temp_set)


if __name__ == '__main__':
    test_case = 4
    expected = \
["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

    solution = Solution()
    result = solution.generateParenthesis(test_case)

    if len(expected) == len(result):
        for s in expected:
            try:
                result.index(s)
            except Exception:
                print(s)
                break
    else:
        print(False)
