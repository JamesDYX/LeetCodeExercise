import math


class Solution:
    def numSquares(self, n: int) -> int:
        res = [0]
        square_nums = [i**2 for i in range(1, 1+int(math.sqrt(n)))]
        for i in range(1, n+1):
            temp_res = i
            for square_num in square_nums:
                if square_num > i:
                    break
                temp_res = min(temp_res, res[i - square_num] + 1)
            res.append(temp_res)
        return res[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSquares(13))
