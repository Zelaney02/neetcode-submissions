class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # # left = buy
        # # right = sell
        # # want: sell > buy
        # buy = 0
        # sell = 1

        # while sell < len(prices):
        #     if prices[sell] < prices[buy]:
        #         buy = sell
        #     else:
        #         # sell > buy
        #         profit = prices[sell] - prices[buy]
        #         max_profit = max(profit, max_profit)
        #     sell += 1

        # return max_profit
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
        