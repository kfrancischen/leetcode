class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2:
            return nums[1]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if nums[mid] < nums[left] and nums[mid] < nums[right]:
                return nums[mid]
            if nums[mid] > nums[left]:
                left = mid
            if nums[mid] < nums[right]:
                right = mid

        return nums[left]