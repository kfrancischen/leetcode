class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        k = 1
        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[k] = nums[i+1]
                k += 1

        nums = nums[0:k]

        print nums
        return k


mytest = Solution()
s = [1,1,2]
print mytest.removeDuplicates(s)
