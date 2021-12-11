#!/usr/bin/python3

import sys

common = []
numbers = []

for line in sys.stdin:
    #i = 0
    #numbers.append(int(line.strip(),2))
    numbers.append(line.strip())

numbers.sort()

def get_common(numbers, pos):
    tot = len(numbers)
    ones = sum([ int(x[pos]) for x in numbers ])
    if ones == tot/2:
        return -1
    elif ones > tot/2:
        return 1
    else:
        return 0

def separate(numbers, pos, value):
    return [ x for x in numbers if x[pos] == value ]
    #bin(numbers[co2])[2:]

def get_o2(numbers, pos):
    common = get_common(numbers, pos)
    if common == -1:
        common = 1
    numbers = separate(numbers, pos, str(common))
    #print(numbers)
    if len(numbers) == 1:
        return numbers[0]
    else:
        return get_o2(numbers, pos + 1)

def get_co2(numbers, pos):
    common = get_common(numbers, pos)
    if common == 1:
        common = 0
    elif common == 0:
        common = 1
    elif common == -1:
        common = 0
    numbers = separate(numbers, pos, str(common))
    if len(numbers) == 1:
        return numbers[0]
    else:
        return get_co2(numbers, pos + 1)

o2 = int(get_o2(numbers.copy(), 0),2)
co2 = int(get_co2(numbers.copy(), 0),2)

print(o2*co2)
