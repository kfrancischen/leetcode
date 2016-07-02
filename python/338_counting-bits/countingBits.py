class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        numOfBits = [0] * (num + 1)
        numOfBits[1] = 1
        power = 0
        for i in range(2, num + 1):
            if i == 2 ** (power + 1):
                numOfBits[i] = 1
                power += 1
                continue
            numOfBits[i] = 1 + numOfBits[i - 2 ** power]
        return numOfBits

mytest = Solution()
num = 1
print mytest.countBits(num)
