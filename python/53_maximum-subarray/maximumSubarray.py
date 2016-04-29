class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            sum = sum + nums[i]
            sum = max(sum, nums[i])
            maximum = max(maximum, sum)
            print sum, maximum

        return maximum


mytest = Solution()
s = [-2,1,-3,4,-1,2,1,-5,4]
#s = [-2,-1]
print mytest.maxSubArray(s)
