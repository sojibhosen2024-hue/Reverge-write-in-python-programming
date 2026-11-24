year = int(input("Enter year ="))

if year % 400 == 0:
    print(year, "is leap year")
else:
    
    if year % 100 != 0 and year % 4 ==0:
        print(year, "is leap year")
    else:
        print(year, "is not leap year")