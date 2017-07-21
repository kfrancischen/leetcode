class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        if len(citations) == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1

        left = 0
        right = len(citations) - 1
        mid = (left + right) / 2
        while left + 1 < right:
            mid = (left + right) / 2
            if citations[mid] == len(citations) - mid:
                return citations[mid]
            if citations[mid] < len(citations) - mid:
                left = mid
            if citations[mid] > len(citations) - mid:
                right = mid
        if citations[right] == 0:
            return 0
        if citations[left] >= len(citations) - left:
            return len(citations) - left
        else:
            return len(citations) - right

mytest = Solution()
s = [1,2,7,9]
print mytest.hIndex(s)
