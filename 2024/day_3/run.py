import re


def match_cases(line: str) -> list[str]:
    pattern = "mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    cases = re.findall(pattern, line)
    return cases


def run():
    with open("input.txt", "r") as f:
        total = 0
        for line in f:
            cases = match_cases(line)
            list_total = sum((map(lambda x: int(x[0]) * int(x[1]), cases)))
            total += list_total
    print(total)


if __name__ == "__main__":
    run()
