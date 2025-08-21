from collections import Counter


def read_lists() -> tuple[list[int], list[int]]:
    with open("day_1_input.txt", "r") as f:
        left, right = [], []
        for line in f:
            left.append(int(line.strip().split("   ")[0]))
            right.append(int(line.strip().split("   ")[1]))
    return left, right


def calculate_difference(left: list[int], right: list[int]) -> int:
    difference = sum((abs(x - y) for x, y in zip(sorted(left), sorted(right))))
    return difference


def calculate_similarity(left: list[int], right: list[int]) -> int:
    element_count = Counter(right)
    sum = 0
    for each in left:
        sum += each * element_count[each]
    return sum


def run():
    left, right = read_lists()
    if len(left) != len(right):
        raise ValueError(
            f"Expected equal list length, but got left:{len(left)}, right:{len(right)}"
        )
    print(f"Difference: {calculate_difference(left, right)}")
    print(f"Similarity: {calculate_similarity(left, right)}")


if __name__ == "__main__":
    run()
