import pytest
from parentheses import matching_parentheses


@pytest.mark.parametrize(
    "string",
    [
        "",
        "()",
        "(())",
        "()()()",
        "(())()",
    ],
)
def test_matching_parentheses(string):
    actual = matching_parentheses(string)
    assert actual == True, f"{string} matches parentheses"


@pytest.mark.parametrize(
    "string",
    [
        "(",
        ")",
        ")(",
        "(()))(()",
    ],
)
def test_not_matching_parentheses(string):
    actual = matching_parentheses(string)
    assert actual == False, f"{string} does not match parentheses"
