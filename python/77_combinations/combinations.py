from copy import deepcopy
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        solution = []
        nums = range(1, n + 1)
        self.backTracking(result, solution, nums, k, 0)
        return result

    def backTracking(self, result, solution, nums, k, start):
        if len(solution) == k:
            result.append(deepcopy(solution))
        if start == len(nums):
            return
        if k - len(solution) > len(nums) - start:
            return
        for i in range(start, len(nums)):
            solution.append(nums[i])
            self.backTracking(result, solution, nums, k, i + 1)
            solution.pop()


mytest = Solution()
n = 20
k = 16
print mytest.combine(n, k)
