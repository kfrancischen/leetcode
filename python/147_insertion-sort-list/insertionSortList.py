# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        curPointer = head.next
        prePointer = head
        while curPointer != None:

            if curPointer.val < head.val:
                prePointer.next = curPointer.next
                curPointer.next = head
                head = curPointer
                curPointer = prePointer.next
                continue

            if curPointer.val >= prePointer.val:
                prePointer = curPointer
                curPointer = curPointer.next
                continue
            comparePointer = head
            
            while comparePointer.val < curPointer.val and comparePointer.next.val < curPointer.val and comparePointer != prePointer:
                comparePointer = comparePointer.next

            prePointer.next = curPointer.next
            curPointer.next = comparePointer.next
            comparePointer.next = curPointer
            curPointer = prePointer.next
        return head
