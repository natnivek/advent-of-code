with open('input.txt') as f:
    commands = f.read().splitlines()

with open('test.txt') as f:
    test = f.read().splitlines()

def compute_multiplied_position(c_list):
    horizontal,depth = [0,0]
    for c in c_list:
        splitted = c.split(' ')
        direction = splitted[0]
        units = int(splitted[1])
        if direction == 'forward':
            horizontal += units
        if direction == 'down':
            depth += units
        if direction == 'up':
            depth -= units
    position_multiplied = horizontal *depth
    return position_multiplied

def compute_multiplied_position_with_aim(c_list):
    horizontal,depth = [0,0]
    aim = 0
    for c in c_list: 
        splitted = c.split(' ')
        direction = splitted[0]
        units = int(splitted[1])
        if direction == 'forward':
            horizontal += units
            depth += aim*units
        if direction == 'down':
            aim += units
        if direction == 'up':
            aim -= units
    position_multiplied = horizontal * depth
    return position_multiplied

# print(compute_multiplied_position(test)) #150
# print(compute_multiplied_position(commands)) #1714950

# print(compute_multiplied_position_with_aim(test)) #900
print(compute_multiplied_position_with_aim(commands))
