class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        dp = [[True] + [False] * m]
        for i in xrange(n):
            dp.append([False]*(m+1))

        for i in xrange(1, n + 1):
            x = p[i-1]
            if x == '*' and i > 1:
                dp[i][0] = dp[i-2][0]
            for j in xrange(1, m+1):
                if x == '*':
                    dp[i][j] = dp[i-2][j] or dp[i-1][j] or \
                        (dp[i-1][j-1] and p[i-2] == s[j-1]) or \
                        (dp[i][j-1] and p[i-2]=='.')
                elif x == '.' or x == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
        print dp
        return dp[n][m]

mytest = Solution()
s = 'aab'
p = 'c*a*b'
print mytest.isMatch(s, p)
