import numpy as np


class Solution:
    def productExceptSelf(self, nums: list) -> list:
        product = 1
        res = np.array([], dtype=int)
        for num in nums:
            res *= num
            res = np.append(res, product)
            product *= num
        return list(res)


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [1, 2, 3, 4]
    ]
    for nums in test_cases:
        print(solution.productExceptSelf(nums))
