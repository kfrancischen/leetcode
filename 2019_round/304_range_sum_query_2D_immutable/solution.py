class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            self._summation_matrix = []
            return

        self._summation_matrix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self._summation_matrix[i+1][j+1] = matrix[i][j] + self._summation_matrix[i][j+1] + self._summation_matrix[i+1][j] - self._summation_matrix[i][j]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self._summation_matrix:
            return
        return self._summation_matrix[row2+1][col2+1] - self._summation_matrix[row1][col2+1] - self._summation_matrix[row2+1][col1] + self._summation_matrix[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)