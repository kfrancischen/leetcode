from copy import deepcopy
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def back_tracking(cur_n, n, solution, result, k):
            if k == 0:
                result.append(deepcopy(solution))
                return
            for i in range(cur_n, n+1):
                solution.append(i)
                back_tracking(i+1, n, solution, result, k-1)
                solution.pop()

        result = []
        back_tracking(1, n, [], result, k)
        return result


test = Solution()
n = 4
k = 2
print test.combine(4, 2)
