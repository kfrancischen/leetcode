class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2:
            return False
        return self.backTracking(nums, 0, 0, sum(nums))


    def backTracking(self, nums, start, summation, total):
        if summation * 2 == total:
            return True
        if summation * 2 > total or start == len(nums):
            return False
        for i in range(start, len(nums)):
            if self.backTracking(nums, i + 1, summation + nums[i], total):
                return True

        return False



mytest = Solution()
s = [1, 2,3,5]
print mytest.canPartition(s)
