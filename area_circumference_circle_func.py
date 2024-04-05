import math

def area_circumference_circle(radius):
    area = math.pi * radius ** 2
    circum = math.pi * 2 * radius
    return area, circum

area, circum = area_circumference_circle(3)
print("Area = ",round(area,2),", and, Circumference =",round(circum,2))