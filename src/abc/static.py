import abc


class Static(abc.ABC):

    @abc.abstractmethod
    def query(self, x):
        raise NotImplementedError(
            "Must implement query(x) function to use this base class")

    @abc.abstractmethod
    def unbuild(self):
        raise NotImplementedError(
            "Must implement unbuild() function to use this base class")
