class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        patch, missing, i = 0, 1 , 0
        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                missing += missing
                patch += 1
        return patch


mytest = Solution()
nums = [1,2,4,13,43]
n = 100
print mytest.minPatches(nums, n)
