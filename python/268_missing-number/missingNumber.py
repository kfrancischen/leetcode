class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expectSum = (n + 1) * n / 2
        sum = 0
        for i in range(0, n):
            sum = sum + nums[i]

        return expectSum - sum


mytest = Solution()
s = [1,2,3]
print mytest.missingNumber(s)
