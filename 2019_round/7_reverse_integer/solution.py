class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = -x
            
        result = 0
        while x:
            residue = x % 10
            x = x / 10
            result = result * 10 + residue
            
        if result >= 2 ** 31 - 1:
            return 0
        
        return sign * result