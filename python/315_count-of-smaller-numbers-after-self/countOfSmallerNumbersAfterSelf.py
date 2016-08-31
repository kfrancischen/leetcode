class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        sortArray = []
        for i in range(len(nums) - 1, -1, -1):
            index = self.findIndex(sortArray, nums[i])
            result.append(index)
            sortArray.insert(index, nums[i])
        result.reverse()
        return result

    def findIndex(self, sortArray, target):
        if not sortArray:
            return 0
        left = 0
        right = len(sortArray) - 1
        if sortArray[-1] < target:
            return len(sortArray)

        while left + 1< right:
            mid = (left + right) / 2
            if sortArray[mid] < target:
                left = mid + 1
            else:
                right = mid
        if sortArray[left] >= target:
            return left
        return right


mytest = Solution()
s = [5,2,3,6,1]
print mytest.countSmaller(s)
