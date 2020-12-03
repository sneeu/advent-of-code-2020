import pytest

from solution import is_valid, is_valid_part2, parse_line


@pytest.mark.parametrize(
    "min,max,letter,password,valid",
    [
        (0, 1, "a", "abcde", True),
        (1, 1, "a", "abcde", True),
        (2, 4, "a", "abcde", False),
        (0, 9, "a", "aaaaa", True),
        (0, 3, "a", "aaaaa", False),
        (8, 9, "a", "aaaaa", False),
    ],
)
def test_is_valid(min, max, letter, password, valid):
    assert is_valid(min, max, letter, password) == valid


@pytest.mark.parametrize(
    "line,min,max,letter,password",
    [
        ("0-1 a: abcde", 0, 1, "a", "abcde"),
        ("1-1 a: abcde", 1, 1, "a", "abcde"),
        ("2-4 a: abcde", 2, 4, "a", "abcde"),
        ("0-9 a: aaaaa", 0, 9, "a", "aaaaa"),
        ("0-3 a: aaaaa", 0, 3, "a", "aaaaa"),
        ("8-9 a: aaaaa", 8, 9, "a", "aaaaa"),
    ],
)
def test_parse_line(line, min, max, letter, password):
    assert parse_line(line) == (min, max, letter, password)


@pytest.mark.parametrize(
    "pos1,pos2,letter,password,valid",
    [
        (1, 2, "a", "abcde", True),
        (1, 1, "a", "abcde", False),
        (2, 4, "a", "abcde", False),
        (1, 9, "a", "aaaaabbbbb", True),
        (3, 6, "a", "aaaaabbbbb", True),
        (8, 9, "a", "aaaaabbbbb", False),
    ],
)
def test_is_valid_part2(pos1, pos2, letter, password, valid):
    assert is_valid_part2(pos1, pos2, letter, password) == valid
