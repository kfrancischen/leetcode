class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = 0
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                int1 = ord(num1[i]) - ord('0')
                int2 = ord(num2[j]) - ord('0')
                result += (int1 * 10 ** (len(num1)-1 - i)) * (int2 * 10 ** (len(num2)-1-j))
        return str(result)

mytest = Solution()
num1 = "0"
num2 = "0"
print mytest.multiply(num1, num2)
