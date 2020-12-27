class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        coins.sort()
        res = [0]
        for i in range(1, amount + 1):
            min_res = i + 1
            for coin in coins:
                if i - coin < 0:
                    break
                if res[i - coin] == -1:
                    continue
                min_res = min(min_res, res[i - coin] + 1)
            if min_res == i + 1:
                res.append(-1)
            else:
                res.append(min_res)
        return res[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange([2], 3))
