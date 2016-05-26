# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        if not head or head.next == None:
            return head

        one_step = head
        two_step = head
        p = ListNode(0)
        left_head = p
        while two_step and two_step.next:
            p.next = one_step
            one_step = one_step.next
            two_step = two_step.next.next
            p = p.next
        p.next = None
        right = self.sortList(one_step)
        left = self.sortList(left_head.next)
        return self.mergeList(left,right)

    def mergeList(self,p1,p2):
        p = ListNode(0)
        head = p

        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next

        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return head.next
