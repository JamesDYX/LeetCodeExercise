class Solution:
    def spiralOrder(self, matrix: list) -> list:
        res = []
        M = len(matrix)
        if M == 0:
            return res
        N = len(matrix[0])
        if N == 0:
            return res
        layer_num = min(M // 2, N // 2)
        for layer_counter in range(layer_num):
            start_row, start_col = layer_counter, layer_counter
            end_row, end_col = M - 1 - layer_counter, N - 1 - layer_counter
            res += matrix[start_row][start_col:end_col]
            res += [matrix[row_id][end_col] for row_id in range(start_row, end_row)]
            res += matrix[end_row][start_col + 1:end_col + 1][::-1]
            res += [matrix[row_id][start_col] for row_id in range(end_row, start_row, -1)]
        if M == N and M % 2 != 0:
            res.append(matrix[layer_num][layer_num])
        elif layer_num > M - 1 - layer_num or layer_num > N - 1 - layer_num:
            return res
        elif layer_num < N - 1 - layer_num:
            res += matrix[layer_num][layer_num:N - layer_num]
        else:
            res += [matrix[row_id][layer_num] for row_id in range(layer_num, M - layer_num)]
        return res


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [
            [2, 5],
            [8, 4],
            [0, -1],
        ],
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ],
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ],
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]
        ],
        [
            [1, 2, 3]
        ],
        [
            [1],
            [2],
            [3]
        ],
        [
            [1]
        ],
        []
    ]
    for matrix in test_cases:
        print(solution.spiralOrder(matrix))
