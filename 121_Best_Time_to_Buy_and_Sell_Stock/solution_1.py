class Solution:
    def maxProfit(self, prices: list) -> int:
        if not prices:
            return 0
        buy = sold = prices[0]
        profit = 0
        for price in prices[1:]:
            if price > sold:
                sold = price
            elif price < buy:
                profit = max(profit, sold-buy)
                buy = sold = price
        profit = max(profit, sold - buy)
        return profit


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1]
    ]
    for prices in test_cases:
        print(solution.maxProfit(prices))
