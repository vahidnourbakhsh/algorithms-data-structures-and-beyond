import random
import pytest
from collections import defaultdict
import math


class GetElementRandomly:
    def __init__(self, arr):
        self.arr = arr
        cum = [0] * len(arr)
        cum[0] = arr[0]
        for i in range(1, len(arr)):
            cum[i] = cum[i-1] + arr[i]
        self.cum = cum
        self.sum = cum[-1]

    def get_random(self, r=None):
        if not r:
            r = random.random() * self.sum

        for ind, _ in enumerate(self.arr):
            if r < self.cum[ind]:
                return self.arr[ind]


if __name__=="__main__":
    random.seed(10)
    array = GetElementRandomly([1,2,3,4])
    d = defaultdict(int)
    for i in range(1000):
        d[array.get_random()] += 1
    print(d)
    assert math.isclose(d[1]/1000, 0.1, abs_tol=0.1)
    assert math.isclose(d[2]/1000, 0.2, abs_tol=0.1)
    assert math.isclose(d[3]/1000, 0.3, abs_tol=0.1)
    assert math.isclose(d[4]/1000, 0.4, abs_tol=0.1)