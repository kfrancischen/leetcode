class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False;
        return (0 == ((n - 1) & n));

mytest = Solution()
n = 4
print mytest.isPowerOfTwo(n)
