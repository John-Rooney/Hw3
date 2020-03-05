import EllipseClass
import random


def overlap(one, two):
    """returns area of overlap for 2 ellipses based on monte carlo simulation"""
    xvals = one.minmaxx(), two.minmaxx()
    minx = 0  # minimum x-val for box
    if xvals[0][0] < xvals[1][0]:
        minx = xvals[0][0]
    else:
        minx = xvals[1][0]

    maxx = 0  # maximum x-val for box
    if xvals[0][1] > xvals[1][1]:
        maxx = xvals[0][1]
    else:
        maxx = xvals[1][1]

    yvals = one.minmaxy(), two.minmaxy()
    miny = 0  # minimum y-val for box
    if yvals[0][0] < yvals[1][0]:
        miny = yvals[0][0]
    else:
        miny = yvals[1][0]

    maxy = 0  # maximum y-val for box
    if yvals[0][1] > yvals[1][1]:
        maxy = yvals[0][1]
    else:
        maxy = yvals[1][1]

    rangex = maxx - minx
    rangey = maxy - miny
    areaofrectangle = rangex * rangey
    random_points = 0
    inboth = 0
    # first = 0
    # second = 0
    while random_points < 10000:
        randx = random.randrange(10000) / 10000
        randy = random.randrange(10000) / 10000
        randpointx = (randx * rangex) + minx
        randpointy = (randy * rangey) + miny
        if one.inside_edge((randpointx, randpointy)) and two.inside_edge((randpointx, randpointy)):
            inboth += 1
        # if one.inside_edge((randpointx, randpointy)):
        #     first += 1
        # if two.inside_edge((randpointx, randpointy)):
        #     second += 1
        random_points += 1
    pointsinboth = inboth / 10000  # ratio of points in both to total random points
    overlaparea = round(pointsinboth * areaofrectangle, 3)

    print('The area of overlap between these ellipses is {}'.format(overlaparea))
    # print('first ', first)
    # print('second ', second)
    # print('inboth ', inboth)
    # print('areaofrectangle ', areaofrectangle)
    return overlaparea


a = EllipseClass.Ellipse(0, 30, 0, -10, 100)
b = EllipseClass.Ellipse(-33, -27, 78, -27, 100)
overlap(a, b)
