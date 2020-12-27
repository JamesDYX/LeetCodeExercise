class Solution:
    def permute(self, nums: list, start_from=0) -> list:
        if start_from == len(nums):
            return [nums.copy()]
        res = []
        for i in range(start_from, len(nums)):
            nums[start_from], nums[i] = nums[i], nums[start_from]
            res += self.permute(nums, start_from+1)
            nums[start_from], nums[i] = nums[i], nums[start_from]
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
