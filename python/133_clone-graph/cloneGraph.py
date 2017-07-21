# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return
        visited = {}
        newNodes = []
        label = node.label
        neighbors = node.neighbors
        root = UndirectedGraphNode(label)
        newNodes.append(root)
        visited[root.label] = 0
        self.dfs(visited, node, root,newNodes)
        return root



    def dfs(self, visited, originalNode, cloneNode, cloneNodes):
        for neighbor in originalNode.neighbors:
            if neighbor.label in visited:
                cloneNode.neighbors.append(cloneNodes[visited[neighbor.label]])
            else:
                newNode = UndirectedGraphNode(neighbor.label)
                cloneNode.neighbors.append(newNode)
                cloneNodes.append(newNode)
                visited[newNode.label] = len(cloneNodes) - 1
                self.dfs(visited, neighbor, cloneNodes[visited[neighbor.label]], cloneNodes)
