class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        self.number = {(0,1):'One', (0,2):'Two', (0,3):'Three', (0,4):'Four', (0,5):'Five', (0,6):'Six',\
            (0,7):'Seven', (0,8):'Eight',(0,9):'Nine', (1,0):'Ten', (1,1):'Eleven', (1,2):'Twelve',(1,3):'Thirteen', \
            (1,4):'Fourteen', (1,5):'Fifteen',(1,6):'Sixteen', (1,7):'Seventeen', (1,8):'Eighteen', (1,9):'Nineteen'}
        self.tens = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
        self.order = {0:'', 3:'Thousand', 6:'Million', 9:'Billion'}
        result = []
        order = 0
        while num != 0:
            curNum = num % 1000
            digit = self.transfrom(curNum)
            curResult= self.threeDigits(digit)
            curResult = curResult.strip()
            if curResult != '':
                curResult += ' ' + self.order[order]
                result.append(curResult)
            order += 3
            num = num / 1000
        print result
        result = ' '.join(result[::-1])
        result = result.strip()
        return result

    def transfrom(self, number):
        digit = []
        while number != 0:
            digit.append(number%10)
            number = number / 10
        if len(digit) != 3:
            digit += [0] * (3-len(digit))
        return digit[::-1]

    def threeDigits(self, digits):
        result = ''
        if digits[0] != 0:
            result += self.number[(0,digits[0])] + ' Hundred' + ' '
        if (digits[1], digits[2]) in self.number:
            result += self.number[(digits[1], digits[2])] + ' '
        elif (digits[1], digits[2]) != (0,0):
            result += self.tens[digits[1]] + ' '
            if digits[2] != 0:
                result += self.number[(0, digits[2])] + ' '
        return result


mytest = Solution()
num = 50868
print mytest.numberToWords(num)
