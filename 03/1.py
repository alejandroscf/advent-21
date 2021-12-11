#!/usr/bin/python3

import sys

common = []

for line in sys.stdin:
    i = 0
    for bit in line.strip():
        if len(common) <= i:
            common.append(0)
        if bit == "1":
            common[i] += 1
        if bit == "0":
            common[i] -= 1
        i += 1

gamma = ""
epsilon = ""

for bit in common:
    if bit > 0:
        gamma += "1"
        epsilon += "0"
    elif bit < 0:
        gamma += "0"
        epsilon += "1"

print(int(gamma, 2)*int(epsilon, 2))
