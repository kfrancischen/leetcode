class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        checkedAtlantic = [[False] * n for _ in range(m)]
        checkedPacific = [[False] * n for _ in range(m)]
        result = []
        for i in range(m):
            self.DFS(matrix, checkedPacific, i, 0, m, n)
            self.DFS(matrix, checkedAtlantic, i, n-1, m, n)

        for i in range(n):
            self.DFS(matrix, checkedPacific, 0, i, m, n)
            self.DFS(matrix, checkedAtlantic, m-1, i, m, n)

        for i in range(m):
            for j in range(n):
                if checkedPacific[i][j] and checkedAtlantic[i][j]:
                    result.append([i, j])
        return result


    def DFS(self, matrix, visited, i, j, m, n):
        if visited[i][j]:
            return
        visited[i][j] = True
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        for dx, dy in direction:
            x, y = i + dx, j + dy
            if x < 0 or x > m-1 or y < 0 or y > n - 1 or matrix[x][y] < matrix[i][j]:
                continue
            self.DFS(matrix, visited, x, y, m, n)

mytest = Solution()
matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print mytest.pacificAtlantic(matrix)
