from copy import deepcopy
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def back_tracking(nums, solution, result):
            result.append(deepcopy(solution))
            for i in range(len(nums)):
                solution.append(nums[i])
                back_tracking(nums[i+1:], solution, result)
                solution.pop()

        result = []
        back_tracking(nums, [], result)
        return result



nums = [1, 2, 3]
test = Solution()
print test.subsets(nums)