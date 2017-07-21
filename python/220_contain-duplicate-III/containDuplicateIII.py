class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        dict = {}
        for i in range(0, len(nums)):
            ratio = nums[i] / (t + 1)
            if ratio in dict and abs(dict[ratio][0] - i) <= k:
                return True
            elif ratio - 1 in dict and abs(dict[ratio - 1][1] - nums[i]) <= t and abs(dict[ratio - 1][0] - i) <= k:
                return True
            elif ratio + 1 in dict and abs(dict[ratio + 1][1] - nums[i]) <= t and abs(dict[ratio + 1][0] - i) <= k:
                return True
            dict[ratio] = [i,nums[i]]
        return False

mytest = Solution()
nums = [1,3,1]
k = 1
t = 1
print mytest.containsNearbyAlmostDuplicate(nums, k, t)
