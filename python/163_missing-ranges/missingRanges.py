class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        if not nums:
            return [str(lower) + '->' + str(upper)] if lower != upper else [str(lower)]
        if lower < nums[0]:
            string = str(lower) + '->' + str(nums[0] - 1) if nums[0] - 1 != lower else str(lower)
            result.append(string)
        for i in range(len(nums)):
            if nums[i] < lower or nums[i] > upper:
                continue
            string = ''
            if i > 0 and nums[i-1] < lower < nums[i]:
                string += str(lower) + '->' + str(nums[i] - 1) if nums[i] - 1 != lower else str(lower)
            elif i < len(nums) - 1 and nums[i] < upper < nums[i+1]:
                string += str(nums[i] + 1) + '->' + str(upper) if nums[i] + 1 != upper else str(upper)
            elif i > 0 and nums[i] - nums[i-1] > 1:
                string += str(nums[i-1] + 1) + '->' + str(nums[i] - 1) if nums[i] - nums[i-1] > 2 else str(nums[i] - 1)
            if len(string) > 0:
                result.append(string)
        if upper > nums[-1]:
            string = str(nums[-1] + 1) + '->' + str(upper) if nums[-1] + 1 != upper else str(upper)
            result.append(string)
        return result