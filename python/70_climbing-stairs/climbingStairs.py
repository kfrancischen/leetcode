class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n == 2:
            return n
        ways = [0] * n
        ways[0] = 1
        ways[1] = 2
        for i in range(2, n):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n-1]

mytest = Solution()
n = 5
print mytest.climbStairs(n)
