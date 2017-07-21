# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        result = [-1] * len(intervals)
        inputs = []
        for i in range(len(intervals)):
            inputs.append((intervals[i], i))
        inputs = sorted(inputs, key = lambda x: x[0].start)

        for interval, index in inputs:
            rightIndex = self.binarySearch(interval, inputs)
            if rightIndex != -1:
                result[index] = inputs[rightIndex][1]

        return result

    def binarySearch(self, interval, inputs):
        left, right = 1, len(inputs) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if inputs[mid - 1][0].start < interval.end <= inputs[mid][0].start:
                return mid
            elif inputs[mid][0].start > interval.end:
                right = mid - 1
            else:
                left = mid + 1
        return -1
