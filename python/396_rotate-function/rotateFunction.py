class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        basic = 0
        n = len(A)
        for i in range(n):
            basic += i * A[i]
        val = basic
        maxVal = val
        summation = sum(A)
        for i in range(n-1,0,-1):
            val = val + summation - n * A[i]
            maxVal = max(maxVal, val)

        return maxVal
