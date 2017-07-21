class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = {0:0, 1:0, 2:0}
        for i in range(0, len(nums)):
            count[nums[i]] += 1

        nums[0:count[0]] = [0 for i in range(0, count[0])]
        nums[count[0]:(count[1] + count[0])] = [1 for i in range(0, count[1])]
        nums[(count[1] + count[0]):(count[2] + count[1] + count[0])] = [2 for i in range(0, count[2])]
            
