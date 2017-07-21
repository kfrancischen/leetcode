class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True

        if len(nums) == 0 or nums[0] == 0:
            return False

        sum = 0
        for i in range(0, len(nums)):
            if sum < i:
                return False
            if sum >= len(nums) - 1:
                return True
            sum = max(sum, i + nums[i])


mytest = Solution()
s = [9,5,3,2,1,0,2,3,3,1,0,0]
print mytest.canJump(s)
