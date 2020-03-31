class Solution(object):
    """
    a clever brute force
    O(n)
    """
    def maxChunksToSorted(self, arr):
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i: ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [4, 3, 2, 1, 0],
        [1, 0, 2, 3, 4],
        [0, 1, 2, 3, 4],
        [2, 1, 3, 0, 4],
        [1, 4, 0, 2, 3, 5],
        [0, 4, 7, 5, 3, 6, 9, 2, 1, 8]
    ]
    for arr in test_cases:
        print(solution.maxChunksToSorted(arr))
