class SplayTree:

    class __SplayTreeIterator:

        def __init__(self, keys):
            self.keys = keys
            self.i    = -1

        def __next__(self):
            self.i += 1
            if self.i >= len(self.keys):
                raise StopIteration
            return self.keys[self.i]

    class __Node:

        def __init__(self, key, value):
            self.key    = key
            self.value  = value
            self.left   = None
            self.right  = None

    def __init__(self, cmp=None):
        self.__cmp   = cmp
        self.__root  = None
        self.__n     = 0

    def __len__(self):
        return self.__n

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        return self.get(key) is not None

    def __str__(self):
        return str(self.keys_in_order())

    def __repr__(self):
        return str(self.keys_in_order())

    def __iter__(self):
        return self.__SplayTreeIterator(self.keys_in_order())

    def max(self):
        if self.empty():
            return None
        cur = self.__root
        while cur.right is not None:
            cur = cur.right
        self.__root = self.__splay(self.__root, cur.key)
        return cur.key

    def min(self):
        if self.empty():
            return None
        cur = self.__root
        while cur.left is not None:
            cur = cur.left
        self.__root = self.__splay(self.__root, cur.key)
        return cur.key

    def empty(self):
        return self.__root is None

    def get(self, key):
        if key is None:
            raise ValueError("Illegal argument 'key' of None Type")

        if self.empty():
            return None

        self.__root = self.__splay(self.__root, key)
        cmp = self.__compare(key, self.__root.key)
        if cmp == 0:
            return self.__root.value
        return None

    def height(self):
        return self.__height(self.__root)

    def put(self, key, value):
        if key is None:
            raise ValueError("Illegal argument 'key' of None Type")

        if value is None:
            self.delete(key)
            return

        if self.__root is None:
            self.__root = self.__Node(key, value)
            self.__n += 1
            return

        self.__root = self.__splay(self.__root, key)

        cmp = self.__compare(key, self.__root.key)

        if cmp < 0:
            x       = self.__Node(key, value)
            x.left  = self.__root.left
            x.right = self.__root
            self.__root.left = None
            self.__root = x
            self.__n += 1
        elif cmp > 0:
            x       = self.__Node(key, value)
            x.right = self.__root.right
            x.left  = self.__root
            self.__root.right = None
            self.__root = x
            self.__n += 1
        else:
            self.__root.value = value

    def delete(self, key):
        if key is None:
            raise ValueError("Illegal argument 'key' of None Type")

        if self.__root is None:
            return

        self.__root = self.__splay(self.__root, key)

        cmp = self.__compare(key, self.__root.key)
        if cmp == 0:
            self.__n -= 1
            if self.__root.left is None:
                self.__root = self.__root.right
            else:

                x = self.__root.right
                self.__root = self.__root.left
                self.__root = self.__splay(self.__root, key)
                self.__root.right = x

    def delete_max(self):
        if self.empty():
            return
        self.delete(self.max())

    def delete_min(self):
        if self.empty():
            return
        self.delete(self.min())

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

    def keys_level_order(self):
        if self.__root is None:
            return []

        keys  = list()
        queue = list()
        queue.append(self.__root)
        while len(queue) > 0:
            node = queue.pop(0)
            keys.append(node.key)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        return keys

    def __splay(self, x, key):
        if x is None:
            return None

        cmp_gf = self.__compare(key, x.key)

        if cmp_gf < 0:
            if x.left is None:
                return x

            cmp_f = self.__compare(key, x.left.key)
            if cmp_f < 0:
                x.left.left = self.__splay(x.left.left, key)
                x = self.__rotate_right(x)
            elif cmp_f > 0:
                x.left.right = self.__splay(x.left.right, key)
                if x.left.right is not None:
                    x.left = self.__rotate_left(x.left)

            if x.left is None:
                return x
            return self.__rotate_right(x)

        if cmp_gf > 0:
            if x.right is None:
                return x

            cmp_f = self.__compare(key, x.right.key)
            if cmp_f < 0:
                x.right.left = self.__splay(x.right.left, key)
                if x.right.left is not None:
                    x.right = self.__rotate_right(x.right)
            elif cmp_f > 0:
                x.right.right = self.__splay(x.right.right, key)
                x = self.__rotate_left(x)

            if x.right is None:
                return x
            return self.__rotate_left(x)

        return x

    def __compare(self, a, b):
        if self.__cmp is not None:
            return self.__cmp(a, b)
        if a < b:
            return -1
        if a > b:
            return 1
        return 0

    @staticmethod
    def __rotate_left(x):
        y       = x.right
        x.right = y.left
        y.left  = x
        return y

    @staticmethod
    def __rotate_right(x):
        y       = x.left
        x.left  = y.right
        y.right = x
        return y

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
