class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return

        for i in range(0, len(matrix)/2):
            self.rotation(matrix[i:(len(matrix)-i)], i, len(matrix))


    def rotation(self, matrix, index, totalLength):
        currentLength = totalLength - 2 * index
        if currentLength == 0 or currentLength == 1:
            return
        start = 0
        while start < currentLength - 1:
            buffer1 = matrix[start][totalLength - index - 1]
            buffer2 = matrix[currentLength - 1][totalLength - index - 1 - start]

            matrix[start][totalLength - index - 1] = matrix[0][index + start]
            matrix[currentLength - 1][totalLength - index - 1 - start] = buffer1

            buffer1 = matrix[currentLength - start - 1][index]
            matrix[currentLength - start - 1][index] = buffer2
            matrix[0][index + start] = buffer1

            start += 1


mytest = Solution()
s = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,4,3]]
mytest.rotate(s)
print s
