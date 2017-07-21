class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordsBit = [0] * len(words)
        for i in range(0, len(words)):
            word = words[i]
            for char in set(word):
                wordsBit[i] |= 1 << (ord(char) - ord('a'))
        maxLength = 0
        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                if wordsBit[i] & wordsBit[j]:
                    continue
                maxLength = max(maxLength, len(words[i]) * len(words[j]))
        return maxLength


mytest = Solution()
s = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print mytest.maxProduct(s)
