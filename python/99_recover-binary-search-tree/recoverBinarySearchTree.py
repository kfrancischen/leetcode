# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.firstElement = None
        self.secondElement = None
        self.prevElement = TreeNode(float('-inf'))
        self.inorderTraversal(root)
        self.firstElement.val, self.secondElement.val = self.secondElement.val, self.firstElement.val


    def inorderTraversal(self, root):
        if not root:
            return
        self.inorderTraversal(root.left)
        if self.firstElement == None and self.prevElement.val >= root.val:
            self.firstElement = self.prevElement

        if self.firstElement != None and self.prevElement.val >= root.val:
            self.secondElement = root

        self.prevElement = root

        self.inorderTraversal(root.right)
