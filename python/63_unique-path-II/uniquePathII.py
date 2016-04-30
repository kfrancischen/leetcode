class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        path = [[0 for i in range(0,n)] for j in range(0,m)]

        for i in range(0,m):
            if obstacleGrid[i][0] == 1:
                break
            path[i][0] = 1

        for i in range(0, n):
            if obstacleGrid[0][i] == 1:
                break
            path[0][i] = 1

        for i in range(1,m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    path[i][j] == 0
                    continue
                path[i][j] = path[i-1][j] + path[i][j-1]

        return path[m-1][n-1]

mytest = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0],[0,0,0]]
print mytest.uniquePathsWithObstacles(obstacleGrid)
