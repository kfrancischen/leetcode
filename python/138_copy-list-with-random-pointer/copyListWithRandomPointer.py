# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        copyDict = {}
        pointer = head
        newHead = RandomListNode(0)
        newPointer = newHead
        while pointer != None:
            newRandomNode = RandomListNode(pointer.label)
            copyDict[pointer] = newRandomNode
            newPointer.next = newRandomNode
            newPointer = newPointer.next
            pointer = pointer.next

        pointer = head
        newPointer = newHead.next
        while pointer != None:
            newPointer.random = copyDict[pointer.random] if pointer.random != None else None
            pointer = pointer.next
            newPointer = newPointer.next

        return newHead.next
