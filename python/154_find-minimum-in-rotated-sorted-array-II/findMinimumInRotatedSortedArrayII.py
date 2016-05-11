class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]


        while left + 1 < right:
            mid = (left + right) / 2
            if nums[mid] > nums[left]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
            elif nums[mid] == nums[left]:
                for j in range(mid, right + 1):
                    if nums[j] != nums[mid]:
                        left = mid
                        break
                    if  j == right:
                        right = mid
                continue
            elif nums[mid] == nums[right]:
                for j in range(0, left + 1):
                    if nums[j] != nums[mid]:
                        right = mid
                        break
                    if j == left:
                        left = mid
                continue

        if nums[left] <= nums[right]:
            return nums[left]
        else:
            return nums[right]

mytest = Solution()
s = [3,3,1,3,3]
print mytest.findMin(s)
