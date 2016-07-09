# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from copy import deepcopy
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        stack = []
        if not root:
            return result
        stack.append(root)
        result.append([root.val])
        nodesNextLevel = []
        valNextLevel = []
        count = 1
        while stack:
            node = stack.pop(0)
            count -= 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if count == 0:
                valNextLevel = [x.val for x in stack]
                result += [valNextLevel] if valNextLevel else []
                count = len(stack)
        return result
