class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        last_ = 1
        last__ = 1

        for i in range(2, n+1):
            last_, last__ = last_ + last__, last_
        return last_


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(4))

