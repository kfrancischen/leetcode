class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[ 0 for i in range(0, n)] for j in range(0,n)]
        for i in range(0, n/2):
            for j in range(0, n - 2 * i):
                matrix[i][i + j] = 4 * i * (n - i) + 1 + j
                matrix[i + j][n-i-1] = 4 * i * (n - i) + n - 2 * i + j
                matrix[n-i-1][n-i-1-j] = 4 * i * (n - i) + 2*(n - 2 * i) -1 + j
                if j == n - 2*i - 1:
                    continue
                matrix[n-i-1-j][i] = 4 * i * (n - i) + 3*(n - 2 * i) -2 + j
        if n % 2 == 1:
            matrix[n/2][n/2] = n * n
        return matrix

mytest = Solution()
n = 7
print mytest.generateMatrix(n)
