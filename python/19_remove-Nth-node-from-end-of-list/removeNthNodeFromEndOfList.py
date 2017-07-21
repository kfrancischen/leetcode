# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import copy
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None and n == 1:
            return None
        pointer_1 = head.next
        pointer_2 = head
        for i in range(0, n):
            pointer_1 = pointer_1.next
            if pointer_1 == None and i!= n - 1:
                return head.next

        while pointer_1 != None:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next

        deletedNode = pointer_2.next
        pointer_2.next = deletedNode.next

        return head
