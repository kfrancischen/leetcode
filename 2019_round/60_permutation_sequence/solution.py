import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = range(1, n+1)
        result = ''
        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            result += str(nums[index])
            nums.remove(nums[index])

        return result

test = Solution()
n = 5
k = 4
print test.getPermutation(n, k)