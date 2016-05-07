import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        firstBuy = -sys.maxint
        firstSell = 0
        secondBuy = -sys.maxint
        secondSell = 0
        for i in range(0, len(prices)):
            curPrice = prices[i]
            if firstBuy < -curPrice:
                firstBuy = -curPrice
            if firstSell < firstBuy + curPrice:
                firstSell = firstBuy + curPrice
            if secondBuy < firstSell - curPrice:
                secondBuy = firstSell - curPrice
            if secondSell < secondBuy + curPrice:
                secondSell = secondBuy + curPrice

        return secondSell

mytest = Solution()
s = [1,2,3,3,4,5,6]
print mytest.maxProfit(s)
