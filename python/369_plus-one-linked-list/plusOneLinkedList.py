# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reverse_list = self.reverseList(head)
        increment = 1
        pointer = reverse_list
        pre_node = reverse_list
        while pointer != None:
            if increment == 1:
                pointer.val += 1
            if pointer.val == 10:
                pointer.val = 0
            else:
                increment = 0
            pre_node = pointer
            pointer = pointer.next
        if increment == 1:
            newNode = ListNode(1)
            pre_node.next = newNode
            
        return self.reverseList(reverse_list)
            
    def reverseList(self, head):
        if head.next == None:
            return head
        pointer1, pointer2 = head, head.next
        head.next = None
        while pointer2 != None:
            nextNode = pointer2.next
            pointer2.next = pointer1
            pointer1, pointer2 = pointer2, nextNode
            
        return pointer1
            
        