# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.preorder(root, result)
        return result

    def preorder(self, root, result):
        if root == None:
            return
        result.append(root.val)
        self.preorder(root.left, result)
        self.preorder(root.right,result)
