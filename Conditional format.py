
mark = int(input("Enter Marks: "))

if 80 <= mark <= 100:
    print("A+")
elif 70 <= mark <= 79:
    print("A-")
elif 60 <= mark <= 69:
    print("B+")
elif 50 <= mark <= 59:
    print("B-")
elif 0 <= mark < 50:
    print("Fail")
else:
    print("Invalid mark")