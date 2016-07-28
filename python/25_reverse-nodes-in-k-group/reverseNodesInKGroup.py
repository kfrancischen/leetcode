# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2:
            return head
        newHead = ListNode(0)
        newHead.next = head
        dummyNode = newHead
        pointer_1 = newHead
        pointer_2 = newHead
        count = 0
        while pointer_2.next != None:
            pointer_2 = pointer_2.next
            count += 1
            if count == k:
                nextNode = pointer_2.next
                nextHead, nextTail = self.reverseList(pointer_1.next, pointer_2)
                print nextHead.val, nextTail.val
                pointer_1.next = nextHead
                nextTail.next = nextNode
                pointer_1 = pointer_2 = nextTail
                count = 0
        return dummyNode.next

    def reverseList(self, head, tail):
        tail.next = None
        firstPointer = head
        secondPointer = head.next
        thirdPointer = head.next.next
        firstPointer.next = None
        if thirdPointer == None:
            secondPointer.next = firstPointer
            return (secondPointer, firstPointer)

        while thirdPointer != None:
            secondPointer.next = firstPointer
            firstPointer = secondPointer
            secondPointer = thirdPointer
            thirdPointer = thirdPointer.next
        secondPointer.next = firstPointer
        return (secondPointer, head)

mytest = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
#n3.next = n4
#n4.next = n5
print mytest.reverseKGroup(n1, 3)
