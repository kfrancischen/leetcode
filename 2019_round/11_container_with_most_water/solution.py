class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pointer1, pointer2 = 0, len(height) - 1
        max_area = min(height[pointer1], height[pointer2]) * (pointer2 - pointer1)
        while pointer1 < pointer2:
            if height[pointer1] < height[pointer2]:
                pointer1 += 1
            else:
                pointer2 -= 1
            max_area = max(max_area, min(height[pointer1], height[pointer2]) * (pointer2 - pointer1))
            
        return max_area
            