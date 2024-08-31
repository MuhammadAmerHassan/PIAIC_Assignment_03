def Percentage(Total_Value:float, Actual_Value:float) -> float:
    return (Actual_Value/Total_Value) * 100

Total_Value:float = float(input("Enter Total Value: "))
Actual_Value:float = float(input(f"Enter actual value to calculate percenatge from {Total_Value}: "))
percentage:float = Percentage(Total_Value, Actual_Value)
print(f"The answer or result is {round(percentage,2)}%")