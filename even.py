num = int(input("Enter number= "))
if num % 2 == 0:
    print(num,"Even number")
else:
    print(num,"odd number")

a = 1
b = 150
c = 0
while a <= b:
    if a % 2 == 0:
        c += 1
    a += 1
print(c)