from copy import deepcopy
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_vals = {}
        for val in nums:
            if val in num_vals:
                num_vals[val] += 1
            else:
                num_vals[val] = 1

        def back_tracking(num_vals, result, one_solution):
            if sum([num_vals[key] for key in num_vals]) == 0:
                result.append(deepcopy(one_solution))

            for key in num_vals:
                if num_vals[key] == 0:
                    continue
                num_vals[key] -= 1
                one_solution.append(key)
                back_tracking(num_vals, result, one_solution)
                num_vals[key] += 1
                one_solution.pop()

        result = []
        one_solution = []
        back_tracking(num_vals, result, one_solution)
        return result


test = Solution()
nums = [1, 1, 2]
print(test.permuteUnique(nums))