import csv
import itertools
 
REQUIRED_SUM = 2020

# product of a tuple
def prod(val) :  
    res = 1 
    for ele in val:  
        res *= ele  
    return res   


def run():
    items = []
    with open('input.csv', 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            items.append(float(row[0]))
        
    for each in itertools.combinations(items, 3):
        print(f'Checking {each}')
        if sum(each) == REQUIRED_SUM:
            print(f'Found the tuple with the required sum: {REQUIRED_SUM} - {each}')
            product = prod(each)
            print(f'The product is {product}')
            break
        else:
            print(f'Does not sum to {REQUIRED_SUM}')

if __name__ == "__main__":
    run()
