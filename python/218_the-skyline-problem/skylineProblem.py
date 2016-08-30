import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        Xs = []
        for l, r, _ in buildings:
            Xs.append(l)
            Xs.append(r)
        Xs.sort()
        result, heap, i = [], [], 0
        for x in Xs:
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)
            while i < len(buildings) and buildings[i][0] == x:
                heapq.heappush(heap, (-buildings[i][2], buildings[i][1]))
                i += 1

            y = 0 if not heap else - heap[0][0]
            if not result or result[-1][1] != y:
                result.append([x,y])
        return result

mytest = Solution()
buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
print mytest.getSkyline(buildings)
