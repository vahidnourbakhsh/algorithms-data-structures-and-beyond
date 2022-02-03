from collections import defaultdict
import math
import random

from randomly_select_an_array_element.use_classes import RichArray

REPETITIONS = 10000


def test_get_random():
    random.seed(
        10
    )  # fixing seed makes sure that our tests doe not fail because of randomness in the generated random number.
    array = RichArray([1, 2, 3, 4])
    counts = defaultdict(int)
    for _ in range(REPETITIONS):
        e = array.get_random()
        counts[e] += 1
    actual_probabilities = {e: v / REPETITIONS for e, v in counts.items()}
    print(
        f"actual: {actual_probabilities} \n expected: {{ 1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4 }}"
    )
    assert math.isclose(actual_probabilities[1], 0.1, abs_tol=0.1)
    assert math.isclose(actual_probabilities[2], 0.2, abs_tol=0.1)
    assert math.isclose(actual_probabilities[3], 0.3, abs_tol=0.1)
    assert math.isclose(actual_probabilities[4], 0.4, abs_tol=0.1)
