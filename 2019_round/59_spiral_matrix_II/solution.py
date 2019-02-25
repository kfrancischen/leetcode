class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0] * n for _ in range(n)]
        visited = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        position = [0, 0]
        cur_direction = 0
        while visited < n ** 2:
            visited += 1
            result[position[0]][position[1]] = visited
            if (position[1] + 1 == n and cur_direction == 0) or (position[1] + 1 < n and result[position[0]][position[1]+1] != 0 and cur_direction == 0):
                cur_direction = 1
            if (position[0] + 1 == n and cur_direction == 1) or (position[0] + 1 < n and result[position[0]+1][position[1]] != 0 and cur_direction == 1):
                cur_direction = 2
            if (position[1] - 1 < 0 and cur_direction == 2) or (position[1] - 1 >= 0 and result[position[0]][position[1]-1] != 0 and cur_direction == 2):
                cur_direction = 3
            if (position[0] - 1 < 0 and cur_direction == 3) or (position[0] - 1 >= 0 and result[position[0]-1][position[1]] != 0 and cur_direction == 3):
                cur_direction = 0

            position[0] += directions[cur_direction][0]
            position[1] += directions[cur_direction][1]

        return result


test = Solution()
n = 3
print test.generateMatrix(n)