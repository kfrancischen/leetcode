# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        pointer_1 = head
        pointer_2 = head.next
        while pointer_2 != None and pointer_2.next != None:
            nextNode1 = pointer_1.next
            nextNode2 = pointer_2.next
            pointer_2.next = nextNode2.next
            pointer_1.next = nextNode2
            nextNode2.next = nextNode1

            pointer_2 = pointer_2.next
            pointer_1 = pointer_1.next
            
        return head
