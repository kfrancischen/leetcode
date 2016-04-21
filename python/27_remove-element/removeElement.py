class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        nums = nums[:k]
        print nums
        return k


mytest = Solution()

s = [1,1,2,3]
val = 3
print mytest.removeElement(s, val)
