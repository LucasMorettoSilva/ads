import abc

from src.abc.static import Static


class StaticToDynamic(abc.ABC):

    def __init__(self, struct):
        if type(struct) != type(Static):
            raise ValueError("Structure is not Static")

        self.__p          = [None]
        self.__high       = 0
        self.__insertions = set()
        self.__struct     = struct

    def __len__(self):
        return len(self.__insertions)

    def insert(self, x):
        if x is None:
            raise ValueError("Illegal argument of None Type")

        if x in self.__insertions:
            return

        self.__insertions.add(x)
        s = set()
        s.add(x)
        i = 0
        while self.__p[i] is not None:
            s.update(self.__p[i].unbuild())
            self.__p[i] = None
            i += 1
        self.__p[i] = self.__struct(s)
        if i  == self.__high:
            self.__high += 1
            self.__p.append(None)

    def query(self, x):
        if x is None:
            raise ValueError("Illegal argument of None Type")

        res = set()
        for p in self.__p:
            if p is not None:
                res.update(p.query(x))
        return res

    def all(self):
        res = set()
        for p in self.__p:
            if p is not None:
                res.update(p.unbuild())
        return res
