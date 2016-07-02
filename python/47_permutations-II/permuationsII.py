from copy import deepcopy
from collections import Counter
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = []
        result = []
        nums = sorted(nums)
        flag = Counter(nums)
        self.backTracking(solution, result, nums, flag)
        return result

    def backTracking(self, solution, result, nums,flag):
        if len(solution) == len(nums):
            result.append(deepcopy(solution))
        for val in flag.keys():
            if flag[val] <= 0:
                continue
            solution.append(val)
            flag[val] -= 1
            self.backTracking(solution, result, nums, flag)
            flag[val] += 1
            solution.pop()

mytest = Solution()
nums = [1,2,1,1]
print mytest.permuteUnique(nums)
