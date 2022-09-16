class ListNode(object):
    def __init__(self, key=None, val=None, next_=None):
        self.key = key
        self.val = val
        self.next = next_

    def __str__(self):
        return "{}:{}".format(self.key, self.val)

    def __repr__(self):
        return "{}:{}".format(self.key, self.val)


class LinkedListMap:
    def __init__(self):
        self.dummyHead = ListNode()
        self.size = 0

    def __str__(self):
        head = self.dummyHead.next
        res = '{'
        while head:
            res += str(head)
            if head.next is not None:
                res += '; '
            head = head.next
        res += '}'
        return res

    def __repr__(self):
        head = self.dummyHead.next
        res = '{'
        while head:
            res += repr(head)
            if head.next is not None:
                res += '; '
            head = head.next
        res += '}'
        return res

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        cur = self.dummyHead.next
        while cur:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

    # if the map is empty
    def is_empty(self):
        return self.size == 0

    # return boolean if key is in the map
    def contains(self, key):
        return self.__getitem__(key) is not None

    # get the value by key
    def get(self, key):
        node = self.__getitem__(key)
        return node.val if node else None

    # private method , add node by index
    def _add(self, index, key, val):
        if index < 0 or index > self.size:
            raise IndexError("Index is out of range")
        prev = self.dummyHead
        for i in range(index):
            prev = prev.next
        prev.next = ListNode(key, val, prev.next)
        self.size += 1

    # add node from head
    def add_first(self, key, val):
        self._add(0, key, val)

    # add node from tail
    def add_last(self, key, val):
        self._add(self.size, key, val)

    # add node
    def add(self, key, val):
        node = self.__getitem__(key)
        if not node:
            self.add_last(key, val)
        else:
            raise Exception("Key is exist, you can use set method change value")

    # set node value, if node exist, update value
    def set(self, key, val):
        node = self.__getitem__(key)
        if not node:
            self.add_last(key, val)
        else:
            node.val = val

    # remove node by key
    def remove(self, key):
        pre = self.dummyHead
        while pre.next:
            if pre.next.key == key:
                break
            pre = pre.next
        if pre.next:
            del_node = pre.next
            pre.next = del_node.next
            del_node.next = None
            self.size -= 1
            return del_node.val
        return None


'''if __name__ == '__main__':
    m = LinkedListMap()
    for i in range(10):
        m.add_last(i,i)
    print(m[0])
    print(m.get(2))
    print(m.contains(3))
    print(len(m))
    m.set(20,30)
    print(m)
    m.remove(20)
    print(m)
    print(len(m))
    m.add_last(90,1)
    print(m)
    m.set(0,1000)
    print(m)
    m.remove(0)
    print(m)
    m.add(1,40)
    print(m)'''
