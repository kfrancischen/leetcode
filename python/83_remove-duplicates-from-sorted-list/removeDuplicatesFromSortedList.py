# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        pointer_1 = head
        pointer_2 = head.next

        while pointer_2 != None:
            if pointer_2.val != pointer_1.val:
                pointer_1.next = pointer_2
                pointer_1 = pointer_1.next

            pointer_2 = pointer_2.next
        pointer_1.next = None
        return head
