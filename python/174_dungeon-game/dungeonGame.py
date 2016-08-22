class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for i in range(0, m)]
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])

        for i in range(m-1, -1 , -1):
            for j in range(n-1, -1 ,-1):
                if not (i == m - 1 and j == n - 1):
                    downWard = dp[i+1][j] if i < m - 1 else float('inf')
                    rightWard = dp[i][j+1] if j < n - 1 else float('inf')
                    dp[i][j] = max(1, min(downWard, rightWard) - dungeon[i][j])
                    
        return dp[0][0]

mytest = Solution()
dungeon = [[-2, -3, 3], [-5, -10, 1], [10,30,-5]]
print mytest.calculateMinimumHP(dungeon)
