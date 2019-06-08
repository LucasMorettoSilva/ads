import random


class Treap:

    class __Node:

        def __init__(self, key, value, height=0, size=1):
            self.key    = key
            self.value  = value
            self.height = height
            self.size   = size
            self.left   = None
            self.right  = None
            self.p      = random.uniform(0, 10000)

    def __init__(self, cmp=None):
        self.__cmp  = cmp
        self.__root = None

    def __len__(self):
        return self.__size(self.__root)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        return self.get(key) is not None

    def __iter__(self):
        return self.__TreapIterator(self.keys_in_order())

    def max(self):
        if self.empty():
            return None
        cur = self.__root
        while cur.right is not None:
            cur = cur.right
        return cur.key

    def min(self):
        if self.empty():
            return None
        cur = self.__root
        while cur.left is not None:
            cur = cur.left
        return cur.key

    def empty(self):
        return self.__root is None

    def get(self, key):
        if key is None:
            raise ValueError("Illegal argument 'key' of None Type")

        x = self.__get(self.__root, key)
        if x is None:
            return None
        return x.value

    def __get(self, x, key):
        if x is None:
            return None

        cmp = self.__compare(key, x.key)
        if   cmp < 0:
            return self.__get(x.left, key)
        elif cmp > 0:
            return self.__get(x.right, key)
        return x

    def height(self):
        return self.__height(self.__root)

    def put(self, key, value):
        if key is None:
            raise ValueError("Illegal argument 'key' of None Type")

        if value is None:
            self.delete(key)
            return

        self.__root = self.__put(self.__root, key, value)

    def __put(self, x, key, value):
        if x is None:
            return self.__Node(key, value)

        cmp = self.__compare(key, x.key)
        if   cmp < 0:
            x.left = self.__put(x.left, key, value)
        elif cmp > 0:
            x.right = self.__put(x.right, key, value)
        else:
            x.value = value
            return x

        self.__update_fields(x)

        return self.__balance(x)

    def delete(self, key):
        if key is None:
            raise ValueError("Illegal argument 'key' of None Type")

        self.__root = self.__delete(self.__root, key)

    def __delete(self, x, key):
        if x is None:
            return None

        cmp = self.__compare(key, x.key)
        if   cmp < 0:
            x.left = self.__delete(x.left, key)
        elif cmp > 0:
            x.right = self.__delete(x.right, key)
        else:
            if x.left is None:
                return x.right
            if x.right is None:
                return x.left

            if self.__prioritiy(x.left) < self.__prioritiy(x.right):
                x = self.__rotate_left(x)
                x.left = self.__delete(x.left, key)
            else:
                x = self.__rotate_right(x)
                x.right = self.__delete(x.right, key)

        self.__update_fields(x)

        return self.__balance(x)

    def delete_min(self):
        if self.empty():
            return
        self.__root = self.__delete_min(self.__root)

    def __delete_min(self, x):
        if x is None:
            return None
        if x.left is None:
            return x.right
        x.left = self.__delete_min(x.left)
        self.__update_fields(x)
        return self.__balance(x)

    def delete_max(self):
        if self.empty():
            return
        self.__root = self.__delete_max(self.__root)

    def __delete_max(self, x):
        if x is None:
            return None
        if x.right is None:
            return x.left
        x.right = self.__delete_max(x.right)
        self.__update_fields(x)
        return self.__balance(x)

    def keys_in_order(self):
        keys  = list()
        stack = list()
        cur   = self.__root
        while cur is not None or len(stack) > 0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            keys.append(cur.key)
            cur = cur.right
        return keys

    def __compare(self, a, b):
        if self.__cmp is not None:
            return self.__cmp(a, b)
        if a < b:
            return -1
        if a > b:
            return 1
        return 0

    def __rotate_left(self, x):
        y       = x.right
        x.right = y.left
        y.left  = x

        self.__update_fields(x)
        self.__update_fields(y)

        return y

    def __rotate_right(self, x):
        y       = x.left
        x.left  = y.right
        y.right = x

        self.__update_fields(x)
        self.__update_fields(y)

        return y

    def __update_fields(self, x):
        if x is None:
            return
        x.size   = 1 + self.__size(x.left) + self.__size(x.right)
        x.height = max(self.__height(x.left), self.__height(x.right))

    @staticmethod
    def __height(x):
        if x is None:
            return -1
        return x.height

    @staticmethod
    def __size(x):
        if x is None:
            return 0
        return x.size

    @staticmethod
    def __max(x):
        cur = x
        while cur.right is not None:
            cur = cur.right
        return cur

    @staticmethod
    def __min(x):
        cur = x
        while cur.left is not None:
            cur = cur.left
        return cur

    @staticmethod
    def __prioritiy(x):
        if x is None:
            return -1
        return x.p

    def __balance(self, x):
        if self.__prioritiy(x) < self.__prioritiy(x.left) or \
           self.__prioritiy(x) < self.__prioritiy(x.right):
            if self.__prioritiy(x.left) - self.__prioritiy(x.right) > 0:
                return self.__rotate_right(x)
            return self.__rotate_left(x)
        return x

    class __TreapIterator:

        def __init__(self, keys):
            self.keys = keys
            self.i    = -1

        def __next__(self):
            self.i += 1
            if self.i >= len(self.keys):
                raise StopIteration
            return self.keys[self.i]
