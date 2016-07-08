class Solution(object):
    # O(1) solution
    #
    # The rationale is that the i-th bit of the result will be set
    # if and only if
    #
    # (1) the i-th bit of m is set
    # (2) the following holds: m - n < (1 << i) - m % (1 << i).
    #
    # The reasoning is as follows: the i-th bit if set, will reset after
    # (1 << i) - m % (1 << i) (try an example to convince yourself that
    # this is true). If the interval is greater than this quantity, this
    # bit will be for sure 0.
    def rangeBitwiseAnd(self, m, n):
        if not m or not n:
            return 0
        res = 1 if (m & 1) and not (m - n) else 0
        for i in range(1, 31):
            if (m & (1 << i)):
                s = (1 << i) - m % (1 << i)
                if n - m < s:
                    res |= (1 << i)
        return res

mytest = Solution()
m = 0
n = 0
print mytest.rangeBitwiseAnd(m, n)
