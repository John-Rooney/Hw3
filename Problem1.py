

class Ellipse:

    def __init__(self, x1=0, y1=0, x2=1, y2=0, semiMajor=1):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.semiMajor = semiMajor

    def setFoci1(self, x1, y1):
        self.F1 = (self.x1, self.y1)

    def setFoci2(self, x2, y2):
        self.F1 = (self.x2, self.y2)

    def setWidth(self, semiMajor):
        self.semiMajor = semiMajor

    def getFoci1(self, x1, y1):
        return (self.x1, self.y1)

    def getFoci2(self, x2, y2):
        return (self.x2, self.y2)

    def getWidth(self, semiMajor):
        return self.semiMajor

    def semiMinor(self, x1, x2, semiMajor):
        C2 = self.width/2
        B2 = abs(self.x1 -self.x2)/2
        semiMinor = (c2 - b2)**0.5
        return semiMinor

    def Area(self, semiMajor, semiMinor):
        pi = 3.1415927
        area = pi * self.semiMajor * self.semiMinor
        return area



def Circumference(semiMajor, semiMinor):
    pi = 3.14159
    h = ((semiMajor - semiMinor)**2)/((semiMajor + semiMinor)**2)
    Circumference = pi*(semiMajor + semiMinor)*(1+((3*h)/(10+(4-(3*h))**0.5)))
    return Circumference

