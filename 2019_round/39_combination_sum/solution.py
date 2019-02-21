from copy import deepcopy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def back_tracking(candidates, solution, result, remaining):
            if remaining < 0 or len(candidates) == 0:
                return
            if remaining == 0:
                result.append(deepcopy(solution))

            for i in range(len(candidates)):
                one_solution.append(candidates[i])
                back_tracking(candidates[i:], one_solution, result, remaining - candidates[i])
                one_solution.pop()
            
        candidates = sorted(candidates)
        one_solution = []
        result = []
        back_tracking(candidates, one_solution, result, target)
        return result


test = Solution()
candidates = [2, 3, 5]
target = 8
print(test.combinationSum(candidates=candidates, target=target))
        