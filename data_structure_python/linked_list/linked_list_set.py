from linked_list import LinkedList


class LinkedListSet:
    def __init__(self):
        self.linked_list = LinkedList()

    def __len__(self):
        return self.linked_list.size

    def __str__(self):
        return str(self.linked_list)

    def __repr__(self):
        return repr(self.linked_list)

    # if the set is empty
    def is_empty(self):
        return self.linked_list.is_empty()

    # if contains val, return boolean
    def contains(self, val):
        return self.linked_list.contains(val)

    # if value is exist, not add
    def add(self, val):
        if self.contains(val):
            return
        self.linked_list.add_last(val)

    # remove value
    def remove(self, val):
        self.linked_list.remove_element(val)


'''if __name__ == '__main__':
    set1 = LinkedListSet()
    for i in range(6):
        set1.add(i)
    print(set1)
    set1.remove(2)
    print(set1)
    set1.add(0)
    print(set1)
    print(set1.contains(7))'''
