class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_one, num_touched = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num_one += 1
                    if i > 0 and grid[i-1][j] == 1:
                        num_touched += 1
                    if i < len(grid)-1 and grid[i+1][j] == 1:
                        num_touched += 1
                    if j > 0 and grid[i][j-1] == 1:
                        num_touched += 1
                        
                    if j < len(grid[0])-1 and grid[i][j+1] == 1:
                        num_touched += 1
             
        return 4*num_one - num_touched