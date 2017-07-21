class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty():
            return
        self.q = self.q[:len(self.q) - 1]

    def top(self):
        """
        :rtype: int
        """
        return None if self.empty() else self.q[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0
