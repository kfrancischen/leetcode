class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        end = nums[0]
        start = 0
        step = 1
        maxDis = nums[0]
        while end < len(nums) - 1:
            for i in range(start + 1, end + 1):
                maxDis = max(maxDis, nums[i] + i)
            start = end
            end = maxDis
            step += 1
        return step

mytest = Solution()
nums = [2,3,1,1,4]
print mytest.jump(nums)
