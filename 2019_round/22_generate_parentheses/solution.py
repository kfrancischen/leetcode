class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return ""
        result = set()
        self.backTracking(n, result, 1)
        return list(result)

    def backTracking(self, n, result, start):
        if start == n:
            result.add("()")
            return
        self.backTracking(n, result, start + 1)

        tempList = list(result)
        result.clear()
        for val in tempList:
            for i in range(0, len(val)):
                result.add(val[:i + 1] + "()" + val[i+1:])
            result.add("(" + val + ")")
            result.add("()" + val)