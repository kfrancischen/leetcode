class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        visited = [[0] * n for _ in range(m)]
        maxLen = 1
        for i in range(0, m):
            for j in range(0, n):
                curLen = self.dfs(matrix, i, j, m, n, visited)
                maxLen = max(maxLen, curLen)
        return maxLen


    def dfs(self, matrix, i, j, m, n, visited):
        if visited[i][j] != 0:
            return visited[i][j]
        maxLen = 1
        if i + 1 < m and matrix[i+1][j] > matrix[i][j]:
            maxLen = max(maxLen, 1 + self.dfs(matrix, i+1, j, m, n, visited))
        if i - 1 >=0 and matrix[i-1][j] > matrix[i][j]:
            maxLen = max(maxLen, 1 + self.dfs(matrix, i-1, j, m, n, visited))
        if j + 1 < n and matrix[i][j+1] > matrix[i][j]:
            maxLen = max(maxLen, 1 + self.dfs(matrix, i, j+1, m, n, visited))
        if j - 1 >=0 and matrix[i][j-1] > matrix[i][j]:
            maxLen = max(maxLen, 1 + self.dfs(matrix, i, j-1, m, n, visited))
        visited[i][j] = maxLen
        return maxLen

mytest = Solution()
matrix =  [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
print mytest.longestIncreasingPath(matrix)
