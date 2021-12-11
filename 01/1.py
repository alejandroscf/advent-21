#!/usr/bin/python3

import sys

#depths = []
#expenses = []

last = -1
mes_down = 0

for line in sys.stdin:
    depth = int(line)
    if last == -1:
        last = depth
    else:
        if depth > last:
            mes_down += 1
        last = depth
        
print(mes_down)
