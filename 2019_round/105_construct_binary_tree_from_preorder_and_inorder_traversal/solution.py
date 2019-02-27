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
        if len(preorder) == 0:
            return None

        
        cur_root = TreeNode(preorder[0])
        
        inorder_pos = 0
        while inorder_pos < len(inorder):
            if inorder[inorder_pos] == preorder[0]:
                break
            inorder_pos += 1

        cur_root.left = self.buildTree(preorder[1:inorder_pos+1], inorder[:inorder_pos])
        cur_root.right = self.buildTree(preorder[inorder_pos+1:], inorder[inorder_pos+1:])
            
        return cur_root
    