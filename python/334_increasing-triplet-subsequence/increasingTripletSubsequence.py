class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min = float('inf')
        secondMin = float('inf')
        for num in nums:
            if num <= min:
                min = num
            elif num < secondMin:
                secondMin = num
            elif num > secondMin:
                return True
        return False

mytest = Solution()
nums = [1,2,6,5,4,2,1,-1,3]
print mytest.increasingTriplet(nums)
