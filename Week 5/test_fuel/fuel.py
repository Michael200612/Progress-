def main():
    while True:
        try:
            x = convert(input("Fraction: "))
            y = gauge(x)
            print(y)
            break
        except ValueError:
            pass
    
def convert(fraction):
    try:
        if "-" in fraction:
            raise ValueError
        x,y = fraction.split("/")
        return int((int(x)/int(y))*100)
    except (ValueError, ZeroDivisionError):
        raise ValueError

def gauge(percentage):
    if 0 < percentage < 100:
        return f"{percentage}%"
    elif percentage == 0:
        return "E"
    elif percentage == 100:
        return "F"
    else:
        pass

if __name__ == "__main__":
    main()
