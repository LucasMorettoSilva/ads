from enum import Enum

import math

from src.graph.forest import Forest


class DynamicGraph:

    class Edge(Enum):
        TREE     = 0,
        NON_TREE = 1

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
        self.logn = math.ceil(math.log(n, 2))
        self.F = [None] * (self.logn + 1)
        for i in range(self.logn + 1):
            self.F[i] = Forest(i)

        self.edges    = [None] * 2
        self.edges[0] = [[[]] * (self.logn + 1)] * n
        self.edges[1] = [[[]] * (self.logn + 1)] * n
        self.level    = dict()
        self.iterator = dict()

    def insert(self, u, v):
        if not self.F[self.logn].connected(u, v):
            self.__insert(u, v, self.logn, self.Edge.TREE)
        else:
            self.__insert(u, v, self.logn, self.Edge.NON_TREE)

    def __insert(self, u, v, l, edge):
        uv = self.Pair(u, v)
        vu = self.Pair(v, u)
        # self.edges[edge][u][l][v] = self.edges[edge][u][l]
        # TODO
        self.level[vu] = l
        self.level[uv] = l
        if edge == self.Edge.TREE:
            self.F[l].mark_white(u)
            self.F[l].mark_white(v)
            for i in range(l, self.logn + 1):
                self.F[i].link(u, v)
        else:
            self.F[l].mark_black(u)
            self.F[l].mark_black(v)

