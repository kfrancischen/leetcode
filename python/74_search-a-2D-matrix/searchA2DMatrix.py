class Solution(object):
    def searchMatrix(self, matrix, target):

        if len(matrix) == 0:
            return False
        return self.searchMatrix_(matrix, target)

    def searchMatrix_(self, matrix, target):
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:

            mid = matrix[row][col]
            if target == mid:
                return True
            if target < mid:
                col -= 1
            else:
                row += 1

        return False
        
