import sys
from enum import Enum, auto


class Safety(Enum):
    UNSAFE = auto()
    SAFE = auto()


def is_increasing(row: list[int]) -> bool:
    return all(row[i] < row[i + 1] for i in range(len(row) - 1))


def is_decreasing(row: list[int]) -> bool:
    return all(row[i] > row[i + 1] for i in range(len(row) - 1))


def is_monotonic(row: list[int]) -> bool:
    return is_decreasing(row) or is_increasing(row)


def check_differences(row: list[int]) -> bool:
    return all(1 <= abs(row[i] - row[i + 1]) <= 3 for i in range(len(row) - 1))


def dampen(row: list[int]) -> Safety:
    for i in range(len(row)):
        copied_row = row.copy()
        copied_row.pop(i)
        if check_differences(copied_row) and is_monotonic(copied_row):
            return Safety.SAFE
    return Safety.UNSAFE


def run_safety(row: list[int], use_dampner: bool) -> Safety:
    if check_differences(row) and is_monotonic(row):
        return Safety.SAFE
    elif use_dampner:
        return dampen(row)
    else:
        return Safety.UNSAFE


def run():
    safe = 0
    bool_map = {"true": True, "false": False}
    use_dampner = sys.argv[1:][0]
    use_dampner = bool_map.get(use_dampner.lower())
    with open("input.txt", "r") as f:
        for line in f:
            row = list(map(int, line.strip().split(" ")))
            if run_safety(row, use_dampner) == Safety.SAFE:
                safe += 1
    print(f"Total safe: {safe}")


if __name__ == "__main__":
    run()
