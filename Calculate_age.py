ageYear:int = int(input("Enter Age Year: "))
currentYear:int = 2024
age:int = 0
for i in range(ageYear, currentYear):
    age += 1
    print("Your age is: ", age)