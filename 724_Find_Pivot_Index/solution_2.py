class Solution:
    def pivotIndex(self, nums):
        sumL = 0
        sumR = sum(nums)
        for i in range(len(nums)):
            sumR -= nums[i]
            if sumL == sumR:
                return i
            sumL += nums[i]
        return -1


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [-1, -1, -1, -1, 1, 0]
    ]
    for nums in test_cases:
        print(solution.pivotIndex(nums))
