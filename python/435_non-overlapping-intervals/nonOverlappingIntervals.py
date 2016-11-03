# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        end = float('-inf')
        erase = 0
        intervals = sorted(intervals, key = lambda x: x.end)
        for i in intervals:
            if i.start >= end:
                end = i.end
            else:
                erase += 1

        return erase
