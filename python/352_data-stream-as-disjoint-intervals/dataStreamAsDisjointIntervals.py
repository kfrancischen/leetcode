# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq
class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.results = []


    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        heapq.heappush(self.results, (val, Interval(val, val)))

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        stack = []
        while self.results:
            index, cur = heapq.heappop(self.results)
            if not stack:
                stack.append((index, cur))
            else:
                _, prev = stack[-1]
                if prev.end + 1 >= cur.start:
                    prev.end = max(prev.end, cur.end)
                else:
                    stack.append((index, cur))
        self.results = stack

        return list(map(lambda x: x[1], stack))

mytest = SummaryRanges()
mytest.addNum(1)
mytest.addNum(3)
mytest.addNum(7)
mytest.addNum(6)
mytest.addNum(2)
print mytest.getIntervals()



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
