from collections import defaultdict
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        newWall = []
        for i in range(len(wall)):
            if len(wall[i]) > 1:
                newWall.append(wall[i])

        if not newWall:
            return len(wall)
        sums = [[val[0]]for val in newWall]
        summation = defaultdict(list)
        for i in range(len(newWall)):
            for j in range(1, len(newWall[i])-1):
                sums[i].append(sums[i][j-1] + newWall[i][j])

        for i in range(len(sums)):
            for j in range(len(sums[i])):
                summation[sums[i][j]].append(i)

        return min([len(wall)-len(val) for val in summation.values()])