from collections import defaultdict
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if not wordDict:
            return []
        dp = defaultdict(list)
        maxLen = max(len(w) for w in wordDict)
        dp[0] = []
        result = []
        solution = []
        for i in range(1, len(s) + 1):
            for j in range(i - maxLen, i):
                if j in dp and s[j:i] in wordDict:
                    dp[i].append(j)

        def backTracking(k, solution):
            if k in dp and len(dp[k]):
                for i in dp[k]:
                    solution.append(s[i:k])
                    backTracking(i, solution)
                    solution.pop()
            elif len(solution) != 0:
                result.append(' '.join(solution[::-1]))
                return

        backTracking(len(s),solution)
        return result


mytest = Solution()
s = "aaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print mytest.wordBreak(s, wordDict)
