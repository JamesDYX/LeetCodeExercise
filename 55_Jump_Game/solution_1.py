class Solution:
    """
    DP
    O(n^2) TLE
    """
    def canJump(self, nums: list) -> bool:
        if not nums:
            return True
        nums[-1] = True
        for index in range(len(nums)-2, -1, -1):
            could_reach = False
            for step in range(nums[index]):
                if nums[index+1+step]:
                    could_reach = True
                    break
            nums[index] = could_reach
        return nums[0]


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
