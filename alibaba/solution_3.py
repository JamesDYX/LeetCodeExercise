import sys


class Solution:
    def solution(self, nums_A, nums_B):
        """
         Brute Force
         """
        length = len(nums_A)
        best_perform = 0
        for i in range(length-1):
            for j in range(i + 1, length):
                best_perform = max(best_perform, min(nums_A[i]+nums_A[j], nums_B[i] + nums_B[j]))
        return best_perform / 2

    def solution2(self, nums_A, nums_B):
        """
        greedy
        """
        first, second = 0, 1
        res = min(nums_A[first] + nums_A[second], nums_B[first] + nums_B[second])
        for i in range(2, len(nums_A)):
            i_first = min(nums_A[first] + nums_A[i], nums_B[first] + nums_B[i])
            i_second = min(nums_A[i] + nums_A[second], nums_B[i] + nums_B[second])
            if i_first >= i_second and i_first > res:
                res = i_first
                second = i
            elif i_second > i_first and i_second > res:
                res = i_second
                first = i
        return res / 2


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    nums_A = []
    nums_B = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        [a, b] = list(map(int, line.split()))
        nums_A.append(a)
        nums_B.append(b)
    solution = Solution()
    print("%.1f" % solution.solution2(nums_A, nums_B))