class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = ''
        if numerator * denominator < 0:
            sign = '-'
            numerator = abs(numerator)
            denominator = abs(denominator)

        int_part = str(numerator / denominator)
        dec_part = ''

        n = numerator % denominator

        occurrence = {}
        cnt = 0
        while True:
            if n == 0:
                break

            val = (n * 10) / denominator
            n = (n * 10) % denominator

            if n in occurrence:
                dec_part = dec_part[:occurrence[n]] + '(' + dec_part[occurrence[n]:] + ')'
                break
            else:
                occurrence[n] = cnt
                cnt += 1
                dec_part += str(val)

        result = sign + int_part
        if dec_part:
            result += '.' + dec_part

        return result
        
            
