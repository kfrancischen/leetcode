# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        newHead = ListNode(0)
        newHead.next = head
        pointer_1 = newHead
        pointer_2 = newHead.next
        while pointer_2 != None:
            if pointer_2.val != val:
                pointer_1 = pointer_1.next
                pointer_2 = pointer_2.next
            else:
                pointer_2 = pointer_2.next
                pointer_1.next = pointer_2
        return newHead.next
