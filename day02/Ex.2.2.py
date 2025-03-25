#Given three points in space A, B and C, determine if the points make a isoceles
#triangle, or right angled triangle or both

import math

print("Enter the coordinates of point A (a1, a2): ")
a1 = float(input("a1: "))
a2 = float(input("a2: "))

print("Enter the coordinates of point B (b1, b2): ")
b1 = float(input("b1: "))
b2 = float(input("b2: "))

print("Enter the coordinates of point C (c1, c2): ")
c1 = float(input("c1: "))
c2 = float(input("c2: "))

AB = math.sqrt((b1 - a1)**2 + (b2 - a2)**2)
BC = math.sqrt((c1 - b1)**2 + (c2 - b2)**2)
CA = math.sqrt((a1 - c1)**2 + (a2 - c2)**2)

max = max(AB, BC, CA)

iso = ((AB == BC) or (CA == BC) or (AB == CA))
is_right = False

if max == AB:
    is_right = AB**2 == BC**2 + CA**2
elif max == BC:
    is_right = BC**2 == AB**2 + CA**2
elif max == CA:
    is_right = CA**2 == AB**2 + BC**2

if iso and is_right:
    print("The triangle is both isosceles and right-angled.")
elif is_right:
    print("The triangle is a right-angled triangle.")
elif iso:
    print("The triangle is an isosceles triangle.")
else:
    print("The triangle is of another type.")