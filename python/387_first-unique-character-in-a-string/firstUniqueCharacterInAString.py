from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        sCounter = Counter(s)
        for i in range(0, len(s)):
            if sCounter[s[i]] == 1:
                return i
        return -1


mytest = Solution()
s = 'loveleetcode'
print mytest.firstUniqChar(s)
