import abc

from src.abc.decomposable.decomposable_sp import DecomposableSP


class Transformation(abc.ABC):

    def __init__(self):
        self._p          = [None]
        self._insertions = set()
        self._struct     = None

    def __len__(self):
        return len(self._insertions)

    def init(self, static):
        if type(static) != type(DecomposableSP):
            raise ValueError("Structure is not Static")
        self._struct = static

    @abc.abstractmethod
    def insert(self, x):
        raise NotImplementedError(
            "Must implement 'insert()' function to use this base class")

    def query(self, x):
        if x is None:
            raise ValueError("Illegal argument of None Type")

        res = set()
        for p in self._p:
            if p is not None:
                res = self._struct.operator(res, p.query(x))
        return res

    def all(self):
        res = set()
        for p in self._p:
            if p is not None:
                res.update(p.unbuild())
        return res
