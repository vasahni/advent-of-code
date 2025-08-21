def read_lists() -> tuple[list[int], list[int]]:
    with open("day_1_input.txt", "r") as f:
        left, right = [], []
        for line in f:
            left.append(int(line.strip().split("   ")[0]))
            right.append(int(line.strip().split("   ")[1]))
    return left, right


def run():
    left, right = read_lists()
    if len(left) != len(right):
        raise ValueError(
            f"Expected equal list length, but got left:{len(left)}, right:{len(right)}"
        )
    difference = sum((abs(x - y) for x, y in zip(sorted(left), sorted(right))))
    print(f"Total difference: {difference}")


if __name__ == "__main__":
    run()
