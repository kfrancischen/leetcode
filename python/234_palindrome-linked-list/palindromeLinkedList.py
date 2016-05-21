# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        pointer = head
        len = 0
        while pointer != None:
            pointer = pointer.next
            len += 1
        count = 1
        pointer = head
        while count < (len + 1) / 2:
            pointer = pointer.next
            count += 1
        secondHalf = self.reverseList(pointer.next)
        pointer.next = None
        firstHalf = head

        while firstHalf != None and secondHalf != None:
            if firstHalf.val != secondHalf.val:
                return False
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        return True

    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        newHead = ListNode(0)
        newHead.next = head
        pointer_1 = newHead
        pointer_2 = newHead.next
        pointer_3 = newHead.next.next
        while pointer_3 != None:
            pointer_2.next = pointer_1
            pointer_1 = pointer_2
            pointer_2 = pointer_3
            pointer_3 = pointer_3.next
        pointer_2.next = pointer_1
        head.next = None
        return pointer_2
