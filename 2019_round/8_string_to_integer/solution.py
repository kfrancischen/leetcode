class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = ''
        sign = 0
        for i in range(len(str)):
            if str[i] == ' ' and len(result) == 0 and sign == 0:
                continue
            elif str[i] in '-+' and sign == 0 and len(result) == 0:
                sign = 1 if str[i] == '+' else -1
            elif str[i] in '0123456789':
                result += str[i]
            else:
                break
        if not result:
            return 0
        else:
            result = sign * int(result) if sign != 0 else int(result)
        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        if result < -2 ** 31:
            result = -2 ** 31
        return result
