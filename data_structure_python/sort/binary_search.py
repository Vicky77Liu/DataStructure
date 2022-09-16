# the basic binary search
# #algorithm with recursion
# 1
class BinarySearch:
    def __init__(self, array):
        self.arr = array

    def __str__(self):
        return str(self.arr)

    def binary_search(self, target):
        return self.search(0, len(self.arr) - 1, target)

    def search(self, left, right, target):
        if left <= right:
            mid = left + (right - left) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] > target:
                return self.search(left, mid - 1, target)
            else:  # self.arr[mid] < target
                return self.search(mid + 1, right, target)
        return -1

    # 2 no recursion algorithm
    def binary_search_iteration(self, target):
        left = 0
        right = len(self.arr) - 1
        # in [left,right] find target
        while left <= right:
            mid = left + (right - left) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] > target:
                right = mid - 1
            elif self.arr[mid] < target:
                left = mid + 1
        return -1


    # 3 fell the different : find in [left,right)
    def binary_search2(self, target):
        left = 0
        right = len(self.arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] > target:
                right = mid
            elif self.arr[mid] < target:
                left = mid + 1

        return -1

    # 4 upper: find the num is the smallest one of greater nums than target(查找大于target的最小的那个值）
    # 循环不变量  target in [left,right]
    def upper(self, target):
        left = 0
        right = len(self.arr)  # 当元素不在数组中，可以返回最大的index的右边的值
        while left < right:
            mid = left + (right - left) // 2
            if self.arr[mid] <= target:
                left = mid + 1
            elif self.arr[mid] > target:
                right = mid
        return left

    # 5 ceil: > target 返回最小索引，==target 返回最大索引
    def upper_ceil(self, target):
        left = 0
        right = len(self.arr)  # 当元素不在数组中，可以返回最大的index的右边的值
        while left < right:
            mid = left + (right - left) // 2
            if self.arr[mid] <= target:
                left = mid + 1
            elif self.arr[mid] > target:
                right = mid
        if left - 1 >= 0 and self.arr[left - 1] == target:
            return left - 1
        else:
            return left

    # 6 lowerceil :如果数组存在元素，返回最小索引，如果数组中不存在索引，返回upper（比target大的最小的值）

    def lower_ceil(self, target):
        left = 0
        right = len(self.arr)
        while left < right:
            mid = left + (right - left) // 2
            if self.arr[mid] >= target:
                right = mid
            elif self.arr[mid] < target:
                left = mid + 1
        if left + 1 < len(self.arr) and self.arr[left + 1] == target:
            return left + 1
        else:
            return left

    # 7 lower: 查找小于target的最大值
    # find in [left,right],left = -1
    def lower(self, target):
        left = -1
        right = len(self.arr) - 1
        while left < right:
            mid = left + (right - left + 1) // 2  # 如果使用mid=left+(right-left)//2，当left和right相邻，会进入死循环，向上取整
            if self.arr[mid] < target:
                left = mid
            elif self.arr[mid] >= target:
                right = mid - 1
        return left


    # 8 lowerfloor 如果数组中存在元素，返回最小索引。如果数组中不存在元素，返回lower(靠近target的最大值）
    def lower_floor(self, target):
        left = -1
        right = len(self.arr) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if self.arr[mid] < target:
                left = mid
            elif self.arr[mid] >= target:
                right = mid - 1
        if left + 1 < len(self.arr) and self.arr[left + 1] == target:
            return left + 1
        else:
            return left
            

    # 9 upperfloor 即<=target的最大索引。
    # #两者区别是是数组中存在元素，一个返回最小索引，一个返回最大索引
    def upper_floor(self, target):
        left = -1
        right = len(self.arr) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if self.arr[mid] <= target:
                left = mid
            elif self.arr[mid] > target:
                right = mid - 1
        return left


if __name__ == '__main__':
    nums = [1, 2, 2, 4, 4, 6, 7, 7, 9]
    nums2 = [1, 2, 4, 5, 9, 10]
    a = BinarySearch(nums2)
    print(a.binary_search(4))
    print(a.binary_search_iteration(4))
    print(a.binary_search2(4))
    print(a.upper(10))
    print(a.upper_ceil(10))
    b = BinarySearch(nums)
    print(b.lower_ceil(6))
