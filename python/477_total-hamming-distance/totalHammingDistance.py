class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(32):
            bit = 0
            for j in range(len(nums)):
                bit += (nums[j] >> i) & 1
            result += bit * (len(nums) - bit)

        return result
            