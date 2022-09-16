from array import Array


class Queue:
    def __init__(self):
        self.data = Array()

    def __str__(self):
        res = '['
        for i in range(self.data.size):
            res += str(self.data[i])
            if i != self.data.size - 1:
                res += ', '
        res += ']'
        return res

    def __repr__(self):
        res = '['
        for i in range(self.data.size):
            res += repr(self.data[i])
            if i != self.data.size - 1:
                res += ', '
        res += ']'
        return res

    def __len__(self):
        return self.data.size

    def __getitem__(self, index):
        if index < 0 or index >= self.data.size:
            raise IndexError("index is out of range")
        return self.data[index]

    # if the queue is empty
    def is_empty(self):
        return self.data.is_empty()

    # add value at the end
    def push(self, value):
        self.data.add_last(value)

    # remove the first element
    def pop(self):
        return self.data.remove_first()

    # get the last element
    @property
    def peek(self):
        return self.data.get_last()


'''if __name__ == '__main__':
    q = Queue()
    q.push(4)
    q.push(6)
    print(q)
    print(q.peek)
    print(q.pop())'''
