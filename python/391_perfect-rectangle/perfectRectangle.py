from collections import defaultdict
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        leftMostX, leftMostY, rightMostX, rightMostY = float('inf'), float('inf'), float('-inf'), float('-inf')
        totalArea = 0
        existedCorners = defaultdict(int)
        for leftX, leftY, rightX, rightY in rectangles:
            existedCorners[(leftX, leftY)] += 1
            existedCorners[(leftX, rightY)] += 1
            existedCorners[(rightX, rightY)] += 1
            existedCorners[(rightX, leftY)] += 1

            leftMostX = min(leftMostX, leftX)
            leftMostY = min(leftMostY, leftY)
            rightMostX = max(rightMostX, rightX)
            rightMostY = max(rightMostY, rightY)
            totalArea += (rightY - leftY) * (rightX - leftX)

        if totalArea != (rightMostY - leftMostY) * (rightMostX - leftMostX):
            return False

        corners = [(leftMostX, leftMostY), (leftMostX, rightMostY), (rightMostX, leftMostY),\
            (rightMostX, rightMostY)]
        for corner in corners:
            if existedCorners[corner] != 1:
                return False
            existedCorners.pop(corner, None)
        for key in existedCorners:
            if existedCorners[key] != 4 and existedCorners[key] != 2:
                return False
        return True

mytest = Solution()
s = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
print mytest.isRectangleCover(s)
