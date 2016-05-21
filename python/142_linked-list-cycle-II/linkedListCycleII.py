# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None

        pointer_1 = head
        pointer_3 = head
        pointer_2 = head

        while True:
            if pointer_2.next == None or pointer_2.next.next == None:
                return None
            pointer_2 = pointer_2.next.next
            pointer_1 = pointer_1.next
            if pointer_2 == pointer_1:
                break

        if pointer_1.next == head:
            return head

        while True:
            if pointer_3 == pointer_1:
                return pointer_3
            pointer_3 = pointer_3.next
            pointer_1 = pointer_1.next

node0 = ListNode(1)
node1 = ListNode(2)
node0.next = node1
node1.next = node0
mytest = Solution()
mytest.detectCycle(node0)
