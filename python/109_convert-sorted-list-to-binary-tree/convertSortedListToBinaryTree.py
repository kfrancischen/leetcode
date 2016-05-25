# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        pointer = head
        values = []
        while pointer != None:
            values.append(pointer.val)
            pointer = pointer.next

        root = self.buildTree(values)
        return root

    def buildTree(self, list):
        n = len(list)
        if n == 0:
            return
        pivot = n/2 if n%2 == 1 else n/2-1

        root = TreeNode(list[pivot])
        if pivot > 0:
            root.left = self.buildTree(list[0:pivot])
        if pivot < n - 1:
            root.right = self.buildTree(list[pivot+1:n])
        return root
