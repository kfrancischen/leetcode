import heapq
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for num in set(nums):
            if len(result) < 3:
                heapq.heappush(result, num)
                continue
            if result[0] < num:
                heapq.heappop(result)
                heapq.heappush(result, num)

        return heapq.heappop(result) if len(result) == 3 else max(result)

mytest = Solution()
nums = [2,2,3,1,4]
print mytest.thirdMax(nums)
