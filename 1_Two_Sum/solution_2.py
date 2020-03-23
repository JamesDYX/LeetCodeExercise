class Solution:
    """
    Hash Table
    """
    def twoSum(self, nums, target):
        hash_table = {}
        for i, num in enumerate(nums):
            residual = target-num
            if residual in hash_table:
                return [hash_table[residual], i]
            else:
                hash_table[num] = i
