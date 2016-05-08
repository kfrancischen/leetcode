import copy
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp = copy.deepcopy(nums[len(nums) - k:])
        nums[k:] = copy.deepcopy(nums[:len(nums)-k])
        nums[:k] = temp


mytest = Solution()
s = [1,2,3,4,5]
k = 2
mytest.rotate(s, k)
