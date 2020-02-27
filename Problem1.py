

class Ellipse:

    def __init__(self, f1=(0, 0), f2=(1, 0), Major=4, Minor=2):
        self.f1 = f1
        self.f2 = f2
        self.Major = Major
        self.Minor = Minor

    def foci1(self, f1):
        self.f1 = f1

    def foci2(self, f2):
        self.f2 = f2

    def semiMajor(self, Major):
        self.Major = Major

    def semiMinor(self, Minor):
        self.Minor = Minor

    def __str__(self):
        # return 'boom'
        return '{} {} {} {}'.format(self.f1, self.f2, self.Major, self.Minor)

def Area(semiMajor, semiMinor):
    pi = 3.1415927
    area = pi * semiMajor * semiMinor
    return area

def Perimeter(semiMajor, semiMinor):
    pi = 3.14159
    h = ((semiMajor - semiMinor)**2)/((semiMajor + semiMinor)**2)
    perimeter = pi*(semiMajor + semiMinor)*(1+((3*h)/(10+(4-(3*h))**0.5)))
    return perimeter

