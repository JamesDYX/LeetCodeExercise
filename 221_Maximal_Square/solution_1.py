class Solution:
    def maximalSquare(self, matrix: list) -> int:
        length = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
                    continue
                upper = 0
                left = 0
                left_upper = 0
                if i > 0:
                    upper = matrix[i-1][j]
                if j > 0:
                    left = matrix[i][j-1]
                if i > 0 and j > 0:
                    left_upper = matrix[i-1][j-1]
                matrix[i][j] = min(upper, left_upper, left) + 1
                length = max(length, matrix[i][j])
        return length ** 2


if __name__ == '__main__':
    test = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]]
    solution = Solution()
    print(solution.maximalSquare(test))
