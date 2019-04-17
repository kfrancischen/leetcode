import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))

test = Solution()
n = 3
print test.bulbSwitch(n)