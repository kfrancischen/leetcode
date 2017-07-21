class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        bits = "{0:b}".format(num)
        numOfZero = len(bits) - 1
        return (0 == (num & (num - 1))) and numOfZero%2 == 0
