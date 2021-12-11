#!/usr/bin/python3

import sys

land = []


for line in sys.stdin:
    point1, point2 = line.strip().split(" -> ")
    x1,y1 = point1.split(",")
    x2,y2 = point2.split(",")
    if x1 == x2:
        y_range = range(int(y1),int(y2)+1)
        print(y1)
        print(y2)
        print(y_range)
