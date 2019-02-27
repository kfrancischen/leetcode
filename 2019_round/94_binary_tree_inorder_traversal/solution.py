# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def traversal(root, result):
            if not root:
                return
            traversal(root.left, result)
            result.append(root.val)
            traversal(root.right, result)

        traversal(root, result)
        return result