class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            output = int(str(x)[::-1])
        else:
            output = -int(str(-x)[::-1])
        if output > 2**31 - 1 or output < -2**31:
            return 0
        return output


if __name__ == '__main__':
    test_cases = [
        -123,
        120
    ]

    solution = Solution()
    for x in test_cases:
        print(solution.reverse(x))
