def main():
    x = fuel("Fraction: ")
    print(x)

def fuel(a):
    while True:
        try:
            x,y = input(a).split("/")
            b = int((int(x)/int(y))*100)
            if 0 < b < 100:
                return f"{b}%"
            elif b == 0:
                return "E"
            elif b == 100:
                return "F"
            else:
                pass
        except (ValueError, ZeroDivisionError):
            pass

main()
