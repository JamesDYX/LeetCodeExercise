import numpy as np

class Solution:
    def numMagicSquaresInside(self, grid: list) -> int:
        possible_magic_square = np.array([
            [8, 1, 6, 3, 5, 7, 4, 9, 2],
            [6, 7, 2, 1, 5, 9, 8, 3, 4],
            [2, 9, 4, 7, 5, 3, 6, 1, 8],
            [4, 3, 8, 9, 5, 1, 2, 7, 6],
            [8, 3, 4, 1, 5, 9, 6, 7, 2],
            [4, 9, 2, 3, 5, 7, 8, 1, 6],
            [2, 7, 6, 9, 5, 1, 4, 3, 8],
            [6, 1, 8, 7, 5, 3, 2, 9, 4],
        ])
        grid = np.array(grid)

        res = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                a = grid[i:i+3, j:j+3].reshape(9)
                for row in possible_magic_square:
                    if (a == row).all():
                        res += 1
                        break
        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [[4, 3, 8, 4],
         [9, 5, 1, 9],
         [2, 7, 6, 2]]
    ]

    for grid in test_cases:
        print(solution.numMagicSquaresInside(grid))
