import copy
class Solution(object):

    def findList(self, list, target, solution, results, index):
        if target < 0:
            return
        elif target == 0:
            results.append(copy.deepcopy(solution))
            return

        for i in range(index, len(list)):
            if i > index and list[i] == list[i-1]:
                continue

            solution.append(list[i])
            self.findList(list, target - list[i], solution, results, i+1)
            solution.pop()

    def combinationSum2(self, candidates, target):
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
s = [10,1,2,7,6,1,5]
target = 8
print mytest.combinationSum2(s, target)
