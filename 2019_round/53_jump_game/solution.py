class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur_max = nums[0]
        for i in range(1, len(nums)):
            if cur_max >= len(nums)-1:
                return True
            if i > cur_max:
                return False
            cur_max = max(cur_max, nums[i] + i)

        return True


test = Solution()
nums = [2, 3, 1, 1, 4]
print test.canJump(nums)