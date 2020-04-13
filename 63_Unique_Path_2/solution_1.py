class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        obstacleGrid[0][0] = -1
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        for row_index in range(M):
            for col_index in range(N):
                if obstacleGrid[row_index][col_index] == 1:
                    continue
                obstacleGrid[row_index][col_index] += obstacleGrid[row_index-1][col_index] if \
                    row_index > 0 and obstacleGrid[row_index-1][col_index] != 1 else 0
                obstacleGrid[row_index][col_index] += obstacleGrid[row_index][col_index-1] if \
                    col_index > 0 and obstacleGrid[row_index][col_index-1] != 1else 0
        return -obstacleGrid[M-1][N-1]


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    ]
    for grid in test_cases:
        print(solution.uniquePathsWithObstacles(grid))
