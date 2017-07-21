class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        numOfBytes = 0
        for num in data:
            bits = "{0:b}".format(num)
            if len(bits) < 8:
                bits = '0' * (8-len(bits)) + bits
            if bits[0] == '0':
                if numOfBytes != 0:
                    return False
            elif bits[1] == '0' and bits[0] == '1':
                numOfBytes -= 1
                if numOfBytes < 0:
                    return False
            else:
                if numOfBytes != 0:
                    return False
                count = 0
                while count < len(bits) and bits[count] != '0':
                    count += 1
                numOfBytes = count - 1
        if numOfBytes != 0:
            return False
        return True

mytest = Solution()
s = [235, 140, 4]
print mytest.validUtf8(s)
