class Sort:
    def __init__(self, array):
        self.arr = array

    def select_sort(self):
        n = len(self.arr)
        for i in range(n):
            temp = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[temp]:
                    temp = j
            if temp != i:
                self.arr[temp], self.arr[i] = self.arr[i], self.arr[temp]

        return self.arr

    def select_sort_reverse(self):
        n = len(self.arr)
        for i in range(n):
            temp = i
            for j in range(i + 1, n):
                if self.arr[j] > self.arr[temp]:
                    temp = j
            if temp != i:
                self.arr[temp], self.arr[i] = self.arr[i], self.arr[temp]

        return self.arr

    def __str__(self):
        return str(self.arr)


if __name__ == '__main__':
    arr = [6, 8, 3, 1, 3, 2]
    s = Sort(arr)
    s.select_sort()
    print(s)
    s.select_sort_reverse()
    print(s)
