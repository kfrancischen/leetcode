import random
from collections import defaultdict
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.idx = defaultdict(set)
        self.vals = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.vals.append(val)
        self.idx[val].add(len(self.vals) - 1)
        return len(self.idx[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.idx[val]:
            out, ins = self.idx[val].pop(), self.vals[-1]
            self.vals[out] = ins
            if self.idx[ins]:
                self.idx[ins].add(out)
                self.idx[ins].discard(len(self.vals) - 1)
            self.vals.pop()
            return True
        return False


    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.vals)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
