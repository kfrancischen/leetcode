class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        digits1 = version1.split('.')
        digits2 = version2.split('.')
        if len(digits1) > len(digits2):
            return self.checkVersion(digits1, digits2)
        else:
            return -self.checkVersion(digits2, digits1)

    def checkVersion(self, digits1, digits2):
        for i in range(0, len(digits2)):
            if int(digits1[i]) > int(digits2[i]):
                return 1
            elif int(digits1[i]) < int(digits2[i]):
                return -1
        for j in range(i + 1, len(digits1)):
            if int(digits1[j]) != 0:
                return 1
        return 0

mytest = Solution()
s1 = "1.0"
s2 = "1.00"
print mytest.compareVersion(s1, s2)
