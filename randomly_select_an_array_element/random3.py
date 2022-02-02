import math
import random
from collections import defaultdict


class RichArray:
    def __init__(self, arr):
        self.arr = arr
        self.cum = self._get_cum()
        self.sum = self.cum[-1]

    def _get_cum(self):
        cum = [0] * len(self.arr)
        cum[0] = self.arr[0]
        for i in range(1, len(self.arr)):
            cum[i] = cum[i - 1] + self.arr[i]
        return cum

    def get_random(self, r=None):
        if not r:
            r = random.random() * self.sum

        for ind, _ in enumerate(self.arr):
            if r < self.cum[ind]:
                return self.arr[ind]


if __name__ == "__main__":
    random.seed(10)
    array = RichArray([1, 2, 3, 4])
    d = defaultdict(int)
    for i in range(1000):
        d[array.get_random()] += 1
    print(d)
    assert math.isclose(d[1] / 1000, 0.1, abs_tol=0.1)
    assert math.isclose(d[2] / 1000, 0.2, abs_tol=0.1)
    assert math.isclose(d[3] / 1000, 0.3, abs_tol=0.1)
    assert math.isclose(d[4] / 1000, 0.4, abs_tol=0.1)
