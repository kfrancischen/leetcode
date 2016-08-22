'''
dp[i, j] = max(dp[i, j-1], prices[j] - prices[jj] + dp[i-1, jj]) { jj in range of [0, j-1] }
           = max(dp[i, j-1], prices[j] + max(dp[i-1, jj] - prices[jj]))
'''

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 0:
            return 0
        if k >= n/2:
            maxPro = 0
            for i in range(1, n):
                if prices[i] - prices[i-1] > 0:
                    maxPro += prices[i] - prices[i-1]
            return maxPro

        dp = [[0] * n for i in range(0, k + 2)]
        for i in range(1, k + 1):
            localMax = dp[i-1][0] - prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + localMax)
                localMax = max(localMax, dp[i-1][j] - prices[j])
        print dp
        return dp[k][n-1]

mytest = Solution()
s = [1,2,3,4,5,6,7]
k = 2
print mytest.maxProfit(k, s)
