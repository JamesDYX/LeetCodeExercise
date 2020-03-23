class Solution:
    def minDominoRotations(self, A: list, B: list) -> int:
        same_in_A = A[0]
        same_in_B = B[0]
        ro_num = 0
        same = 1 if same_in_A == same_in_B else 0

        for i in range(1, len(A)):
            if A[i] == same_in_A or B[i] == same_in_B:
                # don't need to flip
                if A[i] != same_in_A:
                    same_in_A = -1
                if B[i] != same_in_B:
                    same_in_B = -1
                if A[i] == B[i]:
                    same += 1
                continue
            elif A[i] == same_in_B or B[i] == same_in_A:
                # need to flip
                if ro_num == i - same - ro_num:
                    # flip the passed dominos
                    same_in_A, same_in_B = same_in_B, same_in_A
                    if A[i] != same_in_A:
                        same_in_A = -1
                    if B[i] != same_in_B:
                        same_in_B = -1
                else:
                    # flip current
                    ro_num += 1
                    if A[i] != same_in_B:
                        same_in_B = -1
                    if B[i] != same_in_A:
                        same_in_A = -1
            else:
                return -1
        return ro_num


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([2,1,2,4,2,2], [5,2,6,2,3,2]),
        ([3,5,1,2,3], [3,6,3,3,4]),
        ([2, 1, 1, 3, 2, 1, 2, 2, 1], [3, 2, 3, 1, 3, 2, 3, 3, 2]),
        ([2,1,1,1,2,2,2,1,1,2], [1,1,2,1,1,1,1,2,1,1])
    ]

    for A, B in test_cases:
        print(solution.minDominoRotations(A, B))
