class PrioritySearchTree:

    def __init__(self, data, cmp=None):
        if data is None:
            raise ValueError("Invalid argument 'data' of None Type")
        self.__cmp = cmp

    def __compare(self, a, b):
        if self.__cmp is not None:
            return self.__cmp(a, b)
        if a < b:
            return -1
        if a > b:
            return 1
        return 0

