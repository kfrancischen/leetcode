import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heapLeft = []
        self.heapRight = []



    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        poped = heapq.heappushpop(self.heapRight, num)
        heapq.heappush(self.heapLeft, -poped)
        if len(self.heapLeft) > len(self.heapRight):
            heapq.heappush(self.heapRight, -heapq.heappop(self.heapLeft))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.heapRight) > len(self.heapLeft):
            return self.heapRight[0]
        else:
            return (self.heapRight[0] - self.heapLeft[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
