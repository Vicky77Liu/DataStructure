class Sort:
    def __init__(self, array):
        self.arr = array

    def insert_sort(self):
        n = len(self.arr)
        for i in range(n):
            temp = self.arr[i]
            j = i
            while j > 0 and self.arr[j - 1] > temp:
                self.arr[j] = self.arr[j - 1]
                j -= 1
            self.arr[j] = temp
        return self.arr

    def insert_sort_reverse(self):
        n = len(self.arr)
        for i in range(n):
            temp = self.arr[i]
            j = i
            while j > 0 and self.arr[j - 1] < temp:
                self.arr[j] = self.arr[j - 1]
                j -= 1
            self.arr[j] = temp
        return self.arr

    def __str__(self):
        return str(self.arr)


if __name__ == '__main__':
    arr = [6, 8, 3, 1, 3, 2]
    s = Sort(arr)
    s.insert_sort()
    print(s)
    s.insert_sort_reverse()
    print(s)
