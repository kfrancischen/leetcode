class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.val = []
        self.ave = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.val) < self.size:
            self.ave = (self.ave * len(self.val) + val) / (len(self.val) + 1.0)
        else:
            self.ave = (self.ave * self.size - self.val.pop(0) + val) / (1.0 * self.size)
        self.val.append(val)
        return self.ave
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)