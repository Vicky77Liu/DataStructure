# 数据实现线段树,线段树的每一个节点存储的是一个区间相应的信息
# 线段树是平衡二叉树，不是满二叉树和完全二叉树


class SegTree:
    def __init__(self, nums, function):
        self.nums = nums
        self.n = len(self.nums)
        self.tree = [0 for _ in range(4 * self.n)]
        self.function = function  # 线段树所承载的功能，例如最大最小值，和之类的
        if self.n > 0:
            self.__build(0, 0, self.n - 1)

    def __len__(self):
        return self.n

    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2

    def update(self, index, new_value):
        if index < 0 or index >= self.n:
            raise IndexError("Index is out of range")
        self.nums[index] = new_value
        self.__update(0, 0, self.n - 1, index, new_value)

    # 返回区间【query_l,query_r]的值
    def query(self, query_l, query_r):
        if query_l < 0 or query_r < 0 or query_l >= self.n or query_r >= self.n or query_l > query_r:
            raise IndexError('Invalid index')
        return self.__query(0, 0, self.n - 1, query_l, query_r)

    # 在tree_index位置创建表示区间【l...r】的线段树
    def __build(self, tree_index, l, r):
        if l == r:
            self.tree[tree_index] = self.nums[r]
            return
        mid = (l + r) // 2
        left_tree = self._left_child(tree_index)
        right_tree = self._right_child(tree_index)
        self.__build(left_tree, l, mid)
        self.__build(right_tree, mid + 1, r)
        self.tree[tree_index] = self.function(self.tree[left_tree], self.tree[right_tree])

    def __update(self, tree_index, l, r, index, new_value):
        if l == r == index:
            self.tree[tree_index] = new_value
            return
        mid = l + (r - l) // 2
        left_tree = self._left_child(index)
        right_tree = self._right_child(tree_index)
        if index <= mid:
            self.__update(left_tree, l, mid, index, new_value)
        else:
            self.__update(right_tree, mid + 1, r, index, new_value)
        self.tree[tree_index] = self.function(self.tree[left_tree], self.tree[right_tree])

    # 在tree_index为根的线段树【l...r】的范围里，搜索区间[query_l,query_r]的值
    def __query(self, tree_index, l, r, ql, qr):
        if l == ql and r == qr:
            return self.tree[tree_index]
        mid = l + (r - l) // 2
        left_tree = self._left_child(tree_index)
        right_tree = self._right_child(tree_index)
        if qr <= mid:
            return self.__query(left_tree, l, mid, ql, qr)
        elif mid < ql:
            return self.__query(right_tree, mid + 1, r, ql, qr)
        else:
            return self.function(self.__query(left_tree, l, mid, ql, mid),
                                 self.__query(right_tree, mid + 1, r, mid + 1, qr))


class NumArray:
    def __init__(self, nums):
        self.ST = SegTree(nums, lambda x, y: x + y)

    def update(self, index, val):
        self.ST.update(index, val)

    def sum_range(self, query_l, query_r):
        return self.ST.query(query_l, query_r)


if __name__ == '__main__':
    obj = NumArray([8, 1, 3, 2, 5, 11, 9])
    print(obj.sum_range(0, 3))
    print(obj.update(1, 2))
    print(obj.sum_range(2, 4))
