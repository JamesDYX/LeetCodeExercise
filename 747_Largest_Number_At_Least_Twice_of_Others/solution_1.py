class Solution:
    def dominantIndex(self, nums: list) -> int:
        nums.append(0)
        first = second = -1
        for i in range(len(nums)-1):
            if nums[i] >= nums[first]:
                first, second = i, first
            elif nums[i] > nums[second]:
                second = i
        if nums[first] >= 2 * nums[second]:
            return first
        else:
            return -1


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [3, 6, 1, 0],
        [1, 2, 3, 4]
    ]
    for nums in test_cases:
        print(solution.dominantIndex(nums))
