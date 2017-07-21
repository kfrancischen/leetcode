class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = ''
        sign = False
        if numerator * denominator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
            sign = True

        result += str(numerator / denominator)
        residue = numerator % denominator
        if residue == 0:
            if sign:
                result = '-' + result
            return result
        result += '.'
        hashTable = {residue:len(result)}
        count = len(result) + 1
        while True:
            newNumerator = residue * 10
            result += str(newNumerator / denominator)
            residue = newNumerator % denominator
            if residue == 0:
                if sign:
                    result = '-' + result
                return result
            if residue not in hashTable:
                hashTable[residue] = count
                count += 1
            else:
                break
        preIdx = hashTable[residue]
        if sign:
            result = '-' + result[0:preIdx] + '(' + result[preIdx:count] + ')'
        else:
            result = result[0:preIdx] + '(' + result[preIdx:count] + ')'
        return result

mytest = Solution()
numerator = 2147483647
denominator = 37
print mytest.fractionToDecimal(numerator, denominator)
