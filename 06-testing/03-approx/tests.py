import pytest
from pytest import approx
from mystatistics import average


@pytest.mark.parametrize(
    "ns, expected", [([1], 1), ([1, 3], 2), ([0.1, 0.1, 0.1], 0.1)]
)
def test_average(ns, expected):
    assert pytest.approx(expected) == average(ns)
