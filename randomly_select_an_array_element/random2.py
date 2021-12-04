import random
import pytest

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
    a = array.get_random(3.3)
    assert a == 3
    a = array.get_random(3.3)
    assert a == 3
    array2 = GetElementRandomly([1, 100])
    b = array2.get_random(99)
    assert b == 100
    c = array2.get_random(0.5)
    assert c == 1