import heapq
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, [node.val, node])
                node = node.next
        mergedList = ListNode(0)
        head = mergedList
        while heap:
            val, node = heapq.heappop(heap)
            newNode = ListNode(val)
            mergedList.next = newNode
            mergedList = mergedList.next

            node = node.next
            if node:
                heapq.heappush(heap, [node.val, node])

        return head.next

mytest = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3

n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n4.next = n5
n5.next = n6

print mytest.mergeKLists([n1,n4]).val
