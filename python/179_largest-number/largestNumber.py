class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        nums.sort(cmp = lambda x, y: cmp(x + y, y + x), reverse = True)
        print nums
        return '0' if nums[0] == '0' else ''.join(nums)

mytest = Solution()
nums = [3, 30, 34, 5, 9]
print mytest.largestNumber(nums)
