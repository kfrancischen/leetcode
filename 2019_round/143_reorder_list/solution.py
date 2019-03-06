# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        p1 = head 
        p2 = head
        while p2.next != None and p2.next.next != None:
            p1 = p1.next
            p2 = p2.next.next

        next_head = p1.next
        p1.next = None

        p1 = head
        p2 = self.reverse_list(next_head)
        p1_next = p1.next
        p2_next = p2.next
        step = 0
        while True:
            if step % 2 == 0:
                p1.next = p2
                p1 = p1_next
                if not p1:
                    break
                p1_next = p1.next
            else:
                p2.next = p1
                p2 = p2_next
                if not p2:
                    break
                p2_next = p2.next

            step += 1




    def reverse_list(self, head):
        if not head or not head.next:
            return head
        pointer_1 = head
        pointer_2 = head.next
        pointer_1.next = None
        while pointer_2.next:
            next_pointer = pointer_2.next
            pointer_2.next = pointer_1
            pointer_1 = pointer_2
            pointer_2 = next_pointer

        return pointer_1