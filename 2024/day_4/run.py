TARGET = "XMAS"
Mapping = dict[tuple[int, int], str]


def horizontal_forward(mapping: Mapping, height: int, width: int) -> int:
    count = 0
    for x in range(1, height + 1):
        for start_col in range(1, width - len(TARGET) + 2):
            word = "".join(mapping[x, start_col + i] for i in range(len(TARGET)))
            if word == TARGET:
                count += 1
    return count


def find_sequences(mapping: Mapping, height: int, width: int) -> int:
    total_count = 0
    count = horizontal_forward(mapping, height, width)
    total_count += count
    return total_count


def run():
    mapping = {}
    with open("input.txt", "r") as file:
        height = 1
        for line in file:
            width = 1
            for char in line:
                if char == "\n":
                    continue
                mapping[(height, width)] = char
                width += 1
            height += 1
    count = find_sequences(mapping, height - 1, width - 1)
    print(f"Total Count: {count}")


if __name__ == "__main__":
    run()
