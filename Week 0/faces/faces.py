def convert(x):
    x = x.replace(":)", "\U0001F642")
    x = x.replace(":(", "\U0001F641")
    return x

def main():
    print(convert(input()))

main()
