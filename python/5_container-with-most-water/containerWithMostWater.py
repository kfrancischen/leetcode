class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0 or len(height) == 1:
            return 0

        pointLeft = 0
        pointRight = len(height) - 1

        maxVolume = 0

        while pointLeft != pointRight:
            valueLeft = height[pointLeft]
            valueRight = height[pointRight]

            newVolume = min(valueLeft, valueRight) * (pointRight - pointLeft)
            if newVolume > maxVolume:
                maxVolume = newVolume

            if valueLeft > valueRight:
                pointRight -= 1
            else:
                pointLeft += 1

        return maxVolume

mytest = Solution()
height = [7, 5, 6, 9]
print mytest.maxArea(height)
