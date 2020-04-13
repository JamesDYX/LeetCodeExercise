class Solution:
    def exist(self, board: list, word: str) -> bool:
        M = len(board)
        N = len(board[0])
        length = len(word)

        def DFS(i, j, k):
            ch = board[i][j]
            if ch != word[k]:
                return False
            if k+1 == length:
                return True
            board[i][j] = ''
            if i+1 < M and board[i+1][j] != "" and DFS(i+1, j, k+1):
                return True
            if i-1 >= 0 and board[i-1][j] != "" and DFS(i-1, j, k+1):
                return True
            if j+1 < N and board[i][j+1] != "" and DFS(i, j+1, k+1):
                return True
            if j-1 >= 0 and board[i][j-1] != "" and DFS(i, j-1, k+1):
                return True
            board[i][j] = ch
            return False

        for i in range(M):
            for j in range(N):
                if DFS(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        (
            [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ],
            "ABCCED"
        ),
        (
            [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ],
            "SEE"
        ),
        (
            [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ],
            "ABCB"
        ),
        (
            [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ],
            "SABCESEECFDA"
        ),
    ]
    for board, word in test_cases:
        print(solution.exist(board, word))
