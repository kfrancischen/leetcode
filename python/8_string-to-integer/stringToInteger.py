class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        digits = []
        sign = 0
        for i in range(0, len(str)):
            if str[i] == ' ' and len(digits) == 0 and sign == 0:
                continue
            elif str[i] == '-':
                if sign == 0:
                    sign = -1
                else:
                    break
            elif str[i] == '+':
                if sign == 0:
                    sign = 1
                else:
                    break
            elif str[i] >= '0' and str[i] <= '9':
                digits.append(ord(str[i]) - ord('0'))
            else:
                break
        if len(digits) == 0:
            return 0
        elif sign == 0:
            sign = 1
        result = 0
        for i in range(0, len(digits)):
            result += digits[i] * 10 ** (len(digits) - i - 1)
        result = sign * result
        if result > 2147483647:
            return 2147483647
        if result < -2147483648:
            return -2147483648
        return result

mytest = Solution()
s = '+233'
print mytest.myAtoi(s)
