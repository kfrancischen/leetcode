class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        count = 0
        while count <= n - m:
            if haystack[count:count + m] == needle:
                return count
            count += 1
        return -1

mytest = Solution()
haystack = "abcb"
needle = "cb"
print mytest.strStr(haystack, needle)
