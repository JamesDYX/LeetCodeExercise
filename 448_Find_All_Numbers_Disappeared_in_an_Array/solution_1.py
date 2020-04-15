class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        length = len(nums)
        nums = set(nums)
        res = []
        for i in range(1, length+1):
            if i not in nums:
                res.append(i)
        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [4, 3, 2, 7, 8, 2, 3, 1]
    ]
    for nums in test_cases:
        print(solution.findDisappearedNumbers(nums))
