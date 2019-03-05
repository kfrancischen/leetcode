class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = {}
        self.info = wordDict
        return self.containWord(s)


    def containWord(self, s):
        if len(s) == 0:
            return True
        if s in self.memo:
            return False
        
        self.memo[s] = True
        for word in self.info:
            if s.startswith(word) and self.containWord(s[len(word):]):
                return True

        return False
