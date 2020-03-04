from utility import area, circumference, distance

class E:

    def __init__(self, x1=0, y1=0, x2=1, y2=0, semiMajor=1):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.semiMajor = semiMajor

    def setFoci1(self, x1, y1):
        """setting foci 1 of ellipse"""
        self.F1 = (self.x1, self.y1)

    def setFoci2(self, x2, y2):
        """setting foci 2 of ellipse"""
        self.F1 = (self.x2, self.y2)

    def setsemiMajor(self, semiMajor):
        """setting Semi Major of ellipse"""
        self.semiMajor = semiMajor

    def getFoci1(self):
        """Returns foci 1 of ellipse"""
        return (self.x1, self.y1)

    def getFoci2(self,):
        """Returns foci 2 of ellipse"""
        return (self.x2, self.y2)

    def getsemiMajor(self):
        """Returns Semi Major of ellipse"""
        return self.semiMajor

    def getsemiMinor(self):
        """Returns Semi Minor of ellipse"""
        C2 = self.semiMajor
        B2 = abs(self.x1 -self.x2)/2
        semiMinor = (C2 - B2)**0.5
        return semiMinor

    def inside_edge(self, point):
        """returns True if a point is inside or on edge of ellipse"""
        pointdist = distance(self.getFoci1(), point) + distance(self.getFoci2(), point)
        if pointdist > self.semiMajor*2:
            return False
        else:
            return True
