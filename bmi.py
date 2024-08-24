weight:float = float(input("Enter weight in Kilograms: "))
height:float = float(input("Enter height in meters: "))
BMI:float = weight/(height ** 2)
print("The BMI (Body Mass Index) is ", round(BMI,2))