import math

from src.abc.decomposable.decomposable_sp import DecomposableSP


class DynamicDeletion:

    def __init__(self, static, data):
        if static is None:
            raise ValueError("Invalid argument 'static' of None Type")

        if type(static) != type(DecomposableSP):
            raise ValueError("Structure is not DecomposableSP")

        if data is None:
            raise ValueError("Invalid argument 'data' of None Type")

        self.__static = static
        self.__p = list()
        self.__r = dict()
        data = set(data)

        if len(data) > 0:
            content = list()
            m = math.sqrt(len(data))
            for e in data:
                if len(content) == m:
                    self.__p.append(static(content))
                    content = list()
                content.append(e)
                self.__r[e] = len(self.__p)

    def __len__(self):
        return len(self.__r)

    def query(self, x):
        if x is None:
            raise ValueError("Illegal argument of None Type")

        res = set()
        for p in self.__p:
            if p is not None:
                res = self.__static.operator(res, p.query(x))
        return res

    def delete(self, x):
        if x is None:
            raise ValueError("Illegal argument of None Type")

        if x not in self.__r:
            return

        s = self.__p[self.__r[x]].unbuild()
        s.remove(x)

        self.__p[self.__r[x]] = self.__static(s)
        del self.__r[x]
