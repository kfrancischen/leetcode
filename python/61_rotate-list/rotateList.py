# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        pointer = head
        while pointer != None:
            length +=1
            pointer = pointer.next
        if length == 0 or k == 0 or k % length == 0:
            return head

        k = k % length

        count = 0
        pointer_1 = head
        pointer_2 = head

        while pointer_1.next != None:
            pointer_1 = pointer_1.next
            count += 1
            if count > k:
                pointer_2 = pointer_2.next

        newHead = pointer_2.next
        pointer_2.next = None
        pointer_1.next = head
        return newHead
