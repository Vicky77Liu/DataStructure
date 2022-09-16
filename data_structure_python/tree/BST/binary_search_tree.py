import queue


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class BST(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add(self, val):
        self.root = self._add(self.root, val)
        return self.root

    def _add(self, node, val):  # 向以node为根的二分搜索数插入元素val，返回插入新节点后二分搜索数的根
        if node is None:
            self.size += 1
            return TreeNode(val)
        if val == node.val:
            pass
        else:
            if val < node.val:
                node.left = self._add(node.left, val)
            else:
                node.right = self._add(node.right, val)
        return node

    def add2(self, val):  # iterate
        if self.root is None:
            self.root = TreeNode(val)
            self.size += 1
            return
        p = self.root
        while p:
            if val < p.val:
                if p.left is None:
                    p.left = TreeNode(val)
                    self.size += 1
                    return
                p = p.left
            elif val > p.val:
                if p.right is None:
                    p.right = TreeNode(val)
                    self.size += 1
                    return
                p = p.right
            else:
                return

    def contains(self, val):
        return self._contains(self.root, val)

    def _contains(self, node, val):
        if node is None:
            return False
        if val == node.val:
            return True
        elif val > node.val:
            return self._contains(node.right, val)
        else:
            return self._contains(node.left, val)

    def remove(self, val):
        self.root = self.__remove(self.root, val)
        return self.root

    def __remove(self, node, val):  # 删除以node为根的值为val的二分搜索树中的节点，返回删除节点后新的二分搜索树的根
        if node is None:
            return None
        if val < node.val:
            node.left = self.__remove(node.left, val)
            return node
        elif val > node.val:
            node.right = self.__remove(node.right, val)
            return node
        else:  # val == node.val
            if node.left is None:
                right_node = node.right
                node.right = None
                self.size -= 1
                return right_node

            if node.right is None:
                left_node = node.left
                node.left = None
                self.size -= 1
                return left_node
            successor = self.__mini(node.right)  # 待删除节点左右子树均不为空，找到比待删除节点大的最小节点（待删除节点的右子树最小节点），
            # 用这个节点顶替待删除节点

            successor.right = self.__remove_mini(node.right)  # 删除了node.right子树中的最小值后的树
            # 这里本来应该写size+=1 因为在removemin中减去一次
            successor.left = node.left
            node.left = node.right = None
            #       这里本来应该写size-=1 这个时候才是真正删除掉节点，但是上面有一次size+，因此抵消不写了

            return successor

    def remove_mini(self):
        rest = self.mini()
        self.root = self.__remove_mini(self.root)
        return rest

    def __remove_mini(self, node):
        if node.left is None:
            right_node = node.right
            node.right = None
            self.size -= 1
            return right_node
        node.left = self.__remove_mini(node.left)
        return node

    def remove_maxi(self):
        rest = self.maxi()
        self.root = self.__remove_maxi(self.root)
        return rest

    def __remove_maxi(self, node):
        if node.right is None:
            left_node = node.left
            node.left = None
            self.size -= 1
            return left_node
        node.right = self.__remove_maxi(node.right)
        return node

    def mini(self):  # 寻找二分搜索数的最小值，一直向左走走不动的那个元素
        if self.size == 0:  # 捕获异常的需要再重新写
            raise ValueError('BST IS EMPTY')
        return self.__mini(self.root).val
    #   return self.__mini2(self.root).val

    def __mini(self, node):  # recursion
        if not node.left:
            return node
        return self.__mini(node.left)

    def __mini2(self, node):  # iterate
        if not node.left:
            return node
        while node.left:
            node = node.left
        return node

    def maxi(self):  # 寻找二分搜索数的最大值，一直向右走走不动的那个元素
        if self.size == 0:  
            raise ValueError('BST IS EMPTY')
        return self.__maxi(self.root).val

    def __maxi(self, node):  # recursion
        if not node.right:
            return node
        return self.__maxi(node.right)

    def __maxi2(self, node):  # iterate
        if not node.right:
            return node
        while node.right:
            node = node.right
        return node

    # floor:给定一个key，寻找比key小，但在所有比key小的元素中的最大值
    # ceil：给定一个key，寻找比key大，但在所有比key大的元素中的最小值
    def get_floor_and_ceil(self, key):
        return self.__get_floor_and_ceil(self.root, key)

    def __get_floor_and_ceil(self, node, key, floor=None, ceil=None):
        if node is not None:
            if node.val == key:
                floor = key
                ceil = key
                return floor, ceil
            else:
                if node.val < key:
                    floor = node.val
                    return self.__get_floor_and_ceil(node.right, key, floor, ceil)
                else:
                    ceil = node.val
                    return self.__get_floor_and_ceil(node.left, key, floor, ceil)
        else:
            return floor, ceil

    def pre_order(self):
        self.__pre_order(self.root)

    def __pre_order(self, node):
        if node is None:
            return
        print(node.val)
        self.__pre_order(node.left)
        self.__pre_order(node.right)

    def pre_order_iter(self):  # 前序遍历的非递归实现
        stack = [self.root]
        while len(stack) != 0:
            cur = stack.pop()
            print(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

    def in_order(self):  # 中序遍历
        self.__in_order(self.root)

    def __in_order(self, node):
        if node is None:
            return
        self.__in_order(node.left)
        print(node.val)
        self.__in_order(node.right)

    def post_order(self):
        self.__post_order(self.root)

    def __post_order(self, node):
        if node is None:
            return
        self.__post_order(node.left)
        self.__post_order(node.right)
        print(node.val)

    def level_order(self):
        q = queue.Queue()
        q.put(self.root)
        while q.qsize() != 0:
            cur = q.get()
            print(cur.val)
            if cur.left:
                q.put(cur.left)
            if cur.right:
                q.put(cur.right)

    def display_tree(self):  # 中序遍历
        res = []
        self.__display_tree(self.root, res)
        return res

    def __display_tree(self, node, res):
        if node is None:
            return
        self.__display_tree(node.left, res)
        res.append(node.val)
        self.__display_tree(node.right, res)
        return res


if __name__ == '__main__':
    tree = BST()
    for i in range(5):
        tree.add(i)
        tree.add(i*i)
    tree.pre_order()
    print("-----------")
    for i in range(7,15):
        tree.add(i+2)
    tree.in_order()
    print("-----------")
    for i in range(5):
        tree.remove(i)
    tree.post_order()


