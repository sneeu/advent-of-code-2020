


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


if __name__ == "__main__":
    with open("./day03/input.txt") as fh:
        lines = fh.readlines()

        print(part1(lines, 3, 1))
