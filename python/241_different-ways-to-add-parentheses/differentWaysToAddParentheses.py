class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        dic = {}
        return self.getSums(input, dic)

    def getSums(self, string, dic):
        result = []
        if string in dic:
            return dic[string]
        for i in range(len(string)):
            if string[i] == '+' or string[i] == '-' or string[i] == '*':
                foreSum = self.getSums(string[:i], dic)
                afterSum = self.getSums(string[i+1:], dic)
                for v1 in foreSum:
                    for v2 in afterSum:
                        r = self.compute(v1, v2, string[i])
                        result.append(r)
                        dic[string] = result
        if len(result) == 0:
            return [int(string)]
        else:
            return result

    def compute(self, v1, v2, sign):
        if sign == '+':
            return v1 + v2
        elif sign == '-':
            return v1 - v2
        else:
            return v1 * v2




mytest = Solution()
s = '2-1-11'
print mytest.diffWaysToCompute(s)
