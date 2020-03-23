from copy import deepcopy


class Solution:
    def letterCombinations(self, digits: str) -> list:
        if not digits:
            return []
        phone_key = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = [""]
        for digit in digits:
            index = int(digit) - 2
            temp_result = []
            for temp_s in result:
                for alpha in phone_key[index]:
                    temp_result.append(temp_s + alpha)
            result = temp_result
        return result


if __name__ == '__main__':
    test_cases = [
        "",
        "23",
        "233"
    ]

    solution = Solution()
    for test_case in test_cases:
        print(solution.letterCombinations(test_case))
