class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return

        m = len(matrix)
        n = len(matrix[0])
        rowZero = [0 for i in range(0, m)]
        columnZero = [0 for i in range(0, n)]
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == 0:
                    rowZero[i] = 1
                    columnZero[j] = 1

        for i in range(0,m):
            for j in range(0,n):
                if rowZero[i] == 1 or columnZero[j] == 1:
                    matrix[i][j] = 0

test = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
test.setZeroes(matrix)
print matrix