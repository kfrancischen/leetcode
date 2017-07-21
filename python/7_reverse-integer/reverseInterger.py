class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        sign = False
        if x < 0:
            x = -x
            sign = True
        digits = []
        while x != 0:
            digits.append(x % 10)
            x = (x - x%10)/10
        result = 0
        for i in range(0, len(digits)):
            result += digits[i] * 10 ** (len(digits) - i - 1)
        if result >= 2 ** 31 - 1:
            return 0
        if sign:
            result = -result
        return result
