from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        result = []
        for i in range(len(p)-1, len(s)):
            sCounter[s[i]] += 1
            if sCounter == pCounter:
                result.append(i - len(p) + 1)
            sCounter[s[i-len(p) + 1]] -= 1
            if sCounter[s[i-len(p) + 1]] == 0:
                del sCounter[s[i-len(p) + 1]]

        return result


mytest = Solution()
s = "abab"
p = "ab"
print mytest.findAnagrams(s, p)
