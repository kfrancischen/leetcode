class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array_1, array_2 = [nums[0]], [nums[-1]]
        for i in range(1, len(nums)):
            array_1.append(array_1[-1] * nums[i])

        for i in range(len(nums)-2, -1, -1):
            array_2.append(array_2[-1] * nums[i])
        
        array_2 = array_2[::-1]
        
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(array_2[1])
            elif i == len(nums) - 1:
                result.append(array_1[-2])
            else:
                result.append(array_1[i-1] * array_2[i + 1])

        return result

test = Solution()
nums = [1,2,3,4]
print test.productExceptSelf(nums)