# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        isSame = True
        if not p and not q:
            return isSame
        if not p and q != None:
            isSame = False
        elif not q and p != None:
            isSame = False
        elif q.val != p.val:
            isSame = False
        elif q.val == p.val:
            isSame = (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))
        return isSame
