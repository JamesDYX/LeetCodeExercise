class Solution:
    """
    find solution in here
    https://leetcode.com/problems/maximum-product-subarray/discuss/490459/Unofficial-solution-intuitive-explanations-O(n)-two-different-approaches
    """
    def maxProduct(self, nums: list) -> int:
        max_length = len(nums)
        start_index = 0
        while start_index < max_length and nums[start_index] == 0:
            start_index += 1
        if start_index == max_length:
            return 0
        end_index = max_length - 1
        while end_index >= start_index and nums[end_index] == 0:
            end_index -= 1

        max_res = nums[0]
        current_res = 1
        for i in range(start_index, end_index+1):
            current_res *= nums[i]
            max_res = max(max_res, current_res)
            if nums[i] == 0:
                current_res = 1
                continue

        current_res = 1
        for i in range(end_index, start_index-1, -1):
            current_res *= nums[i]
            max_res = max(max_res, current_res)
            if nums[i] == 0:
                current_res = 1
                continue
        return max_res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [2, 3, -2, 4],
        [-2, 0, -1],
    ]
    for nums in test_cases:
        print(solution.maxProduct(nums))
