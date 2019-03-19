# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0
        while root:
            l, r = self.get_height(root.left), self.get_height(root.right)
            if l == r:
                count += 2 ** l
                root = root.right
            else:
                count += 2 ** r
                root = root.left

        return count


    def get_height(self, root):
        h = 0
        while root:
            h += 1
            root = root.left

        return h