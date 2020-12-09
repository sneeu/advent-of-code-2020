import functools
import operator


def parse_lines(lines):
    group = []

    for line in lines:
        if line == "\n":
            yield group
            group = []
        else:
            # Strip off trailing \n
            group.append(line[:-1])

    yield group


def unique_for_group(group):
    return len(set("".join(group)))


def part1(lines):
    return sum(unique_for_group(group) for group in parse_lines(lines))


def all_in_group(group):
    return functools.reduce(operator.and_, (set(answers) for answers in group))


def part2(lines):
    return sum(len(all_in_group(group)) for group in parse_lines(lines))
