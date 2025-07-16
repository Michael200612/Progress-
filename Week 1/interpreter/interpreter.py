a = input().split()
x = float(a[0])
y = a[1]
z = float(a[2])
if y == "+":
    print(x + z)
elif y == "*":
    print(x * z)
elif y == "-":
    print(x - z)
elif y == "/":
    if z == 0:
        print("Cannot divide by zero")
    else:
        print(x / z)
else:
    print("Unsupported operator")

