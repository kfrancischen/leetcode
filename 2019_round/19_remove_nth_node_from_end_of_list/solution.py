# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        dummy_head.next = head
        pointer1, pointer2, pointer3 = dummy_head, dummy_head, dummy_head
        for i in range(n):
            pointer1 = pointer1.next

        while pointer1.next:
            pointer2 = pointer2.next
            pointer3 = pointer3.next
            pointer1 = pointer1.next
            
        pointer2 = pointer2.next
        pointer3.next = pointer2.next
        return dummy_head.next
