class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        if not nums or nums[0] > target:
            return 0
        solution = [0] * (target + 1)
        visited = [False] * (target + 1)
        for i in range(0, len(nums)):
            if nums[i] <= target:
                solution[nums[i]] = 1
        return self.totalSolution(nums, target, visited, solution)

    def totalSolution(self, nums, target, visited, solution):
        if target <= 0 :
            return 0
        if visited[target] == False:
            for num in nums:
                solution[target] += self.totalSolution(nums, target - num, visited, solution)
        visited[target] = True
        return solution[target]


mytest = Solution()
nums = [4,2,1]
target = 32
print mytest.combinationSum4(nums, target)
