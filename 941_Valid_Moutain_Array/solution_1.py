class Solution:
    def validMountainArray(self, A: list) -> bool:
        length = len(A)
        if length < 3:
            return False
        peek = 1
        while peek < length:
            if A[peek] == A[peek-1]:
                return False
            elif A[peek] > A[peek-1]:
                peek += 1
            else:
                break
        if peek == 1 or peek == length:
            return False
        while peek < length:
            if A[peek] >= A[peek-1]:
                return False
            else:
                peek += 1
        return True


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [2, 1],
        [3, 5, 5],
        [0, 3, 2, 1],
        [1, 2, 3, 4],
        [4, 3, 2, 1]
    ]
    for A in test_cases:
        print(solution.validMountainArray(A))
