a = input().split()
x = float(a[0])
y = a[1]
z = float(a[2])
match y:
    case "+":
       print(x + z)
    case "*":
       print(x * z)
    case "-":
       print(x - z)
    case "/":
       if z == 0:
           print("Cannot divide by zero")
       else:
           print(x / z)
    case _:
       print("Unsupported operator")

