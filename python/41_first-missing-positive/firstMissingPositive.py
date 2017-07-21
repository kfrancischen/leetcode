class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        if len(nums) == 1:
            if nums[0] == 1:
                return 2
            else
                return 1
        i = 0
        while i < len(nums):
            value = nums[i]
            if value <= 0 or value > len(nums) or value == i+1:
                i += 1
                continue

            nums[value - 1], nums[i] = nums[i], nums[value - 1]
            if nums[i] != nums[value - 1]:
                i -= 1
            i += 1
        for i in range(0, len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


mytest = Solution()
s = [3]
print mytest.firstMissingPositive(s)
