class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                break
        s = s[:i + 1]
        for i in range(0, len(s)):
            if s[i] == " ":
                count = 0
            else:
                count += 1
        return count

mytest = Solution()
s = " "
print mytest.lengthOfLastWord(s)
