import numpy as np


class Solution:
    def sortedSquares(self, A: list) -> list:
        i = 0
        while i < len(A) and A[i] < 0:
            i += 1
        left = A[:i][::-1]
        right = A[i:]
        index_left = index_right = 0
        res = []
        while index_left < len(left) and index_right < len(right):
            if -left[index_left] <= right[index_right]:
                res.append(left[index_left])
                index_left += 1
            else:
                res.append(right[index_right])
                index_right += 1
        res += left[index_left:] + right[index_right:]
        return list(np.array(res) ** 2)


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [-4, -1, 0, 3, 10],
        [-7, -3, 2, 3, 11],
        [1],
        [-1]
    ]
    for A in test_cases:
        print(solution.sortedSquares(A))
