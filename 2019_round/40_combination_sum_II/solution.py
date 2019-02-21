from copy import deepcopy
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def back_tracking(candidates, one_solution, result, remaining):
            if remaining == 0:
                result.append(deepcopy(one_solution))
            if remaining < 0 or len(candidates) == 0:
                return

            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                one_solution.append(candidates[i])
                back_tracking(candidates[i+1:], one_solution, result, remaining - candidates[i])
                one_solution.pop()
            
        candidates = sorted(candidates)
        one_solution = []
        result = []
        back_tracking(candidates, one_solution, result, target)
        return result


test = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(test.combinationSum2(candidates=candidates, target=target))
candidates = [2,5,2,1,2]
target = 5
print(test.combinationSum2(candidates=candidates, target=target))
