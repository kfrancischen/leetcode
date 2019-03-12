class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        def dfs(grid, i, j, visited):
            visited[i][j] = True
            if i < len(grid)-1 and visited[i+1][j] == False and grid[i+1][j] == '1':
                dfs(grid, i+1, j, visited)

            if i > 0 and visited[i-1][j] == False and grid[i-1][j] == '1':
                dfs(grid, i-1, j, visited)

            if j < len(grid[0]) - 1 and visited[i][j+1] == False and grid[i][j+1] == '1':
                dfs(grid, i, j+1, visited)

            if j > 0 and visited[i][j-1] == False and grid[i][j-1] == '1':
                dfs(grid, i, j-1, visited)

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and visited[i][j] == False:
                    result += 1
                    dfs(grid, i, j ,visited)

        return result