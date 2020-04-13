class Solution:
    """
    fast & slow pointers
    """
    def findDuplicate(self, nums: list) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [1, 3, 4, 2, 2]
    ]
    for nums in test_cases:
        print(solution.findDuplicate(nums))
