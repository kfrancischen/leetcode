class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        itable = {}
        for i in range(0, len(nums)):
            if nums[i] not in itable:
                itable[nums[i]] = i
            else:
                if i - itable[nums[i]] <= k:
                    return True
                itable[nums[i]] = i

        return False
