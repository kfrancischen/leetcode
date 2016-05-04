import copy
class Solution(object):

    def backTracking(self, nums, subset, solution, start):
        subset.append(copy.deepcopy(solution))
        if start == len(nums):
            return
        for i in range(start, len(nums)):
            solution.append(nums[i])
            self.backTracking(nums, subset, solution, i + 1)
            solution.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        nums = sorted(nums)
        subset = []
        solution = []
        self.backTracking(nums, subset, solution, 0)
        return subset




mytest = Solution()
s = [1,2,3]
print mytest.subsets(s)
