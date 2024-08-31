import math # importing math library for the exact value of PI

def Cylinder(radius:float, height:float) -> float:
    return math.pi * (radius ** 2) * height


radius:float = float(input("Enter the radius of a cylinder: "))
height:float = float(input("Enter the height of a cylinder: "))
volume:float = Cylinder(radius, height)
print(f"The volume of Cylinder is {volume} m³")