class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lps = self.LPS(s + '$' + s[::-1])
        return s[lps[-1]:len(s)][::-1] + s

    def LPS(self, p):
        lps = [0] * len(p)
        l = 0
        for i in range(1, len(p)):
            while l > 0 and p[i] != p[l]:
                l = lps[l-1]
            if p[i] == p[l]:
                l += 1
                lps[i] += l
        return lps


mytest = Solution()
s = "aabc"
print mytest.shortestPalindrome(s)
