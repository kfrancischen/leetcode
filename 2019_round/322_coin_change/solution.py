class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [amount+1]*(1+amount)

        dp[0] = 0
        for i in xrange(1,amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i],dp[i-coin]+1)

        return -1 if dp[-1] == amount+1 else dp[-1]
