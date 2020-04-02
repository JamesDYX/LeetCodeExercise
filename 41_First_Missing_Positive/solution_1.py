class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        nums = set(nums)
        for i in range(1, len(nums)+1):
            if i not in nums:
                return i
        return len(nums)+1


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [1, 2, 0],
        [3, 4, -1, 1],
        [7, 8, 9, 11, 12],
        [1, 2, 3]
    ]
    for nums in test_cases:
        print(solution.firstMissingPositive(nums))
