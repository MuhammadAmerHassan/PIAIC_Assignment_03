def Calculate_BMI(weight:float, height:float) -> float:
    return weight/(height ** 2)

weight:float = float(input("Enter weight in Kilograms: "))
height:float = float(input("Enter height in meters: "))
BMI:float = Calculate_BMI(weight, height)
print("The BMI (Body Mass Index) is ", round(BMI,2))