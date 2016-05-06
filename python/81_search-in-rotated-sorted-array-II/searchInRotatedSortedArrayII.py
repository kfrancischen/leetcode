class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            if nums[0] == target:
                return True
            else:
                return False

        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return True
            elif nums[left] <= target < nums[mid]:
                right = mid
            elif nums[right] >= target > nums[mid]:
                left = mid

            elif nums[right] < nums[mid]:
                left = mid
            elif nums[right] > nums[mid]:
                right = mid
            elif nums[right] == nums[mid]:
                for i in range(mid, right + 1):
                    if nums[i] == target:
                        return True
                right = mid

        if nums[left] == target or nums[right] == target:
            return True
        return False

mytest = Solution()
s = [3,1,1]
target = 3
print mytest.search(s, target)
