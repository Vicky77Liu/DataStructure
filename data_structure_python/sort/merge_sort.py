# （4）merge sort :O(nlogn)
'''
将一个数组拆成A、B两个小组，两个小组继续拆，直到每个小组只有一个元素为止。
按照拆分过程逐步合并小组，由于各小组初始只有一个元素，可以看做小组内部是有序的，合并小组可以被看做是合并两个有序数组的过程。
对左右两个小数列重复第二步，直至各区间只有1个数
'''


# def merge(arr, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m
#
#     # 创建临时数组
#     L = [0] * (n1)
#     R = [0] * (n2)
#
#     # 拷贝数据到临时数组 arrays L[] 和 R[]
#     for i in range(0, n1):
#         L[i] = arr[l + i]
#
#     for j in range(0, n2):
#         R[j] = arr[m + 1 + j]
#
#         # 归并临时数组到 arr[l..r]
#     i = 0  # 初始化第一个子数组的索引
#     j = 0  # 初始化第二个子数组的索引
#     k = l  # 初始归并子数组的索引
#
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
#
#     # 拷贝 L[] 的保留元素
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#
#     # 拷贝 R[] 的保留元素
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1

# def mergeSort(arr, l, r):
#     if l < r:   # if l >= r: return
#         m = int((l + (r - 1)) / 2)
#
#         mergeSort(arr, l, m)
#         mergeSort(arr, m + 1, r)
#         if arr[m] > arr[m+1]:
#             merge(arr, l, m, r)
#

# def merge(left,right):
#     result = []
#     while left and right:
#         if left[0] < right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     if left:
#         result += left
#     if right:
#         result += right
#     return result
#
# def mergeSort(arr):
#     if len(arr) == 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     return merge(mergeSort(left),mergeSort(right))
#
# if __name__ == '__main__':
#     arr = [2, 9, 6, 7,7,1,0,3,-2]
#     a = mergeSort(arr)
#     print(a)



class Sort:
    def __init__(self, array):
        self.arr = array

    def __str__(self):
        return str(self.arr)

    def sort(self, l, r):
        if l >= r:
            return
        mid = l + (r - l) // 2
        self.sort(l, mid)
        self.sort(mid + 1, r)
        if self.arr[mid] > self.arr[mid + 1]:
            self.merge(l, mid, r)
        return self.arr

    def merge(self, l, mid, r):
        temp = self.arr.copy()
        i = l
        j = mid + 1
        for k in range(l, r + 1):
            # if i > mid, what left in [j,mid],add to arr directly
            if i > mid:
                self.arr[k] = temp[j]
                j += 1
            # if [mid+1, r] has items left ,add to arr directly
            elif j > r:
                self.arr[k] = temp[i]
                i += 1

            elif temp[i] < temp[j]:
                self.arr[k] = temp[i]
                i += 1
            else:  # temp[i] > temp[j]:
                self.arr[k] = temp[j]
                j += 1
        return self.arr

    def merge_sort(self):
        return self.sort(0, len(self.arr) - 1)

    def merge_sort_up(self):
        n = len(self.arr)
        size = 1
        while size < n:
            i = 0
            while i + size < n:
                self.merge(i, i + size - 1, min(n - 1, i + size + size - 1))
                i += size + size
            size += size
        return self.arr


if __name__ == '__main__':
    s = Sort([1, 10, 3, 6, 7, 2, 9])
    s.merge_sort_up()
    print(s)