# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head == None or head.next == None or m == n:
            return head
        newHead = ListNode(0)
        newHead.next = head
        pointer_1 = newHead
        pointer_2 = newHead
        count = 1
        while count < m:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next
            count += 1
        while count <= n:
            count += 1
            pointer_2 = pointer_2.next


        segementHead = pointer_1.next
        segmentTail = pointer_2

        pointer_2 = pointer_2.next
        segmentTail.next = None
        (segementHead, segmentTail) = self.reverseList(segementHead)
        pointer_1.next = segementHead
        if pointer_2 != None:
            segmentTail.next = pointer_2
        return newHead.next

    def reverseList(self, head):
        firstPointer = head
        secondPointer = head.next
        thirdPointer = head.next.next
        firstPointer.next = None
        if thirdPointer == None:
            secondPointer.next = firstPointer
            return (secondPointer, head)

        while thirdPointer != None:
            secondPointer.next = firstPointer
            firstPointer = secondPointer
            secondPointer = thirdPointer
            thirdPointer = thirdPointer.next
        secondPointer.next = firstPointer
        return (secondPointer,head)
