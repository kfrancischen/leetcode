class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        r = 0
        seen = {0: -1}
        for i, num in enumerate(nums):
            r = (r + num) % k if k else r + num
            if r not in seen: seen[r] = i
            if i - seen[r] > 1: return True
        return False