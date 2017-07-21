# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        pointerA = headA
        pointerB = headB
        lenA = 1
        lenB = 1
        while pointerA.next != None:
            lenA += 1
            pointerA = pointerA.next
        while pointerB.next != None:
            lenB += 1
            pointerB = pointerB.next
        if pointerA != pointerB:
            return None

        pointerA = headA
        pointerB = headB
        count = 0
        if lenA < lenB:
            while count < lenB - lenA:
                pointerB = pointerB.next
                count += 1
        elif lenB < lenA:
            while count < lenA - lenB:
                pointerA = pointerA.next
                count += 1
        while pointerA != pointerB:
            pointerA = pointerA.next
            pointerB = pointerB.next
        return pointerA
