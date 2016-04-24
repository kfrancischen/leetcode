class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        left = len(nums) - 2
        while left >= 0:
            if nums[left] >= nums[left + 1]:
                left -= 1
            else:
                for pivot in range(left+1, len(nums)):
                    if nums[pivot - 1] > nums[left] and nums[pivot] <= nums[left]:
                        pivot -= 1
                        break
                print pivot
                nums[pivot], nums[left] = nums[left], nums[pivot]
                nums[left + 1:] = list(reversed(nums[left + 1:]))
                return

        if left == -1:
            nums.reverse()


mytest = Solution()
s = [3,2,1]
mytest.nextPermutation(s)
print s
