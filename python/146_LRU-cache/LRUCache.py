class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoubleLL(object):
    def __init__(self):
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.size = 0

    def add_to_head(self, node):
        self.dummy.next, node.next, node.prev = node, self.dummy.next, self.dummy
        if node.next:
            node.next.prev = node
        if self.tail is self.dummy:
            self.tail = self.tail.next
        self.size += 1

    def del_node(self, node):
        if not node:
            return
        if node is self.tail:
            self.tail = self.tail.prev
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.size -= 1


class LRUCache(object):

    def __init__(self, size):
        self.queue, self.dic, self.size, self.n = DoubleLL(), {}, size, 0


    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self.queue.del_node(node)
            self.queue.add_to_head(node)
            return node.val[1]
        return -1

    def set(self, key, value):
        if key not in self.dic and self.queue.size >= self.size:
            rem_node = self.queue.tail
            self.queue.del_node(rem_node)
            self.dic.pop(rem_node.val[0], None)

        self.queue.del_node(self.dic.pop(key, None))
        self.queue.add_to_head(ListNode((key, value)))
        self.dic[key] = self.queue.dummy.next
