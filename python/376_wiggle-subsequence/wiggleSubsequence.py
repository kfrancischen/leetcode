class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        trend = (nums[1] - nums[0] > 0)
        result = 2
        for i in range(2, len(nums)):
            if trend == False and nums[i] > nums[i - 1]:
                result +=1
                trend = True
            elif trend == True and nums[i] < nums[i - 1]:
                result += 1
                trend = False

        return result


mytest = Solution()
nums = [1,2,3,4,5,6,7,8,9]
print mytest.wiggleMaxLength(nums)
