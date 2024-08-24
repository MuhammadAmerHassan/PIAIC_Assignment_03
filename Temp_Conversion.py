def Fahrenheit_to_Celsius():
    F_Temp:float = float(input("Enter Temperature (°F): "))
    Celsius:float = (F_Temp - 32) * (5/9)
    return Celsius

def Celsius_to_Fahrenheit():
    C_Temp:float = float(input("Enter Temperature (°C): "))
    Fahrenheit:float = (C_Temp * 9/5) + 32
    return Fahrenheit

if __name__ == "__main__":

    while True:

        choice:str = input("""Choose what you want
            1. Convert Temperature Fahrenheit to Celsius
            2. Convert Temperature Celsius to Fahrenheit
            3. Exit: """)


        match choice:
            case "1":
                result1:float = Fahrenheit_to_Celsius()
                print(f"Temperature in Celcius {result1}°C")  
            case "2":
                result2:float = Celsius_to_Fahrenheit()
                print(f"Temperature in Fahrenheit {result2}°F") 
            case "3":
                break    
            case _:
                print("Invalid Choice")



