class Array:
    def __init__(self):
        self.data = []
        self.size = 0

    def __str__(self):
        res = '['
        for i in range(self.size):
            res += str(self.data[i])
            if i != self.size - 1:
                res += ', '
        res += ']'
        return res

    def __repr__(self):
        res = '['
        for i in range(self.size):
            res += repr(self.data[i])
            if i != self.size - 1:
                res += ', '
        res += ']'
        return res

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index is out of range")
        return self.data[index]

    # return boolean if array is empty
    def is_empty(self):
        return self.size == 0

    # get element by index
    def get_element(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Invalid Index")
        return self.data[index]

    # get first element
    def get_first(self):
        return self.get_element(0)

    # get last element
    def get_last(self):
        return self.get_element(self.size - 1)

    # find element by value, and return it's index or -1
    def find(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1

    # return boolean if array has element
    def contains(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return True
        return False

    # change element value by index
    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Invalid Index")
        self.data[index] = value

    # add element by index
    def add(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Invalid Index")
        self.data.insert(index, value)
        self.size += 1

    # add element on first of array
    def add_first(self, value):
        self.add(0, value)

    # add element on last of array
    def add_last(self, value):
        self.add(self.size, value)

    # remove element by index
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Invalid Index")
        removed_element = self.data[index]
        for i in range(index + 1, self.size):
            self.data[i - 1] = self.data[i]
        self.size -= 1
        self.data[self.size] = None
        return removed_element

    # remove first element
    def remove_first(self):
        return self.remove(0)

    # remove last element
    def remove_last(self):
        return self.remove(self.size - 1)

    # delete element
    def remove_element(self, value):
        element_index = self.find(value)
        if element_index != -1:
            self.remove(element_index)

    # change 2 elements by index
    def swap(self, index1, index2):
        if index1 < 0 or index1 >= self.size or index2 < 0 or index2 >= self.size:
            temp = self.data[index1]
            self.data[index1] = self.data[index2]
            self.data[index2] = temp


'''if __name__ == '__main__':
    arr = Array()
    arr.add(0, 5)
    arr.add_last(3)
    arr.add_first(6)
    print(len(arr))
    print(arr)
    arr.remove_element(3)
    print(arr)'''
