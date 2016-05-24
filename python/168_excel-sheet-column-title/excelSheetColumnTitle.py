class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        digits = []
        while n!= 0:
            n = n - 1
            residue = n - 26 * (n/26)
            digits.append(chr(residue + 65))
            n -= residue
            n /= 26
        return ''.join(reversed(digits))
