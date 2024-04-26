from pytest import approx
import pytest
from mergesort import split_in_two


@pytest.mark.parametrize("ns", [list(range(k)) for k in range(101)])
def test_split_in_two(ns):
    left, right = split_in_two(ns)
    assert left + right == ns
    assert abs(len(right) - len(left)) <= 1
