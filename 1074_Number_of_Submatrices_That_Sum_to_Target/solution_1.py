import numpy


class Solution:
    """
    Bruce Force
    O(N^4)
    """
    def numSubmatrixSumTarget(self, matrix: list, target: int) -> int:
        matrix = numpy.array(matrix)
        res = 0
        for i in range(len(matrix)):
            for i_ in range(i+1, len(matrix)+1):
                for j in range(len(matrix[0])):
                    for j_ in range(j+1, len(matrix[0])+1):
                        res += matrix[i:i_, j:j_].sum() == target
        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([[0,1,0],[1,1,1],[0,1,0]], 0),
        ([[1,-1],[-1,1]], 0)
    ]

    for mat, target in test_cases:
        print(solution.numSubmatrixSumTarget(mat, target))
