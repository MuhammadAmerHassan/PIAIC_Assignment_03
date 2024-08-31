def Calculate_age(ageYear:int)->int:
    currentYear:int = 2024
    return currentYear - ageYear
ageYear:int = int(input("Enter Age Year: "))
age:int = Calculate_age(ageYear)
print("Your age is: ", age)    