class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        solution = []
        self.backTracking(s, solution, result)
        return result


    def backTracking(self, s, solution, result):
        if not s:
            result.append(solution)
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                self.backTracking(s[i:], solution + [s[:i]], result)


mytest = Solution()
s = "amana"
print mytest.partition(s)
