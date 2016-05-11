class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
            
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]

        while left + 1 < right:
            mid = (left + right) / 2
            if nums[mid] > nums[left]:
                left = mid
            if nums[mid] < nums[right]:
                right = mid
        if nums[left] < nums[mid]:
            mid = left
        if nums[right] < nums[mid]:
            mid = right

        return nums[mid]


mytest = Solution()
s = [4,6,7,2,3]
print mytest.findMin(s)
