class Solution:
    def productExceptSelf(self, nums: list) -> list:
        left = 1
        right = 1
        length = len(nums)
        res = [1 for i in range(length)]
        for i in range(length):
            res[i] *= left
            res[length-1-i] *= right
            left *= nums[i]
            right *= nums[length-1-i]
        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [1, 2, 3, 4]
    ]
    for nums in test_cases:
        print(solution.productExceptSelf(nums))
