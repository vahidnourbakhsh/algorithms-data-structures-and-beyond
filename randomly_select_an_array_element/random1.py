import random
from collections import defaultdict


def get_random(arr, r=None):
    cum = [0] * len(arr)
    cum[0] = arr[0]
    for i in range(1, len(arr)):
        cum[i] = cum[i - 1] + arr[i]

    if not r:
        r = random.random() * sum(arr)

    for ind, element in enumerate(arr):
        if r < cum[ind]:
            return arr[ind]


if __name__ == "__main__":
    a = get_random([1, 2, 3, 4], 3.3)
    assert a == 3
    a = get_random([1, 2, 3, 4], 3.3)
    assert a == 3
    b = get_random([1, 100], 99)
    assert b == 100
    c = get_random([1, 100], 0.5)
    assert c == 1

    random.seed(1)
    d = defaultdict(int)
    for _ in range(1000):
        e = get_random([1, 2, 3, 4])
        d[e] += 1
    d = {e: v / 1000 for e, v in d.items()}
    print(f"actual: {d} \n expected: {{ 1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4 }}")
