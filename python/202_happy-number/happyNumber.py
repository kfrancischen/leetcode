class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hashTable = {}
        sum = 0
        while True:
            digits = self.getDigits(n)
            n = reduce(lambda x,y: x + y, digits)
            if n == 1:
                return True
            if n not in hashTable:
                hashTable[n] = 1
            else:
                return False

    def getDigits(self, n):
        digits = []
        while n != 0:
            digits.append((n % 10) ** 2)
            n = (n - n % 10) / 10
        return digits

mytest = Solution()
s = 14
print mytest.isHappy(s)
