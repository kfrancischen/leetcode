class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) <= len(nums2):
            return self.helper(nums1, nums2)
        else:
            return self.helper(nums2, nums1)

    def helper(self, nums1, nums2):
        hashTable = {v:i for (i,v) in enumerate(nums2)}
        newNums1 = list(set(nums1))
        result = []
        for i in range(0, len(newNums1)):
            if newNums1[i] in hashTable:
                result.append(newNums1[i])
        return result

mytest = Solution()
s = [2,1]
t = [1,1]
print mytest.intersection(s,t)
