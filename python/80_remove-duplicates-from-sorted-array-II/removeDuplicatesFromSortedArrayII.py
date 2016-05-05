class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        firstPointer = 0
        secondPointer = 1
        length = 1
        while secondPointer < len(nums):
            if nums[secondPointer] != nums[firstPointer]:
                nums[length] = nums[secondPointer]
                length += 1
                firstPointer = secondPointer

            else:
                if secondPointer - firstPointer < 2:
                    nums[length] = nums[secondPointer]
                    length += 1
            secondPointer += 1

        return length



mytest = Solution()
s = [1,1,1,2,5]
print mytest.removeDuplicates(s)
