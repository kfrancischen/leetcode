
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum, mask = 0, 0
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            hashTable = {}
            for num in nums:
                hashTable[num & mask] = 1

            temp = maximum | (1 << i)
            for prefix in hashTable:
                if temp ^ prefix in hashTable:
                    maximum = temp
                    break


        return maximum
