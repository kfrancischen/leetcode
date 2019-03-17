from copy import deepcopy
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def backtracking(nums, k, n, solution, result):
            if k == 0:
                if n == 0:
                    result.append(deepcopy(solution))
                else:
                    return

            for i in range(len(nums)):
                solution.append(nums[i])
                backtracking(nums[i+1:], k-1, n-nums[i], solution, result)
                solution.pop()



        nums = range(1, 10)
        result = []
        backtracking(nums, min(k, 9), n, [], result)
        return result


test = Solution()
k = 2
n = 9
print test.combinationSum3(k, n)