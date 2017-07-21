class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            self.matrix = []
            return
        m, n = len(matrix), len(matrix[0])
        self.matrix = [[0 for i in range(0, n)] for j in range(0, m)]
        for i in range(0, m):
            for j in range(0, n):
                self.matrix[i][j] = matrix[i][j]
                if i > 0:
                    self.matrix[i][j] += self.matrix[i - 1][j]
                if j > 0:
                    self.matrix[i][j] += self.matrix[i][j - 1]
                if i > 0 and j > 0:
                    self.matrix[i][j] -= self.matrix[i - 1][j - 1]



    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.matrix or not self.matrix[0]:
            return 0
        result = self.matrix[row2][col2]
        if row1 > 0:
            result -= self.matrix[row1 -1][col2]
        if col1 > 0:
            result -= self.matrix[row2][col1 - 1]
        if col1 > 0 and row1 > 0:
            result += self.matrix[row1 - 1][col1 - 1]
        return result

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
mytest = NumMatrix(matrix)
print mytest.sumRegion(1,2,2,4)

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
