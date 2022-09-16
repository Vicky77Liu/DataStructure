# AVL

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0

    def __str__(self):
        return str(self.val)


class AVLTree:
    def __init__(self):
        self.root = None

    def find(self, key):
        if not self.root:
            return None
        else:
            return self._find(key, self.root)

    def _find(self, key, node):
        if not node:
            return None
        elif key < node.val:
            return self._find(key, node.left)
        elif key > node.val:
            return self._find(key, node.right)
        else:  # key = node.val
            return node

    def find_min(self):
        if self.root is None:
            return None
        else:
            return self._find_min(self.root)

    def _find_min(self, node):
        if node.left is None:
            return node
        return self._find_min(node.left)

    def find_max(self):
        if self.root is None:
            return None
        else:
            return self._find_max(self.root)

    def _find_max(self, node):
        if node.right is None:
            return node
        return self._find_max(node.right)

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    # LL:在node节点的左孩子 k1 的左子树 添加了新节点，左旋转
    def left_left_rotate(self, node):
        k1 = node.left
        node.left = k1.right
        k1.right = node
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        k1.height = max(self.height(k1.left), self.height(k1.right)) + 1
        return k1  # 新的节点的根

    # RR:在node节点的右孩子 k1 的右子树 添加了新节点，右旋转
    def right_right_rotate(self, node):
        k1 = node.right
        node.right = k1.left
        k1.left = node
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        k1.height = max(self.height(k1.left), self.height(k1.right)) + 1
        return k1  # 新的节点的根

    # LR:在node节点的左孩子的右子树添加新节点，先左旋再右旋
    def left_right_rotate(self, node):
        node.left = self.left_left_rotate(node.left)
        return self.right_right_rotate(node)

    # RL:在node节点的右孩子的左子树添加新节点，先右旋再左旋
    def right_left_rotate(self, node):
        node.right = self.right_right_rotate(node.right)
        return self.left_left_rotate(node)

    def add(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self.root = self._add(key, self.root)

    def _add(self, key, node):
        if node is None:
            node = TreeNode(key)
        elif key < node.val:
            node.left = self._add(key, node.left)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if key < node.left.val:
                    node = self.left_left_rotate(node)
                else:
                    node = self.left_right_rotate(node)
        elif key > node.val:
            node.right = self._add(key, node.right)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if key > node.right.val:
                    node = self.right_right_rotate(node)
                else:
                    node = self.right_left_rotate(node)

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return node

    def delete(self, key):
        if self.root is None:
            raise KeyError('Empty Tree')
        else:
            self.root = self._delete(key, self.root)

    def _delete(self, key, node):
        if node is None:
            raise KeyError('Error,Key not in tree')
        elif key < node.val:
            node.left = self._delete(key, node.left)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if self.height(node.right.right) >= self.height(node.right.left):
                    node = self.right_right_rotate(node)
                else:
                    node = self.right_left_rotate(node)

            node.height = max(self.height(node.left), self.height(node.right)) + 1

        elif key > node.val:
            node.right = self._delete(key, node.right)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if self.height(node.left.left) >= self.height(node.left.right):
                    node = self.left_left_rotate(node)
                else:
                    node = self.left_right_rotate(node)

            node.height = max(self.height(node.left), self.height(node.right)) + 1

        elif node.left and node.right:
            if node.left.height <= node.right.height:
                min_node = self._find_min(node.right)
                node.key = min_node.key
                node.right = self._delete(node.key, node.right)

            else:
                max_node = self._find_max(node.left)
                node.key = max_node.key
                node.left = self._delete(node.key, node.left)
            node.height = max(self.height(node.left), self.height(node.right)) + 1

        else:
            if node.right:
                node = node.right
            else:
                node = node.left

        return node

    def _inorder(self, node, lst):
        if node is None:
            return
        self._inorder(node.left, lst)
        lst.append(node.val)
        self._inorder(node.right, lst)

    def __str__(self):
        lst = []
        self._inorder(self.root, lst)
        return str(lst)


if __name__ == '__main__':
    # n = list(map(int,input().split()))
    n = [6, 8, 10]
    avl = AVLTree()
    for i in range(len(n)):
        avl.add(n[i])

    print(avl)
