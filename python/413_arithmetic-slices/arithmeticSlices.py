class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 2:
            return 0
        diff = [A[i] - A[i-1] for i in range(1,len(A))]
        length = 2
        result = 0
        i, j = 0, 1
        while j < len(diff):
            if diff[j] == diff[j-1]:
                length += 1
            else:
                i = j
                length = 2
            if length >= 3:
                result += length - 2
            j += 1

        return result

mytest = Solution()
A = [1,3]
print mytest.numberOfArithmeticSlices(A)
