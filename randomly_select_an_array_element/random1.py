import random
import pytest

def get_random(arr, r=None):
    cum = [0] * len(arr)
    cum[0] = arr[0]
    for i in range(1, len(arr)):
        cum[i] = cum[i-1] + arr[i]

    if not r:
        r = random.random() * sum(arr)

    for ind, element in enumerate(arr):
        if r < cum[ind]:
            yield arr[ind]


if __name__=="__main__":
    random.seed(10)
    a = get_random([1,2,3,4], 3.3)
    assert a == 3
    a = get_random([1,2,3,4], 3.3)
    assert a == 3
    b = get_random([1, 100], 99)
    assert b == 100
    c = get_random([1, 100], 0.5)
    assert c == 1