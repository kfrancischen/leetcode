class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        star = -1
        s_star = 0
        i = j = 0
        while i < len(s):
            if i < len(s) and j < len(p) and (p[j] == '?' or p[j] == s[i]):
                j += 1
                i += 1

            elif j < len(p) and p[j] == '*':
                star = j
                s_star = i
                j += 1

            elif star != -1:
                j = star + 1
                s_star += 1
                i = s_star
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)

mytest = Solution()
s = 'aab'
p = 'c*a*b'
print mytest.isMatch(s, p)
