class Solution:
    """
    There are three solutions
    1. Kadane Algo
    2. DP
    3. divide and conquer
    """
    def maxSubArray(self, nums: list) -> int:
        if not nums:
            return 0
        # 1. find the first positive number
        left = 0
        max_sum = nums[0]
        while left < len(nums):
            if nums[left] > 0:
                break
            max_sum = max(max_sum, nums[left])
            left += 1
        if left == len(nums):
            return max_sum
        # 2. find the last positive number
        right = len(nums) - 1
        while right > left:
            if nums[right] > 0:
                break
            right -= 1

        max_sum = 0
        current_sum = 0

        i = left
        while i <= right:
            current_sum += nums[i]
            if current_sum < 0:
                # find the fist positive
                while i <= right:
                    if nums[i] > 0:
                        current_sum = nums[i]
                        break
                    i += 1
            max_sum = max(max_sum, current_sum)
            i += 1
        return max_sum


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [-1]
    ]
    for test_case in test_cases:
        print(solution.maxSubArray(test_case))
