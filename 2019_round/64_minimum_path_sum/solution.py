class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        paths = [[0] * n for _ in range(m)]
        paths[0][0] = grid[0][0]
        for i in range(1, m):
            paths[i][0] = grid[i][0] + paths[i-1][0]
            
        for i in range(1, n):
            paths[0][i] = grid[0][i] + paths[0][i-1]
            
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = min(paths[i][j-1], paths[i-1][j]) + grid[i][j]
                
                
        return paths[-1][-1]
        