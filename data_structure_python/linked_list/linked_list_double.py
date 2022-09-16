class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self):
        val = "{}:{}".format(self.key, self.val)
        return val

    def __repr__(self):
        val = "{}:{}".format(self.key, self.val)
        return val


class LinkedList:
    def __init__(self, capacity=0xffff):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        p = self.head
        line = "{"
        while p:
            line += "{}".format(p)
            p = p.next
            if p:
                line += "->"
        line += "}"
        return str(line)

    def __repr__(self):
        p = self.head
        line = "{"
        while p:
            line += "{}".format(p)
            p = p.next
            if p:
                line += "->"
        line += "}"
        return repr(line)

    def __len__(self):
        return self.size

    # private method,add from head
    def _add_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.head.prev = None
            self.tail.next = None
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None
        self.size += 1

    # public method, append from head
    def append_front(self, node):
        self._add_head(node)

    # private method, add from tail
    def _add_tail(self, node):
        if not self.tail:
            self.tail = node
            self.head = node
            self.tail.next = None
            self.head.prev = None
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = None
        self.size += 1

    # public method, append from tail
    def append(self, node):
        self._add_tail(node)

    # private method, remove from head
    def _remove_head(self):
        if not self.head:
            return
        node = self.head
        if node.next:
            self.head = node.next
            self.head.prev = None
        else:
            self.head = self.tail = None
        self.size -= 1
        return node

    # public method, remove from head
    def pop(self):
        return self._remove_head()

    # private method, remove from tail
    def _remove_tail(self):
        if not self.tail:
            return
        node = self.tail
        if node.prev:
            self.tail = node.prev
            self.tail.next = None
        else:
            self.tail = self.head = None
        self.size -= 1
        return node

    # public method, remove from tail
    def remove(self):
        return self._remove_tail()


'''if __name__ == '__main__':
    l = LinkedList(10)
    nodes = []
    for i in range(10):
        node = LinkedNode(i, i)
        nodes.append(node)
    print(nodes)

    l.append(nodes[0])
    print(l)
    l.append_front(nodes[1])
    l.append(nodes[2])
    l.append_front(nodes[3])
    print(l)
    a = l.remove()
    print(a)
    print(l)
    b = l.pop()
    print(b)
    print(l)
    print(len(l))'''
