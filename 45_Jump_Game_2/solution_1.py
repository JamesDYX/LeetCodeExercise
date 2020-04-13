class Solution:
    """
    DP
    """
    def jump(self, nums: list) -> int:
        length = len(nums)
        if length < 2:
            return 0
        nums[-1] = 0
        for start_index in range(length-2, -1, -1):
            max_step = nums[start_index]
            if max_step == 0:
                nums[start_index] = length
            else:
                nums[start_index] = 1 + min(nums[start_index+1:
                                                 min(length, start_index+max_step+1)]
                                            )
        return nums[0]


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [2, 3, 1, 1, 4],
        [9, 2]
    ]
    for nums in test_cases:
        print(solution.jump(nums))
