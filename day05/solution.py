import math
from typing import Tuple


def parse_seat_code(code):
    row, col = code[:7], code[7:]

    # Rows & columns are just binary numbers
    r = int(row.replace("F", "0").replace("B", "1"), 2)
    c = int(col.replace("L", "0").replace("R", "1"), 2)

    return r, c, (r * 8 + c)


def part1(lines):
    return max([parse_seat_code(line)[2] for line in lines])


def part2(lines):
    seats = set(parse_seat_code(line)[2] for line in lines)

    mn, mx = min(seats), max(seats)

    # Flight is full, so only 1 missing seat
    return list(set(range(mn, mx + 1)) - seats)[0]


if __name__ == "__main__":
    with open("./day05/input.txt") as fh:
        lines = fh.readlines()

        print(part1(lines))
        print(part2(lines))
