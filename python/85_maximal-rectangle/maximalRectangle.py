from copy import deepcopy
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix[0]) == 0:
            return 0
        intMatrix = [[int(matrix[i][j]) for j in range(0, len(matrix[0]))] for i in range(0, len(matrix))]
        result = self.largestRectangle(intMatrix[0])
        for i in range(1 ,len(intMatrix)):
            for j in range(0, len(intMatrix[0])):
                if intMatrix[i][j] == 1:
                    intMatrix[i][j] += intMatrix[i-1][j]
            result = max(result, self.largestRectangle(intMatrix[i]))
        return result

    def largestRectangle(self, heights):
        newHeights = deepcopy(heights)
        newHeights.append(0)
        stack = [0]
        result = 0
        for i in range(1 ,len(newHeights)):
            while stack and newHeights[i] < newHeights[stack[-1]]:
                h = newHeights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                result = max(result, w * h)
            stack.append(i)
        return result


mytest = Solution()
s = ["10100","10111","11111","10010"]
print mytest.maximalRectangle(s)
