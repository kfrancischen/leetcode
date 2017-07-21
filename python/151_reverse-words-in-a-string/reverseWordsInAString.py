class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        wordsList = s.split()
        wordsList.reverse()
        return " ".join(wordsList)

mytest = Solution()
s = "the sky is blue "
print mytest.reverseWords(s)
