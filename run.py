import importlib
import sys


def run_day(day):
    try:
        module = importlib.import_module(f"day{day:02d}.solution")
    except ImportError:
        return

    with open(f"day{day:02d}/input.txt") as fh:
        lines = fh.readlines()

        results = {}

        for part in ("part1", "part2"):
            if hasattr(module, part):
                results[part] = getattr(module, part)(lines)

        if results:
            print(f"Day {day:02d}")
            for part, result in results.items():
                print(f"  {part}: {result}")
            print()


def run_all():
    for day in range(2, 7):
        run_day(day)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        day = int(sys.argv[1])
        run_day(day)
    else:
        run_all()
