from copy import deepcopy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = []
        result = []
        flag = [False] * len(nums)
        self.backTracking(solution, result, nums, flag)
        return result

    def backTracking(self, solution, result, nums,flag):
        if len(solution) == len(nums):
            result.append(deepcopy(solution))
        for i in range(0, len(nums)):
            if flag[i]:
                continue
            solution.append(nums[i])
            flag[i] = True
            self.backTracking(solution, result, nums, flag)
            flag[i] = False
            solution.pop()


mytest = Solution()
nums = [1,2,3]
print mytest.permute(nums)
