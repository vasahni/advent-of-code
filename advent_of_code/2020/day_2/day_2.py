

def check_if_valid(lower_bound, upper_bound, letter, password):
    first_instance = password[lower_bound - 1]
    second_instance = password[upper_bound - 1]

    if (first_instance == letter) and (second_instance == letter):
        valid = 0
    elif (first_instance == letter) or (second_instance == letter):
        valid = 1
    elif (first_instance != letter) and (second_instance != letter):
        valid = 0

    return valid


def parse(line):
    parsed = line.split(' ')
    lower_bound = int(parsed[0].split('-')[0])
    upper_bound = int(parsed[0].split('-')[1])
    letter = parsed[1][0]
    password = parsed[2]
    
    return lower_bound, upper_bound, letter, password


def run():
    valid_passwords = []
    with open('input.txt', 'r') as file_in:
        for line in file_in:
            lower_bound, upper_bound, letter, password = parse(line)
            valid = check_if_valid(lower_bound, upper_bound, letter, password)
            valid_passwords.append(valid)
    
    print(f'Total passwords {len(valid_passwords)}')
    print(f'Total valid passwords {sum(valid_passwords)}')


if __name__ == "__main__":
    run()
