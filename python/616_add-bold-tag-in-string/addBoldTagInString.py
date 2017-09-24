class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        paint = [False] * len(s)
        for i in xrange(len(s)):
            block = s[i:]
            for word in dict:
                if block.startswith(word):
                    paint[i:i+len(word)] = [True] * len(word)

        ans = []
        for i, u in enumerate(s):
            if paint[i] and (i == 0 or not paint[i-1]):
                ans.append('<b>')
            ans.append(u)
            if paint[i] and (i == len(s) - 1 or not paint[i+1]):
                ans.append('</b>')

        return "".join(ans)
                