class Solution:
    def plusOne(self, digits: list) -> list:
        i = len(digits) - 1
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
        if i >= 0:
            digits[i] += 1
            return digits
        else:
            return [1] + digits


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [4, 3, 2, 1],
        [9]
    ]

    for digits in test_cases:
        print(solution.plusOne(digits))
