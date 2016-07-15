# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        v = self.Aux(root)
        return max(v[0], v[1])

    def Aux(self, node):
        if node == None:
            return [0, 0]
        else:
            l = self.Aux(node.left)
            r = self.Aux(node.right)
            return [node.val + l[1] + r[1], max(l[0], l[1]) + max(r[0], r[1])]
