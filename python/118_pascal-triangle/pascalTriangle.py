import copy
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        triangle = []
        preRow = []
        self.genRow(triangle, preRow, numRows, 1)

        return triangle

    def genRow(self, triangle, preRow, numRows, start):
        if start > numRows:
            return
        newRow = [1]
        for i in range(0, len(preRow) - 1):
            newRow.append(preRow[i] + preRow[i+1])
        if start != 1:
            newRow.append(1)
        triangle.append(copy.deepcopy(newRow))
        preRow = newRow
        self.genRow(triangle, preRow, numRows, start + 1)

mytest = Solution()
n = 6
print mytest.generate(n)
