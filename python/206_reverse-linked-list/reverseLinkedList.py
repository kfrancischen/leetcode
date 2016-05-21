# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        firstPointer = head
        secondPointer = head.next
        thirdPointer = head.next.next
        firstPointer.next = None
        if thirdPointer == None:
            secondPointer.next = firstPointer
            return secondPointer

        while thirdPointer != None:
            secondPointer.next = firstPointer
            firstPointer = secondPointer
            secondPointer = thirdPointer
            thirdPointer = thirdPointer.next
        secondPointer.next = firstPointer
        return secondPointer
