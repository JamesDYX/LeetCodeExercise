class Solution:
    def isToeplitzMatrix(self, matrix: list) -> bool:
        if not matrix:
            return True
        last_row = matrix[0]
        for row in matrix[1:]:
            if last_row[:-1] == row[1:]:
                last_row = row
            else:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [
            [1, 2, 3, 4],
            [5, 1, 2, 3],
            [9, 5, 1, 2]
        ],
        [
            [1, 2, 3, 4],
            [5, 1, 2, 3],
            [9, 5, 1, 3]
        ],
        [

        ]
    ]
    for matrix in test_cases:
        print(solution.isToeplitzMatrix(matrix))
