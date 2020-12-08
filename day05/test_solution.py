import pytest

from .solution import parse_seat_code


@pytest.mark.parametrize(
    "code,expected",
    [
        ("BFFFBBFRRR", (70, 7, 567)),
        ("FFFBBBFRRR", (14, 7, 119)),
        ("BBFFBBFRLL", (102, 4, 820)),
    ],
)
def test_parse_seat_code(code, expected):
    assert parse_seat_code(code) == expected
