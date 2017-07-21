import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newString = "".join(re.findall("[a-zA-Z0-9]*", s)).lower()
        return newString == newString[::-1]


mytest = Solution()
s = "A man, a plan, a canal: Panama"
print mytest.isPalindrome(s)
