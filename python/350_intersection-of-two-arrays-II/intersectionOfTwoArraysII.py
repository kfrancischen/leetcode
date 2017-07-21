class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.findIntersect(nums1, nums2)
        else:
            return self.findIntersect(nums2, nums1)

    def findIntersect(self, nums1, nums2):
        result = []
        hashTable_1 = {v:0 for (i,v) in enumerate(nums1)}
        for i in range(0, len(nums1)):
            hashTable_1[nums1[i]] += 1

        for i in range(0, len(nums2)):
            if nums2[i] not in hashTable_1:
                continue
            if hashTable_1[nums2[i]] != 0:
                result.append(nums2[i])
                hashTable_1[nums2[i]] -= 1
        return result
