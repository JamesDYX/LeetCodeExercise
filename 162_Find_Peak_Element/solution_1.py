class Solution:
    """
    Binary Search
    """
    def findPeakElement(self, nums: list) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid+1
        return left


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
        [1, 2],
        [1],
        [2, 1]
    ]
    for nums in test_cases:
        print(solution.findPeakElement(nums))
