# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.table = {v:i for (i, v) in enumerate(inorder)}
        postorder.reverse()
        return self.build(inorder, postorder, 0, 0, len(postorder))

    def build(self, inorder, preorder, istart, pstart, size):
        if size == 0:
            return None
        idxInorder = self.table[preorder[pstart]]
        leftSize = idxInorder - istart
        rightSize = size - leftSize - 1
        tree = TreeNode(preorder[pstart])
        tree.left = self.build(inorder, preorder, istart, pstart + rightSize + 1, leftSize)
        tree.right = self.build(inorder, preorder, idxInorder + 1, pstart + 1, rightSize)
        return tree