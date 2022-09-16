class Sort:
    def __init__(self, array):
        self.arr = array

    def bubble_sort(self):
        n = len(self.arr)
        i = 0
        while i < n - 1:
            last_swap_index = 0
            for j in range(n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    last_swap_index = j + 1
            i = n - last_swap_index
        return self.arr

    def bubble_sort_reverse(self):
        n = len(self.arr)
        i = 0
        while i < n - 1:
            last_swap_index = 0
            for j in range(n - i - 1):
                if self.arr[j] < self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    last_swap_index = j + 1
            i = n - last_swap_index

        return self.arr

    def __str__(self):
        return str(self.arr)


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    s = Sort(arr)
    s.bubble_sort()
    print(s)
    s.bubble_sort_reverse()
    print(s)
