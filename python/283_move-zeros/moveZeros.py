class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                continue
            nums[pointer] = nums[i]
            pointer += 1

        nums[pointer:len(nums)] = [0] * (len(nums) - pointer)
        
