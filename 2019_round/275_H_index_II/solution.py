class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        left, right = 0, len(citations) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if citations[mid] <= len(citations) - mid:
                left = mid
            else:
                right = mid
        
        if citations[left] >= len(citations) - left:
            return len(citations) - left
        if citations[right] >= len(citations) - right:
            return len(citations) - right

        return 0


test = Solution()
citations = [0, 1, 3, 5, 6]
print test.hIndex(citations)
