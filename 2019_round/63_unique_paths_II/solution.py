class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        paths = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                paths[i][0] = 1
                
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            else:
                paths[0][i] = 1
        
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
        
        return paths[-1][-1]