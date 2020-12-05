import functools
import operator


def part1(lines, right, down):
    forest_height = len(lines)
    # Subtract one for the \n
    forest_width = len(lines[0]) - 1

    trees_hit = 0

    for step, y in enumerate(range(0, forest_height, down)):
        x = (right * step) % forest_width

        if lines[y][x] == "#":
            trees_hit += 1

    return trees_hit


def part2(lines, movements):
    return functools.reduce(
        operator.__mul__, (part1(lines, *movement) for movement in movements)
    )


if __name__ == "__main__":
    with open("./day03/input.txt") as fh:
        lines = fh.readlines()
        movements = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

        print(part1(lines, 3, 1))
        print(part2(lines, movements))
