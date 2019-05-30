import random
import time

import matplotlib.pyplot as plt

from src.abc.decomposable.binomial_transform import BinomialTransform

from src.geometric.prim.interval             import Interval
from src.geometric.ds.dynamic_interval_tree  import DynamicIntervalTree


def main():
    a = DynamicIntervalTree()
    b = DynamicIntervalTree(BinomialTransform(3))

    binomial = list()
    binary   = list()
    for i in range(200):
        interval = Interval(random.uniform(0, 1000), random.uniform(0, 1000))

        start = time.time()
        a.insert(interval)
        end = time.time()
        binary.append(end - start)

        start = time.time()
        b.insert(interval)
        end = time.time()
        binomial.append(end - start)

    plt.subplot(2, 1, 1)
    plt.yscale("log")
    plt.xscale("log")
    plt.title("Insertion Time")
    plt.plot(binary,   color="blue")
    plt.plot(binomial, color="red")

    plt.subplot(2, 1, 2)
    plt.yscale("log")
    plt.xscale("log")
    binomial = list()
    binary   = list()
    for i in range(200):
        p = random.uniform(0, 1000)

        start = time.time()
        a.query(p)
        end = time.time()
        binary.append(end - start)

        start = time.time()
        b.query(p)
        end = time.time()
        binomial.append(end - start)
    plt.title("Query Time")
    plt.plot(binary, color="blue")
    plt.plot(binomial, color="red")
    plt.show()


if __name__ == "__main__":
    main()
