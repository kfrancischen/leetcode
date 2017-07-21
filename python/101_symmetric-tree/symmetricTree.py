# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.checkNodes(root.left, root.right)

    def checkNodes(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        else:
            if node1.val != node2.val:
                return False
            else:
                return self.checkNodes(node1.left, node2.right) \
                    and self.checkNodes(node1.right, node2.left)
