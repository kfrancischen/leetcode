class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue = [(0, 0)]
        visited = set()
        while queue:
            val, dis = queue.pop(0)
            for i in xrange(1, n+1):
                j = val + i*i
                if j > n:
                    break
                if j == n:
                    return dis+1
                if j not in visited:
                    visited.add(j)
                    queue.append((j, dis+1))


test = Solution()
n = 12
print test.numSquares(n)
