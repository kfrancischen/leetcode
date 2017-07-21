# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from random import randint
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.pointer = head


    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        result = self.pointer.val
        count = 1
        cur = self.pointer.next
        while cur:
            if randint(1, count + 1) == 1:
                result = cur.val
            cur = cur.next
            count += 1

        return result




# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
