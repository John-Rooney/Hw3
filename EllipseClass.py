import utility


class Ellipse:
    """Defines and edits ellipse objects based on 2 foci and the Semi Major"""
    def __init__(self, x1=0, y1=0, x2=1, y2=0, semiMajor=1):
        self.x1 = x1
        if type(self.x1) == str:
            raise TypeError('Numbers Only Please')

        self.y1 = y1
        if type(self.y1) == str:
            raise TypeError('Numbers Only Please')

        self.x2 = x2
        if type(self.x2) == str:
            raise TypeError('Numbers Only Please')

        self.y2 = y2
        if type(self.y2) == str:
            raise TypeError('Numbers Only Please')

        self.semiMajor = semiMajor
        if self.x1 == self.x2 or self.y1 == self.y2:
            if self.semiMajor <= utility.distance((self.x1, self.y1), (self.x2, self.y2))/2:
                raise ValueError('semiMajor must be larger than half the distance between Foci1 and Foci2')
        else:
            raise ValueError('X1 and X2 or Y1 and Y2 must be equal')

    def __repr__(self):
        return 'X1:{} Y1:{} X2:{} Y2:{} Semi Major:{}'.format(self.x1, self.y1, self.x2, self.y2, self.semiMajor)

    def setFoci1(self, x1, y1):
        """setting foci 1 of ellipse"""
        try:
            float(x1)
        except:
            raise TypeError('Numbers Only Please')
        try:
            float(y1)
        except:
            raise TypeError('Numbers Only Please')
        self.x1 = x1
        self.y1 = y1

    def setFoci2(self, x2, y2):
        """setting foci 2 of ellipse"""
        try:
            float(x2)
        except:
            raise TypeError('Numbers Only Please')
        try:
            float(y2)
        except:
            raise TypeError('Numbers Only Please')
        self.x2 = x2
        self.y2 = y2

    def setsemiMajor(self, semiMajor):
        """setting Semi Major of ellipse"""
        try:
            float(semiMajor)
        except:
            raise TypeError('Numbers Only Please')
        if semiMajor <= utility.distance((self.x1, self.y1), (self.x2, self.y2)) / 2:
            raise ValueError('semiMajor must be larger than half the distance between Foci1 and Foci2')
        self.semiMajor = semiMajor

    def getFoci1(self):
        """Returns foci 1 of ellipse"""
        return (self.x1, self.y1)

    def getFoci2(self):
        """Returns foci 2 of ellipse"""
        return (self.x2, self.y2)

    def getsemiMajor(self):
        """Returns Semi Major of ellipse"""
        return self.semiMajor

    def getsemiMinor(self):
        """Returns Semi Minor of ellipse"""
        if self.y1 == self.y2:
            C2 = self.semiMajor**2
            B2 = (abs(self.x1 - self.x2) / 2)**2
            semiMinor = (C2 - B2)**0.5
        else:
            C2 = self.semiMajor**2
            B2 = (abs(self.y1 - self.y2) / 2)**2
            semiMinor = (C2 - B2)**0.5
        return round(semiMinor, 6)

    def minmaxx(self):
        """Returns the min and max X value for the ellipse"""
        semiMinor = self.getsemiMinor()
        if self.y1 == self.y2:
            midx = (abs(self.x1 - self.x2)) / 2 + min(self.x1, self.x2)
            minx = round(midx - self.semiMajor, 6)
            maxx = round(midx + self.semiMajor, 6)
        else:
            minx = round(self.x1 - semiMinor, 6)
            maxx = round(self.x1 + semiMinor, 6)
        return minx, maxx

    def minmaxy(self):
        """Returns the min and max Y value for the ellipse"""
        semiMinor = self.getsemiMinor()
        if self.x1 == self.x2:
            midy = (abs(self.y1 - self.y2)) / 2 + min(self.y1, self.y2)
            miny = round(midy - self.semiMajor, 6)
            maxy = round(midy + self.semiMajor, 6)
        else:
            miny = round(self.y1 - semiMinor, 6)
            maxy = round(self.y1 + semiMinor, 6)
        return miny, maxy

    def inside_edge(self, point):
        """returns True if a point is inside or on edge of ellipse"""
        pointdist = utility.distance(self.getFoci1(), point) + utility.distance(self.getFoci2(), point)
        if pointdist > self.semiMajor * 2:
            return False
        else:
            return True

# a=Ellipse(-1, 0, 1, 0, 3)
# print(a.getsemiMinor())
# print(a.inside_edge((-1, 0)))
