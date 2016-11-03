class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) / 2
            if mid * (mid + 1) <= n * 2 and (mid + 1) * (mid + 2) > n * 2:
                return mid
            elif mid * (mid + 1) > n * 2:
                right = mid - 1
            else:
                left = mid + 1


mytest = Solution()
n = 3
print mytest.arrangeCoins(n)
