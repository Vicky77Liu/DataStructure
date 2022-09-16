class UnionFindSet(object):
    def __init__(self, data_list):
        self.father = {}
        self.size = {}

        for node in data_list:
            self.father[node] = node
            self.size[node] = 1

    def find(self, node):
        father = self.father[node]
        if node != father:
            if father != self.father[father]:
                self.size[father] -= 1
            father = self.find(father)

        self.father[node] = father
        return father

    def is_connected(self, node_a, node_b):
        return self.find(node_a) == self.find(node_b)

    def union(self, node_a, node_b):
        if node_a is None and node_b is None:
            return

        a_root = self.find(node_a)
        b_root = self.find(node_b)

        if a_root != b_root:
            a_size = self.size[a_root]
            b_size = self.size[b_root]

            if a_size < b_size:
                self.father[a_root] = b_root
                self.size[b_root] = b_size + a_size
            else:
                self.father[b_root] = a_root
                self.size[a_root] = a_size + b_size


if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9]
    a = UnionFindSet(lst)
    print(a.size)
    print(a.father)
    print("000000000000")
    a.union(1, 3)
    print(a.size)
    print(a.father)

    print(a.find(3))

    print(a.size)
    print(a.father)
    print("000000000000")
    a.union(1, 7)
    print(a.size)
    print(a.father)
