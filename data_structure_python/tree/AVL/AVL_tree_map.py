# 平衡二叉树：对于任意一个节点，左子树和右子树的高度差不能超过1
# AVL:平衡二分搜索树

class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.height = 1

    def __str__(self):
        return "{}:{}".format(self.key, self.val)


class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    # if the avl tree is a bst tree
    def is_bst(self):
        lst = []
        self._inorder(self.root, lst)
        for i in range(1, self.size):
            if lst[i - 1] > lst[i]:
                return False
        return True

    def _inorder(self, node, lst):
        if node is None:
            return
        self._inorder(node.left, lst)
        lst.append(node.key)
        self._inorder(node.right, lst)

    # if the AVL tree is a balanced tree
    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, node):
        if node is None:
            return True
        balance_fac = self.get_balance_factor(node)
        if abs(balance_fac) > 1:
            return False
        return self._is_balanced(node.left) and self._is_balanced(node.right)

    # get the node's height
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    # 对节点y进行向右旋转操作。返回旋转后的新的根节点x
    #        y                        x
    #      /   \                   /    \
    #     x     T4                z      y
    #    /  \        右旋转>>>>   /  \    /  \
    #   z   T3                  T1  T2  T3  T4
    #  / \
    # T1  T2
    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        x.right = y

        # update height, update y's height first
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    # 对节点y进行向左旋转操作。返回旋转后的新的根节点x
    #        y                         x
    #      /   \                      /  \
    #     T1    x                   y      z
    #          /  \   左旋转>>>>   /  \    /  \
    #         T2   z             T1  T2  T3  T4
    #              / \
    #             T3  T4

    def _left_rotate(self, y):
        x = y.right
        y.right = x.left
        x.left = y
        # update height, update y's height first
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    # get node's balance factor
    def get_balance_factor(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def add(self, key, val):
        if self.root is None:
            self.root = TreeNode(key, val)
        else:
            self.root = self._add(self.root, key, val)

    def _add(self, node, key, val):
        if node is None:
            self.size += 1
            return TreeNode(key, val)
        if key < node.key:
            node.left = self._add(node.left, key, val)
        elif key > node.key:
            node.right = self._add(node.right, key, val)
        else:
            node.val = val

        # update the node's height
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        # calculate balanced factor
        balanced_fac = self.get_balance_factor(node)

        # maintain the balance
        # LL，插入的元素在不平衡的节点的左侧的左侧
        if balanced_fac > 1 and self.get_balance_factor(node.left) >= 0:
            return self._right_rotate(node)
        # RR，插入的元素在不平衡的节点的右侧的右侧
        if balanced_fac < -1 and self.get_balance_factor(node.right) <= 0:
            return self._left_rotate(node)
        # LR，插入的元素在不平衡的节点的左侧的右侧
        # 先转成LL
        if balanced_fac > 1 and self.get_balance_factor(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # RL，插入的元素在不平衡的节点的右侧的左侧
        # 先转成RR
        if balanced_fac < -1 and self.get_balance_factor(node.right) < 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    # return the node which key is key
    def _get_node(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._get_node(node.left, key)
        else:
            return self._get_node(node.right, key)

    # return the minimum in the tree which root is node
    def _mini(self, node):
        if node.left is None:
            return node
        return self._mini(node.left)

    # delete key in the tree which root is node
    # return the new tree node :ret_node
    def _remove(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
            ret_node = node
        elif key > node.key:
            node.right = self._remove(node.right, key)
            ret_node = node
        # find the node which will be deleted
        else:
            if node.left is None:  # the node's left is None
                right_node = node.right
                node.right = None
                self.size -= 1
                ret_node = right_node
            elif node.right is None:
                left_node = node.left
                node.left = None
                self.size -= 1
                ret_node = left_node
            else:
                successor = self._mini(node.right)
                successor.right = self._remove(node.right, successor.key)
                successor.left = node.left
                node.left = node.right = None
                ret_node = successor
        if ret_node is None:
            return None

        # update the node's height
        ret_node = 1 + max(self.get_height(ret_node.left), self.get_height(ret_node.right))

        # calculate balanced factor
        balanced_fac = self.get_balance_factor(ret_node)

        # maintain the balance
        # LL，插入的元素在不平衡的节点的左侧的左侧
        if balanced_fac > 1 and self.get_balance_factor(ret_node.left) >= 0:
            return self._right_rotate(ret_node)
        # RR，插入的元素在不平衡的节点的右侧的右侧
        if balanced_fac < -1 and self.get_balance_factor(ret_node.right) <= 0:
            return self._left_rotate(ret_node)
        # LR，插入的元素在不平衡的节点的左侧的右侧
        # 先转成LL
        if balanced_fac > 1 and self.get_balance_factor(ret_node.left) < 0:
            ret_node.left = self._left_rotate(ret_node.left)
            return self._right_rotate(ret_node)

        # RL，插入的元素在不平衡的节点的右侧的左侧
        # 先转成RR
        if balanced_fac < -1 and self.get_balance_factor(ret_node.right) < 0:
            ret_node.right = self._right_rotate(ret_node.right)
            return self._left_rotate(ret_node)

        return ret_node

    def remove(self, key):
        if self.root is None:
            raise KeyError("Empty Tree")
        else:
            return self._remove(self.root, key)

    def _inorder2(self, node, dic):
        if node is None:
            return
        self._inorder2(node.left, dic)
        dic[node.key] = node.val
        self._inorder2(node.right, dic)

    def __str__(self):
        rest = {}
        self._inorder2(self.root, rest)
        return str(rest)


if __name__ == '__main__':
    tree = AVLTree()
    tree.add(6,6)
    tree.add(8,8)
    tree.add(10,10)
    print(tree)
