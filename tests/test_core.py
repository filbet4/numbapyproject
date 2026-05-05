import numpy as np
import pytest

from numbapy import sum_of_squares


def test_sum_of_squares_matches_numpy() -> None:
    x = np.array([1.0, 2.0, 3.0], dtype=np.float64)
    assert sum_of_squares(x) == pytest.approx(float(np.sum(x * x)))


def test_sum_of_squares_rejects_2d() -> None:
    x = np.ones((2, 2), dtype=np.float64)
    with pytest.raises(ValueError):
        sum_of_squares(x)
