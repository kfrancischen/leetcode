class TreeNode:
    def __init__(self, x):
        self.val = x
        self.next = {}

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.map = {}
        self.visited = {}
        for i in range(0, len(equations)):
            m, n = equations[i]
            if m not in self.map:
                self.map[m] = TreeNode(m)
                self.visited[m] = False
            if n not in self.map:
                self.map[n] = TreeNode(n)
                self.visited[n] = False

            self.map[m].next[self.map[n]] = values[i]
            self.map[n].next[self.map[m]] = 1.0 / values[i]
        result = []
        for query in queries:
            result.append(self.dfs(query[0], query[1], 1.0))
        return result

    def dfs(self, start, end, value):
        if start not in self.map or end not in self.map or self.visited[start]:
            return -1.0
        if start == end:
            return value
        self.visited[start] = True
        nextNodes = self.map[start].next.keys()
        f = -1.0
        for nextNode in nextNodes:
            f = self.dfs(nextNode.val, end, value * self.map[start].next[nextNode])
            if f != -1.0:
                break
        self.visited[start] = False
        return f




mytest = Solution()
equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
#queries = [["a", "c"]]
print mytest.calcEquation(equations, values, queries)
