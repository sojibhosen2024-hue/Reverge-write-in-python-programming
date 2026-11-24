print("1. Feet to Metter")
print("2. Metter to Feet")

c = (input("Choice your number ="))

if c == "1":
    f = float(input("Enter Feet Value ="))
    m =round(f/3.28 ,2)
    print("Metter =", m)

elif c =="2":
    m = float(input("Enter Metter Value ="))
    f = round(m*3.28 ,2)
    print("Feet =", f)

else:
    print("Invalid Number")