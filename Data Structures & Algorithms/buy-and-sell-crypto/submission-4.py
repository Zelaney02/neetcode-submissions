class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # method: two-pointer
        # # l and r are beside each other, r also acts as a sneakpeak to the next value
        # # ask is it profitable? -> l < r
        # # if not update l
        # # r should always update to keep it moving
        # # track the max profit, only update if find larger value
        # l, r = 0, 1 # left=buy, right=sell
        # maxP = 0

        # while r < len(prices): # only sweep the array once, r is our constant moving pointer "next value"
        #     # is this profitable?
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxP = max(maxP, profit)
        #     else:
        #         l = r # [2,8,1,10] -> l+1 old val of r, we know is > l, trying to find next min
        #     r += 1
        # return maxP

        # q: what's the min value - greedy method
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price) #compares curr price w/ next price
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit



