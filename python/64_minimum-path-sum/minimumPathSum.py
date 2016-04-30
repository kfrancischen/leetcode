class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        sum = [[0 for i in range(0,n)] for j in range(0,m)]
        sum[0][0] = grid[0][0]
        for i in range(1, m):
            sum[i][0] = sum[i-1][0] + grid[i][0]

        for j in range(1,n):
            sum[0][j] = sum[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                sum[i][j] = min(sum[i-1][j], sum[i][j-1]) + grid[i][j]

        return sum[m-1][n-1]

mytest = Solution()
grid = [[1,2,3],[1,1,1]]
print mytest.minPathSum(grid)
