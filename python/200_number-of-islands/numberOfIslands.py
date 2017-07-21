class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        result = 0
        visited = [[0 for i in range(0, len(grid[0]))] for j in range(0, len(grid))]
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    self.dfs(visited, grid, i, j)
                    result += 1
        return result


    def dfs(self, visited, grid, i, j):
        if grid[i][j] == '0' or visited[i][j] == 1:
            return
        num = 0
        visited[i][j] = 1
        if i + 1 <= len(grid) - 1:
            self.dfs(visited, grid, i + 1, j)
        if i - 1 >= 0:
            self.dfs(visited, grid, i - 1, j)
        if j + 1 <= len(grid[0]) - 1:
            self.dfs(visited, grid, i, j + 1)
        if j - 1 >= 0:
            self.dfs(visited, grid, i, j - 1)
        return

mytest = Solution()
grid = ["11000","11000","00100","00011"]
print mytest.numIslands(grid)
