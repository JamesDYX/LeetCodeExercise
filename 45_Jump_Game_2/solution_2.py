class Solution:
    """
    Smarter DP
    """
    def jump(self, nums: list) -> int:
        if len(nums) == 1: return 0
        dp = [0] * len(nums)
        frontier = 0
        for i, n in enumerate(nums):
            if i + n > frontier:
                dp[frontier + 1:i + n + 1] = [dp[i] + 1] * (i + n - frontier)
                frontier = i + n
                if i + n >= len(nums) - 1: break
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [2, 3, 1, 1, 4],
        [9, 2]
    ]
    for nums in test_cases:
        print(solution.jump(nums))
