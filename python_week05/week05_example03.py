# Example 4

import math

def main():
    radius = float(input("Enter the radius of a circle: "))
    area = circle_area(radius)
    print(f"area: {area:.1f}")

def circle_area(radius):
    area = math.pi * radius * radius
    return area


main()


# =============================

import math

def main():
    radius1 = float(input("Enter the radius1 of a ellipse: "))
    radius2 = float(input("Enter the radius2 of a ellipse: "))
    area = ellipse_area(radius1,radius2)
    print(f"area: {area:.1f}")

def ellipse_area(radius1,radius2):
    area = math.pi * radius1 * radius2
    return area

main()


# =============================

import math

def main():
    base = float(input("Enter the base of a triangle: "))
    hight = float(input("Enter the  hight of a triangle: "))
    area = triangle_area(base,hight)
    print(f"area: {area:.1f}")

def triangle_area(base,hight):
    area =  base * hight/2
    return area

main()
