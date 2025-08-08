from tabulate import tabulate
import sys

def main():
    x = function(get())
    print(tabulate(x))

def get():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not (sys.argv[1]).endswith(".csv"):
        sys.exit("Not a CVS file")
    return sys.argv[1]

def function(file):
    try:
        l = []
        with open(file) as file:
            for lines in file:
                x = lines.split(",")
                l.append(x)
        return l
    except FileNotFoundError:
        sys.exit("File does not exit")

main()

