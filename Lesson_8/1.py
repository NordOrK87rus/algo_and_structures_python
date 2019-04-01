"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

from collections import Counter


class Huffman(object):
    class Node:
        def __init__(self, left=None, right=None):
            self.left = left
            self.right = right
            self.weight = left[1] + right[1]

    def __init__(self, data):
        self.data = data
        self.encode_table = dict()
        self.tree = sorted(Counter(self.data).items(), key=lambda c: c[1])
        self.build_tree()
        self.encode_path(self.tree[0])

    def __repr__(self):
        return " ".join([self.encode_table[c] for c in self.data])

    def c_freq(self):
        while len(self.tree) > 1:
            yield self.tree.pop(0), self.tree.pop(0)

    def build_tree(self):
        for p1, p2 in self.c_freq():
            n = self.Node(left=p1, right=p2)

            for i, item in enumerate(self.tree):
                if n.weight > item[1]:
                    continue
                else:
                    self.tree.insert(i, (n, n.weight))
                    break
            else:
                self.tree.append((n, n.weight))

    def encode_path(self, obj, bin_path=''):
        if not isinstance(obj[0], Huffman.Node):
            self.encode_table[obj[0]] = bin_path
        else:
            self.encode_path(obj[0].left, bin_path=f"{bin_path}0")
            self.encode_path(obj[0].right, bin_path=f"{bin_path}1")


s = "beep boop beer!"
print(f"Исходная строка: {s}")

h = Huffman(s)
print(h)
