class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = [0] * 10
        for i in range(len(s)):
            if s[i] == 'z':
                counter[0] += 1
            if s[i] == 'w':
                counter[2] += 1
            if s[i] == 'x':
                counter[6] += 1
            if s[i] == 's':
                counter[7] += 1
            if s[i] == 'g':
                counter[8] += 1
            if s[i] == 'u':
                counter[4] += 1
            if s[i] == 'f':
                counter[5] += 1
            if s[i] == 'h':
                counter[3] += 1
            if s[i] == 'i':
                counter[9] += 1
            if s[i] == 'o':
                counter[1] += 1

        counter[7] -= counter[6]
        counter[5] -= counter[4]
        counter[3] -= counter[8]
        counter[9] = counter[9] - counter[8] - counter[5] - counter[6]
        counter[1] = counter[1] - counter[0] - counter[2] - counter[4]

        result = ''
        for i in range(10):
            result += counter[i] * str(i)
        return result


mytest = Solution()
s = "owoztneoer"
print mytest.originalDigits(s)
