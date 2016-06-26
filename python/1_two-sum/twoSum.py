class Solution(object):
	def twoSum(self, nums, target):
		lengthOfNums = len(nums)
		if lengthOfNums < 2:
			return
		else:
			for firstPointer in range(0, lengthOfNums):
				for secondPointer in range(firstPointer + 1, lengthOfNums):
					if nums[firstPointer] + nums[secondPointer] == target:
						return [firstPointer, secondPointer]
			
			if firstPointer == lengthOfNums and secondPointer == lengthOfNums:
				return

mytest = Solution()
print mytest.twoSum([1,2,3],3)
print mytest.twoSum([3,2,1],3)
