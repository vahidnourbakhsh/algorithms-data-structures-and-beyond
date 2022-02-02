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
    repetitions = 10000
    for _ in range(repetitions):
        e = array.get_random()
        d[e] += 1
    d = {e: v / repetitions for e, v in d.items()}
    print(f"actual: {d} \n expected: {{ 1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4 }}")
    assert math.isclose(d[1], 0.1, abs_tol=0.1)
    assert math.isclose(d[2], 0.2, abs_tol=0.1)
    assert math.isclose(d[3], 0.3, abs_tol=0.1)
    assert math.isclose(d[4], 0.4, abs_tol=0.1)
