class Solution:
    def moveZeroes(self, nums: list) -> None:
        valid_idx = 0
        length = len(nums)
        while valid_idx < length and nums[valid_idx] != 0:
            valid_idx += 1
        for idx in range(valid_idx, length):
            if nums[idx] == 0:
                continue
            nums[valid_idx] = nums[idx]
            valid_idx += 1
        nums[valid_idx:] = [0] * (length - valid_idx)


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [0, 1, 0, 3, 12]
    ]
    for nums in test_cases:
        solution.moveZeroes(nums)
        print(nums)
