import math


class Solution:
    """
    DP
    """
    def minPathSum(self, grid: list) -> int:
        M, N = len(grid), len(grid[0])
        for i in range(M + N - 2, 0, -1):
            row_id = i-1 if i <= M else M - 1
            col_id = 0 if i <= M else i - M
            while row_id >= 0 and col_id < N:
                right_step = grid[row_id][col_id+1] if col_id < N - 1 else math.inf
                down_step = grid[row_id+1][col_id] if row_id < M - 1 else math.inf
                grid[row_id][col_id] += min(right_step,  down_step)
                row_id -= 1
                col_id += 1
        return grid[0][0]


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ],

        [[1, 2], [1, 1]]
    ]
    for grid in test_cases:
        print(solution.minPathSum(grid))
