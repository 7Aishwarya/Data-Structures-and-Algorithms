class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min1 = sys.maxsize
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min1:
                min1 = prices[i]
            price = prices[i]
            if (price - min1) > max_profit:
                max_profit = price - min1
        return max_profit