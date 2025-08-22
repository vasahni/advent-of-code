from enum import Enum, auto


class Safety(Enum):
    UNSAFE = auto()
    SAFE = auto()


# TODO: convert using all and map
def is_increasing(row: list[int]):
    previous = row[0]
    for current in row[1:]:
        if previous > current:
            return False
        previous = current
    return True


# TODO: convert using all and map
def is_decreasing(row: list[int]):
    previous = row[0]
    for current in row[1:]:
        if previous < current:
            return False
        previous = current
    return True


def is_monotonic(row: list[int]) -> bool:
    return is_decreasing(row) or is_increasing(row)


def check_differences(row: list[int]) -> bool:
    previous = row[0]
    for current in row[1:]:
        diff = abs(current - previous)
        if diff < 1 or diff > 3:
            return False
        previous = current
    return True


def check_safety(row: list[int]) -> Safety:
    if check_differences(row) and is_monotonic(row):
        return Safety.SAFE
    return Safety.UNSAFE


def run():
    counter = {"Safe": 0, "Unsafe": 0}
    with open("input.txt", "r") as f:
        for line in f:
            split_line = line.split(" ")
            split_line = list(map(int, split_line))
            if check_safety(split_line) == Safety.SAFE:
                counter["Safe"] += 1
            else:
                counter["Unsafe"] += 1
    print(counter)


if __name__ == "__main__":
    run()
