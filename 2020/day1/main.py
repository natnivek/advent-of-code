with open('input.txt') as f:
    input = list(map(int,f.read().splitlines()))

with open('test.txt') as f:
    test = list(map(int,f.read().splitlines()))

# https://adventofcode.com/2020/day/1
def multiply_from_sum2(expense_report):
    found = False
    idx = 0
    while not found:
        complement = 2020 - expense_report[idx]
        if complement in expense_report:
            found = True
        else:
            idx += 1
    multiplied = expense_report[idx]*complement
    return multiplied

# https://adventofcode.com/2020/day/1#part2
def multiply_from_sum3(expense_report):
    found = False
    idx = 0 
    while not found:
        x = expense_report[idx]
        complement = 2020 - x
        if complement in expense_report:
            found = True
        else:
            idx += 1
    multiplied = expense_report[idx]*complement
    return multiplied

# print(multiply_from_sum2(test)) # 514579
# print(multiply_from_sum2(input)) # 1020099
