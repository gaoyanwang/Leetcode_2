class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) < 2:
            return 0
        minP = prices[0]
        profit = 0
        for e in prices:
            profit = max(profit, e - minP)
            minP = min(minP, e)
        return profit
# Space: O(1)
# Time: O(n)
