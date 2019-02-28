class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        f = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in xrange(len(row)):
                f[i] = row[i] + min(f[i], f[i + 1])
        return f[0]