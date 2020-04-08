class Solution:
    def maxProfit(self, prices: list) -> int:
        profit = 0
        last_price = prices[0]
        for price in prices[1:]:
            if price > last_price:
                profit += price - last_price
            last_price = price
        return profit


if __name__ == '__main__':
    solution = Solution()
    test_cases =[
        [7, 1, 5, 3, 6, 4],
        [1, 2, 3, 4, 5],
        [7, 6, 4, 3, 1]
    ]
    for prices in test_cases:
        print(solution.maxProfit(prices))
