class Solution:
    def subarraySum(self, nums: list, k: int) -> int:
        counter = {0: 1}
        res = 0
        sum = 0
        for num in nums:
            sum += num
            if sum - k in counter:
                res += counter[sum - k]
            if sum in counter:
                counter[sum] += 1
            else:
                counter[sum] = 1
        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([1, 1, 1, -1], 0)
    ]
    for nums, k in test_cases:
        print(solution.subarraySum(nums, k))
