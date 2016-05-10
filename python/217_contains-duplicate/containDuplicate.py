class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        new_nums = list(set(nums))
        if len(new_nums) != len(nums):
            return True
        return False
