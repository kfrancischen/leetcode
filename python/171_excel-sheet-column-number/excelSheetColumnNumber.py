class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = []
        result = 0
        for str in s:
            digits.append(ord(str) - ord('A') + 1)
        for i in range(0, len(digits)):
            result += digits[i] * 26 ** (len(digits) - i - 1)
        return result


mytest = Solution()
s = 'ZA'
print mytest.titleToNumber(s)
