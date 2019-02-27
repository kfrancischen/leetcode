class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        result = [0] * len(s)
        if s[0] != '0':
            result[0] = 1
        
        for i in range(1, len(s)):
            if s[i] != '0':
                result[i] = result[i-1]

            if '01' <= s[i-1:i+1] <= '26':
                result[i] += result[i-2] if i > 1 else 1
        return result[-1]

s = "226"
test = Solution()
print(test.numDecodings(s))
