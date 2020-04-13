class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) in (0, 1):
            return
        i = len(nums)-2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        if i == -1:
            nums[:] = nums[::-1]
        else:
            j = len(nums) - 1
            while j > i:
                if nums[j] > nums[i]:
                    break
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1:] = nums[i + 1:][::-1]


if __name__ == '__main__':
    test_cases = [
        [1, 2, 3],
        [3, 2, 1],
        [1, 1, 5],
        [],
        [1]
    ]

    solution = Solution()
    for test_case in test_cases:
        solution.nextPermutation(test_case)
    print(test_cases)
