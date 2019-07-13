from enum import IntEnum

import random


class Forest:

    class Color(IntEnum):
        BLACK = 0,
        WHITE = 1

    class Node:

        def __init__(self, priority, label = -1):
            self.priority = priority
            self.label    = label

            self.left   = None
            self.right  = None
            self.parent = None

            self.size = 1
            self.greater_p = False
            self.marks = [0, 0]
            self.sub_marks = [0, 0]

        def root(self):
            cur = self
            while cur.parent:
                cur = cur.parent
            return cur

        def refresh(self):
            self.size = 1
            self.sub_marks[Forest.Color.WHITE] = self.marks[Forest.Color.WHITE]
            self.sub_marks[Forest.Color.BLACK] = self.marks[Forest.Color.BLACK]
            if self.left:
                self.size += self.left.size
                self.sub_marks[Forest.Color.WHITE] += self.left.sub_marks[Forest.Color.WHITE]
                self.sub_marks[Forest.Color.BLACK] += self.left.sub_marks[Forest.Color.BLACK]
            if self.right:
                self.size += self.right.size
                self.sub_marks[Forest.Color.WHITE] += self.right.sub_marks[Forest.Color.WHITE]
                self.sub_marks[Forest.Color.BLACK] += self.right.sub_marks[Forest.Color.BLACK]

    class Pair:

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __hash__(self):
            return 31 * hash(self.x) + hash(self.y)

        def __getitem__(self, i):
            if i == 0:
                return self.x
            if i == 1:
                return self.y
            raise ValueError()

    def __init__(self, n):
        self.dic = dict()
        for i in range(n):
            self.dic[self.Pair(i, i)] = self.Node(random.uniform(0, 10000), i)

    def reroot(self, v):
        w = self.dic[self.Pair(v, v)]
        k = self.__order(w)
        root = w.root()
        spl  = self.split(root, k - 1)
        return self.merge(spl[1], spl[0])

    def link(self, u, v):
        self.dic[self.Pair(u, v)] = self.Node(random.uniform(0, 10000))
        self.dic[self.Pair(v, u)] = self.Node(random.uniform(0, 10000))
        uv = self.dic[self.Pair(u, v)]
        vu = self.dic[self.Pair(v, u)]
        nu = self.reroot(u)
        nv = self.reroot(v)
        self.merge(nu, self.merge(uv, self.merge(nv, vu)))

    def remove(self, u, v):
        uv = self.dic[self.Pair(u, v)]
        vu = self.dic[self.Pair(v, u)]
        root = uv.root()
        left = self.__order(uv)
        right = self.__order(vu)
        if left > right:
            left, right = right, left
        tmp = self.split(root, right)
        ur = tmp[1]
        tmp = self.split(tmp[0], left - 1)
        ul = tmp[0]
        vm = tmp[1]
        self.merge(ul, ur)

        tmp = self.split(vm, vm.size - 1)
        tmp = self.split(tmp[0], 1)
        del self.dic[self.Pair(u, v)]
        del self.dic[self.Pair(v, u)]

    def connected(self, u, v):
        return self.dic[self.Pair(u, v)].root() is self.dic[self.Pair(v, u)].root()

    def has_edge(self, u, v):
        return self.Pair(u, v) in self.dic

    def size(self, u):
        sz = self.dic[self.Pair(u, u)].root().size
        return (sz + 2) / 3

    def mark_white(self, u):
        self.__mark(u, self.Color.WHITE, 1)

    def mark_black(self, u):
        self.__mark(u, self.Color.BLACK, 1)

    def unmark_white(self, u):
        self.__mark(u, self.Color.WHITE, -1)

    def unmark_black(self, u):
        self.__mark(u, self.Color.BLACK, -1)

    def __mark(self, u, color, d):
        node = self.dic[self.Pair(u, u)]
        node.marks[color] += d
        while node:
            node.sub_marks[color] += d
            node = node.parent

    def split(self, node, k):
        if node is None:
            return [None, None]

        less = 0
        if node.left:
            less = node.left.size

        if less < k:
            spl  = self.split(node.right, k - less - 1)
            left  = spl[0]
            right = spl[1]
            node.right = left
            if left:
                left.parent = node
                left.greater_p = True
            node.parent = None
            node.refresh()
            return [node, right]
        else:
            spl = self.split(node.left, k)
            left  = spl[0]
            right = spl[1]
            node.left = right
            if right:
                right.parent = node
                right.greater_p = False
            node.parent = None
            node.refresh()
            return [left, node]

    def merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        if a.priority < b.priority:
            node = self.merge(a, b.left)
            b.left = node
            b.refresh()
            node.parent = b
            node.greater_p = False
            return b

        node = self.merge(a.right, b)
        a.right = node
        a.refresh()
        node.parent = a
        node.greater_p = True
        return a

    @staticmethod
    def __order(x):
        qt = 0
        le = True
        cur = x
        while cur:
            if le:
                qt += 1
                if cur.left:
                    qt += cur.left.size
            le = cur.greater_p
            cur = cur.parent
        return qt
