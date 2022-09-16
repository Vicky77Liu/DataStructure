import random


class MinHeap(object):
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def _parent(self, index):
        if index == 0:
            raise IndexError("index 0 have no parent")
        return (index - 1) // 2

    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2

    def add(self, val):
        self.data.append(val)
        self._sift_up(len(self.data) - 1)

    def _sift_up(self, k):
        while k > 0 and self.data[self._parent(k)] > self.data[k]:
            self.data[self._parent(k)], self.data[k] = self.data[k], self.data[self._parent(k)]
            k = self._parent(k)

    def find_min(self):
        if len(self.data) == 0:
            raise ValueError("can't find min in empty heap")
        return self.data[0]

    def extract_min(self):
        ret = self.find_min()
        self.data[0], self.data[len(self.data) - 1] = self.data[len(self.data) - 1], self.data[0]
        self.data.pop()
        self._sift_down(0)
        return ret

    def _sift_down(self, k):
        while self._left_child(k) < len(self.data):
            i = self._left_child(k)
            if i + 1 < len(self.data) and self.data[i + 1] < self.data[i]:
                i += 1
                # 此时i 是左右孩子里的那个最小的
            if self.data[k] <= self.data[i]:
                break
            self.data[k], self.data[i] = self.data[i], self.data[k]
            k = i

    # 替换队顶元素为val 并返回堆顶元素
    def replace(self, val):
        ret = self.find_min()
        self.data[0] = val
        self._sift_down(0)
        return ret

    # 从第一个非叶子节点开始，从后向前进行 sift down操作
    def heapify(self, arr):
        self.data = arr.copy()
        if len(arr) != 1:
            # 最后一个非叶子节点 ： 最后一个节点的父亲节点
            i = self._parent(len(self.data) - 1)
            while i >= 0:
                self._sift_down(i)
                i -= 1

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    hq = MinHeap()
    arr1 = [4, 6, 2, 3, 9]
    hq.heapify(arr1)
    print(hq)
