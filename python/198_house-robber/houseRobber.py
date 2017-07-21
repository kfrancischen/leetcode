class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        money = [0] * len(nums)
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            money[i] = max(money[i - 2] + nums[i], money[i - 1])

        return money[len(nums) - 1]

mytest = Solution()
nums = [2,3,4,2,3,5]
print mytest.rob(nums)
