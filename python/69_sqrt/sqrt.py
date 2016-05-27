class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        if x == 0 or x == 1:
            return x
        left = 0
        right = x
        while True:
            root = (left + right) / 2
            if root ** 2 == x:
                return root
            if root ** 2 < x and (root + 1) ** 2 > x:
                return root
            if root ** 2 > x:
                right = root
            else:
                left = root
        if right ** 2 == x:
            return right
        if right ** 2 < x and (right + 1) ** 2 > x:
            return right

mytest = Solution()
x = 100
print mytest.mySqrt(x)
