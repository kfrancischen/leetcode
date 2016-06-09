class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        possibility = [0] * len(s)
        for i in range(len(s) - 1, -1 ,-1):
            if ord(s[i]) < ord('1') or ord(s[i]) > ord('9'):
                continue
            if i == len(s) - 1:
                possibility[i] = 1
            else:
                if int(s[i:i+2]) > 26:
                    possibility[i] = possibility[i + 1]
                else:
                    possibility[i] = possibility[i + 1] + possibility[i + 2] if i < len(s) - 2 else 1 + possibility[-1]
        return possibility[0]
mytest = Solution()
s = "11"
print mytest.numDecodings(s)
