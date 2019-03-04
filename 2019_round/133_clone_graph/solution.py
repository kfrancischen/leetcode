"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return
        visited = {}
        newNodes = []
        val = node.val
        neighbors = node.neighbors
        root = Node(val, [])
        newNodes.append(root)
        visited[root.val] = 0
        self.dfs(visited, node, root,newNodes)
        return root



    def dfs(self, visited, originalNode, cloneNode, cloneNodes):
        for neighbor in originalNode.neighbors:
            if neighbor.val in visited:
                cloneNode.neighbors.append(cloneNodes[visited[neighbor.val]])
            else:
                newNode = Node(neighbor.val, [])
                cloneNode.neighbors.append(newNode)
                cloneNodes.append(newNode)
                visited[newNode.val] = len(cloneNodes) - 1
                self.dfs(visited, neighbor, cloneNodes[visited[neighbor.val]], cloneNodes)
                
        