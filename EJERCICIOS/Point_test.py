from Point import Point
#Create a Point
p3 = Point(6,2)
#Print its coordinate x
print(p3.x)
#Set the coordinate x = 0
p3.x = 0
#Print the Point
print(p3)
#Distance to another point
p2 = Point(4,3)
distance = p3.distance_to(p2)
print(f"La distancia de p3 a p2 es {round(distance)}")