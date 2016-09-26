import heapq
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        q = []
        for i in range(m):
            visited[i][0] = True
            heapq.heappush(q, [heightMap[i][0], i, 0])
            visited[i][n-1] = True
            heapq.heappush(q, [heightMap[i][n-1], i, n-1])

        for i in range(1, n-1):
            visited[0][i] = True
            heapq.heappush(q, [heightMap[0][i], 0, i])
            visited[m-1][i] = True
            heapq.heappush(q, [heightMap[m-1][i], m-1, i])

        result = 0
        while q:
            cell = heapq.heappop(q)
            for (i,j) in [(1,0), (-1,0),(0,1), (0,-1)]:
                x = cell[1] + i
                y = cell[2] + j
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    result += max(0, cell[0] - heightMap[x][y])
                    heapq.heappush(q,[max(heightMap[x][y], cell[0]), x, y])
                    visited[x][y] = True
        return result

mytest = Solution()
s = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
print mytest.trapRainWater(s)
