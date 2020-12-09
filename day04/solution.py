import re


"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""
REQUIRED_FIELDS = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def parse_line(line):
    kv_pairs = [pair.split(":") for pair in line.split(" ")]

    return {kv[0]: kv[1] for kv in kv_pairs}


def parse_lines(lines):
    record = {}

    for raw_line in lines:
        line = raw_line.strip()

        if line == "":
            yield record
            record = {}
        else:
            record.update(parse_line(line))

    yield record


def valid_passport(passport):
    return len(set(passport.keys()) & REQUIRED_FIELDS) == len(REQUIRED_FIELDS)


def part1(lines):
    return len([1 for passport in parse_lines(lines) if valid_passport(passport)])


def validate_in_set(value, s):
    return value in s


def validate_regex(value, r):
    return re.match(r, value)


def validate_range(value, mn, mx):
    return validate_in_set(int(value), range(mn, mx + 1))


def validate_height(value):
    if validate_regex(value, r"[0-9]+in$"):
        return validate_range(int(value[:-2]), 59, 76)
    if validate_regex(value, r"[0-9]+cm$"):
        return validate_range(int(value[:-2]), 150, 193)
    return False


def valid_passport2(passport):
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """

    if not valid_passport(passport):
        return False

    return all([
        validate_range(passport["byr"], 1920, 2002),
        validate_range(passport["iyr"], 2010, 2020),
        validate_range(passport["eyr"], 2020, 2030),
        validate_height(passport["hgt"]),
        validate_regex(passport["hcl"], r"^#[0-9a-f]{6}$"),
        validate_in_set(passport["ecl"], set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])),
        validate_regex(passport["pid"], r"^[0-9]{9}$"),
    ])


def part2(lines):
    return len([1 for passport in parse_lines(lines) if valid_passport2(passport)])
