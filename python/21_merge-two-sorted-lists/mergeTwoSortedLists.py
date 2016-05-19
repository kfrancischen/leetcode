# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        atHead = True
        result = ListNode(0)
        head = result
        while l1 != None and l2!= None:
            if l1.val <= l2.val:
                newNode = ListNode(l1.val)
                l1 = l1.next
            else:
                newNode = ListNode(l2.val)
                l2 = l2.next

            result.next = newNode
            result = result.next

        while l1 != None:
            result.next = ListNode(l1.val)
            l1 = l1.next
            result = result.next
        while l2 != None:
            result.next = ListNode(l2.val)
            l2 = l2.next
            result = result.next

        return head.next
