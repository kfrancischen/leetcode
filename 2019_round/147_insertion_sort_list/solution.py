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
        if not head or not head.next:
            return head

        cur_pointer = head.next
        pre_pointer = head
        while cur_pointer:
            if cur_pointer.val < head.val:
                pre_pointer.next = cur_pointer.next
                cur_pointer.next = head
                head = cur_pointer
                cur_pointer = pre_pointer.next
                continue

            if cur_pointer.val >= pre_pointer.val:
                pre_pointer = cur_pointer
                cur_pointer = cur_pointer.next
                continue

            compare_pointer = head
            while compare_pointer.val < cur_pointer.val and compare_pointer.next.val < cur_pointer.val:
                compare_pointer = compare_pointer.next

            pre_pointer.next = cur_pointer.next
            cur_pointer.next = compare_pointer.next
            compare_pointer.next = cur_pointer
            cur_pointer = pre_pointer.next

    return head
