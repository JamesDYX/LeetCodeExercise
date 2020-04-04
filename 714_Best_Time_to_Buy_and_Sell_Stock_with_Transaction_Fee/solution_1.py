class Solution:
    def maxProfit(self, prices: list, fee: int) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        buy = sold = prices[0]
        for price in prices[1:]:
            # if current price is higher, then we will consider this new price as sold price
            if price >= sold:
                sold = price

            # if current price is lower, then we may think sold the stock at "sold price"
            else:
                gain = sold - buy - fee
                # we will perform a transmission only if
                # 1. we can earn money, and
                # 2. gain is large enough to pay “opportunity cost”, because
                #       if we perform transmission, the new buying price
                #       maybe higher than current one, eg.
                #       prices are [1, 5, 4, 10] with fee = 3,
                #       if we sold the stock at 5, then we cannot
                #       get a higher profit with "buy at 1 sold at 10"
                if gain > 0 and gain > price - buy:
                    profit += gain
                    buy = sold = price
                # if we cannot earn profit, then we should rethink changing the buying price
                elif price < buy:
                    buy = sold = price
        if sold - buy > fee:
            profit += sold - buy - fee
        return profit


if __name__ == '__main__' :
    solution = Solution()
    test_cases = [
        ([1, 3, 2, 8, 4, 9], 2),
        ([1,4,6,2,8,3,10,14], 3)
    ]
    for prices, fee in test_cases:
        print(solution.maxProfit(prices, fee))
