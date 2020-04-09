import numpy as np


class Solution:
    def countServers(self, grid: list) -> int:
        grid = np.array(grid)
        res = 0
        for row in grid:
            server = row.sum()
            if server == 0:
                continue
            elif server == 1 and grid[:, row.argmax()].sum() == 1:
                continue
            res += server

        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [[1, 0], [0, 1]],
        [[1, 0], [1, 1]],
        [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    ]
    for grid in test_cases:
        print(solution.countServers(grid))
