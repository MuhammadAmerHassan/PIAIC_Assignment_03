import math # Import Math library for exact value of PI

def Calculate_area(radius:float)-> float:
    return math.pi * (radius ** 2)

radius:float = float(input("Enter radius of a circle: "))
area = Calculate_area(radius)
print("Area of circle is: ", area)