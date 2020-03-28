class Solution:
    """kadane would be proud..."""
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums: return -2147483648
        record = _max = -float('inf')
        for e in nums:
            # max between we add it, or we start another chain
            _max = max(_max + e, e)
            # keep in memory the global maximum
            record = max(record, _max)
        return record