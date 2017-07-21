class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        pointer_s, pointer_t = 0, 0
        while pointer_t != len(t):
            if t[pointer_t] == s[pointer_s]:
                pointer_s += 1
            pointer_t += 1
            if pointer_s == len(s):
                return True
        return False

mytest = Solution()
s = "axc"
t = "ahbgdc"
print mytest.isSubsequence(s, t)
