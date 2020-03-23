import numpy as np


class Solution:
    """
    Double Pointer
    """
    def twoSum(self, nums: list, target: int) -> list:
        if len(nums) < 2:
            return [0, 0]

        nums_indices = np.argsort(nums)
        indices = [0, len(nums)-1]  # left index and right index

        move_index = 1  # 1 means right index, 0 means left index
        move_direction = -1

        while True:
            if nums[nums_indices[indices[0]]] + nums[nums_indices[indices[1]]] == target:
                return [nums_indices[indices[0]], nums_indices[indices[1]]]
            if move_direction == -1:
                # is greater than target
                if nums[nums_indices[indices[0]]] + nums[nums_indices[indices[1]]] > target \
                        and indices[move_index] + move_direction != indices[1-move_index]\
                        and indices[move_index] != 0:
                    # keep moving leftward
                    indices[move_index] += move_direction
                elif nums[nums_indices[indices[0]]] + nums[nums_indices[indices[1]]] < target:
                    # violation
                    move_index = 1 - move_index
                    move_direction = 1
                else:
                    # beyond the bound
                    move_index = 1 - move_index
            else:
                # is smaller than target
                if nums[nums_indices[indices[0]]] + nums[nums_indices[indices[1]]] < target \
                        and indices[move_index] + move_direction != indices[1-move_index]\
                        and indices[move_index] != len(nums) - 1:
                    # keep moving rightward
                    indices[move_index] += move_direction
                elif nums[nums_indices[indices[0]]] + nums[nums_indices[indices[1]]] > target:
                    # violation
                    move_index = 1 - move_index
                    move_direction = -1
                else:
                    # beyond the bound
                    move_index = 1 - move_index


if __name__ == '__main__':
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([2, 7, 11, 15], 18),
        ([2, 7, 11, 15], 26),
        ([2, 3, 11, 15], 14),
        ([3, 2, 15, 11], 14),
    ]
    solution = Solution()
    for nums, target in test_cases:
        indices = solution.twoSum(nums, target)
        print(indices)
