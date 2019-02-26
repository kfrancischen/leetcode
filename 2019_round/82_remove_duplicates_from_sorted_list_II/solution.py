# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        head_val = head.val
        dummy_node = ListNode(head_val-1)
        dummy_node.next = head
        pointer_1 = dummy_node
        pointer_2 = head
        cur_val = dummy_node.val
        while pointer_2:
            
            if not pointer_2.next:
                if cur_val != pointer_2.val:
                    pointer_1.next = pointer_2
                else:
                    pointer_1.next = None
            else:
                if cur_val != pointer_2.val and pointer_2.val != pointer_2.next.val:
                    pointer_1.next = pointer_2
                    pointer_1 = pointer_1.next
                cur_val = pointer_2.val
                
            pointer_2 = pointer_2.next
            
        return dummy_node.next