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
        if not head:
            return None

        pointer1, pointer2, pointer1_prev = head, head, None
        while pointer2 and pointer2.next:
            pointer2 = pointer2.next.next
            pointer1_prev = pointer1
            pointer1 = pointer1.next
        if pointer1_prev:
            pointer1_prev.next = None
        cur_node = TreeNode(pointer1.val)
        if pointer1 == head:
            return cur_node
        
        cur_node.left = self.sortedListToBST(head)
        cur_node.right = self.sortedListToBST(pointer1.next)
        return cur_node
        
