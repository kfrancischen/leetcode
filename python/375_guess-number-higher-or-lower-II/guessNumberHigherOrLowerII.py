class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        money = [[0] * (n+1) for _ in range(0, n+1)]
        for i in range(n, 0, -1):
            for j in range(i + 1, n + 1):
                money[i][j] = min(x + max(money[i][x - 1], money[x + 1][j]) \
                    for x in range(i, j))
        return money[1][n]


mytest = Solution()
n = 6
print mytest.getMoneyAmount(n)
