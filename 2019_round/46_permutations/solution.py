from copy import deepcopy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def back_tracking(nums, result, one_solution):
            if len(nums) == 0:
                result.append(deepcopy(one_solution))

            for i in range(len(nums)):
                one_solution.append(nums[i])
                back_tracking(nums[:i] + nums[i+1:], result, one_solution)
                one_solution.pop()

        result = []
        one_solution = []
        back_tracking(nums, result, one_solution)
        return result


nums = [1, 2, 3]
test = Solution()
print(test.permute(nums))