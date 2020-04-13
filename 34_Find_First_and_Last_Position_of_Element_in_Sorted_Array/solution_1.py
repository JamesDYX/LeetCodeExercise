class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        left, right = 0, len(nums) - 1
        left_possible_bound, right_possible_bound = None, right
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
                right_possible_bound = right
            else:
                right = mid - 1
                left_possible_bound = mid if left_possible_bound is None else left_possible_bound

        if left_possible_bound is None:
            return [-1, -1]
        while left_possible_bound <= right_possible_bound:
            mid = (left_possible_bound + right_possible_bound) // 2
            if nums[mid] <= target:
                left_possible_bound = mid + 1
            else:
                right_possible_bound = mid - 1
        return [left, right_possible_bound]


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([5,7,7,8,8,10], 8),
        ([5, 7, 7, 8, 8, 10], 6),
        ([5, 7, 7, 8, 8, 10], 5),
        ([5, 7, 7, 8, 8, 10], 4),
    ]

    for nums, target in test_cases:
        print(solution.searchRange(nums, target))
