class Solution:
    def solution(self, N: int, L: int):
        max_l = int((2*N)**0.5)
        max_l = min(max_l, 100)
        l = L
        if l * (l-1) == 2 * N:
            return 0, l
        while l <= max_l:
            if 2 * N % l != 0:
                l += 1
                continue
            a2 = 2 * N // l + 1 - l
            if a2 % 2 == 0:
                return a2 // 2, l
            else:
                l += 1
        return 0, 0


if __name__ == '__main__':
    solution = Solution()
    [N, L] = list(map(int, input().split(' ')))
    start, length = solution.solution(N, L)
    if length == 0:
        print('No')
    else:
        res = ''
        for i in range(length-1):
            res += '%d ' % (start + i)
        res += str(start + length - 1)
        print(res)
