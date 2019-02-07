class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        element_list = []
        while x:
            val = x % 10
            x = x / 10
            element_list.append(val)

        return element_list == element_list[::-1]