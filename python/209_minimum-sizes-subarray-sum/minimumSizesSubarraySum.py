class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            if nums[0] < s:
                return 0
            else:
                return 1

        left = 0
        right = 1
        currentSum = nums[0]
        currentLen = 1
        minLen = len(nums)
        if currentSum >= s:
            return 1
        while right < len(nums):
            currentSum = currentSum + nums[right]
            currentLen += 1

            while left < right:
                if currentSum >= s and currentSum - nums[left] >= s:
                    currentSum = currentSum - nums[left]
                    left += 1
                    currentLen -= 1
                else:
                    break
                    
            if currentSum >= s:
                minLen = min(minLen, currentLen)

            right += 1

        if currentSum < s:
            return 0
        for i in range(left, len(nums)):
            if currentSum - nums[i] < s:
                break
            currentSum = currentSum - nums[i]
            minLen -= 1

        return minLen

mytest = Solution()
s = [1,4,4]
sum = 4
print mytest.minSubArrayLen(sum, s)
