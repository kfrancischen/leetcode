class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        info = [[] for _ in range(n)]
        for i, j in edges:
            info[i].append(j)
            info[j].append(i)

        leaves = [i for i in range(n) if len(info[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leave in leaves:
                parent = info[leave].pop()
                info[parent].remove(leave)
                if len(info[parent]) == 1:
                    new_leaves.append(parent)

            leaves = new_leaves
        return leaves

test = Solution()
n = 4
edges = [[1,0],[1,2],[1,3]]
print test.findMinHeightTrees(n, edges)