from Rectangle import Rectangle
from Point import Point

p1 = Point(2, 8)
p2 = Point(4, 5)

r1 = Rectangle(p1,p2)

print(f"El rectángulo es: {r1}")
print(f"El área del rectángulo es: {r1.area}")
print(f"El perímetro del rectángulo es: {r1.perimeter}")



