import bisect
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        A = [[0] * n for _ in range(m)]
        result = float('-inf')
        for i in range(0, m):
            A[i][0] = matrix[i][0]
            for j in range(1, n):
                A[i][j] = A[i][j-1] + matrix[i][j]
        print A
        for i in range(n):
            for j in range(i, n):
                x, t = [0], 0
                for r in range(m):
                    if i == 0:
                        t += A[r][j]
                    else:
                        t += A[r][j] - A[r][i - 1]

                    u = bisect.bisect_left(x, t - k)
                    if u <= r:
                        if result < t - x[u]:
                            result = t - x[u]
                            if result == k:
                                return k
                    bisect.insort(x, t)
        return result

mytest = Solution()
matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
print mytest.maxSumSubmatrix(matrix, k)
