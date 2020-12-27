class Solution:
    def solve(self , n , a ):
        # write code here
        stack = []
        res = 0
        for index in range(n):
            while len(stack) > 0:
                if a[index] >= a[stack[-1]]:
                    stack.pop(-1)
                else:
                    break
            if len(stack) > 0:
                res += stack[-1]+1
            stack.append(index)
        return res


if __name__ == '__main__':
    test_cases = [
        (5,[5,4,3,2,1]),
        (5, [1, 2, 3, 4, 5])
    ]
    solution = Solution()
    for n, a in test_cases:
        print(solution.solve(n, a))
