class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        p1, p2 = 0, 0
        cur_sum = 0
        min_len = len(nums) + 1
        while p2 < len(nums):
            cur_sum += nums[p2]
            p2 += 1
            while cur_sum - nums[p1] >= s:
                cur_sum -= nums[p1]
                p1 += 1

            if cur_sum >= s:
                min_len = min(min_len, p2 - p1)

        return min_len if min_len < len(nums) + 1 else 0
            

test = Solution()
s = 1000
nums = [2, 3, 1, 2, 4, 3]
print test.minSubArrayLen(s, nums)
