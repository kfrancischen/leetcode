class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = []
        round = -1
        while num != 0:
            residue = num % 10
            num = (num - residue) / 10
            round += 1
            if residue == 0:
                continue
            if round == 0:
                roman.extend(self.findLetter(residue, 'I', 'V', 'X'))
            elif round == 1:
                roman.extend(self.findLetter(residue, 'X', 'L', 'C'))
            elif round == 2:
                roman.extend(self.findLetter(residue, 'C', 'D', 'M'))
            elif round == 3:
                roman.extend(['M'] * residue)
        return ''.join(reversed(roman))

    def findLetter(self, residue, s1, s2, s3):
        digits = []
        if 1 <= residue <= 3:
            digits.extend([s1] * residue)
        elif residue == 4:
            digits.extend([s2,s1])
        elif 5 <= residue <= 8:
            digits.extend([s1] * (residue - 5))
            digits.append(s2)
        elif residue == 9:
            digits.extend([s3, s1])
        return digits

mytest = Solution()
s = 9
print mytest.intToRoman(s)
