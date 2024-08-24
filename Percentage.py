Total_Value:float = float(input("Enter Total Value: "))
Actual_Value:float = float(input(f"Enter actual value to calculate percenatge from {Total_Value}: "))
percentage:float = (Actual_Value/Total_Value) * 100
print(f"The answer or result is {round(percentage,2)}%")