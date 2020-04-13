class Solution:
    def numSubarrayProductLessThanK(self, nums: list, k: int) -> int:
        start = -1
        to = 0
        product = 1
        res = 0
        while to < len(nums):
            if nums[to] >= k:
                start = to
                to += 1
                continue
            product *= nums[to]
            while product >= k and start < to:
                start += 1
                product /= nums[start]
            res += to - start
            to += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([10, 5, 2, 6], 100)
    ]
    for nums, k in test_cases:
        print(solution.numSubarrayProductLessThanK(nums, k))
