import numpy


class Solution:
    # convolution layer, slide matrix
    def largestOverlap(self, A: list, B: list) -> int:
        size = len(A)
        B = numpy.array(B)
        A = numpy.array(A)
        A_ = numpy.zeros((3*size-2, 3*size-2))
        A_[size-1:2*size-1, size-1:2*size-1] = A
        result = 0
        max_result = int(min(A.sum(), B.sum()))
        for i in range(2*size-1):
            for j in range(2*size-1):
                temp_result = int((A_[i:i+size, j:j+size] * B).sum())
                result = max(result, temp_result)
                if result == max_result:
                    return result
        return result


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        (
            [[1, 1, 0],
             [0, 1, 0],
             [0, 1, 0]],
            [[0, 0, 0],
             [0, 1, 1],
             [0, 0, 1]]
        )
    ]

    for A, B in test_cases:
        print(solution.largestOverlap(A, B))
