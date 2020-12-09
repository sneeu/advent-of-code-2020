import pytest

from .solution import navigate


SMALL_FOREST = ["..\n", "#.\n"]
LONG_FOREST = ["..\n", "#.\n", "..\n", "..\n"]


@pytest.mark.parametrize(
    "forest,right,down,expected",
    [
        (SMALL_FOREST, 1, 1, 0),
        (SMALL_FOREST, 0, 1, 1),
        (LONG_FOREST, 0, 1, 1),
        (LONG_FOREST, 1, 2, 0),
    ],
)
def test_navigate(forest, right, down, expected):
    assert navigate(forest, right, down) == expected
