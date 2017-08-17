class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if self.hits and timestamp - self.hits[0] >= 300:
            self.hits.pop(0)
        self.hits.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        count = 0
        for i in range(len(self.hits)):
            if timestamp - self.hits[i] >= 300:
                count += 1
            else:
                break
        return len(self.hits) - count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)