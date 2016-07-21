# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked = []


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.hasNext():
            if len(self.peeked) != 0:
                return self.peeked[0]
            else:
                self.peeked.append(self.iterator.next())
                return self.peeked[-1]
        return None

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            if len(self.peeked) != 0:
                val = self.peeked[0]
                self.peeked = self.peeked[1:]
                return val
            else:
                return self.iterator.next()
        return None


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iterator.hasNext() or len(self.peeked) != 0


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
