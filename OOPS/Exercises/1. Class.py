# 1.  Write a Python program to create a class representing a Circle.
# Include methods to calculate its area and perimeter.
class Circle:
  def perimeter(self, r):
    pi = 3.14
    perimeter_of_the_circle = 2 * pi * r
    return perimeter_of_the_circle 
  def area(self, r):
    pi = 3.14
    area_of_the_circle = pi * (r ** 2)
    return area_of_the_circle 
obj = Circle()    
radius = 50
per = Circle.perimeter(obj, radius)
print(per)

are = Circle.area(obj, radius)
print(are)