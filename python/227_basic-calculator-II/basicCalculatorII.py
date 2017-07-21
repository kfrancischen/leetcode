class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ','')
        newS = []
        i = 0
        tempS = ''
        while i < len(s):
            if s[i] == '-' or s[i] == '+' or s[i] == '/' or s[i] == '*':
                newS.append(tempS)
                newS.append(s[i])
                tempS = ''
            else:
                tempS += s[i]
            i += 1
        if tempS != '':
            newS.append(tempS)

        s = newS
        newS = []
        i = 0
        while i < len(s):
            if s[i] == '/':
                val = int(newS.pop())
                newS.append(str(val / int(s[i + 1])))
                i += 1
            elif s[i] == '*':
                val = int(newS.pop())
                newS.append(str(val * int(s[i + 1])))
                i += 1
            else:
                newS.append(s[i])
            i += 1

        i = 1
        result = int(newS[0])
        while i < len(newS):
            if newS[i] == '-':
                result -= int(newS[i + 1])
                i += 1
            elif newS[i] == '+':
                result += int(newS[i + 1])
                i += 1
            i += 1
        return result

mytest = Solution()
s = " 3 + 42/2"
print mytest.calculate(s)
