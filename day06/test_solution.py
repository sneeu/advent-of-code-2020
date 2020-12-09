import pytest

from .solution import all_in_group, unique_for_group


@pytest.mark.parametrize(
    "lines,expected",
    [
        (["a"], set("a")),
        (["abc"], set("abc")),
        (["abc", "cba"], set("abc")),
        (["a", "a", "a", "a"], set("a")),
    ],
)
def test_unique_for_group(lines, expected):
    assert unique_for_group(lines) == expected


@pytest.mark.parametrize(
    "lines,expected",
    [
        (["a"], set("a")),
        (["abc"], set("abc")),
        (["abc", "cba"], set("abc")),
        (["a", "a", "a", "a"], set("a")),
        (["a", "b"], set()),
        (["a", "b", "c", "d"], set()),
        (["a", "ab", "ac", "ad"], set("a")),
    ],
)
def test_all_in_group(lines, expected):
    assert all_in_group(lines) == expected
