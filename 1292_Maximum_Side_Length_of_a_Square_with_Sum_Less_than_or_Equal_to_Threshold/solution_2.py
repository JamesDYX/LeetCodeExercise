import numpy


class Solution:
    """
    Smarter Bruce Force
    820 ms beat 90% in runtime
    """
    def maxSideLength(self, mat: list, threshold: int) -> int:
        out = 0
        m = len(mat)
        n = len(mat[0])
        mat = numpy.array(mat)

        for i in range(min(m, n)):
            for y in range(m - i):
                s = mat[y:y + i + 1].sum(0)
                mat_sum = sum(s[0:i+1])
                if mat_sum <= threshold:
                    out = i + 1
                    break
                for x in range(1, n-i):
                    mat_sum = mat_sum - s[x-1] + s[x+i]
                    if mat_sum <= threshold:
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
