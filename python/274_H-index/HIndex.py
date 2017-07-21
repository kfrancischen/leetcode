class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0

        citations = sorted(citations)
        index = range(len(citations), 0, -1)
        for i in range(0, len(citations) - 1):
            if citations[i] < index[i] and citations[i+1] >= index[i+1]:
                return index[i+1]
        if citations[len(citations) - 1] < 1:
            return 0
        return len(citations)


mytest = Solution()
s = [0,3,5,6,1]
print mytest.hIndex(s)
