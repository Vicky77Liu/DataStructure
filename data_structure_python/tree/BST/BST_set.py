from tree.BST.binary_search_tree import BST


class BSTSet():
    def __init__(self):
        self.bst = BST()

    def __len__(self):
        return self.bst.size

    def is_empty(self):
        return self.bst.is_empty()

    def add(self, val):
        self.bst.add(val)

    def contains(self, val):
        return self.bst.contains(val)

    def remove(self, val):
        self.bst.remove(val)

    def __str__(self):
        return str(self.bst.display_tree())


if __name__ == '__main__':
    set1 = BSTSet()
    for i in range(5):
        set1.add(i*i+2)
    print(set1)




