import copy
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        row = [0] * (rowIndex + 1)
        newRow = [0] * (rowIndex + 1)
        row[0] = 1
        newRow[0] = 1
        for i in range(1, rowIndex + 1):
            newRow[i] = 1
            for j in range(1, i):
                newRow[j] = row[j-1] + row[j]
            row = copy.deepcopy(newRow)
        return row


mytest = Solution()
n = 7
print mytest.getRow(n)
