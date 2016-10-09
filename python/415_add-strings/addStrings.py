class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            num1 = '0' * (len(num2) - len(num1)) + num1
        else:
            num2 = '0' * (len(num1) - len(num2)) + num2

        increment = 0
        result = ''
        for i in range(len(num1)-1, -1, -1):
            summation = ord(num1[i]) - ord('0') + ord(num2[i]) - ord('0') + increment
            if summation >= 10:
                increment = 1
                result += str(summation - 10)
            else:
                increment = 0
                result += str(summation)

        if increment == 1:
            result += '1'

        return result[::-1]

mytest = Solution()
num1 = '7934'
num2 = '3483'
print mytest.addStrings(num1, num2)
