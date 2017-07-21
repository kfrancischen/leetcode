class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num
        while left + 1 < right:
            mid = (left + right) / 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid
            else:
                right = mid

        if left ** 2 == num or right ** 2 == num:
            return True

        return False

mytest = Solution()
num = 14
print mytest.isPerfectSquare(num)
