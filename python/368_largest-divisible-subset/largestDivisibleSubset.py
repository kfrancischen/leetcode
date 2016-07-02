from copy import copy
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        if not nums:
            return []
        possibleArray = [0] * len(nums)
        possibleArray[0] = [nums[0]]
        for i in range(1, len(nums)):
            maxSet = []
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    localSet = copy(possibleArray[j])
                    if len(localSet) > len(maxSet):
                        maxSet = localSet
            maxSet.append(nums[i])
            possibleArray[i] = maxSet

        result = []
        for localSet in possibleArray:
            if len(localSet) > len(result):
                result = localSet

        return result

mytest = Solution()
nums = [1,2,3,4]
print mytest.largestDivisibleSubset(nums)
