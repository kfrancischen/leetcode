class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        if m == 0:
            return triangle[0][0]
        dist = [[0] * i for i in range(1,m+1)]
        dist[m-1] = triangle[m-1]
        for i in range(m-2, -1, -1):
            for j in range(0, i + 1):
                dist[i][j] = min(dist[i+1][j], dist[i+1][j+1]) + triangle[i][j]
        return dist[0][0]


mytest = Solution()
s = [[2],[3,4],[6,5,7],[4,1,8,3]]
print mytest.minimumTotal(s)
