class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        sideLen = [map(int, row) for row in matrix]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    sideLen[i][j] = 1 + min(sideLen[i - 1][j], sideLen[i][j - 1], sideLen[i - 1][j - 1])
        return max(max(row) for row in sideLen) ** 2
        #return max(max(sideLen)) ** 2

mytest = Solution()
matrix = ["0001","1101","1111","0111","0111"]
print mytest.maximalSquare(matrix)
