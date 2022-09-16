class MaxHeap(object):
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的父亲节点的索引
    def _parent(self, index):
        if index == 0:
            raise IndexError(" index 0 does not have a parent")
        return (index - 1) // 2

    def _left_child(self, index):
        return (index * 2) + 1

    def _right_child(self, index):
        return (index * 2) + 2

    def add(self, val):
        self.data.append(val)
        self._sift_up(len(self.data) - 1)

    def _sift_up(self, k):
        while k > 0 and self.data[self._parent(k)] < self.data[k]:
            self.data[self._parent(k)], self.data[k] = self.data[k], self.data[self._parent(k)]
            k = self._parent(k)

    def find_max(self):
        if len(self.data) == 0:
            raise Exception(" can't find max when heap is empty")
        return self.data[0]

    def extract_max(self):
        ret = self.find_max()
        self.data[0], self.data[len(self.data) - 1] = self.data[len(self.data) - 1], self.data[0]
        self.data.pop()
        self._sift_down(0)
        return ret

    def _sift_down(self, k):
        while self._left_child(k) < len(self.data):
            i = self._left_child(k)
            if i + 1 < len(self.data) and self.data[i + 1] > self.data[i]:
                i += 1  # i = self.__rightChild(k). i此时是左右孩子里的大的那个值

            if self.data[k] >= self.data[i]:
                break

            self.data[k], self.data[i] = self.data[i], self.data[k]
            k = i

    # 取出最大元素，并且替换为val
    def replace(self, val):
        ret = self.find_max()
        self.data[0] = val
        self._sift_down(0)
        return ret

    def heapify(self, lis):
        self.data = lis.copy()
        if len(lis) != 1:
            i = self._parent(len(self.data) - 1)
            while i >= 0:
                self._sift_down(i)
                i -= 1

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    hq = MaxHeap()
    # for i in range(5,20):
    #     hq.add(i)
    # print(hq)
    #
    # hq.replace(2)
    # print(hq)
    #
    # a = hq.getSize()
    # print(a)
    lst = [2, 3, 7, 5, 0]
    hq.heapify(lst)
    print(hq)
