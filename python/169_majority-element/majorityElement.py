class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = {}
        for i in range(0, len(nums)):
            if nums[i] not in table.keys():
                table[nums[i]] = 1
            else:
                table[nums[i]] += 1
            if table[nums[i]] > len(nums) / 2:
                return nums[i]


mytest = Solution()
s = [6,5,5]
print mytest.majorityElement(s)
