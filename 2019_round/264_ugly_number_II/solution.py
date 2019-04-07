class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        ugly = [1] * n
        l2 = l3 = l5 = 0
        for i in range(1, n):
            ugly[i] = min(ugly[l2] * 2, ugly[l3] * 3, ugly[l5] * 5)
            if ugly[i] == ugly[l2] * 2:
                l2 += 1
            if ugly[i] == ugly[l3] * 3:
                l3 += 1
            if ugly[i] == ugly[l5] * 5:
                l5 += 1
        return ugly[-1]

test = Solution()
n = 10
print test.nthUglyNumber(n)