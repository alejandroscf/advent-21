#!/usr/bin/python3

import sys

pos = {
    "h": 0,
    "v": 0,
    "aim": 0,
}

for line in sys.stdin:
    command, units = line.split(" ")
    units = int(units)
    if command == "forward":
        pos["h"] += units
        pos["v"] += units*pos["aim"]
    elif command == "down":
        pos["aim"] += units
    elif command == "up":
        pos["aim"] -= units
print(pos["v"]*pos["h"])
