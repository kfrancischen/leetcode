class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashTables = {}
        hashTablet = {}
        for i in range(0, len(s)):
            if s[i] not in hashTables:
                hashTables[s[i]] = t[i]
            if t[i] not in hashTablet:
                hashTablet[t[i]] = s[i]
            if hashTables[s[i]] != t[i] or hashTablet[t[i]] != s[i]:
                    return False
        return True

mytest = Solution()
s = "aa"
t = "ab"
print mytest.isIsomorphic(s, t)
