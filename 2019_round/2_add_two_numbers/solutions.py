# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2

        if not l2:
            return l1

        has_increments = 0
        pointer1, pointer2 = l1, l2

        # a dummy node
        head = ListNode(0)
        pointer = head
        while pointer1 and pointer2:
            if pointer1.val + pointer2.val + has_increments >= 10:
                new_node = ListNode(pointer1.val + pointer2.val + has_increments - 10)
                has_increments = 1
            else:
                new_node = ListNode(pointer1.val + pointer2.val + has_increments)
                has_increments = 0
            pointer.next = new_node
            pointer = pointer.next

            pointer1, pointer2 = pointer1.next, pointer2.next


        def continue_update(result_pointer, input_pointer, has_increments):
            while input_pointer:
                if input_pointer.val + has_increments >= 10:
                    new_node = ListNode(input_pointer.val + has_increments - 10)
                    has_increments = 1
                else:
                    new_node = ListNode(input_pointer.val + has_increments)
                    has_increments = 0

                result_pointer.next = new_node
                if input_pointer.next:
                    result_pointer = result_pointer.next
                input_pointer = input_pointer.next
            return has_increments

        if pointer1:
            while pointer1:
                if pointer1.val + has_increments >= 10:
                    new_node = ListNode(pointer1.val + has_increments - 10)
                    has_increments = 1
                else:
                    new_node = ListNode(pointer1.val + has_increments)
                    has_increments = 0

                pointer.next = new_node
                pointer = pointer.next
                pointer1 = pointer1.next
        elif pointer2:
            while pointer2:
                if pointer2.val + has_increments >= 10:
                    new_node = ListNode(pointer2.val + has_increments - 10)
                    has_increments = 1
                else:
                    new_node = ListNode(pointer2.val + has_increments)
                    has_increments = 0

                pointer.next = new_node
                pointer = pointer.next
                pointer2 = pointer2.next

        if has_increments:
            pointer.next = ListNode(1)

        return head.next
