import math


class Solution:
    """
    Time complexity is O(n)
    Another solution is divide and conquer, time complexity in O(nlogn)
    """
    def minSubArrayLen(self, s: int, nums: list) -> int:
        left_index = right_index = 0
        current_sum = 0
        minimum_length = math.inf
        total_length = len(nums)

        while True:
            while current_sum < s and right_index < total_length:
                current_sum += nums[right_index]
                right_index += 1
            if current_sum < s:
                break
            while current_sum >= s and left_index < right_index:
                current_sum -= nums[left_index]
                left_index += 1
            minimum_length = min(minimum_length, right_index - left_index + 1)
        return minimum_length if minimum_length != math.inf else 0


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        (7, [2,3,1,2,4,3]),
        (3, [2, 3, 1, 2, 4, 3]),
        (1, []),
        (1000, [2,3,1,2,4,3]),
    ]

    for s, nums in test_cases:
        print(solution.minSubArrayLen(s, nums))
