class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{}:{}".format(self.key, self.val)


class BSTMap:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add(self, key, val):
        self.root = self.__add(self.root, key, val)
        return self.root

    def __add(self, node, key, val):
        if node is None:
            self.size += 1
            return TreeNode(key, val)
        if key < node.key:
            node.left = self.__add(node.left, key, val)
        elif key > node.key:
            node.right = self.__add(node.right, key, val)
        else:
            node.val = val

        return node

    def __get_node(self, node, key):  # return node which contains key
        if not node:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self.__get_node(node.left, key)
        else:
            return self.__get_node(node.right, key)

    def contains(self, key):
        return self.__get_node(self.root, key) is not None

    def get(self, key):  # return key's val
        node = self.__get_node(self.root, key)
        return node.val if node else None

    def set(self, key, new_val):
        node = self.__get_node(self.root, key)
        if not node:
            raise ValueError("{} is not exist".format(key))
        node.val = new_val

    def remove(self, key):  # return key:val pair
        node = self.__get_node(self.root, key)
        if node:
            self.root = self.__remove(self.root, key)
            return node
        return None

    def __mini(self, node):
        if node.left is None:
            return node
        return self.__mini(node.left)

    def __remove_mini(self, node):
        if node.left is None:
            right_node = node.right
            node.right = None
            self.size -= 1
            return right_node

    def __remove(self, node, key):  # return the new node which removed the key
        if node is None:
            return None
        if key < node.key:
            node.left = self.__remove(node.left, key)
            return node
        elif key > node.key:
            node.right = self.__remove(node.right, key)
            return node
        else:
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
            successor = self.__mini(node.right)
            successor.right = self.__remove_mini(node.right)
            successor.left = node.left
            return successor

    def __str__(self):
        res = {}
        self.inorder_display_tree(self.root, res)
        return str(res)

    def inorder_display_tree(self, node, res):
        if node is None:
            return
        self.inorder_display_tree(node.left, res)
        res[node.key] = node.val
        self.inorder_display_tree(node.right, res)
        return res


if __name__ == '__main__':
    map1 = BSTMap()
    for i in range(6):
        map1.add(i+2, i)
    print(map1)
    map1.remove(1)
    print(map1)
    print(map1.contains(2))
    print(map1.get(5))
