# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.convertToBST(nums)

    def convertToBST(self, nums):
        if not nums:
            return None
        mid = (len(nums) - 1) / 2
        root = TreeNode(nums[mid])
        root.left = self.convertToBST(nums[:mid])
        root.right = self.convertToBST(nums[mid + 1:])
        return root
