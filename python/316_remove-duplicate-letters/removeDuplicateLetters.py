class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic, used, result = {}, {}, ''
        for i in range(len(s)):
            dic[s[i]] = i
        i, j, sc = 0, 0, sorted(dic.values())
        while j < len(sc):
            if s[sc[j]] in used:
                j += 1
                continue

            c, k = min([(s[k], k) for k in range(i, sc[j] + 1) if s[k] not in used])
            result += c

            if len(result) == len(dic):
                return result
            i, used[c] = k + 1, True

        return result


mytest = Solution()
s = "cbacdcbc"
print mytest.removeDuplicateLetters(s)
