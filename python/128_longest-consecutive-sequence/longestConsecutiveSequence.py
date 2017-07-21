class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        maxLength = 1
        for item in nums:
            if item in dic:
                continue
            left = dic.get(item - 1, 0)
            right = dic.get(item + 1, 0)
            totalLength = left + right + 1
            dic[item] = totalLength
            dic[item - left] = totalLength
            dic[item + right] = totalLength
            maxLength = max(maxLength, dic[item])

        return maxLength

mytest = Solution()
nums = [1,-1,0,3,2]
print mytest.longestConsecutive(nums)
