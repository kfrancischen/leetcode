class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        intS = []
        result = 0
        for i in range(0, len(s)):
            if s[i] == 'I':
                intS.append(1)
            elif s[i] == 'V':
                intS.append(5)
            elif s[i] == 'X':
                intS.append(10)
            elif s[i] == 'L':
                intS.append(50)
            elif s[i] == 'C':
                intS.append(100)
            elif s[i] == 'D':
                intS.append(500)
            elif s[i] == 'M':
                intS.append(1000)
            if i > 0:
                result += intS[i-1] if intS[i] <= intS[i-1] else - intS[i-1]
        result += intS[-1]
        return result
