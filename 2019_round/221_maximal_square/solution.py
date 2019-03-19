class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        side_len = [map(int, row) for row in matrix]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    side_len[i][j] = 1 + min(side_len[i-1][j], side_len[i][j-1], side_len[i-1][j-1])

        print side_len
        return max(max(row) for row in side_len) ** 2

test = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print test.maximalSquare(matrix)