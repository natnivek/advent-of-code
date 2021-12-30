with open('input.txt') as f:
    measurements = list(map(int,f.read().splitlines()))

with open('input_test.txt') as f:
    test = list(map(int,f.read().splitlines())) #7 increases

def day1(m_list):
    larger = 0 
    for i in range(1,len(m_list)):
        if m_list[i-1]<m_list[i]:
            larger +=1

    return larger

def day1_part2(m_list):
    larger = 0
    prev_sum = m_list[0] + m_list[1] + m_list[2]
    for i in range(3,len(m_list)):
        current_sum = m_list[i-2] + m_list[i-1] + m_list[i]
        if current_sum > prev_sum:
            larger +=1 
        prev_sum = current_sum
    return larger

# print(day1(measurements)) #1390
print(day1_part2(measurements))
