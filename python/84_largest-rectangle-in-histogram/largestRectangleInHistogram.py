class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        result = 0
        heights.append(0)
        stack = [0]
        for i in range(1, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                result = max(result, w * h)

            stack.append(i)

        return result

mytest = Solution()
heights = [2,1,5,6,2,3]
print mytest.largestRectangleArea(heights)
