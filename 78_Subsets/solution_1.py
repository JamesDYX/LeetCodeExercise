class Solution:
    def subsets(self, nums: list):
        res = []
        res.append([])
        for num in nums:
            res += [Set + [num] for Set in res]
        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [1, 2, 3],
        [1]
    ]
    for nums in test_cases:
        print(solution.subsets(nums))
