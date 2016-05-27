class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        sign = 1
        if n < 0:
            sign = 0
            n = -n
        result = self.calPower(x, n/2)
        if n % 2 == 1:
            result = result * result * x
        else:
            result = result * result
        if sign:
            return result
        else:
            return 1.0 / result

    def calPower(self, x, n):
        if n == 0:
            return 1
        result = self.calPower(x, n/2)
        if n % 2 == 1:
            return result * result * x
        else:
            return result * result

mytest = Solution()
x = -3
n = -3
print mytest.myPow(x,n)
