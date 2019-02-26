# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lessList = ListNode(0)
        greaterList = ListNode(0)
        lessPointer = lessList
        greaterPointer = greaterList
        pointer = head
        while pointer != None:
            if pointer.val < x:
                lessPointer.next = ListNode(pointer.val)
                lessPointer = lessPointer.next
            else:
                greaterPointer.next = ListNode(pointer.val)
                greaterPointer = greaterPointer.next
            pointer = pointer.next
            
        if lessList.next == None:
            return greaterList.next
        if greaterList.next == None:
            return lessList.next
        lessPointer.next = greaterList.next
        return lessList.next