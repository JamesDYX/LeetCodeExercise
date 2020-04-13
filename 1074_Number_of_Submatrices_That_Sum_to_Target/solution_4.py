class Solution:
    """
    https://www.acwing.com/solution/leetcode/content/2366/
    O(n^3)
    """
    def numSubmatrixSumTarget(self, matrix: list, target: int) -> int:
        res = 0
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            nums = [0] * n
            for j in range(i, m):
                for k in range(n):
                    nums[k] += matrix[j][k]
                res += self.num_for_one_row(nums, target)

        return res

    def num_for_one_row(self, nums, target):
        # O(n)
        prev = {0: 1}
        cur_sum = 0
        ans = 0
        for num in nums:
            cur_sum += num
            if cur_sum - target in prev:
                ans += prev[cur_sum - target]
            if cur_sum in prev:
                prev[cur_sum] += 1
            else:
                prev[cur_sum] = 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([[0,1,0],[1,1,1],[0,1,0]], 0),
        ([[1,-1],[-1,1]], 0)
    ]

    for mat, target in test_cases:
        print(solution.numSubmatrixSumTarget(mat, target))