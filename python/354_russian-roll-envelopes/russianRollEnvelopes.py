class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        n = len(envelopes)
        if n == 1:
            return 1
        envelopes.sort(cmp = lambda x,y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])

        width = [e[1] for e in envelopes]
        result = self.longestSubsequence(width)
        return result

    def longestSubsequence(self, nums):
        if not nums:
            return 0
        result = []
        for num in nums:
            pos = self.binarySearch(num, result)
            if pos >= len(result):
                result.append(num)
            else:
                result[pos] = num

        return len(result)

    def binarySearch(self, target, nums):
        if not nums:
            return 0

        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start


mytest = Solution()
s = [[5,4],[6,4],[6,7],[2,3]]
print mytest.maxEnvelopes(s)
