import math
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return 1 if n >= 1 else 0
        h = int(pow(10, int(math.log10(n))))
        return (h if n/h >= 2 else n-h+1) + n/h * self.countDigitOne(h-1) + self.countDigitOne(n%h)


mytest = Solution()
n = 100
print mytest.countDigitOne(n)
