def distance(one, two):
    """returns distance between 2 points"""
    xdist = abs(one[0] - two[0])
    ydist = abs(one[1] - two[1])
    dist = (xdist ** 2 + ydist ** 2) ** 0.5
    return dist

def circumference(a, b):
    """Returns circumference of ellipse"""
    #a = semimajor, b = semiminor
    pi = 3.1415927
    h = ((a - b)**2)/((a + b)**2)
    circumference = pi*(a + b)*(1+((3*h)/(10+(4-(3*h))**0.5)))
    return circumference

def area(a, b):
    """Returns approximate area of ellipse"""
    # a = semimajor, b = semiminor
    pi = 3.1415927
    area = pi * a * b
    return area