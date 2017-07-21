class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if len(s) == 0:
            return False

        i = 0
        if s[i] == '-' or s[i] == '+':
            i += 1

        n_nm = n_pt = 0
        while i < len(s) and s[i] in '0123456789.':
            if s[i] == '.':
                n_pt += 1
            else:
                n_nm += 1
            i += 1
        if n_pt > 1 or n_nm < 1:
            return False

        if i < len(s) and s[i] == 'e':
            i += 1
            if i < len(s) and (s[i] == '+' or s[i] == '-'):
                i += 1
            n_nm = 0
            while i < len(s) and s[i] in '0123456789':
                i += 1
                n_nm += 1

            if n_nm < 1:
                return False

        return i == len(s)

mytest = Solution()
s = ' .1'
print mytest.isNumber(s)
