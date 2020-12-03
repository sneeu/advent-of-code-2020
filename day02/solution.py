import operator


def is_valid(min, max, letter, password):
    letters_removed = password.replace(letter, "")

    number_of_letters_removed = len(password) - len(letters_removed)

    return min <= number_of_letters_removed <= max


def is_valid_part2(pos1, pos2, letter, password):
    return operator.xor(password[pos1 - 1] == letter, password[pos2 - 1] == letter)


def parse_line(line):
    config, password = line.split(":")
    minmax, char = config.split(" ")
    left, right = minmax.split("-")

    return (int(left), int(right), char.strip(), password.strip())


def part1(password_lines):
    return sum(
        1 for password_line in password_lines if is_valid(*parse_line(password_line))
    )


def part2(password_lines):
    return sum(
        1
        for password_line in password_lines
        if is_valid_part2(*parse_line(password_line))
    )


if __name__ == "__main__":
    with open("input.txt") as fh:
        lines = fh.readlines()

        print(part1(lines))
        print(part2(lines))
