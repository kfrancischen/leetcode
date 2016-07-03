class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(0, n):
            newArray = [val + 2 ** i for val in result]
            result.extend(reversed(newArray))
        return result

mytest = Solution()
n = 4
print mytest.grayCode(n)
