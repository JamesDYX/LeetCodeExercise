class Solution:
    def checkPossibility(self, nums: list) -> bool:
        i = 0
        while i+2 < len(nums) and nums[i] <= nums[i+1]:
            i += 1
        if i >= len(nums) - 2:
            return True
        j = len(nums) - 1
        while j - 1 > 0 and nums[j] >= nums[j-1]:
            j -= 1
        if j <= 1:
            return True
        if j != i + 1:
            return False
        if nums[i-1] <= nums[j] or nums[i] <= nums[j+1]:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [4, 2, 3],
        [4, 2, 1],
        [1, 2, 3, 5, 4, 6]
    ]
    for nums in test_cases:
        print(solution.checkPossibility(nums))
