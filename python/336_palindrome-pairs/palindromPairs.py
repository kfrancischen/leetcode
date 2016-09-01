class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if not words:
            return []
        dic = {w:i for i, w in enumerate(words)}
        result = []
        for w in words:
            i = dic[w]
            for j in range(len(w)):
                s1, s2 = w[:j], w[j:]
                if s1 == s1[::-1] and s2[::-1] in dic and dic[s2[::-1]] != i:
                    result.append([dic[s2[::-1]], i])
                if s2 == s2[::-1] and s1[::-1] in dic and dic[s1[::-1]] != i:
                    result.append([i, dic[s1[::-1]]])
            if w != '' and w == w[::-1] and '' in dic:
                result.append([dic[''], i])
        return result


mytest = Solution()
s = ["bat", "tab", "cat"]
print mytest.palindromePairs(s)
