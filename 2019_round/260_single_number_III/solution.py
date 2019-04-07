class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0, 0]
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]

        bit = xor & ~(xor - 1)
        for num in nums:
            if num & bit > 0:
                result[0] ^= num
            else:
                result[1] ^= num

        return result

test = Solution()
s = [1,2,1,3,2,5]
print test.singleNumber(s)
