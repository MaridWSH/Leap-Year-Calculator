year = int(input("Please Enter The Year You Want To Check : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print(f"Year {year} is a Leap Year.")
        else:
            print(f"Year {year} isn't a Leap Year.")
    else:
        print(f"Year {year} is a Leap Year.")
else:
    print(f"Year {year} isn't a Leap Year.")
    
print(input("Please Press Enter To Exit. "))
