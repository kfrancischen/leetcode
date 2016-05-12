import copy
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        solution = []
        array = [i for i in range(1,10)]

        if k > 0 or n > 0:
            self.backTracking(array, result, solution, n, k, 0)
        return result


    def backTracking(self, array, result, solution, n, k, start):
        if k == 0 and n == 0:
            result.append(copy.deepcopy(solution))
        if k == 0 and n != 0:
            return
        if n < 0 or start >= len(array):
            return

        for i in range(start, len(array)):
            solution.append(array[i])
            self.backTracking(array, result, solution, n - array[i], k - 1, i + 1)
            solution.pop()

mytest = Solution()
k = 3
n = 10
print mytest.combinationSum3(k, n)
