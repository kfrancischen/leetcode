class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0

        minValue = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < minValue:
                minValue = prices[i]
            else:
                profit = max(profit, prices[i] - minValue)
        return profit


mytest = Solution()
s = [3,2,3]
print mytest.maxProfit(s)
