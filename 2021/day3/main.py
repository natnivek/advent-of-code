import numpy as np

with open('input.txt') as f:
    input = f.read().splitlines()

with open('test.txt') as f:
    test = f.read().splitlines()

# https://adventofcode.com/2021/day/3
def compute_power_comsumption(report):
    positions_number = len(report[0])
    bit_sum = np.zeros(positions_number)
    for entry in report:
        for pos in range(positions_number):
            bit = int(entry[pos])
            bit_sum[pos] += bit
    entries_number = len(report)
    bit_avg = bit_sum/entries_number
    bit_converted = np.zeros(positions_number)
    bit_converted[bit_avg>0.5] =1
    gamma_rate = 0
    epsilon_rate = 0
    for i in range(len(bit_converted)):
        gamma_rate += 2**(positions_number-i-1)*bit_converted[i]
        epsilon_rate += 2**(positions_number-i-1)*(1-bit_converted[i])
    return gamma_rate * epsilon_rate

def bit_criteria(report,rating_type):
    positions_number = len(report[0])
    bit_sum = 0
    pos = 0
    while pos < positions_number and len(report)>1:
        print(pos,report)
        for entry in report:
            bit = int(entry[pos])
            bit_sum += bit
        entries_number = len(report)
        bit_avg = bit_sum/entries_number
        bit_converted = 0 
        if bit_avg >= 0.5:
            bit_converted  = 1
        if rating_type == 'co2':
            bit_converted = (1-bit_converted)
        new_report = []
        for entry in report:
            if int(entry[pos]) == bit_converted:
                new_report.append(entry) 
        report = new_report
        pos +=1
        bit_sum = 0 
    rating =  report[0]
    return rating


def compute_life_support_rating(report):
    oxygen_generator_rating_bit = bit_criteria(report,'oxygen')
    co2_scrubber_rating_bit = bit_criteria(report,'co2')
    positions_number = len(report[0])
    oxygen_generator_rating = 0 
    co2_scrubber_rating = 0
    for i in range(len(oxygen_generator_rating_bit)):
        oxygen_generator_rating += 2**(positions_number-i-1)*int(oxygen_generator_rating_bit[i])
        co2_scrubber_rating += 2**(positions_number-i-1)*int(co2_scrubber_rating_bit[i])
    return oxygen_generator_rating * co2_scrubber_rating

# compute_power_comsumption(test) # 198
# compute_power_comsumption(input) # 3882564

# compute_life_support_rating(test) #230
# compute_life_support_rating(input) #3385170
