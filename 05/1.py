#!/usr/bin/python3

import sys

land_set = set()
overlaps = set()

land_dict = {}

hor = 0
ver = 0
diag = 0

for line in sys.stdin:
    point1, point2 = line.strip().split(" -> ")
    x1,y1 = point1.split(",")
    x2,y2 = point2.split(",")
    if x1 == x2:
        ver += 1
        if int(y1) > int(y2):
            temp = y2
            y2 = y1
            y1 = temp
        y_range = range(int(y1),int(y2)+1)
        for y in y_range:
            #if (int(x1),y) in land_set:
                #overlaps.add((int(x1),y))
            if (int(x1),y) in land_dict:
                land_dict[(int(x1),y)] += 1
            else:
                #land_set.add((int(x1),y))
                land_dict[(int(x1),y)] = 1
    elif y1 == y2:
        hor += 1
        if int(x1) > int(x2):
            temp = x2
            x2 = x1
            x1 = temp
        x_range = range(int(x1),int(x2)+1)
        for x in x_range:
            #if (x,int(y1)) in land_set:
                #overlaps.add((x,int(y1)))
            if (x,int(y1)) in land_dict:
                land_dict[(x,int(y1))] += 1
            else:
                #land_set.add((x,int(y1)))
                land_dict[(x,int(y1))] = 1
    else:
        diag += 1
#print(land)
result = 0
for point in land_dict.values():
    if point > 1:
        result += 1
print(result)

print((hor, ver, diag))
#print(len(land_set))
#print(len(overlaps))
