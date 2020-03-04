from Problem1 import *
import random


def overlap(one, two):
    xvals = one.minmaxx(), two.minmaxx()
    minx = 0
    if xvals[0][0] < xvals[1][0]:
        minx = xvals[0][0]
    else:
        minx = xvals[1][0]

    maxx = 0
    if xvals[0][1] > xvals[1][1]:
        maxx = xvals[0][1]
    else:
        maxx = xvals[1][1]

    yvals = one.minmaxy(), two.minmaxy()
    miny = 0
    if yvals[0][0] < yvals[1][0]:
        miny = yvals[0][0]
    else:
        miny = yvals[1][0]

    maxy = 0
    if yvals[0][1] > yvals[1][1]:
        maxy = yvals[0][1]
    else:
        maxy = yvals[1][1]
    print(minx, maxx, miny, maxy)
    random_points = 0
    inboth = 0
    while random_points < 50:
        randx = random.randrange(minx, maxx)/100
        randy = random.randrange(miny, maxy)/100
        print(randx, randy)
        if one.inside_edge((randx, randy)) and two.inside_edge((randx, randy)):
            inboth += 1
        random_points += 1
    print(random_points)


a = E()
b = E()
overlap(a, b)
