from Problem1 import *
import random


def overlap(one, two):
    """returns area of overlap for 2 ellipses"""
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

    rangex = maxx - minx
    rangey = maxy - miny
    areaofrectangle = rangex * rangey

    random_points = 0
    inboth = 0
    while random_points < 10000:
        randx = random.randrange(10000)/10000
        randy = random.randrange(10000)/10000
        randpointx = (randx*rangex)+minx
        randpointy = (randy * rangey) + miny
        if one.inside_edge((randx, randy)) and two.inside_edge((randx, randy)):
            inboth += 1
        random_points += 1
    pointinboth = inboth / 10000
    overlaparea = round(pointinboth*areaofrectangle, 3)

    print('The area of overlap between these ellipses is {}'.format(overlaparea))


a = E(0,0,0,0,1)
b = E(10,0,1,0,6)
overlap(a, b)
