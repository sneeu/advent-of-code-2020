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


def parse_file(file):
    record = {}

    for raw_line in file:
        line = raw_line.strip()

        if line == "":
            yield record
            record = {}
        else:
            record.update(parse_line(line))

    yield record


def valid_passport(passport):
    return len(set(passport.keys()) & REQUIRED_FIELDS) == len(REQUIRED_FIELDS)


def part1(fh):
    return len([1 for passport in parse_file(fh) if valid_passport(passport)])


if __name__ == "__main__":
    with open("./day04/input.txt") as fh:
        print(part1(fh))
