from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sCounter = Counter(s)
        for string in t:
            if sCounter[string] == 0:
                return string
            else:
                sCounter[string] -= 1


mytest = Solution()
s = 'abcd'
t = 'abcde'
print mytest.findTheDifference(s,t)
