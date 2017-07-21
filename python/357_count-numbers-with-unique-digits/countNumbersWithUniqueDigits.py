import math
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        numOfUnique = [0] * n
        numOfUnique[0] = 10
        numOfPossibility = [math.factorial(i) for i in range(0, 10)]
        for i in range(1, n):
            numOfUnique[i] = numOfUnique[i - 1] + 9 * numOfPossibility[-1] / numOfPossibility[-1-i]
        return numOfUnique[-1]

mytest = Solution()
n = 3
print mytest.countNumbersWithUniqueDigits(n)
