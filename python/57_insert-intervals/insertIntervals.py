# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        data = []
        for interval in intervals:
            heapq.heappush(data, [interval.start, 'a'])
            heapq.heappush(data, [interval.end, 'b'])

        cacheData = []
        result = []
        for i in range(len(data)):
            val, flag = heapq.heappop(data)
            if flag == 'a':
                cacheData.append([val, flag])
            else:
                start_val, _ = cacheData.pop()
            if len(cacheData) == 0:
                newInterval = Interval(start_val, val)
                result.append(newInterval)

        return result
