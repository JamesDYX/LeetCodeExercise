class Solution(object):
    """
    DP
    cash means the maximum profit we could have if we did not have a share of stock
    hold mean the maximum profit we could have if we had a share of stock
    """
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            """
            In case of holding two share of stock,
            we should first consider sell it and then whether to buy.
            It's safe because selling and buying on the same day can't 
            be better than just continuing to hold the stock.
            """
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
