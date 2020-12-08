import pytest

from .solution import parse_file, parse_line


@pytest.mark.parametrize(
    "line,expected",
    [
        ("a:b", {"a": "b"}),
        ("a:1 b:2", {"a": "1", "b": "2"}),
    ],
)
def test_parse_line(line, expected):
    assert parse_line(line) == expected


def test_parse_file():
    file = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""".splitlines(
        True
    )
    assert list(parse_file(file)) == [
        {
            "byr": "1937",
            "cid": "147",
            "ecl": "gry",
            "eyr": "2020",
            "hcl": "#fffffd",
            "hgt": "183cm",
            "iyr": "2017",
            "pid": "860033327",
        },
        {
            "byr": "1929",
            "cid": "350",
            "ecl": "amb",
            "eyr": "2023",
            "hcl": "#cfa07d",
            "iyr": "2013",
            "pid": "028048884",
        },
        {
            "byr": "1931",
            "ecl": "brn",
            "eyr": "2024",
            "hcl": "#ae17e1",
            "hgt": "179cm",
            "iyr": "2013",
            "pid": "760753108",
        },
        {
            "ecl": "brn",
            "eyr": "2025",
            "hcl": "#cfa07d",
            "hgt": "59in",
            "iyr": "2011",
            "pid": "166559648",
        },
    ]
