# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.traversal(result, root)
        return result

    def traversal(self, result, root):
        if not root:
            return
        self.traversal(result, root.left)
        self.traversal(result, root.right)
        result.append(root.val)
