class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        leftMax = 0
        rightMax = 0
        leftPointer = 0
        rightPointer = len(height) - 1
        water = 0
        while leftPointer <= rightPointer:
            leftMax = max(leftMax, height[leftPointer])
            rightMax = max(rightMax, height[rightPointer])

            if leftMax < rightMax:
                water += leftMax - height[leftPointer]
                leftPointer += 1
            else:
                water += rightMax - height[rightPointer]
                rightPointer -= 1

        return water

mytest = Solution()
s = [0,1,0,2,1,0,1,3,2,1,2,1]
print mytest.trap(s)
