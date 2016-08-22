# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        lines = {}
        occurence = {}
        allPoints = []
        for point in points:
            if (point.x, point.y) not in occurence:
                occurence[(point.x, point.y)] = 1
                allPoints.append((point.x, point.y))
            else:
                occurence[(point.x, point.y)] += 1
        if len(allPoints) == 1:
            return occurence[allPoints[0]]
            
        for i in range(0, len(allPoints)):
            point_1x, point_1y = allPoints[i]

            for j in range(i+1, len(allPoints)):
                point_2x, point_2y = allPoints[j]

                if point_1x == point_2x:
                    k = 'INF'
                    b = point_1x
                else:
                    k = (point_2y - point_1y) * 1.0 / (point_2x - point_1x)
                    b = point_2y - k * point_2x
                if (k,b) not in lines:
                    lines[(k, b)] = set([i,j])
                else:
                    lines[(k, b)].add(i)
                    lines[(k, b)].add(j)

        maxNum = 0
        for key in lines.keys():
            curMax = 0
            for point in lines[key]:
                curMax += occurence[allPoints[point]]
            maxNum = max(maxNum, curMax)

        return maxNum
