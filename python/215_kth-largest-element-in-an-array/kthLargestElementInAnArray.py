import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = []
        for i in range(0,k):
            heapq.heappush(result, nums[i])
            i += 1
        while i < len(nums):
            if result[0] < nums[i]:
                heapq.heappushpop(result, nums[i])
            i += 1
        return result[0]

mytest = Solution()
s = [3,2,1,5,6,4]
k = 2
print mytest.findKthLargest(s,k)
