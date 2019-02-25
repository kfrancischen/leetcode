class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        start_direction = 0
        m, n  = len(matrix), len(matrix[0])
        visited = [[0] * n for _ in range(m)]

        position = [0, 0]
        result = []
        while True:
            visited[position[0]][position[1]] = 1
            result.append(matrix[position[0]][position[1]])

            if (position[1] == n-1 and start_direction == 0) or (position[1]+1 < n and visited[position[0]][position[1]+1] == 1 and start_direction == 0):
                start_direction = 1
            if (position[0] == m - 1 and start_direction == 1) or (position[0] + 1 < m and visited[position[0]+1][position[1]] == 1 and start_direction == 1):
                start_direction = 2
            if (position[1] == 0 and start_direction == 2) or (position[1] > 0 and visited[position[0]][position[1]-1] == 1 and start_direction == 2):
                start_direction = 3
            if (position[0] == 0 and start_direction == 3) or (position[0] > 0 and visited[position[0]-1][position[1]] == 1 and start_direction == 3):
                start_direction = 0

            if len(result) == m * n:
                return result

            position[0] = position[0] + directions[start_direction][0]
            position[1] = position[1] + directions[start_direction][1]


test = Solution()
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print test.spiralOrder(matrix)
            