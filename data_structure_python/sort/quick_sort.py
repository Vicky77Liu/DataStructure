# (3) quick sort: O(nlogn)  "sort of binary search"
"""选择数组一个数作为基数，并从数组中取出此基数
遍历数组，逐个与基数比对。"""
# def partition(arr, low, high):
#     i = low - 1
#     pivot = arr[high]
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return i + 1
#
#
# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)
#
# if __name__ == '__main__':
#     arr = [2, 9, 6, 7, 3]
#     n = len(arr)
#     quickSort(arr,0,n-1)
#     result = []
#     for i in range(n):
#         result.append(arr[i])
#     print(result)

# singgle way
# import random

# def partition(arr,l,r):
#     rnd = random.randint(l,r) #使用随机数避免有序数组造成的时间性能下降
#     arr[l],arr[rnd] = arr[rnd],arr[l]
#
#     i = l + 1
#     j = l
#
#     while i <= r:
#         if arr[i] < arr[l]:
#             j += 1
#             arr[i], arr[j] = arr[j], arr[i]
#         i += 1
#     arr[j], arr[l] = arr[l],arr[j]
#     return j
#
# def quicksort1(arr,l,r):
#     if l < r:
#         p = partition(arr,l,r)
#         quicksort1(arr,l,p-1)
#         quicksort1(arr,p+1,r)
#     return arr
#
# def sort1(arr):
#     quicksort1(arr, 0, len(arr)-1)
#     return arr
#
# if __name__ == '__main__':
#     arr = [0,2,5,3,1,4]
#     a = sort1(arr)
#     print(a)
# import random
#
# double ways
# def partition(arr,left,right):
#     rnd = random.randint(left,right)
#     arr[left],arr[rnd] = arr[rnd],arr[left]
#
#     i = left + 1
#     j = right
#     while True:
#         while i <= j and arr[i] < arr[left]:
#             i += 1
#         while i <= j and arr[j] > arr[left]:
#             j -= 1
#
#         if i > j:
#             break
#         else:
#             arr[i],arr[j] = arr[j],arr[i]
#             i += 1
#             j += 1
#
#     arr[left],arr[j] = arr[j],arr[left]
#
#     return j
#
# def quicksort2(arr,left,right):
#     if left < right:
#         p = partition(arr,left,right)
#         quicksort2(arr,left,p-1)
#         quicksort2(arr,p+1,right)
#
#     return arr
#
# def sort2(arr):
#     quicksort2(arr,0,len(arr)-1)
#     return arr
#
# if __name__ == '__main__':
#     arr = [0,2,5,3,1,4]
#     a = sort2(arr)
#     print(a)

# three ways
# import random
# def partition(arr,left,right):
#
#     rnd = random.randint(left,right)
#     arr[left],arr[rnd] = arr[rnd],arr[left]
#
#     lt = left
#     i = left + 1
#     gt = right + 1
#
#     # arr[left+1,lt] <arr[left],arr[lt+1,i]==arr[left],arr[gt,right]>arr[left] 循环不变量的设定
#     while i < gt: # i == gt 比较结束
#         if arr[i] < arr[left]:
#             arr[i],arr[lt+1] = arr[lt+1],arr[i]
#             i += 1
#             lt += 1
#         elif arr[i] > arr[left]:
#             arr[i],arr[gt-1] = arr[gt-1],arr[i]
#             gt -= 1
#         else:
#             i += 1
#     arr[left],arr[lt] = arr[lt],arr[left]
#     return lt,gt
#
# def quicksort3(arr,left,right):
#     if left < right:
#         lt,gt = partition(arr,left,right)
#         quicksort3(arr,left,lt-1)
#         quicksort3(arr,gt,right)
#     return arr

# def sort3(arr):
#     low = 0
#     high = len(arr)-1
#     quicksort3(arr,low,high)
#     return arr
#
# if __name__ == '__main__':
#     arr = [1,2,7,4,5,3,4,2,8]
#     a = sort3(arr)
#     print(a)


import random


class Sort:
    def __init__(self, array):
        self.arr = array

    def __str__(self):
        return str(self.arr)

    # single way quick sort
    def partition(self, left, right):
        rnd = random.randint(left, right)
        self.arr[left], self.arr[rnd] = self.arr[rnd], self.arr[left]
        i = left + 1
        j = left

        while i <= right:
            if self.arr[i] < self.arr[left]:
                j += 1
                self.arr[j], self.arr[i] = self.arr[i], self.arr[j]
            i += 1

        self.arr[left], self.arr[j] = self.arr[j], self.arr[left]
        return j

    def sort(self, left, right):
        if left >= right:
            return
        p = self.partition(left, right)
        self.sort(left, p - 1)
        self.sort(p + 1, right)
        return self.arr

    def quicksort(self):
        self.sort(0, len(self.arr) - 1)
        return self.arr

    # two way quick sort
    def partitions2(self, l, r):
        rnd = random.randint(l, r)
        self.arr[rnd], self.arr[l] = self.arr[l], self.arr[rnd]
        i = l + 1
        j = r
        while True:
            while i <= j and arr[i] < arr[l]:  # 找到第一个比arr[l]大于等于的位置后，i停下
                i += 1
            while j >= i and arr[j] > arr[l]:  # 找到第一个比arr[j]小于等于的位置后，j停下
                j -= 1
            if i >= j:
                break
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            i += 1
            j -= 1

        self.arr[l], self.arr[j] = self.arr[j], self.arr[l]
        return j

    def sort2ways(self, l, r):
        if l >= r:
            return
        p = self.partitions2(l, r)
        self.sort2ways(l, p - 1)
        self.sort2ways( p + 1, r)
        return self.arr

    def quicksort2ways(self):
        return self.sort2ways(0, len(self.arr) - 1)

    # three ways quick sort (避免一个方法返回2个返回值）
    def sort3ways(self, l, r):
        if l >= r:
            return
        rnd = random.randint(l, r)
        self.arr[l], self.arr[rnd] = self.arr[rnd], self.arr[l]
        lt = l
        i = l + 1
        gt = r + 1
        while i < gt:
            # arr[l,lt-1] < 0
            if self.arr[i] < self.arr[l]:
                lt += 1
                self.arr[i], self.arr[lt] = self.arr[lt], self.arr[i]
                i += 1
            # arr[gt,r] > 0
            elif self.arr[i] > self.arr[l]:
                gt -= 1
                self.arr[i], self.arr[gt] = self.arr[gt], self.arr[i]
            # arr[i] == arr[l], arr[lt,gt-1] == 0
            else:
                i += 1
        self.arr[l], self.arr[lt] = self.arr[lt], self.arr[l]

        self.sort3ways(l, lt - 1)

        self.sort3ways(gt, r)
        return self.arr

    def quicksort3ways(self):
        return self.sort3ways(0, len(arr) - 1)


if __name__ == '__main__':
    arr = [6, 2, 7, 4, 1, 3, 3, 3, 5, 3]
    a = Sort(arr)
    a.quicksort()
    print(a)
    b = Sort(arr)
    b.quicksort2ways()
    print(b)
    c = Sort(arr)
    c.quicksort3ways()
    print(c)

    print(a)
