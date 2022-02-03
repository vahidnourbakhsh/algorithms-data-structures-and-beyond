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
    array = RichArray([1, 2, 3, 4])
    a = array.get_random(3.3)
    assert a == 3
    b = array.get_random(3.3)
    assert b == 3
    array2 = RichArray([1, 100])
    c = array2.get_random(99)
    assert c == 100
    d = array2.get_random(0.5)
    assert d == 1

    random.seed(1)
    repetitions = 10000
    counts = defaultdict(int)
    for _ in range(repetitions):
        e = array.get_random()
        counts[e] += 1
    actual_probabilites = {e: v / repetitions for e, v in counts.items()}
    print(
        f"actual: {actual_probabilites} \n expected: {{ 1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4 }}"
    )
