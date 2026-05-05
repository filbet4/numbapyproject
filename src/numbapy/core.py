from __future__ import annotations

import numpy as np
from numba import njit


@njit(cache=True)
def _sum_of_squares_numba(x: np.ndarray) -> float:
    total = 0.0
    for i in range(x.size):
        v = float(x[i])
        total += v * v
    return total


def sum_of_squares(x: np.ndarray) -> float:
    r"""Return $\sum_i x_i^2$.

    Parameters
    ----------
    x:
        1D NumPy array.

    Returns
    -------
    float
        Sum of squares as a Python float.
    """
    arr = np.asarray(x, dtype=np.float64)
    if arr.ndim != 1:
        raise ValueError("x must be 1D")
    return float(_sum_of_squares_numba(arr))
