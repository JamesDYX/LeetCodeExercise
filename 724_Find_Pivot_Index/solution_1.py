class Solution:
    """
    Initially I thought the double pointer would work,
    but I was wrong
    Wrong Answer

    If all the numbers is non-negative, then two pointers would work
    """
    def pivotIndex(self, nums: list) -> int:
        left, right = 0, len(nums) - 1
        diff_left_minus_right = 0
        while left < right:
            if diff_left_minus_right < 0:
                diff_left_minus_right += nums[left]
                left += 1
            else:
                diff_left_minus_right -= nums[right]
                right -= 1
        if diff_left_minus_right == 0 and left == right:
            return left
        return -1


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [-1, -1, -1, -1, 1, 0],
    ]
    for nums in test_cases:
        print(solution.pivotIndex(nums))
