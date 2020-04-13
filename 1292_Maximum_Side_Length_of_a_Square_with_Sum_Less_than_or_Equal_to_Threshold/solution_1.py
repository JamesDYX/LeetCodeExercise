import numpy as np


class Solution:
    """
    Bruce Force
    1600ms only beat 40% in runtime
    """
    def maxSideLength(self, mat: list, threshold: int) -> int:
        out = 0
        m = len(mat)
        n = len(mat[0])
        mat = np.array(mat)

        for i in range(min(m, n)):
            for y in range(m - i):
                for x in range(n - i):
                    new_mat = mat[y:y + i + 1, x:x + i + 1]
                    s = new_mat.sum()
                    if s <= threshold:
                        out = i + 1
                        break
                if out == i + 1:
                    break
            if out != i + 1:
                break
        return out


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        (
            [[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], 4
        ),
        (
            [[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]], 1
        ),
        (
            [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], 6
        )
    ]
    for mat, thresh in test_cases:
        print(solution.maxSideLength(mat, thresh))
