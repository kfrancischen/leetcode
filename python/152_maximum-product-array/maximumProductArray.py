class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxProd = nums[0]
        minProd = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                maxProd = max(maxProd * nums[i], nums[i])
                minProd = min(minProd * nums[i], nums[i])
            else:
                temp = maxProd
                maxProd = max(minProd * nums[i], nums[i])
                minProd = min(temp * nums[i], nums[i])
            result = max(maxProd, result)

        return result

mytest = Solution()
s = [-4, -3, -2]
print mytest.maxProduct(s)
