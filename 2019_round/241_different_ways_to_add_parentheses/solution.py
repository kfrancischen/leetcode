class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        dic = {}
        return self.get_sum(input, dic)
        
    def get_sum(self, string, dic):
        result = []
        if string in dic:
            return dic[string]
        for i in range(len(string)):
            if string[i] in ['+', '-', '*']:
                before_sum = self.get_sum(string[:i], dic)
                after_sum = self.get_sum(string[i+1:], dic)
                for v1 in before_sum:
                    for v2 in after_sum:
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

test = Solution()
input = '2-1-1'
print test.diffWaysToCompute(input)
