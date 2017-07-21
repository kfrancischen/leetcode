class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        hashTable = {}
        outputTable = {}
        output = []
        for i in range(0, len(nums)):
            hashTable[nums[i]] = i

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                num_1 = nums[i]
                num_2 = nums[j]
                target = -num_1 - num_2
                if hashTable.get(target) == None or hashTable.get(target) <= max(i,j):
                    continue

                newResult = [num_1, num_2, target]
                if outputTable.get(tuple(newResult)) == None:
                    outputTable[tuple(newResult)] = 1
                    output.append(newResult)


        return output


mytest = Solution();
nums = [1,2,1,-2]
print mytest.threeSum(nums)
