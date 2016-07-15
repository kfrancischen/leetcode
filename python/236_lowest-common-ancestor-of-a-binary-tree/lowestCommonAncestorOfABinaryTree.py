# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from copy import deepcopy
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [(root,[])]
        pathp = []
        pathq = []
        count = 0
        while stack:
            node, parentList = stack.pop()
            if node == p:
                pathp = parentList + [p]
                count += 1
            if node == q:
                pathq = parentList + [q]
                count += 1

            if count == 2:
                break

            if node.left:
                stack.append((node.left, parentList + [node]))
            if node.right:
                stack.append((node.right, parentList+ [node]))

        for node1 in reversed(pathp):
            for node2 in reversed(pathq):
                if node1 == node2:
                    return node1
