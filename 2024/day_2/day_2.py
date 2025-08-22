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


def check_safety(row: list[int]) -> Safety:
    if check_differences(row) and is_monotonic(row):
        return Safety.SAFE
    return Safety.UNSAFE


def run():
    safe = 0
    with open("input.txt", "r") as f:
        for line in f:
            row = list(map(int, line.strip().split(" ")))
            if check_safety(row) == Safety.SAFE:
                safe += 1
    print(f"Total safe: {safe}")


if __name__ == "__main__":
    run()
