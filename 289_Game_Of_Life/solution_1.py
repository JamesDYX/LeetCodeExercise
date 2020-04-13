class Solution:
    def gameOfLife(self, board: list) -> None:
        M = len(board)
        N = len(board[0])

        for i in range(M):
            for j in range(N):
                start_row, end_row = max(0, i-1), min(M, i+2)
                start_col, end_col = max(0, j-1), min(N, j+2)
                live_num = 0
                for rowid in range(start_row, end_row):
                    for colid in range(start_col, end_col):
                        if rowid == i and colid == j:
                            continue
                        live_num += 1 if board[rowid][colid] in (1, -1) else 0
                if board[i][j] == 0 and live_num == 3:
                    board[i][j] = 2
                elif board[i][j] == 1 and (live_num < 2 or live_num > 3):
                    board[i][j] = -1

                # the top left item is the last time be processed
                if i - 1 >= 0 and j - 1 >= 0:
                    if board[i-1][j-1] == 2:
                        board[i - 1][j - 1] = 1
                    elif board[i-1][j-1] == -1:
                        board[i - 1][j - 1] = 0

            # the top item is the last time be processed
            if i - 1 >= 0:
                if board[i-1][-1] == 2:
                    board[i - 1][-1] = 1
                elif board[i-1][-1] == -1:
                    board[i - 1][-1] = 0

        # the bottom line is the last time be processed
        for j in range(N):
            if board[-1][j] == 2:
                board[-1][j] = 1
            elif board[-1][j] == -1:
                board[-1][j] = 0


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ],
        [
            [0]
        ]
    ]
    for board in test_cases:
        solution.gameOfLife(board)
        print(board)
