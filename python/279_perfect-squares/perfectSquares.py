import collections
class Solution(object):
    def numSquares(self, n):
        queue = collections.deque([(0, 0)])
        visited = set()
        while queue:
            val, dis = queue.popleft()
            # if val == n:
            #     return dis
            for i in xrange(1, n+1):
                j = val + i*i
                if j > n:
                    break
                if j == n:
                    return dis+1
                if j not in visited:
                    visited.add(j)
                    queue.append((j, dis+1))


mytest = Solution()
n = 13
print mytest.numSquares(n)
