import re


def parse_line(line: str) -> list[str]:
    pattern = "(?:mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\))"
    cases = re.findall(pattern, line)
    return cases


def process_array(line: list[str], include: bool) -> tuple[int, bool]:
    total = 0
    for item in line:
        if item == "don't()":
            include = False
        elif item == "do()":
            include = True
        else:
            if include is False:
                continue
            left = int(item.split(",")[0].replace("mul(", ""))
            right = int(item.split(",")[1].replace(")", ""))
            product = left * right
            total += product
    return (total, include)


def run():
    with open("input.txt", "r") as f:
        total = 0
        include = True
        for line in f:
            case = parse_line(line)
            sub_total, include = process_array(case, include)
            total += sub_total


if __name__ == "__main__":
    run()
