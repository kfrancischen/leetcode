class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) / 2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid] < nums[mid-1] and nums[mid] < nums[mid + 1]:
                left = mid
            elif nums[mid-1] < nums[mid] < nums[mid+1]:
                left = mid
            elif nums[mid-1] > nums[mid] > nums[mid+1]:
                right = mid

        if nums[left] > nums[right]:
            return left
        else:
            return right

mytest = Solution()
s = [1]
print mytest.findPeakElement(s)
