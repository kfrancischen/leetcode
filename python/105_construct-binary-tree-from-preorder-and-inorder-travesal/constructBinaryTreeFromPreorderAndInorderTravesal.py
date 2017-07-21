# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0 or len(preorder) != len(inorder):
            return None
        self.itable = {v:i for i,v in enumerate(inorder) }
        return self.build(preorder, inorder, 0, 0, len(preorder))

    def build(self, preorder, inorder, pstart, istart, size):
        if size == 0:
            return None
        idxInorder = self.itable[preorder[pstart]]
        leftSize = idxInorder - istart
        rightSize = size - leftSize - 1
        tree = TreeNode(preorder[pstart])
        tree.left = self.build(preorder, inorder, pstart + 1, istart, leftSize )
        tree.right = self.build(preorder, inorder, pstart + 1 + leftSize, idxInorder + 1, rightSize )
        return tree

mytest = Solution()
preorder = [1,2,3]
inorder = [2,1,3]
tree = mytest.buildTree(preorder, inorder)
print tree.val
