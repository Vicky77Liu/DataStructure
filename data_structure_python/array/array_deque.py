from array import Array


class Deque:
    def __init__(self):
        self.data = Array()

    def __len__(self):
        return self.data.size

    def __getitem__(self, index):
        if index < 0 or index >= self.data.size:
            raise IndexError("index is out of range")
        return self.data[index]

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
        for i in range(len(self.data)):
            res += repr(self.data[i])
            if i != len(self.data) - 1:
                res += ', '
        res += ']'
        return res

    # if deque is empty
    def is_empty(self):
        return self.data.is_empty()

    # add value at front
    def add_first(self, value):
        self.data.add_first(value)

    # add value at the end
    def add_last(self, value):
        self.data.add_last(value)

    # remove the first element
    def remove_first(self):
        return self.data.remove_first()

    # remove the last element
    def remove_last(self):
        return self.data.remove_last()

    # get the first element
    def get_front(self):
        return self.data.get_first()

    # get the last element
    def get_last(self):
        return self.get_last()
