def Rectangle_area(length:float, width:float) -> float:
    return length * width

length:float = float(input("Enter length of a rectangle: "))
width:float = float(input("Enter width of a rectangle: "))
area:float = Rectangle_area(length, width)
print("Area of Rectangle is: ", area)