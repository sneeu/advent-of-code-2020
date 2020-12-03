def is_valid(min, max, letter, password):
    letters_removed = password.replace(letter, "")

    number_of_letters_removed = len(password) - len(letters_removed)

    return min <= number_of_letters_removed <= max


def parse_line(line):
    config, password = line.split(":")
    minmax, char = config.split(" ")
    min, max = minmax.split("-")

    return (int(min), int(max), char.strip(), password.strip())


def part1(password_lines):
    return sum(
        1 for password_line in password_lines if is_valid(*parse_line(password_line))
    )


if __name__ == "__main__":
    with open("input.txt") as fh:
        print(part1(fh.readlines()))
