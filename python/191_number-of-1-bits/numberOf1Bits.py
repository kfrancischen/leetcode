class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = "{0:b}".format(n)
        return sum(map(int, list(bits)))



mytest = Solution()
n = 11
print mytest.hammingWeight(n)
