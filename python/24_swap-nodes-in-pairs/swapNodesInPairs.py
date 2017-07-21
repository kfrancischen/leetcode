# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        newHead = head.next
        head.next = newHead.next
        newHead.next = head

        pointer = newHead.next
        prePointer = newHead
        while pointer != None and pointer.next != None and pointer.next.next != None:
            prePointer = pointer
            pointer = pointer.next
            nextPointer = pointer.next
            pointer.next = nextPointer.next
            prePointer.next = nextPointer
            nextPointer.next = pointer


        return newHead
