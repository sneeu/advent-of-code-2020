import pytest

from solution import is_valid


@pytest.mark.parametrize(
    "min,max,letter,password,valid",
    [
        (0, 1, "a", "abcde", True),
    ],
)
def test_is_valid(min, max, letter, password, valid):
    assert is_valid(min, max, letter, password) == valid
