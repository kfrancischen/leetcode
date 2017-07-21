class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        if not nums:
            return -1

        start = 0;
        end = len(nums)-1
        while start + 1 < end:
            mid = (start+end)/2
            if nums[mid] == target:
                return mid
            if nums[start] <= target < nums[mid]:
                end = mid
            elif nums[mid] < target <= nums[end]:
                start = mid
            elif nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1

mytest = Solution()
s = [4,5,6,7,0,1,2]
target = 6
print mytest.search(s, target)
