class Solution:
    """
    Also DP
    """
    def minPathSum(self, grid: list) -> int:
        M, N = len(grid), len(grid[0])
        for i in range(M-2, -1, -1):
            grid[i][N-1] += grid[i+1][N-1]
        for j in range(N-2, -1, -1):
            grid[M-1][j] += grid[M-1][j+1]

        for i in range(M - 2, -1, -1):
            for j in range(N - 2, -1, -1):
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
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
