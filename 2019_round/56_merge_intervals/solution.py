# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
import heapq
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
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

interval_1 = Interval(1, 3)
interval_2 = Interval(0, 0)
# interval_3 = Interval(8, 10)
# interval_4 = Interval(15, 18)
test = Solution()
print test.merge([interval_1, interval_2])