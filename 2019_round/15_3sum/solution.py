class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        nums_map = {nums[i]: i for i in range(len(nums))}
        result = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if -nums[i]-nums[j] in nums_map and nums_map[-nums[i]-nums[j]] > i and nums_map[-nums[i]-nums[j]] > j:
                    result.append([nums[i], nums[j], -nums[i]-nums[j]])
                    
        return result
                