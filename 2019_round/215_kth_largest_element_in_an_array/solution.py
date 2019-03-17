class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pos = self.partition(nums, 0, len(nums)-1)
        if pos > len(nums) - k:
            return self.findKthLargest(nums[:pos], k-(len(nums)-pos))
        elif pos < len(nums) - k:
            return self.findKthLargest(nums[pos+1:], k)
        else:
            return nums[pos]

    def partition(self, nums, l, r):
        pivot = nums[r]
        lo = l 
        for i in xrange(l, r):
            if nums[i] < pivot:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
        nums[lo], nums[r] = nums[r], nums[lo]
        return lo