#!/usr/bin/python3

import sys

pos = {
    "h": 0,
    "v": 0,
}

for line in sys.stdin:
    command, units = line.split(" ")
    units = int(units)
    if command == "forward":
        pos["h"] += units
    elif command == "down":
        pos["v"] += units
    elif command == "up":
        pos["v"] -= units
print(pos["v"]*pos["h"])
