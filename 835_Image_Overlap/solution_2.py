import numpy


class Solution:
    # convolution layer, slide index
    def largestOverlap(self, A: list, B: list) -> int:
        size = len(A)
        A = numpy.array(A)
        B = numpy.array(B)
        result = 0
        max_result = int(min(A.sum(), B.sum()))

        for i in range(-size+1, size):
            start_A_r, end_A_r = max(0, i), min(size, i + size)
            start_B_r, end_B_r = size-end_A_r, size-start_A_r
            for j in range(-size+1, size):
                start_A_c, end_A_c = max(0, j), min(size, j+size)
                start_B_c, end_B_c = size-end_A_c, size-start_A_c
                temp_result = int(
                    (A[start_A_r:end_A_r, start_A_c:end_A_c] *
                     B[start_B_r:end_B_r, start_B_c:end_B_c]
                     ).sum()
                )
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
