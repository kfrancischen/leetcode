from copy import deepcopy
from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        k = len(words[0])
        totalLen = k * len(words)
        self.wordsTable = Counter(words)
        result = []
        for i in range(0, k):
            used = deepcopy(self.wordsTable)
            start = i
            for j in range(start, len(s) - k + 1, k):
                substring = s[j:j+k]
                used[substring] -= 1
                while used[substring] < 0:
                    used[s[start:start+k]] += 1
                    start += k
                if j + k - start == totalLen:
                    result.append(start)
        return result

mytest = Solution()
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print mytest.findSubstring(s, words)
