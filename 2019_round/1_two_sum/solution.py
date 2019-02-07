class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        val_to_index_map = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            if target - nums[i] in val_to_index_map and val_to_index_map[target - nums[i]] != i:
                return [i, val_to_index_map[target - nums[i]]]
