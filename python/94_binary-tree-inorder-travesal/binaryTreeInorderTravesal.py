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
        self.recursionInorder(root, result)
        return result


    def recursionInorder(self, tree, result):
        if tree == None:
            return
        self.recursionInorder(tree.left, result)
        result.append(tree.val)
        self.recursionInorder(tree.right, result)
