import utility, EllipseClass, main

print('Functions in utility.py')
print('******distance******')
print('returns distance between 2 points')
print('testing with 2 points left of y axis')
print('utility.distance((-5, -3), (-10, -3))')
print(utility.distance((-5, -3), (-10, -3)))

print()
print('testing with 1 point left of y axis and one on the right')
print('utility.distance((-5, -3), (10, 3))')
print(utility.distance((-5, -3), (10, 3)))

print()
print('******circumference******')
print('returns circumference of ellipse')
print('testing with different semi major and semi minor')
print('utility.circumference(1, 2)')
print(utility.circumference(1, 2))

print()
print('testing with same semi major and semi minor')
print('utility.circumference(1, 1)')
print(utility.circumference(1, 1))

print()
print('******area******')
print('Returns approximate area of ellipse')
print('testing with different semi major and semi minor')
print('utility.area(1, 2)')
print(utility.area(1, 2))

print()
print('testing with same semi major and semi minor')
print('utility.area(1, 1)')
print(utility.area(1, 1))

print()
print('Functions in EllipseClass.py')
print('******Ellipse Class******')
print('Defines and edits ellipse objects based on 2 foci and the Semi Major')
print('testing with allowed parameters')
print('EllipseClass.Ellipse(0, 0, 1, 0, 2)')
print(EllipseClass.Ellipse(0, 0, 1, 0, 2))

print()
print('testing with string in x1')
print('EllipseClass.Ellipse(\'string\', 0, 1, 0, 2)')
try:
    print(EllipseClass.Ellipse('string', 0, 1, 0, 2))
except:
    print('TypeError')

print()
print('testing with string in y1')
print('EllipseClass.Ellipse(0,  \'string\', 1, 0, 2)')
try:
    print(EllipseClass.Ellipse(0, 'string', 1, 0, 2))
except:
    print('TypeError')

print()
print('testing with string in x2')
print('EllipseClass.Ellipse(0, 0, \'string\', 0, 2)')
try:
    print(EllipseClass.Ellipse(0, 0, 'string', 0, 2))
except:
    print('TypeError')

print()
print('testing with string in y2')
print('EllipseClass.Ellipse(0, 0, 1, \'string\', 2)')
try:
    print(EllipseClass.Ellipse(0, 0, 1, 'string', 2))
except:
    print('TypeError')

print()
print('testing with string in semi Major')
print('EllipseClass.Ellipse(0, 0, 1, 0, \'string\')')
try:
    print(EllipseClass.Ellipse(0, 0, 1, 0, 'string'))
except:
    print('TypeError')

print()
print('testing with semi Major and both X\'s and Y\'s different')
print('EllipseClass.Ellipse(1, 2, 3, 4, 4)')
try:
    print(EllipseClass.Ellipse(1, 2, 3, 4, 4))
except:
    print('ValueError')

print()
print('testing with negative semi Major')
print('EllipseClass.Ellipse(1, 2, 3, 4, -4)')
try:
    print(EllipseClass.Ellipse(1, 2, 3, 4, -4))
except:
    print('ValueError')

print()
print('*****setFoci1*****')
print('setting foci 1 of ellipse')
print('testing with ints')
print('a = EllipseClass.Ellipse()\na.setFoci1(3, 4)\na.getFoci1()')
a = EllipseClass.Ellipse()
try:
    a.setFoci1(3, 4)
    print(a.getFoci1())
except:
    print('TypeError')

print()
print('testing with string')
print('a = EllipseClass.Ellipse()\na.setFoci1(\'w\', 4)\na.getFoci1()')
a = EllipseClass.Ellipse()
try:
    a.setFoci1('w', 4)
    print(a.getFoci1())
except:
    print('TypeError')

print()
print('*****setFoci2*****')
print('setting foci 2 of ellipse')
print('testing with ints')
print('a = EllipseClass.Ellipse()\na.setFoci2(3, 4)\na.getFoci2()')
a = EllipseClass.Ellipse()
try:
    a.setFoci2(3, 4)
    print(a.getFoci2())
except:
    print('TypeError')

print()
print('testing with string')
print('a = EllipseClass.Ellipse()\na.setFoci2(\'w\', 4)\na.getFoci2()')
a = EllipseClass.Ellipse()
try:
    a.setFoci2('w', 4)
    print(a.getFoci2())
except:
    print('TypeError')

print()
print('*****setsemiMajor*****')
print('setting semiMajor of ellipse')
print('testing with ints')
print('a = EllipseClass.Ellipse()\na.setsemiMajor(4)\na.getsemiMajor()')
a = EllipseClass.Ellipse()
try:
    a.setsemiMajor(4)
    print(a.getsemiMajor())
except:
    print('TypeError')

print()
print('testing with string')
print('a = EllipseClass.Ellipse()\na.setsemiMajor(\'w\')\na.getsemiMajor()')
a = EllipseClass.Ellipse()
try:
    a.setsemiMajor('w')
    print(a.getsemiMajor())
except:
    print('TypeError')

print()
print('*****getsemiMinor*****')
print('Returns Semi Minor of ellipse')
print('testing with 2 points with same y-value')
print('a = EllipseClass.Ellipse(0, 0, 8, 0, 5)\na.getsemiMinor()')
a = EllipseClass.Ellipse(0, 0, 8, 0, 5)
print(a.getsemiMinor())

print()
print('testing with 2 points with same x-value')
print('a = EllipseClass.Ellipse(0, 0, 0, 8, 5)\na.getsemiMinor()')
a = EllipseClass.Ellipse(0, 0, 8, 0, 5)
print(a.getsemiMinor())