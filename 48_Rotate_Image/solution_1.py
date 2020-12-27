class Solution:
    def rotate(self, matrix: list) -> None:
        for i in range(0, len(matrix) // 2):
            temp = matrix[i]
            matrix[i] = matrix[len(matrix) - 1 - i]
            matrix[len(matrix) - 1 - i] = temp

        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp


if __name__ == '__main__':
    solution = Solution()
    test_case = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    solution.rotate(test_case)
    print(test_case)
