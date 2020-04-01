class Solution:
    """
    Greedy
    O(n)
    """
    def canJump(self, nums: list) -> bool:
        farest_index = 0
        current_index = 0
        max_index = len(nums) - 1
        while current_index <= farest_index:
            if farest_index >= max_index:
                return True
            farest_index = max(farest_index, current_index+nums[current_index])
            current_index += 1
        return False


if __name__ == '__main__':
    solution = Solution()
    test_cases =[
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4],
        [],
        [7]
    ]
    for nums in test_cases:
        print(solution.canJump(nums))
