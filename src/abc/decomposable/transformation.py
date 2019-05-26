import abc

from src.abc.static import Static


class Transformation(abc.ABC):

    def __init__(self, struct):
        if type(struct) != type(Static):
            raise ValueError("Structure is not Static")

        self._p          = [None]
        self._insertions = set()
        self._struct     = struct

    def __len__(self):
        return len(self._insertions)

    @abc.abstractmethod
    def insert(self, x):
        raise NotImplementedError(
            "Must implement 'insert' function to use this base class")

    def query(self, x):
        if x is None:
            raise ValueError("Illegal argument of None Type")

        res = set()
        for p in self._p:
            if p is not None:
                res.update(p.query(x))
        return res

    def all(self):
        res = set()
        for p in self._p:
            if p is not None:
                res.update(p.unbuild())
        return res
