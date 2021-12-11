#!/usr/bin/python3

import sys

WINDOW_SIZE = 3

last = []
mes_down = 0
i = 0

for line in sys.stdin:
    depth = int(line)
    if len(last) < WINDOW_SIZE:
        last.append(depth)
    else:
        if depth > last[i%WINDOW_SIZE]:
            mes_down += 1
        last[i%WINDOW_SIZE] = depth
    i += 1
        
print(mes_down)
