class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            result[i][0] = 1
        for i in range(n):
            result[0][i] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = result[i][j-1] + result[i-1][j]
                
                
        return result[-1][-1]