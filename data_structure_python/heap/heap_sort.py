# 用最大堆实现排序

class HeapSort:
    def __init__(self, array):
        self.arr = array

    def sort(self):
        if len(self.arr) <= 1:
            return
        for i in range((len(self.arr) - 2) // 2, -1, -1):  # heapify的过程
            self.sift_down(i, len(self.arr))

        for i in range(len(self.arr) - 1, -1, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.sift_down(0, i)

    # 对[0,n)所形成的最大堆中，索引k的元素，执行sift_down
    def sift_down(self, k, n):
        while 2 * k + 1 < n:  # 左孩子的索引小于size
            i = 2 * k + 1  # i = 左孩子索引
            if i + 1 < n and self.arr[i + 1] > self.arr[i]:
                i += 1  # i 是左右孩子的大的那个
            if self.arr[k] >= self.arr[i]:
                break
            self.arr[k], self.arr[i] = self.arr[i], self.arr[k]

            k = i  # k指向被换后的位置,继续判断是否需要sift_down

    def __str__(self):
        return str(self.arr)


if __name__ == '__main__':
    ll = [2, 3, 1, 0, 5, 4]
    hq = HeapSort(ll)
    hq.sort()
    print(hq)
