class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.dic = {0:v1, 1:v2}
        self.cur = 1

    def next(self):
        """
        :rtype: int
        """
        if len(self.dic[1-self.cur]) != 0:
            self.cur = 1 - self.cur
        return self.dic[self.cur].pop(0)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.dic[0]) != 0 or len(self.dic[1]) != 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())