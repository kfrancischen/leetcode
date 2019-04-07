class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations = sorted(citations, reverse=True)
        h_index = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h_index = i + 1
            else:
                break
        return h_index


    
test = Solution()
citations = [1, 2]
print test.hIndex(citations)
