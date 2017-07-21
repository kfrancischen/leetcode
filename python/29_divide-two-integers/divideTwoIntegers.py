class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1
        sign = 1 if divisor * dividend > 0 else -1
        divisor = abs(divisor)
        dividend = abs(dividend)
        left = 0
        right = dividend
        result = 0
        while left  + 1 < right:
            mid = (left + right) / 2
            if divisor * mid <= dividend and divisor * (mid + 1) > dividend:
                result = sign * mid
                break
            elif divisor * mid > dividend:
                right = mid
            elif divisor * mid < dividend:
                left = mid

        if divisor * right <= dividend and divisor * (right + 1) > dividend:
            result = sign * right
        if result > 2147483647:
            return 2147483647
        if result < -2147483648:
            return -2147483648
        return result

mytest = Solution()
dividend = 2
divisor = 2
print mytest.divide(dividend, divisor)
