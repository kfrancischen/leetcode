class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        maximum = min(m/2, n/2)
        newOrder = []
        for i in range(0, maximum + 1):
            self.recurseMatrix(matrix[i:(m-i)], i, m, n, newOrder)
        return newOrder

    def recurseMatrix(self, matrix, index, m, n, order):
        currentSize = min(m, n) - 2 * index
        if currentSize <= 0:
            return

        if m - 2 * index == 1:
            order.extend(matrix[0][index:(n-index)])
            return

        if n - 2 * index == 1:
            for i in range(0, m - 2 * index):
                order.append(matrix[i][index])
            return

        order.extend(matrix[0][index:(n - index - 1)])

        for i in range(0, m - 2 * index - 1):
            order.append(matrix[i][n - index - 1])

        order.extend(list(reversed(matrix[m - 2 * index - 1][(index + 1):(n - index)])))

        for i in range(1, m - 2 * index):
            order.append(matrix[m - 2 * index - i][index])

mytest = Solution()
s = []
print mytest.spiralOrder(s)
