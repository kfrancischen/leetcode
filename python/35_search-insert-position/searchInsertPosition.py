class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or target <= nums[0]:
            return 0
        if target > nums[len(nums) - 1]:
            return len(nums)

        start = 0
        end = len(nums) - 1

        while start + 1 != end:

            mid = (start + end) / 2
            if target == nums[mid]:
                return mid
            if nums[start] <= target < nums[mid]:
                end = mid
            if nums[end] >= target > nums[mid]:
                start = mid

        if nums[start] < target <= nums[end]:
            return end
        if target == nums[start]:
            return start

mytest = Solution()
s = [1,3,5,6]
target = 2
print mytest.searchInsert(s, target)
