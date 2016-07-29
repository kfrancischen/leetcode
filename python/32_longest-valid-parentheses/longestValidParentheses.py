class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) < 2:
            return 0
        ans = 0
        n = len(s)
        dp = [0 for i in xrange(n + 1)]
        for i in xrange(2, n + 1):
            if s[i - 1] == '(':
                dp[i] = 0
            else:
                if s[i - 2] == '(':
                    dp[i] = dp[i - 2] + 2
                else:
                    left = i - 1 - dp[i - 1]
                    if left > 0 and s[left - 1] != s[i - 1]:
                        dp[i] = dp[i - 1] + 2 + dp[left - 1]
            ans = max(ans, dp[i])
        print dp
        return ans

mytest = Solution()
s = '()(())'
print mytest.longestValidParentheses(s)
