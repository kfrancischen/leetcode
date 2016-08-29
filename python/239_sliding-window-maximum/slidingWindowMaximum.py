from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d.append(i)
            if d[0] == i-k:
                d.popleft()
            if i >= k - 1:
                out.append(nums[d[0]])
        return out

mytest = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print mytest.maxSlidingWindow(nums, k)
