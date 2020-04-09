class Solution:
    def summaryRanges(self, nums: list) -> list:
        length = len(nums)
        res = []
        i = 0
        while i < length:
            range = str(nums[i])
            i += 1
            if i < length and nums[i] - nums[i-1] == 1:
                range += '->'
                i += 1
                while i < length and nums[i] - nums[i-1] == 1:
                    i += 1
                range += str(nums[i-1])
            res.append(range)

        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [0, 1, 2, 4, 5, 7],
        [0, 2, 3, 4, 6, 8, 9],
        [1]
    ]
    for nums in test_cases:
        print(solution.summaryRanges(nums))
