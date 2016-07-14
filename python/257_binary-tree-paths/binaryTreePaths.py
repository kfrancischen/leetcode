# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result = []

        if not root:
            return []
        if root.left == None and root.right == None:
            return [str(root.val)]
        path = str(root.val)
        self.dfs(root.left, result, path)
        self.dfs(root.right, result, path)

        return result

    def dfs(self, root, result, path):
        if not root:
            return
        if root.left == None and root.right == None:
            path += '->' + str(root.val)
            result.append(path)
            return
        else:
            self.dfs(root.left, result, path + '->' + str(root.val))
            self.dfs(root.right, result, path + '->' + str(root.val))
