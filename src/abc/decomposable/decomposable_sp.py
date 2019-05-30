import abc


class DecomposableSP(abc.ABC):

    @abc.abstractclassmethod
    def operator(cls, a, b):
        raise NotImplementedError(
            "Must implement operator() function to use this base class")

    @abc.abstractmethod
    def query(self, x):
        raise NotImplementedError(
            "Must implement query() function to use this base class")

    @abc.abstractmethod
    def unbuild(self):
        raise NotImplementedError(
            "Must implement unbuild() function to use this base class")
