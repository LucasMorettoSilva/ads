class IntervalTree:

    class __Node:

        def __init__(self, x_mid, intervals):
            self.x_mid     = x_mid
            self.left_mid  = None
            self.right_mid = None

            # Children
            self.left  = None
            self.right = None

    def __init__(self, intervals):
        if intervals is None:
            raise ValueError("Invalid argument 'intervals' of None Type")

        intervals   = set(intervals)
        self.__size = len(intervals)

    def __len__(self):
        return self.__size
