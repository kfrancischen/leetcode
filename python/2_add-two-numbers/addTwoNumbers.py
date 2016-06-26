# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        increment = 0
        if l1 == None:
            return l2

        if l2 == None:
            return l1

        if l1.val + l2.val >= 10:
            result = ListNode(l1.val + l2.val - 10)
            increment = 1
        else:
            result = ListNode(l1.val + l2.val)
        l1 = l1.next
        l2 = l2.next
        output = result

        while l1 != None or l2 != None:
            if l1 != None and l2 != None:

                if l1.val + l2.val + increment >= 10:
                    result_next = ListNode(l1.val + l2.val + increment - 10)
                    increment = 1
                else:
                    result_next = ListNode(l1.val + l2.val + increment)
                    increment = 0

                l1 = l1.next
                l2 = l2.next

            elif l1 != None and l2 == None:
                if l1.val + increment >= 10:
                    result_next = ListNode(l1.val + increment - 10)
                    increment = 1
                else:
                    result_next = ListNode(l1.val + increment)
                    increment = 0
                l1 = l1.next

            else:
                if l2.val + increment >= 10:
                    result_next = ListNode(l2.val + increment - 10)
                    increment = 1
                else:
                    result_next = ListNode(l2.val + increment)
                    increment = 0
                l2 = l2.next

            result.next = result_next
            result = result.next



        if increment == 1:
            result_next = ListNode(1)
            result.next = result_next

        return output


