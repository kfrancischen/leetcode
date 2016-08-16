class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n, m = len(s1), len(s2)
        if len(s3) != n + m:
            return False
        f = [True] + [False] * n
        for i in xrange(n):
            f[i + 1] = f[i] and s1[i] == s3[i]
        for j in xrange(m):
            f[0] = f[0] and s2[j] == s3[j]
            for i in xrange(n):
                f[i + 1] = (f[i] and s1[i] == s3[i + j + 1]) or (f[i + 1] and s2[j] == s3[i + j + 1])
        return f[n]

mytest = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print mytest.isInterleave(s1, s2, s3)
