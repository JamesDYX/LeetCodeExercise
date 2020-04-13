class Solution:
    def minDominoRotations(self, A: list, B: list) -> int:
        possible_sol = {A[0], B[0]}  # For a solution to exist all values should be either A[0] or B[0] after swapping
        l = len(A)
        for i in possible_sol:  # check both the cases
            Aswap = Bswap = 0  # set number of swaps for A and B to 0
            flag = 0
            for j in range(l):
                if A[j] == B[j] == i:  # if both are same no need to swap
                    pass
                elif A[j] == i:  # if only B[j] is different it can be swapped
                    Bswap += 1
                elif B[j] == i:  # if only A[j] is different it can be swapped
                    Aswap += 1
                else:  # if both are different, then solution does not exist for current value of i
                    flag = 1
                    break
            if flag == 0:
                return min(Aswap, Bswap)  # return the minimum number of swaps
        return -1  # return -1 if solution does not exist in both the cases
