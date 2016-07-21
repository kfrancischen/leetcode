class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        info = [[] for i in range(0, n)]
        for i,j in edges:
            info[i].append(j)
            info[j].append(i)
        leaves = [i for i in range(0, n) if len(info[i]) == 1]
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for leave in leaves:
                parent = info[leave].pop()
                info[parent].remove(leave)
                if len(info[parent]) == 1:
                    newLeaves.append(parent)
            leaves = newLeaves
        return leaves

mytest = Solution()
n = 4
edges = [[1,0],[1,2],[1,3]]
print mytest.findMinHeightTrees(n, edges)
