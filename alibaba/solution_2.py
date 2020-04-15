import sys


class Solution:
    def solution(self, nums):
        nums.sort()
        res = 0
        solution = [0] * len(nums)
        i, j = 0, len(nums) - 1
        while i < j:
            solution[2 * i] = nums[i]
            solution[2 * i + 1] = nums[j]
            res += abs(nums[i] - solution[2 * i - 1])
            res += abs(nums[j] - nums[i])
            i += 1
            j -= 1
        if i == j:
            solution[2 * i] = nums[i]
            res += abs(nums[i] - solution[2 * i - 1])
        res += solution[-1] - 2 * nums[0]
        return solution, res


if __name__ == '__main__':
    solution = Solution()
    n = int(sys.stdin.readline().strip())
    nums = sys.stdin.readline().strip()
    nums = list(map(int, nums.split()))
    a, b = solution.solution(nums)
    a = list(map(str, a))
    print(b)
    res = ' '.join(a)
    print(res)
