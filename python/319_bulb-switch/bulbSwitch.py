class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        while i ** 2 <= n:
            i += 1
        return i - 1


mytest = Solution()
n = 999999
print mytest.bulbSwitch(n)
