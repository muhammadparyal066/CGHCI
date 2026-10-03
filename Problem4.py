import numpy as np
#TODO 1: Use the formula from the problem description, then np.clip to stay in [out_min, out_max].
def contrast_stretch(
    image: np.ndarray,
    in_min: float,
    in_max: float,
    out_min: float = 0.0,
    out_max: float = 255.0,
) -> np.ndarray:
    """Change image values from one range to another."""
    stretched = (image - in_min) / (in_max - in_min) * (out_max - out_min) + out_min
    return np.clip(stretched, out_min, out_max).astype(np.float32)

problem_4_input = np.array([50, 100, 150], dtype=np.float32)

# TODO 2: Remove the # symbols and run the given test.
expected = np.array([0.0, 127.5, 255.0], dtype=np.float32)
np.testing.assert_allclose(contrast_stretch(problem_4_input, 50, 150), expected)
print("Problem 4 passed")