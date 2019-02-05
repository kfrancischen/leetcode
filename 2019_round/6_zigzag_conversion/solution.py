class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = [''] * numRows
        start_row = 0
        for i in range(len(s)):
            result[start_row] += s[i]
            if start_row == numRows - 1:
                direction = -1
            if start_row == 0:
                direction = 1
                
            if direction == 1:
                start_row += 1
            else:
                start_row -= 1

        return ''.join(result)