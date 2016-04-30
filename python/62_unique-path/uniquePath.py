class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path = [[0 for i in range(0,n)] for y in range(0,m)]

        for i in range(0, m):
            path[i][0] = 1
        for i in range(0, n):
            path[0][i] = 1

        for i in range(1, m):
            for j in range(1,n):
                path[i][j] = path[i-1][j] + path[i][j-1]

        return path[m-1][n-1]

mytest = Solution()
m = 4
n = 3
print mytest.uniquePaths(m,n)
