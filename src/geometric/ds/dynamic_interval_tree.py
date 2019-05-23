from src.abc.static_to_dynamic      import StaticToDynamic

from src.geometric.ds.interval_tree import IntervalTree


class DynamicIntervalTree(StaticToDynamic):

    def __init__(self):
        super().__init__(IntervalTree)
