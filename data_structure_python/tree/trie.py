# Trie  字典树/前缀树
import collections


class TreeNode(object):
    def __init__(self):
        # initialize data structure
        self.data = {}
        self.is_word = False

    def __str__(self):
        return str(self.data)


class Trie(object):
    def __init__(self):
        self.root = TreeNode()
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.root)

    def add(self, word):
        node = self.root  # 插入节点时从根节点开始判断，根节点是一个空字典
        for char in word:
            child = node.data.get(char)
            if not child:  # 如果当前节点没有该元素，则增加节点
                node.data[char] = TreeNode()
            node = node.data[char]  # 判断节点下移
        if node.is_word is False:
            node.is_word = True
            self.size += 1

    # 查询但是是否在trie中
    def search(self, word):
        node = self.root
        for char in word:
            node = node.data.get(char)
            if not node:
                return False
        # 直接返回true不能保证单词存在在trie中，例如panda存在，而查询pan必须看n是否存储的isWord
        return node.isword

    # 查询trie中是否有单词以prefix为前缀
    def start_with(self, prefix):
        node = self.root
        for char in prefix:
            if node.data.get(char) is None:
                return False
            node = node.data.get(char)
        return True


"""class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.next = collections.defaultdict(TrieNode)

    def __str__(self):
        return str(self.next)


class Trie2(object):
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def __str__(self):
        return str(self.root)
    def add(self, word):
        cur = self.root
        for c in word:
            cur = cur.next[c]

        cur.isWord = True

    def contains(self, word):
        cur = self.root
        for c in word:
            cur = cur.next.get(c)
            if cur is None:
                return False
            cur = cur.next.get(c)

        return cur.isWord

    def isPrefix(self, prefix):
        cur = self.root
        for c in prefix:
            cur = cur.next.get(c)
            if cur is None:
                return False
        return True"""

if __name__ == '__main__':
    p = Trie()
    p.add("hello")
    # p.add("world")
    # p.add("help")
    print(p)
