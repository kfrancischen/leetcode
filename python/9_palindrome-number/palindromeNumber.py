class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return x >= 0 and x == int(''.join(list(str(x))[::-1]))
