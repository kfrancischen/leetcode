# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left + 1 < right:
            mid = (left + right) / 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        if isBadVersion(left):
            return left
        return right
