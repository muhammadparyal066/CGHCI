import numpy as np
# TODO 1: Add all 9 values, divide by 9, and round the answer.
def mean_filter_3x3(neighborhood: np.ndarray) -> int:
    """Return the rounded average of 9 pixels."""
    return int(round(np.mean(neighborhood)))

problem_3_input = np.array([[10, 20, 10], [30, 50, 30], [10, 20, 10]], dtype=np.uint8)

# TODO 2: Remove the # symbols and run the given test.
assert mean_filter_3x3(problem_3_input) == 21
print("Problem 3 passed")