class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        table = {i:[] for i in range(0, numRows)}
        count = 0
        forward = True
        for i in range(0, len(s)):
            table[count].append(s[i])
            if count == numRows - 1:
                forward = False
            if count == 0:
                forward = True
            if forward:
                count += 1
            else:
                count -= 1
        result = []
        for value in table.values():
            result.extend(value)
        return "".join(result)


mytest = Solution()
s = "PAYPALISHIRING"
numRows = 3
print mytest.convert(s, numRows)
