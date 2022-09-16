
class ListNode(object):
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next = next_

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return repr(self.val)


class LinkedList(object):
    def __init__(self):
        self.dummyHead = ListNode()
        self.size = 0

    def __str__(self):
        temp = self.dummyHead.next
        result = "["
        while temp is not None:
            result += str(temp.val)
            temp = temp.next
            if temp:
                result += ","
        result += "]"
        return result

    def __repr__(self):
        temp = self.dummyHead.next
        result = "["
        while temp is not None:
            result += repr(temp.val)
            temp = temp.next
        result += "]"
        return repr(result)

    def __len__(self):
        return self.size

    # if the list is empty
    def is_empty(self):
        return self.size == 0

    # add element
    def add(self, index, val):
        if index < 0 or index > self.size:
            raise IndexError("index is invalid")
        prev = self.dummyHead
        for i in range(index):
            prev = prev.next
        prev.next = ListNode(val, prev.next)
        self.size += 1

    # add element at front
    def add_first(self, val):
        self.add(0, val)

    # add element at the end
    def add_last(self, val):
        self.add(self.size, val)

    # get element value by index
    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index is invalid")
        cur = self.dummyHead.next
        for i in range(index):
            cur = cur.next
        return cur.val

    # get first element
    def get_first(self):
        return self.get(0)

    # get last element
    def get_last(self):
        return self.get(self.size - 1)

    # return boolean if value is in the list
    def contains(self, val):
        cur = self.dummyHead.next
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False

    # update element value by index
    def set(self, index, val):
        if index < 0 or index >= self.size:
            raise IndexError("index is invalid")
        cur = self.dummyHead.next
        for i in range(index):
            cur = cur.next
        cur.val = val

    # remove element by index and return value
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index is invalid")
        prev = self.dummyHead
        for i in range(index):
            prev = prev.next
        del_node = prev.next
        prev.next = del_node.next
        del_node.next = None
        self.size -= 1
        return del_node.val

    # remove first element
    def remove_first(self):
        return self.remove(0)

    # remove last element
    def remove_last(self):
        return self.remove(self.size - 1)

    # remove element by value
    def remove_element(self, val):
        pre = self.dummyHead
        cur = self.dummyHead.next
        while cur and cur.val != val:
            pre = cur
            cur = cur.next
        if cur.val == val:
            pre.next = cur.next
        self.size -= 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.add_first(2)
    ll.add_last(3)
    print(ll)
    ll.remove(0)
    print(ll)
    # a = ll.contains(2)
    # print(a)