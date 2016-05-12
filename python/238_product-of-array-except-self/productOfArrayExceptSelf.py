class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]
        product = 1
        for i in range(len(nums)-2, -1, -1):
            product = nums[i+1] * product
            output[i] = output[i] * product

        return output

mytest = Solution()
s = [1,2,3,4,4]
print mytest.productExceptSelf(s)
