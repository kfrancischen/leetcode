class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) == 1:
            if target != nums[0]:
                return [-1, -1]
            else:
                return [0, 0]
        start = 0
        end = len(nums) - 1
        left = len(nums) - 1

        if target > nums[end] or target < nums[start]:
            return [-1, -1]

        while start + 1 != end:
            mid = (start + end) / 2
            if target == nums[mid]:
                end = mid
                left = mid
            if nums[mid] < target <= nums[end]:
                start = mid
            elif nums[start] <= target < nums[mid]:
                end = mid

        if target == nums[start] and start < left:
            left = start
        if target == nums[end] and end < left:
            left = end

        start = 0
        end = len(nums) - 1
        right = 0

        while start + 1 != end:

            mid = (start + end) / 2
            if target == nums[mid]:
                start = mid
                right = mid
            if nums[mid] < target <= nums[end]:
                start = mid
            elif nums[start] <= target < nums[mid]:
                end = mid

        if target == nums[start] and start > right:
            right = start
        if target == nums[end] and end > right:
            right = end

        if left > right:
            return [-1,-1]
        return [left, right]

mytest = Solution()
s = [1,3,5,6]
target = 4
print mytest.searchRange(s, target)
