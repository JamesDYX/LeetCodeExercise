class Solution:
    """
    solution[i][j] means the number of matrix ended (right-bottom) at [i, j]
    DP Algorithm
    """
    def countSquares(self, matrix) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]:
                    matrix[i][j] = 1 + min(matrix[i-1][j],
                                           matrix[i][j-1],
                                           matrix[i-1][j-1])
        return sum([sum(row) for row in matrix])


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 1, 1, 1]
        ],
        [
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 0]
        ],
    ]

    for matrix in test_cases:
        print(solution.countSquares(matrix))

