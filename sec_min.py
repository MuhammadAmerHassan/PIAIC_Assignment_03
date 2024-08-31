def sec_to_min():
    seconds:int = int(input("Enter seconds: "))
    minutes:int = seconds/60
    return minutes

def min_to_sec():
    minutes:int = int(input("Enter minutes: "))
    seconds:int = minutes * 60
    return seconds

if __name__ == "__main__":

    while True:
        choice:str = input("""Choose what do you want
                          1. Convert Seconds into minutes
                          2. Convert minutes into seconds
                          3. Exit: """)
        
        match choice:
            case "1":
                result1:int = sec_to_min()
                print(f"The result is {result1} min")
            case "2":
                result2:int = min_to_sec()
                print(f"The result is {result2} sec")   
            case "3":
                break
            case _:
                print("invalid choice")                        