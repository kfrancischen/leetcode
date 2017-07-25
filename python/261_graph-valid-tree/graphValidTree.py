class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        dic = {i: set() for i in xrange(n)}
        for i, j in edges:
            dic[i].add(j)
            dic[j].add(i)
        visited = set()
        queue = collections.deque([dic.keys()[0]])
        while queue:
            node = queue.popleft()
            if node in visited:
                return False
            visited.add(node)
            for neighbour in dic[node]:
                queue.append(neighbour)
                dic[neighbour].remove(node)
            dic.pop(node)
        return not dic