# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        pointer_1 = head
        pointer_2 = head.next
        while True:
            if pointer_2.next == None or pointer_2.next.next == None:
                return False
            pointer_2 = pointer_2.next.next
            pointer_1 = pointer_1.next
            if pointer_2 == pointer_1:
                return True
