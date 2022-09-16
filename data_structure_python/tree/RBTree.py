"""A red_black tree is a binary tree that satisfies the following red-black properties:
1, Every node is either red or black
2, The root is black
3, Every leaf (and node is none) is black
4, If a node is red, then both its children are black
5, For each node, all simple paths from the node to descendant leaves contain the same number of black nodes
红黑树是保持"黑平衡"的二叉树
"""

RED = True
BLACK = False


class TreeNode:
    def __init__(self, key, val, color=RED):
        self.key = key
        self.val = val
        self.color = color
        self.left = None
        self.right = None
    def __str__(self):
        return "{}:{}".format(self.key,self.val)

class RBTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def __len__(self):
        return self.size
    def is_red(self, node):
        if node is None:
            return BLACK
        return node.color

    # 对节点node进行向左旋转操作。返回旋转后的新的根节点x
    #       node                       x
    #      /   \                      /  \
    #     T1    x                  node    z
    #          /  \   左旋转>>>>   /  \
    #         T2   z             T1  T2
    def _left_rotate(self, node):
        x = node.right

        # left rotate
        node.right = x.left
        x.left = node

        x.color = node.color
        node.color = RED
        return x

    # 对节点node进行向右旋转操作。返回旋转后的新的根节点x
    #       node                     x
    #      /   \                   /    \
    #     x     T4                z     node
    #    /  \        右旋转>>>>          /  \
    #   z   T3                         T3  T4

    def _right_rotate(self, node):
        x = node.left
        # right rotate
        node.left = x.right
        x.right = node

        x.color = node.color
        node.color = RED
        return x

    def _flip_colors(self, node):
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK

    def add(self, key, val):
        self.root = self._add(self.root, key, val)
        self.root.color = BLACK

    def _add(self, node, key, val):
        if node is None:
            self.size += 1
            return TreeNode(key, val)

        if key > node.key:
            node.right = self._add(node.right, key, val)
        elif key < node.key:
            node.left = self._add(node.left, key, val)
        else:
            node.val = val

        # 维护黑平衡
        if self.is_red(node.right) and not self.is_red(node.left):
            node = self._left_rotate(node)

        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self._right_rotate(node)

        if self.is_red(node.left) and self.is_red(node.right) :
            self._flip_colors(node)

        return node

    def _inorder(self, node, dic):
        if node is None:
            return
        self._inorder(node.left, dic)
        dic[node.key] = node.val
        self._inorder(node.right, dic)

    def __str__(self):
        rest = {}
        self._inorder(self.root, rest)
        return str(rest)


if __name__ == '__main__':
    nodes = [5, 1, 3, 9, 4]
    RBT = RBTree()

    for node in nodes:
        RBT.add(node, node)
    print(RBT)
    print(len(RBT))
