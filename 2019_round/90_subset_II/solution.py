from copy import deepcopy
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def back_tracking(nums, start, solution, result):
            result.append(deepcopy(solution))
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                solution.append(nums[i])
                back_tracking(nums, i+1, solution, result)
                solution.pop()
        nums = sorted(nums)
        result = []
        back_tracking(nums, 0, [], result)
        return result
                