def horizontal_forward(mapping) -> int:
    count = 0
    for x in range(1, 141):
        first = 1
        second = 2
        third = 3
        fourth = 4
        while fourth <= 140:
            combined = (
                mapping[x, first]
                + mapping[x, second]
                + mapping[x, third]
                + mapping[x, fourth]
            )
            if combined == "XMAS":
                count += 1
            first, second, third, fourth = first + 1, second + 1, third + 1, fourth + 1
    print(f"Horizontal Forward Total: {count}")
    return count


def find_sequences(mapping: dict[tuple[int, int], str]) -> int:
    total_count = 0
    count = horizontal_forward(mapping)
    total_count += count
    return total_count


def run():
    mapping = {}
    with open("input.txt", "r") as file:
        x = 1
        for line in file:
            for y, char in enumerate(line, start=1):
                if char == "\n":
                    continue
                mapping[(x, y)] = char
            x += 1
    count = find_sequences(mapping)
    print(f"Total XMAS: {count}")


if __name__ == "__main__":
    run()
