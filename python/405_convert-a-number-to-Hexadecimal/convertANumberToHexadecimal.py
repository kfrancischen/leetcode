class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num = 16 ** 8 + num
        if num == 0:
            return '0'
        dic = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        result = ''
        while num:
            result += dic[num % 16]
            num = num / 16

        return result[::-1]


mytest = Solution()
num = 26
print mytest.toHex(num)
