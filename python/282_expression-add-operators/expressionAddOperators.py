class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        solution = ''
        curNum = 0
        result = []
        self.backTracking(solution, result, num, curNum, target, 0)
        return result

    def backTracking(self, solution, result, num, curNum, target, mult):
        if not num:
            if curNum == target:
                result.append(solution)
            return

        for i in range(0, len(num)):
            if i != 0 and num[0] == '0':
                break
            if solution == '':
                self.backTracking(solution + num[:i+1], result, num[i+1:], curNum + int(num[:i+1]), target, int(num[:i+1]))
            else:
                self.backTracking(solution + '+' + num[:i+1], result, num[i+1:], curNum + int(num[:i+1]), target, int(num[:i+1]))
                self.backTracking(solution + '-' + num[:i+1], result, num[i+1:], curNum - int(num[:i+1]), target, -int(num[:i+1]))
                self.backTracking(solution + '*' + num[:i+1], result, num[i+1:], curNum - mult + mult * int(num[:i+1]), target, mult * int(num[:i+1]))



mytest = Solution()
num = '105'
target = 5
print mytest.addOperators(num, target)
