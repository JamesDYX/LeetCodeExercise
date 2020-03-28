class Solution:
    def longestConsecutive(self, nums: list) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num-1 in nums:
                continue
            temp_length = 1
            temp_num = num + 1
            while temp_num in nums:
                temp_num += 1
                temp_length += 1
            longest = max(longest, temp_length)
        return longest


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [100, 4, 200, 1, 3, 2]
    ]
    for nums in test_cases:
        print(solution.longestConsecutive(nums))
