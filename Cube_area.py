def Cube_area(length:float) -> float:
    return 6 * (length ** 2)


length:float = float(input("Enter length of one side of a cube: "))
area:float = Cube_area(length)
print("The area of a cube is: ", area) 