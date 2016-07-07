class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = "{0:b}".format(n)

        if len(bits) < 32:
            bits = '0' * (32 - len(bits)) + bits
        return int(bits[::-1], 2)


mytest = Solution()
n = 43261596
print mytest.reverseBits(n)
