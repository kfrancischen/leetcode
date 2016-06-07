class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ""
        result = "1"
        for i in range(1, n):
            count = 1
            newStr = ""
            for j in range(0, len(result) - 1):
                if result[j] == result[j + 1]:
                    count += 1
                else:
                    newStr += str(count) + result[j]
                    count = 1

            newStr += str(count) + result[-1]
            result = newStr
        return result

mytest = Solution()
n = 2
print mytest.countAndSay(n)
