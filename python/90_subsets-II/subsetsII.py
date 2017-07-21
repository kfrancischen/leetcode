import copy
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        nums = sorted(nums)
        subset = []
        solution = []
        self.backTracking(nums, solution, subset, 0)

        return subset

    def backTracking(self, nums, solution, subset, start):
        subset.append(copy.deepcopy(solution))
        if start == len(nums):
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            solution.append(nums[i])
            self.backTracking(nums, solution, subset, i + 1)
            solution.pop()



mytest = Solution()
s = [1,2,2]
print mytest.subsetsWithDup(s)
