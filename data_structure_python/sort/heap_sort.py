

class Sort:
    # 最大堆顺序排序
    def heap_sort(self, arr):
        if len(arr) <= 1:
            return
        for i in range((len(arr) - 2) // 2, -1, -1):  # heapify的过程
            self.sift_down(arr, i, len(arr))

        for i in range(len(arr) - 1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.sift_down(arr, 0, i)
        return arr

    # 对[0,n)所形成的最大堆中，索引k的元素，执行sift_down
    @staticmethod
    def sift_down(arr, k, n):
        while 2 * k + 1 < n:  # 左孩子的索引小于size
            i = 2 * k + 1  # i = 左孩子索引
            if i + 1 < n and arr[i + 1] > arr[i]:
                i += 1  # i 是左右孩子的大的那个
            if arr[k] >= arr[i]:
                break
            arr[k], arr[i] = arr[i], arr[k]

            k = i  # k指向被换后的位置继续判断是否需要sift_down

    # 最小堆 (倒序排序）
    def heapsort2(self, arr):
        if len(arr) <= 1:
            return
        for i in range((len(arr) - 2) // 2, -1, -1):  # heapify 为最小堆
            self.sift_down2(arr, i, len(arr))

        for i in range(len(arr) - 1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.sift_down2(arr, 0, i)
        return arr

    @staticmethod
    def sift_down2(arr, k, n):
        while 2 * k + 1 < n:
            i = 2 * k + 1
            if i + 1 < n and arr[i + 1] < arr[i]:
                i += 1
            if arr[k] <= arr[i]:
                break

            arr[k], arr[i] = arr[i], arr[k]
            k = i


if __name__ == '__main__':
    hp = Sort()
    ll = [2, 3, 1, 0, 5, 4]
    ll2 = [2, 3, 1, 0, 5, 4]
    a = hp.heap_sort(ll)
    b = hp.heapsort2(ll2)

    print(a)
    print(b)
