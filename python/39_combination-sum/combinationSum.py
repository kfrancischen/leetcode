import copy
class Solution(object):

    def findList(self, list, target, solution, results, index):
        if target < 0:
            return
        elif target == 0:
            results.append(copy.deepcopy(solution))
            return

        for i in range(index, len(list)):
            solution.append(list[i])
            self.findList(list, target - list[i], solution, results, i)
            solution.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        results = []
        solution = []
        self.findList(candidates, target, solution, results, 0)
        return results



mytest = Solution()
s = [2,3,6,7]
target = 7
print mytest.combinationSum(s, target)
