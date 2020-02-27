class DefaultEllipse:

    def __init__(self, foci1=(0, 0), foci2=(1, 0), semiMajor=2, semiMinor=1):
        return


class ManualEllipse(DefaultEllipse):

    def foci1(self, foci1):
        self.foci1 = foci1

    def foci2(self, foci2):
        self.foci2 = foci2

    def SemiMajor(self, semiMajor):
        self.semiMajor = semiMajor

    def SemiMinor(self, semiMinor):
        self.semiMinor = semiMinor

    # def __repr__(self):
    #     return '{} {} {} {}'.format(self.f1, self.f2, self.Major, self.Minor)

    def read(self):
        print('fuck')
        print('{} {} {} {}'.format(self.foci1, self.foci2, self.semiMajor, self.semiMinor))


hello = ManualEllipse()

