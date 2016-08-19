from copy import deepcopy
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        buckets = {i:[] for i in range(0, 10)}
        n = len(nums)
        maxLen = 0
        for num in nums:
            maxLen = max(len(str(num)), maxLen)
        count = 0
        while count < maxLen:
            newNums = []
            for num in nums:
                toString = str(num)[::-1]
                if len(toString) > count:
                    buckets[int(toString[count])].append(num)
                else:
                    buckets[0].append(num)

            for key in buckets.keys():
                newNums.extend(buckets[key])
                buckets[key] = []
            nums = deepcopy(newNums)
            count += 1

        return max(nums[i] - nums[i-1] for i in range(1, len(nums)))


mytest = Solution()
nums = [2,3,100,1,4]
print mytest.maximumGap(nums)
