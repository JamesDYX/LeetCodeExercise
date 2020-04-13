class Solution:
    def findUnsortedSubarray(self, nums: list) -> int:
        i = 1
        while i < len(nums) and nums[i] >= nums[i-1]:
            i += 1
        if i == len(nums):
            return 0
        j = len(nums) - 2
        while j >= 0 and nums[j] <= nums[j+1]:
            j -= 1
        max_value = max(nums[j], nums[i-1])
        min_value = min(nums[i], nums[j+1])
        for k in range(i+1, j):
            max_value = max(max_value, nums[k])
            min_value = min(min_value, nums[k])
        i -= 1
        while i >= 0 and nums[i] > min_value:
            i -= 1
        j += 1
        while j < len(nums) and nums[j] < max_value:
            j += 1
        return j - i - 1


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [2, 6, 4, 8, 10, 9, 15],
        [1, 2, 3],
        [3, 2, 1],
        [1, 2, 3, 4, 6, 5],
        [1, 3, 5, 4, 2]
    ]
    for nums in test_cases:
        print(solution.findUnsortedSubarray(nums))
